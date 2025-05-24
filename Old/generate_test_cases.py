import pandas as pd  # type: ignore
from faker import Faker  # type: ignore
from datetime import datetime, timedelta
import random
import json
import itertools
import re
from tqdm import tqdm # type: ignore
import sys
from multiprocessing import Pool
from functools import partial
from data.test_case_data import scenarios, carriers, vehicles, city_state_mapping, base_idv_ranges, products, available_addons

# Initialize Faker
fake = Faker('en_IN')

test_cases = []

def calculate_depreciation(vehicle_age):
    """Calculate depreciation percentage based on vehicle age."""
    if vehicle_age <= 1:
        return 0.05
    elif vehicle_age <= 2:
        return 0.15
    elif vehicle_age <= 3:
        return 0.25
    elif vehicle_age <= 4:
        return 0.35
    elif vehicle_age <= 5:
        return 0.45
    elif vehicle_age <= 10:
        return 0.50
    else:
        return 0.60

# Pre-generate customer data pool
def pre_generate_customer_data_pool(size=10000):
    pool = []
    state_codes = ['KA', 'MH', 'DL', 'TN', 'WB', 'UP', 'GJ', 'RJ']
    for _ in tqdm(range(size), desc="Pre-generating customer data"):
        name = fake.name()
        phone_number = ''.join(filter(str.isdigit, fake.phone_number()))[:10]
        state_code = random.choice(state_codes)
        series_letter = random.choice(['', 'A', 'B', 'C', 'AB', 'CD'])
        registration_number = f"{state_code}{random.randint(1, 99):02d}{series_letter}{random.randint(1, 9999):04d}"
        while not re.match(r'^[A-Z]{2}\d{2}[A-Z]{0,2}\d{4}$', registration_number):
            state_code = random.choice(state_codes)
            series_letter = random.choice(['', 'A', 'B', 'C', 'AB', 'CD'])
            registration_number = f"{state_code}{random.randint(1, 99):02d}{series_letter}{random.randint(1, 9999):04d}"
        
        city = random.choice(list(city_state_mapping.keys()))
        state = city_state_mapping[city]
        
        pool.append({
            'name': name,
            'phone_number': phone_number,
            'email': fake.email(),
            'registration_number': registration_number,
            'address': {
                'address_line_1': fake.street_address(),
                'pincode': fake.postcode(),
                'city': city,
                'state': state
            }
        })
    return pool

customer_data_pool = pre_generate_customer_data_pool(10000)

def generate_customer_data():
    """Select a random customer profile."""
    return random.choice(customer_data_pool)

def generate_test_case(scenario, testcase_id):
    try:
        required_fields = ['name', 'category', 'journey_type', 'policy_type', 'ownership', 
                         'ownership_changed', 'claim_taken', 'tp_status', 'od_status']
        for field in required_fields:
            if field not in scenario:
                return None

        vehicle = random.choice([v for v in vehicles if v['category'] == scenario['category']])
        
        category_code = 'MOTOR_RETAIL' if scenario['category'] == 'four_wheeler' else 'TWO_WHEELER_RETAIL'
        product_class = {'comprehensive': 'Comprehensive', 'third_party': 'TP Only', 'OD': 'OD Only'}[scenario['policy_type']]
        matching_products = [p for p in products if p['category_code'] == category_code and p['product_class'] == product_class]
        if not matching_products:
            return None
        product = random.choice(matching_products)
        product_code = product['code']
        carrier_name = product['carrier_name']

        current_date = datetime.now()
        current_year = current_date.year

        if scenario.get('manufacturing_year', '') == '<2018-09':
            manufacturing_year = random.randint(2000, 2018)
            manufacturing_date = datetime(manufacturing_year, random.randint(1, 8), 1)
        elif scenario.get('manufacturing_year', '') == '<2010':
            manufacturing_year = random.randint(2000, 2009)
            manufacturing_date = datetime(manufacturing_year, random.randint(1, 12), 1)
        else:
            manufacturing_year = random.randint(current_year - 1, current_year)
            manufacturing_date = datetime(manufacturing_year, random.randint(1, 12), 1)

        vehicle_age = current_year - manufacturing_year
        if vehicle_age > 15 and scenario['name'] != 'VEHICLE_AGE_GT_15Y':
            return None

        base_idv_min, base_idv_max = base_idv_ranges.get(vehicle['make_model'], (50000, 1500000))
        depreciation = calculate_depreciation(vehicle_age)
        
        variant = vehicle['variant']
        engine_cc = int(re.search(r'CC - (\d+)', variant).group(1)) if re.search(r'CC - (\d+)', variant) else 1000
        fuel_type = re.search(r'Fuel - (\w+)', variant).group(1) if re.search(r'Fuel - (\w+)', variant) else 'Petrol'

        idv_adjustment = 1.0
        if fuel_type == 'Diesel':
            idv_adjustment *= 1.1
        if scenario['category'] == 'four_wheeler' and engine_cc > 1500:
            idv_adjustment *= 1.2
        elif scenario['category'] == 'two_wheeler' and engine_cc > 250:
            idv_adjustment *= 1.15

        if scenario['ownership_changed'] != 'Yes' and scenario['claim_taken'] == 'Yes':
            idv_adjustment *= 0.95

        idv_min = int(base_idv_min * (1 - depreciation) * idv_adjustment * 0.8)
        idv_max = int(base_idv_max * (1 - depreciation) * idv_adjustment * 1.2)
        idv = random.randint(idv_min, idv_max) if scenario['journey_type'] == 'without_registration' else 0

        inspection_required = 'No'
        if scenario['journey_type'] == 'new_journey':
            inspection_required = 'No'
        elif scenario['ownership_changed'] == 'Yes':
            inspection_required = 'Yes'
        elif scenario['journey_type'] == 'rollover':
            expired_statuses = ['>90D', '<90D', '<60D', '<3D', '60D-90D']
            if scenario['od_status'] in expired_statuses or scenario['tp_status'] in expired_statuses:
                inspection_required = 'Yes'
            elif scenario['od_status'] == 'today' and scenario['tp_status'] == 'today':
                inspection_required = 'No'

        ncb = ''
        if scenario['journey_type'] != 'new_journey' and scenario['ownership_changed'] != 'Yes' and scenario['journey_type'] == 'rollover':
            if scenario['claim_taken'] == 'Yes':
                ncb = '0%'
            elif inspection_required == 'No':
                ncb = random.choice(['0%', '20%', '25%', '35%', '45%', '50%'])

        claim_taken = '' if scenario['ownership_changed'] == 'Yes' or scenario['journey_type'] == 'new_journey' else scenario['claim_taken']

        previous_expiry_date = '' if scenario['journey_type'] == 'new_journey' else ''
        previous_tp_expiry_date = '' if scenario['journey_type'] == 'new_journey' else ''
        registration_year = random.choice([manufacturing_year, manufacturing_year + 1])
        max_date = min(datetime.now(), datetime(registration_year, 12, 31))
        registration_date_obj = fake.date_between(start_date=datetime(registration_year, 1, 1), end_date=max_date)
        registration_date = registration_date_obj.strftime('%d/%m/%Y')

        if scenario['journey_type'] == 'rollover':
            if scenario['od_status'] == '>90D':
                previous_expiry_date = (current_date - timedelta(days=random.choice([120, 123, 365]))).strftime('%d/%m/%Y')
            elif scenario['od_status'] == '<90D':
                previous_expiry_date = (current_date - timedelta(days=random.randint(15, 89))).strftime('%d/%m/%Y')
            elif scenario['od_status'] == 'today':
                previous_expiry_date = current_date.strftime('%d/%m/%Y')

            tp_tenure = random.choice([1, 3]) if scenario['category'] == 'four_wheeler' else random.choice([1, 5])
            if scenario['tp_status'] == '>90D':
                previous_tp_expiry_date = (current_date - timedelta(days=random.choice([120, 365]))).strftime('%d/%m/%Y')
            elif scenario['tp_status'] == '<60D':
                previous_tp_expiry_date = (current_date - timedelta(days=random.randint(4, 59))).strftime('%d/%m/%Y')
            elif scenario['tp_status'] == '<3D':
                previous_tp_expiry_date = (current_date - timedelta(days=random.randint(1, 3))).strftime('%d/%m/%Y')
            elif scenario['tp_status'] == 'today':
                previous_tp_expiry_date = current_date.strftime('%d/%m/%Y')
            elif scenario['tp_status'] == '60D-90D':
                previous_tp_expiry_date = (current_date - timedelta(days=random.randint(60, 90))).strftime('%d/%m/%Y')

        customer_data = generate_customer_data()

        registration_number = ''
        if scenario['journey_type'] == 'without_registration':
            registration_number = ''
        elif scenario['journey_type'] == 'rollover':
            registration_number = customer_data['registration_number']
            if not registration_number:
                return None

        not_sure = '' if scenario['journey_type'] == 'new_journey' else ('Yes' if scenario['od_status'] == 'not_sure' or scenario['tp_status'] == 'no_tp' else 'No')

        is_ownership_changed = '' if scenario['journey_type'] == 'new_journey' else scenario['ownership_changed']
        previous_insurer = '' if scenario['journey_type'] == 'new_journey' else random.choice(carriers) if previous_expiry_date else ''
        previous_tp_insurer = '' if scenario['journey_type'] == 'new_journey' else random.choice(carriers) if previous_tp_expiry_date else ''
        know_previous_tp_expiry_date = '' if scenario['journey_type'] == 'new_journey' else 'No' if scenario['tp_status'] == 'no_tp' else 'Yes'

        
        if scenario['category'] == 'four_wheeler':
            available_addons.append('LPG_CNG_KIT_IDV')
        available_discounts = ['TPPD_DISCOUNT', 'VOLUNTARY_DEDUCTIBLE_DISCOUNT', 'ANTI_THEFT_DISCOUNT']
        addons = []
        discounts = []
        if scenario['policy_type'] in ['comprehensive', 'OD']:
            num_addons = random.randint(0, len(available_addons))
            selected_addons = random.sample(available_addons, num_addons)
            if 'NCB_PROTECTION' in selected_addons or 'LOSS_OF_USE' in selected_addons:
                selected_addons.append('ZERO_DEPRECIATION_COVER')
            addons = [{'insurance_cover_code': addon} for addon in set(selected_addons)]
            num_discounts = random.randint(0, len(available_discounts))
            discounts = [{'discount_code': random.choice(available_discounts)} for _ in range(num_discounts)]

        risk_start_date = (current_date + timedelta(days=2)).strftime('%d/%m/%Y') if inspection_required == 'Yes' else current_date.strftime('%d/%m/%Y')

        kyc_verification = scenario.get('kyc_verification', random.choice(['Yes', 'No']))
        kyc_type = scenario.get('kyc_type', random.choice(['PAN', 'AADHAR', 'CKYC']))
        kyc_details = []
        proposer_pan = ''
        proposer_aadhaar = ''
        if kyc_verification == 'Yes':
            if kyc_type == 'PAN':
                proposer_pan = fake.bothify(text='?????####?').upper()
                while not re.match(r'^[A-Z]{5}\d{4}[A-Z]$', proposer_pan):
                    proposer_pan = fake.bothify(text='?????####?').upper()
                kyc_details = [{'PAN': {'pan': proposer_pan, 'dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')}}]
            elif kyc_type == 'AADHAR':
                proposer_aadhaar = fake.bothify(text='#### #### ####')
                while not re.match(r'^\d{4}\s\d{4}\s\d{4}$', proposer_aadhaar):
                    proposer_aadhaar = fake.bothify(text='#### #### ####')
                kyc_details = [{'AADHAR': {'number': proposer_aadhaar, 'dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')}}]
            else:
                kyc_details = [{'CKYC': {'number': fake.bothify(text='##############'), 'dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')}}]
        else:
            kyc_details = []

        has_financier = random.choice([True, False])
        financier_name = fake.company() if has_financier else ''
        financier_type = random.choice(['Bank', 'NBFC']) if has_financier else ''

        valid_puc = 'Yes'
        puc_number = fake.bothify(text='PUC####')
        puc_expiry = (current_date + timedelta(days=random.randint(1, 365))).strftime('%d/%m/%Y')

        nominee_details = {}
        if 'PERSONAL_ACCIDENT' in [addon['insurance_cover_code'] for addon in addons]:
            nominee_details = {
                'nominee_first_name': fake.first_name(),
                'nominee_last_name': fake.last_name(),
                'nominee_age': random.randint(18, 70),
                'nominee_relation': random.choice(['Spouse', 'Parent', 'Child', 'Sibling'])
            }
        no_pa_cover = 'Yes' if 'PERSONAL_ACCIDENT' not in [addon['insurance_cover_code'] for addon in addons] else 'No'

        previous_policy_details = {}
        if scenario['journey_type'] == 'rollover':
            previous_policy_details = {
                'previous_policy_carrier_code': random.choice(['BAJAJ_ALLIANZ', 'TATA_AIG']) if previous_expiry_date else '',
                'previous_policy_type': scenario['policy_type'],
                'previous_policy_number': fake.bothify(text='POL####'),
                'previous_policy_expiry_date': previous_expiry_date
            }
            if scenario['policy_type'] != 'comprehensive':
                previous_policy_details.update({
                    'previous_tp_policy_start_date': (datetime.strptime(registration_date, '%d/%m/%Y') - timedelta(days=365 * tp_tenure)).strftime('%d/%m/%Y') if previous_tp_expiry_date else '',
                    'previous_tp_policy_expiry_date': previous_tp_expiry_date,
                    'previous_tp_policy_carrier_code': random.choice(['BAJAJ_ALLIANZ', 'TATA_AIG']) if previous_tp_expiry_date else '',
                    'previous_tp_policy_number': fake.bothify(text='TPPOL####') if previous_tp_expiry_date else ''
                })

        company_details = {}
        if scenario['ownership'] == 'Company':
            company_details = {
                'company_gstin': fake.bothify(text='##AAAAA####A#A#'),
                'company_name': fake.company(),
                'proposer_dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
                'proposer_pan': proposer_pan
            }

        individual_details = {}
        if scenario['ownership'] == 'Individual':
            gender = random.choice(['Male', 'Female'])
            title = 'Mr' if gender == 'Male' else random.choice(['Ms', 'Mrs'])
            individual_details = {
                'proposer_first_name': customer_data['name'].split()[0],
                'proposer_last_name': customer_data['name'].split()[-1] if len(customer_data['name'].split()) > 1 else '',
                'proposer_dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
                'proposer_gender': gender,
                'proposer_title': title,
                'proposer_aadhaar': proposer_aadhaar,
                'proposer_marital_status': random.choice(['Married', 'Single']),
                'proposer_pan': proposer_pan
            }

        test_case = {
            'Testcase_id': f"{product['insurance_company_code']}_{scenario['category'].upper()}_{scenario['name']}_{testcase_id:03d}",
            'category': scenario['category'],
            'journey_type': scenario['journey_type'],
            'registration_number': registration_number,
            'make_model': vehicle['make_model'],
            'variant': vehicle['variant'],
            'registration_date': registration_date,
            'rto': random.choice(['KA01', 'MH05', 'MH01', 'KA08']),
            'owned_by': scenario['ownership'],
            'is_ownership_changed': is_ownership_changed,
            'previous_expiry_date': previous_expiry_date,
            'previous_insurer': previous_insurer,
            'previous_tp_expiry_date': previous_tp_expiry_date,
            'previous_tp_insurer': previous_tp_insurer,
            'not_sure': not_sure,
            'know_previous_tp_expiry_date': know_previous_tp_expiry_date,
            'claim_taken': claim_taken,
            'previous_ncb': ncb,
            'product_code': product_code,
            'customer_name': customer_data['name'],
            'contact_number': customer_data['phone_number'],
            'idv': idv,
            'idv_min': idv_min,
            'idv_max': idv_max,
            'addons': json.dumps(addons),
            'discounts': json.dumps(discounts),
            'select_tab': scenario['policy_type'],
            'email': customer_data['email'],
            'kyc': json.dumps(kyc_details),
            'kyc_verification': kyc_verification,
            'proposal_questions': json.dumps({
                'vehicle_details': {
                    'manufacturing_year': str(manufacturing_year),
                    'registration_number': registration_number,
                    'engine_number': fake.bothify(text='##########'),
                    'chassis_number': fake.bothify(text='#################'),
                    'financier_name': financier_name,
                    'financier_type': financier_type,
                    'valid_puc': valid_puc,
                    'puc_number': puc_number,
                    'puc_expiry': puc_expiry
                },
                'nominee_details': nominee_details,
                'contact_details': {
                    'proposer_email': customer_data['email'],
                    'proposer_phone_number': customer_data['phone_number']
                },
                'individual_details': individual_details,
                'company_details': company_details,
                'customer_address': {
                    'address': customer_data['address'],
                    'is_address_same': random.choice(['Yes', 'No']) if random.choice([True, False]) else '',
                    'registration_address': customer_data['address'] if random.choice([True, False]) else ''
                },
                'previous_policy_details': previous_policy_details,
                'NO_PA_Cover': no_pa_cover,
                'proposal_occupation': fake.job() if scenario['ownership'] == 'Individual' else 'Business Owner'
            }),
            'is_inspection_required': inspection_required,
            'carrier_name': carrier_name,
            'payment_time': current_date.strftime('%d/%m/%Y %H:%M:%S'),
            'breakin_inspection_approval': 'Yes' if inspection_required == 'Yes' else 'No'
        }

        return test_case

    except Exception as e:
        return None

def expand_scenarios():
    categories = ['four_wheeler', 'two_wheeler']
    journey_types = ['new_journey', 'without_registration', 'rollover']
    policy_types = ['comprehensive', 'third_party', 'OD']
    ownerships = ['Individual', 'Company']
    ownership_changes = ['Yes', 'No']
    claims = ['Yes', 'No']
    manufacturing_years = ['<2018-09', '>2018-09', '<2010']
    tp_statuses = ['no_tp', '<3D', '<60D', '>90D', 'today', '60D-90D']
    od_statuses = ['not_sure', 'today', '<90D', '>90D']
    kyc_verifications = ['Yes', 'No']
    kyc_types = ['PAN', 'AADHAR', 'CKYC']

    additional_scenarios = []
    index = len(scenarios) + 1
    for combo in itertools.product(categories, journey_types, policy_types, ownerships, ownership_changes, claims, manufacturing_years, tp_statuses, od_statuses, kyc_verifications, kyc_types):
        category, journey_type, policy_type, ownership, ownership_changed, claim_taken, manufacturing_year, tp_status, od_status, kyc_verification, kyc_type = combo
        
        if journey_type in ['new_journey', 'without_registration'] and (od_status != 'not_sure' or tp_status != 'no_tp'):
            continue
        if policy_type == 'third_party' and od_status != 'not_sure':
            continue
        if journey_type == 'rollover' and od_status == 'not_sure':
            continue
        if manufacturing_year == '<2010' and 'VEHICLE_AGE_GT_15Y' not in [s['name'] for s in scenarios]:
            continue

        additional_scenarios.append({
            'name': f'ADDITIONAL_{index}',
            'category': category,
            'journey_type': journey_type,
            'policy_type': policy_type,
            'ownership': ownership,
            'ownership_changed': ownership_changed,
            'claim_taken': claim_taken,
            'manufacturing_year': manufacturing_year,
            'tp_status': tp_status,
            'od_status': od_status,
            'kyc_verification': kyc_verification,
            'kyc_type': kyc_type
        })
        index += 1
    return additional_scenarios

def generate_test_case_wrapper(args):
    scenario, testcase_id = args
    return generate_test_case(scenario, testcase_id)

def generate_test_cases_parallel(scenarios):
    
    total_scenarios = len(scenarios)
    with Pool() as pool:
        args = [(scenario, i) for i, scenario in enumerate(scenarios, 1)]
        with tqdm(total=total_scenarios, desc="Generating test cases", unit="scenario") as pbar:
            for test_case in pool.imap_unordered(generate_test_case_wrapper, args):
                if test_case:
                    test_cases.append(test_case)
                    if len(test_cases) % 100 == 0:
                        pd.DataFrame(test_cases).to_csv('automation_data_table_temp.csv', index=False)
                pbar.update(1)
    return test_cases

all_scenarios = scenarios + expand_scenarios()
try:
    test_cases = generate_test_cases_parallel(all_scenarios)
except KeyboardInterrupt:
    pd.DataFrame(test_cases).to_csv('automation_data_table_temp.csv', index=False)
except Exception as e:
    print(f"Error during parallel processing: {str(e)}")
    pd.DataFrame(test_cases).to_csv('automation_data_table_temp.csv', index=False)

try:
    df = pd.DataFrame(test_cases)
    output_file = 'automation_data_table_generated.xlsx'
    df.to_excel(output_file, index=False)
    print(f"Excel file generated: {output_file} with {len(test_cases)} test cases")
except Exception as e:
    print(f"Error saving Excel file: {str(e)}")
    sys.exit(1)