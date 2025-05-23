import pandas as pd
from faker import Faker
from datetime import datetime, timedelta, date
import random
import json
import itertools
import re
from tqdm import tqdm
import sys
from multiprocessing import Pool
from functools import partial
from data.test_case_data import scenarios, carriers, vehicles

# Initialize Faker
fake = Faker('en_IN')

# Pre-generate a pool of customer data
def pre_generate_customer_data_pool(size=10000):  # Reduced size for efficiency
    pool = []
    for _ in tqdm(range(size), desc="Pre-generating customer data"):
        name = fake.name()
        phone_number = ''.join(filter(str.isdigit, fake.phone_number()))[:10]
        registration_number = fake.bothify(text='??##??####')
        if not re.match(r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$', registration_number):
            registration_number = random.choice(['KA01AB1234', 'MH05CD5678', 'DL03EF9012'])
        
        pool.append({
            'name': name,
            'phone_number': phone_number,
            'email': fake.email(),
            'registration_number': registration_number,
            'address': {
                'address_line_1': fake.street_address(),
                'pincode': fake.postcode(),
                'city': fake.city(),
                'state': fake.state()
            }
        })
    return pool

customer_data_pool = pre_generate_customer_data_pool(10000)

def generate_customer_data():
    return random.choice(customer_data_pool)

def generate_test_case(scenario, testcase_id):
    try:
        vehicle = random.choice([v for v in vehicles if v['category'] == scenario['category']])
        carrier = random.choice(carriers)
        current_date = datetime.now()
        
        # Manufacturing year logic
        current_year = current_date.year
        manufacturing_year = random.randint(2000, 2018) if scenario.get('manufacturing_year', '') == '<2018-09' else \
                           random.randint(2000, 2009) if scenario.get('manufacturing_year', '') == '<2010' else \
                           random.randint(current_year - 1, current_year)  # Same or previous year

        # Vehicle age check
        if current_year - manufacturing_year > 15 and scenario['name'] != 'VEHICLE_AGE_GT_15Y':
            return None

        # Apply business rules
        ncb = '0%'
        inspection_required = 'Yes'
        if scenario['journey_type'] == 'rollover' and scenario['claim_taken'] == 'Yes' or scenario['ownership_changed'] == 'Yes':
            ncb = '0%'
        elif scenario['journey_type'] == 'rollover' and scenario['od_status'] in ['today', '<90D'] and scenario['tp_status'] in ['today', '<3D', '<60D', '60D-90D']:
            ncb = random.choice(['0%', '20%', '25%', '35%', '45%', '50%'])
            inspection_required = 'No' if scenario['od_status'] == 'today' and scenario['tp_status'] == 'today' else 'Yes'

        # Set expiry dates
        previous_expiry_date = ''
        previous_tp_expiry_date = ''
        if scenario['journey_type'] == 'rollover':
            if scenario['od_status'] == '>90D':
                previous_expiry_date = (current_date - timedelta(days=random.choice([120, 123, 365]))).strftime('%d/%m/%Y')
            elif scenario['od_status'] == '<90D':
                previous_expiry_date = (current_date - timedelta(days=random.choice([15, 45, 89]))).strftime('%d/%m/%Y')
            elif scenario['od_status'] == 'today':
                previous_expiry_date = current_date.strftime('%d/%m/%Y')

            # Third-party tenure calculation
            registration_date_obj = fake.date_between(start_date=date(manufacturing_year, 1, 1), end_date='today')
            registration_date = registration_date_obj.strftime('%d/%m/%Y')
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
        else:
            registration_date = fake.date_between(start_date=date(manufacturing_year, 1, 1), end_date='today').strftime('%d/%m/%Y')

        # Generate customer data
        customer_data = generate_customer_data()

        # Add-ons and discounts
        available_addons = ['ZERO_DEPRECIATION_COVER', 'ROAD_SIDE_ASSISTANCE', 'PERSONAL_ACCIDENT', 'NCB_PROTECTION', 'INCONVENIENCE_ALLOWANCE']
        available_discounts = ['ANTI_THEFT_DISCOUNT', 'TPPD_DISCOUNT', 'VOLUNTARY_DEDUCTIBLE']
        addons = []
        discounts = []
        if scenario['policy_type'] in ['comprehensive', 'OD']:
            num_addons = random.randint(0, len(available_addons))
            selected_addons = random.sample(available_addons, num_addons)
            if 'NCB_PROTECTION' in selected_addons or 'INCONVENIENCE_ALLOWANCE' in selected_addons:
                selected_addons.append('ZERO_DEPRECIATION_COVER')
            addons = [{'insurance_cover_code': addon} for addon in set(selected_addons)]
            num_discounts = random.randint(0, len(available_discounts))
            discounts = [{'discount_code': random.choice(available_discounts)} for _ in range(num_discounts)]

        # Risk start date
        risk_start_date = (current_date + timedelta(days=2)).strftime('%d/%m/%Y') if inspection_required == 'Yes' else current_date.strftime('%d/%m/%Y')

        # KYC details
        kyc_verification = scenario.get('kyc_verification', random.choice(['Yes', 'No']))
        kyc_type = scenario.get('kyc_type', random.choice(['PAN', 'AADHAR', 'CKYC']))
        kyc_details = []
        proposer_pan = ''
        proposer_aadhaar = ''
        if kyc_type == 'PAN':
            proposer_pan = fake.bothify(text='?????####?')
            kyc_details = [{'PAN': {'pan': proposer_pan, 'dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')}}]
        elif kyc_type == 'AADHAR':
            proposer_aadhaar = fake.bothify(text='#### #### ####')
            kyc_details = [{'AADHAR': {'number': proposer_aadhaar, 'dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')}}]
        else:
            kyc_details = [{'CKYC': {'number': fake.bothify(text='##############'), 'dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')}}]

        # Financier details
        has_financier = random.choice([True, False])
        financier_name = fake.company() if has_financier else ''
        financier_type = random.choice(['Bank', 'NBFC']) if has_financier else ''

        # PUC details
        valid_puc = 'Yes'
        puc_number = fake.bothify(text='PUC####')
        puc_expiry = (current_date + timedelta(days=random.randint(1, 365))).strftime('%d/%m/%Y')

        # Nominee details
        nominee_details = {}
        if 'PERSONAL_ACCIDENT' in [addon['insurance_cover_code'] for addon in addons]:
            nominee_details = {
                'nominee_first_name': fake.first_name(),
                'nominee_last_name': fake.last_name(),
                'nominee_age': random.randint(18, 70),
                'nominee_relation': random.choice(['Spouse', 'Parent', 'Child', 'Sibling'])
            }
        no_pa_cover = 'Yes' if 'PERSONAL_ACCIDENT' not in [addon['insurance_cover_code'] for addon in addons] else 'No'

        # Previous policy details
        previous_policy_details = {}
        if scenario['journey_type'] == 'rollover':
            previous_policy_details = {
                'previous_policy_carrier_code': random.choice(['BAJAJ_ALLIANZ', 'TATA_AIG']) if previous_expiry_date else '',
                'previous_policy_type': scenario['policy_type'],
                'previous_policy_number': fake.bothify(text='POL####'),
                'previous_policy_expiry_date': previous_expiry_date,
                'previous_tp_policy_start_date': (datetime.strptime(registration_date, '%d/%m/%Y') - timedelta(days=365 * tp_tenure)).strftime('%d/%m/%Y') if previous_tp_expiry_date else '',
                'previous_tp_policy_expiry_date': previous_tp_expiry_date,
                'previous_tp_policy_carrier_code': random.choice(['BAJAJ_ALLIANZ', 'TATA_AIG']) if previous_tp_expiry_date else '',
                'previous_tp_policy_number': fake.bothify(text='TPPOL####') if previous_tp_expiry_date else ''
            }

        # Company details
        company_details = {}
        if scenario['ownership'] == 'Company':
            company_details = {
                'company_gstin': fake.bothify(text='##AAAAA####A#A#'),
                'company_name': fake.company(),
                'proposer_dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
                'proposer_pan': proposer_pan
            }

        # IDV
        idv_min = 50000
        idv_max = 1500000
        idv = random.randint(idv_min, idv_max) if scenario['journey_type'] == 'without_registration' else 0

        return {
            'Testcase_id': f"{carrier.upper().replace(' ', '_')}_{scenario['category'].upper()}_{scenario['name']}_{testcase_id:03d}",
            'category': scenario['category'],
            'journey_type': scenario['journey_type'],
            'registration_number': customer_data['registration_number'] if scenario['journey_type'] == 'without_registration' else '',
            'make_model': vehicle['make_model'],
            'variant': vehicle['variant'],
            'registration_date': registration_date,
            'rto': random.choice(['KA01', 'MH05', 'MH01', 'KA08']),
            'owned_by': scenario['ownership'],
            'is_ownership_changed': scenario['ownership_changed'],
            'previous_expiry_date': previous_expiry_date,
            'previous_insurer': random.choice(['Bajaj Allianz General Insurance Co. Ltd.', 'Tata AIG General Insurance']) if previous_expiry_date else '',
            'previous_tp_expiry_date': previous_tp_expiry_date,
            'previous_tp_insurer': random.choice(['Bajaj Allianz General Insurance Co. Ltd.', 'Tata AIG General Insurance']) if previous_tp_expiry_date else '',
            'not_sure': 'Yes' if scenario['od_status'] == 'not_sure' or scenario['tp_status'] == 'no_tp' else 'No',
            'know_previous_tp_expiry_date': 'No' if scenario['tp_status'] == 'no_tp' else 'Yes',
            'claim_taken': scenario['claim_taken'],
            'previous_ncb': ncb,
            'product_code': f"{carrier.upper().replace(' ', '_')}_{scenario['category'].upper()}_{scenario['policy_type'].upper()}",
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
                    'registration_number': customer_data['registration_number'] if scenario['journey_type'] == 'without_registration' else '',
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
                'individual_details': {
                    'proposer_first_name': customer_data['name'].split()[0],
                    'proposer_last_name': customer_data['name'].split()[-1] if len(customer_data['name'].split()) > 1 else '',
                    'proposer_dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
                    'proposer_gender': random.choice(['Male', 'Female']),
                    'proposer_title': random.choice(['Mr', 'Ms', 'Mrs']),
                    'proposer_aadhaar': proposer_aadhaar,
                    'proposer_marital_status': random.choice(['Married', 'Single']),
                    'proposer_pan': proposer_pan
                } if scenario['ownership'] == 'Individual' else {},
                'company_details': company_details,
                'customer_address': {
                    'address': customer_data['address'],
                    'is_address_same': random.choice(['Yes', 'No']) if random.choice([True, False]) else '',
                    'registration_address': customer_data['address'] if random.choice([True, False]) else ''
                },
                'previous_policy_details': previous_policy_details,
                'NO_PA_Cover': no_pa_cover
            }),
            'is_inspection_required': inspection_required,
            'carrier_name': carrier,
            'payment_time': current_date.strftime('%d/%m/%Y %H:%M:%S'),
            'risk_start_date': risk_start_date,
            'breakin_inspection_approval': 'Yes' if inspection_required == 'Yes' else 'No'
        }
    except Exception:
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
        
        # Filter invalid combinations
        if journey_type in ['new_journey', 'without_registration'] and (od_status != 'not_sure' or tp_status != 'no_tp'):
            continue
        if policy_type == 'third_party' and od_status != 'not_sure':
            continue
        if journey_type == 'rollover' and od_status == 'not_sure':
            continue
        if manufacturing_year == '<2010' and 'VEHICLE_AGE_GT_15Y' not in scenarios:
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
    test_cases = []
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

# Generate test cases
all_scenarios = scenarios + expand_scenarios()
try:
    test_cases = generate_test_cases_parallel(all_scenarios)
except KeyboardInterrupt:
    pd.DataFrame(test_cases).to_csv('automation_data_table_temp.csv', index=False)
except Exception:
    pd.DataFrame(test_cases).to_csv('automation_data_table_temp.csv', index=False)

# Save to Excel
try:
    df = pd.DataFrame(test_cases)
    df.to_excel('automation_data_table_generated.xlsx', index=False)
    print(f"Excel file generated: automation_data_table_generated.xlsx with {len(test_cases)} test cases")
except Exception:
    sys.exit(1)