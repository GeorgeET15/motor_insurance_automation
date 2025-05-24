import pandas as pd
from faker import Faker
import random
import json
import itertools
import logging
import re
from datetime import datetime, timedelta
from tqdm import tqdm
from data.test_case_data import carriers, vehicles, city_state_mapping, base_idv_ranges, products, available_addons

# Initialize Faker
fake = Faker('en_IN')

# Pre-generate customer data pool
def pre_generate_customer_data_pool(size=1000):
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

customer_data_pool = pre_generate_customer_data_pool(1000)

def calculate_depreciation(vehicle_age):
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

def setup_logging():
    log_file = "test_data_generation_log.txt"
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Logging initialized")
    return log_file

def infer_scenario_details(s_no):
    logging.info("Inferring details for scenario: %s", s_no)
    s_no_lower = s_no.lower()
    
    # Default scenario
    scenario = {
        'name': s_no,
        'category': 'two_wheeler',  # Default
        'journey_type': 'new_journey',
        'policy_type': 'comprehensive',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'kyc_verification': random.choice(['Yes', 'No']),
        'kyc_type': random.choice(['PAN', 'AADHAR', 'CKYC']),
        'manufacturing_year': '>2018-09'
    }
    
    # Parse scenario string
    if 'four' in s_no_lower:
        scenario['category'] = 'four_wheeler'
    if 'nb' in s_no_lower:
        scenario['journey_type'] = 'new_journey'
    if 'ro' in s_no_lower:
        scenario['journey_type'] = 'rollover'
    if 'without' in s_no_lower:
        scenario['journey_type'] = 'without_registration'
    if 'comp' in s_no_lower:
        scenario['policy_type'] = 'comprehensive'
    if 'tp' in s_no_lower:
        scenario['policy_type'] = 'third_party'
    if 'od' in s_no_lower:
        scenario['policy_type'] = 'OD'
    if 'company' in s_no_lower:
        scenario['ownership'] = 'Company'
    if 'change' in s_no_lower:
        scenario['ownership_changed'] = 'Yes'
    if 'claim' in s_no_lower:
        scenario['claim_taken'] = 'Yes'
    if any(x in s_no_lower for x in ['break-in', '6_', 'not_sure']):
        scenario['tp_status'] = 'no_tp' if 'not_sure' in s_no_lower else '>90D'
        scenario['od_status'] = 'not_sure' if 'not_sure' in s_no_lower else '>90D'
    if 'old' in s_no_lower or '2010' in s_no_lower:
        scenario['manufacturing_year'] = '<2010'
    if '2018' in s_no_lower:
        scenario['manufacturing_year'] = '<2018-09'
    
    description = f"Custom scenario: {scenario['category'].replace('_', ' ')}, {scenario['journey_type'].replace('_', ' ')}, {scenario['policy_type']}"
    if scenario['ownership_changed'] == 'Yes':
        description += ", ownership changed"
    if scenario['claim_taken'] == 'Yes':
        description += ", claim taken"
    if 'addon' in s_no_lower and 'without add-on' not in s_no_lower:
        description += ", with add-ons"
    if 'break-in' in s_no_lower or '6_' in s_no_lower:
        description += ", break-in"
    
    logging.info("Inferred scenario: %s, Description: %s", scenario, description)
    return scenario, description

def generate_test_data(s_no, scenario, description):
    logging.info("Generating test data for scenario: %s - %s", s_no, description)
    
    # Variation options
    claim_taken_options = ['Yes', 'No'] if scenario['journey_type'] not in ['new_journey', 'without_registration'] else ['No']
    ncb_options = ['0%', '20%', '25%', '35%', '45%', '50%'] if scenario['journey_type'] == 'rollover' and scenario['ownership_changed'] == 'No' else ['0%']
    addon_counts = [0] if 'without add-on' in s_no.lower() else ([0, 1, 2, 3] if scenario['policy_type'] in ['comprehensive', 'OD'] and 'addon' in s_no.lower() else [0])
    kyc_verification_options = ['Yes', 'No']
    kyc_type_options = ['PAN', 'AADHAR', 'CKYC']
    tp_status_options = ['no_tp', '<3D', '<60D', '>90D', 'today', '60D-90D'] if scenario['journey_type'] == 'rollover' else ['no_tp']
    od_status_options = ['today', '<90D', '>90D'] if scenario['journey_type'] == 'rollover' else ['not_sure']
    
    test_data_list = []
    current_date = datetime.now()
    current_year = current_date.year
    
    for claim, ncb, addon_count, kyc_ver, kyc_type, tp_status, od_status in itertools.product(
        claim_taken_options, ncb_options, addon_counts, kyc_verification_options, kyc_type_options, tp_status_options, od_status_options
    ):
        # Skip invalid combinations
        if scenario['journey_type'] in ['new_journey', 'without_registration'] and (od_status != 'not_sure' or tp_status != 'no_tp'):
            continue
        if scenario['policy_type'] == 'third_party' and od_status != 'not_sure':
            continue
        if scenario['journey_type'] == 'rollover' and od_status == 'not_sure':
            continue
        
        # Update scenario with variations
        temp_scenario = scenario.copy()
        temp_scenario['claim_taken'] = claim
        temp_scenario['kyc_verification'] = kyc_ver
        temp_scenario['kyc_type'] = kyc_type
        temp_scenario['tp_status'] = tp_status
        temp_scenario['od_status'] = od_status
        
        # Vehicle selection
        vehicle = random.choice([v for v in vehicles if v['category'] == temp_scenario['category']])
        variant = vehicle['variant']
        engine_cc = int(re.search(r'CC - (\d+)', variant).group(1)) if re.search(r'CC - (\d+)', variant) else 1000
        fuel_type = re.search(r'Fuel - (\w+)', variant).group(1) if re.search(r'Fuel - (\w+)', variant) else 'Petrol'
        
        # Product selection
        category_code = 'MOTOR_RETAIL' if temp_scenario['category'] == 'four_wheeler' else 'TWO_WHEELER_RETAIL'
        product_class = {'comprehensive': 'Comprehensive', 'third_party': 'TP Only', 'OD': 'OD Only'}[temp_scenario['policy_type']]
        matching_products = [p for p in products if p['category_code'] == category_code and p['product_class'] == product_class]
        if not matching_products:
            continue
        product = random.choice(matching_products)
        
        # Manufacturing year
        if temp_scenario['manufacturing_year'] == '<2018-09':
            manufacturing_year = random.randint(2000, 2018)
            manufacturing_date = datetime(manufacturing_year, random.randint(1, 8), 1)
        elif temp_scenario['manufacturing_year'] == '<2010':
            manufacturing_year = random.randint(2000, 2009)
            manufacturing_date = datetime(manufacturing_year, random.randint(1, 12), 1)
        else:
            manufacturing_year = random.randint(max(2000, current_year - 5), current_year)  # Avoid future years
            manufacturing_date = datetime(manufacturing_year, random.randint(1, 12), 1)
        
        vehicle_age = current_year - manufacturing_year
        if vehicle_age > 15 and temp_scenario['name'] != 'VEHICLE_AGE_GT_15Y':
            continue
        
        # IDV calculation
        base_idv_min, base_idv_max = base_idv_ranges.get(vehicle['make_model'], (50000, 1500000))
        depreciation = calculate_depreciation(vehicle_age)
        idv_adjustment = 1.0
        if fuel_type == 'Diesel':
            idv_adjustment *= 1.1
        if temp_scenario['category'] == 'four_wheeler' and engine_cc > 1500:
            idv_adjustment *= 1.2
        elif temp_scenario['category'] == 'two_wheeler' and engine_cc > 250:
            idv_adjustment *= 1.15
        if temp_scenario['ownership_changed'] != 'Yes' and claim == 'Yes':
            idv_adjustment *= 0.95
        idv_min = int(base_idv_min * (1 - depreciation) * idv_adjustment * 0.8)
        idv_max = int(base_idv_max * (1 - depreciation) * idv_adjustment * 1.2)
        idv = random.randint(idv_min, idv_max) if temp_scenario['journey_type'] != 'new_journey' else 0
        
        # Inspection
        inspection_required = 'No'
        if temp_scenario['journey_type'] == 'new_journey':
            inspection_required = 'No'
        elif temp_scenario['ownership_changed'] == 'Yes':
            inspection_required = 'Yes'
        elif temp_scenario['journey_type'] == 'rollover':
            expired_statuses = ['>90D', '<90D', '<60D', '<3D', '60D-90D']
            if od_status in expired_statuses or tp_status in expired_statuses:
                inspection_required = 'Yes'
            elif od_status == 'today' and tp_status == 'today':
                inspection_required = 'No'
        
        # NCB
        ncb_value = ''
        if temp_scenario['journey_type'] == 'rollover' and temp_scenario['ownership_changed'] != 'Yes':
            ncb_value = '0%' if claim == 'Yes' else ncb
        
        # Expiry dates
        previous_expiry_date = ''
        previous_tp_expiry_date = ''
        registration_year = min(manufacturing_year, current_year)  # Ensure registration_year is not in the future
        start_date = datetime(registration_year, 1, 1)
        max_date = min(datetime.now(), datetime(registration_year, 12, 31))
        if start_date >= max_date:
            max_date = start_date + timedelta(days=1)  # Ensure at least one day range
        try:
            registration_date_obj = fake.date_between(start_date=start_date, end_date=max_date)
            registration_date = registration_date_obj.strftime('%d/%m/%Y')
            logging.info("Generated registration_date: %s for registration_year: %s", registration_date, registration_year)
        except ValueError as e:
            logging.error("Failed to generate registration_date for year %s: %s", registration_year, str(e))
            continue
        
        if temp_scenario['journey_type'] == 'rollover':
            if od_status == '>90D':
                previous_expiry_date = (current_date - timedelta(days=random.choice([120, 123, 365]))).strftime('%d/%m/%Y')
            elif od_status == '<90D':
                previous_expiry_date = (current_date - timedelta(days=random.randint(15, 89))).strftime('%d/%m/%Y')
            elif od_status == 'today':
                previous_expiry_date = current_date.strftime('%d/%m/%Y')
            tp_tenure = random.choice([1, 3]) if temp_scenario['category'] == 'four_wheeler' else random.choice([1, 5])
            if tp_status == '>90D':
                previous_tp_expiry_date = (current_date - timedelta(days=random.choice([120, 365]))).strftime('%d/%m/%Y')
            elif tp_status == '<60D':
                previous_tp_expiry_date = (current_date - timedelta(days=random.randint(4, 59))).strftime('%d/%m/%Y')
            elif tp_status == '<3D':
                previous_tp_expiry_date = (current_date - timedelta(days=random.randint(1, 3))).strftime('%d/%m/%Y')
            elif tp_status == 'today':
                previous_tp_expiry_date = current_date.strftime('%d/%m/%Y')
            elif tp_status == '60D-90D':
                previous_tp_expiry_date = (current_date - timedelta(days=random.randint(60, 90))).strftime('%d/%m/%Y')
        
        # Customer data
        customer_data = random.choice(customer_data_pool)
        registration_number = '' if temp_scenario['journey_type'] == 'without_registration' else customer_data['registration_number']
        
        # Other fields
        not_sure = 'Yes' if temp_scenario['od_status'] == 'not_sure' or temp_scenario['tp_status'] == 'no_tp' else 'No'
        previous_insurer = random.choice(carriers) if previous_expiry_date else ''
        previous_tp_insurer = random.choice(carriers) if previous_tp_expiry_date else ''
        know_previous_tp_expiry_date = 'No' if temp_scenario['tp_status'] == 'no_tp' else 'Yes'
        
        # Add-ons and discounts
        temp_addons = available_addons.copy()
        if temp_scenario['category'] == 'four_wheeler':
            temp_addons.append('LPG_CNG_KIT_IDV')
        selected_addons = random.sample(temp_addons, addon_count) if addon_count > 0 else []
        if 'NCB_PROTECTION' in selected_addons or 'LOSS_OF_USE' in selected_addons:
            selected_addons.append('ZERO_DEPRECIATION_COVER')
        addons = [{'insurance_cover_code': addon} for addon in set(selected_addons)]
        available_discounts = ['TPPD_DISCOUNT', 'VOLUNTARY_DEDUCTIBLE_DISCOUNT', 'ANTI_THEFT_DISCOUNT']
        discounts = [{'discount_code': random.choice(available_discounts)} for _ in range(random.randint(0, len(available_discounts)))]
        
        # KYC
        proposer_pan = ''
        proposer_aadhaar = ''
        kyc_details = []
        if kyc_ver == 'Yes':
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
        
        # Financier
        has_financier = random.choice([True, False])
        financier_name = fake.company() if has_financier else ''
        financier_type = random.choice(['Bank', 'NBFC']) if has_financier else ''
        
        # PUC
        valid_puc = 'Yes'
        puc_number = fake.bothify(text='PUC####')
        puc_expiry = (current_date + timedelta(days=random.randint(1, 365))).strftime('%d/%m/%Y')
        
        # Nominee
        nominee_details = {}
        no_pa_cover = 'Yes' if 'PERSONAL_ACCIDENT' not in [addon['insurance_cover_code'] for addon in addons] else 'No'
        if 'PERSONAL_ACCIDENT' in [addon['insurance_cover_code'] for addon in addons]:
            nominee_details = {
                'nominee_first_name': fake.first_name(),
                'nominee_last_name': fake.last_name(),
                'nominee_age': random.randint(18, 70),
                'nominee_relation': random.choice(['Spouse', 'Parent', 'Child', 'Sibling'])
            }
        
        # Previous policy
        previous_policy_details = {}
        if temp_scenario['journey_type'] == 'rollover':
            previous_policy_details = {
                'previous_policy_carrier_code': random.choice(['BAJAJ_ALLIANZ', 'TATA_AIG']) if previous_expiry_date else '',
                'previous_policy_type': temp_scenario['policy_type'],
                'previous_policy_number': fake.bothify(text='POL####'),
                'previous_policy_expiry_date': previous_expiry_date
            }
            if temp_scenario['policy_type'] != 'comprehensive':
                previous_policy_details.update({
                    'previous_tp_policy_start_date': (datetime.strptime(registration_date, '%d/%m/%Y') - timedelta(days=365 * tp_tenure)).strftime('%d/%m/%Y') if previous_tp_expiry_date else '',
                    'previous_tp_policy_expiry_date': previous_tp_expiry_date,
                    'previous_tp_policy_carrier_code': random.choice(['BAJAJ_ALLIANZ', 'TATA_AIG']) if previous_tp_expiry_date else '',
                    'previous_tp_policy_number': fake.bothify(text='TPPOL####') if previous_tp_expiry_date else ''
                })
        
        # Company/Individual details
        company_details = {}
        if temp_scenario['ownership'] == 'Company':
            company_details = {
                'company_gstin': fake.bothify(text='##AAAAA####A#A#'),
                'company_name': fake.company(),
                'proposer_dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
                'proposer_pan': proposer_pan
            }
        individual_details = {}
        if temp_scenario['ownership'] == 'Individual':
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
        
        # Test case
        test_case = {
            'Testcase_id': f"{product['insurance_company_code']}_{temp_scenario['category'].upper()}_{temp_scenario['name']}_{len(test_data_list) + 1:03d}",
            'category': temp_scenario['category'],
            'journey_type': temp_scenario['journey_type'],
            'registration_number': registration_number,
            'make_model': vehicle['make_model'],
            'variant': variant,
            'registration_date': registration_date,
            'rto': random.choice(['KA01', 'MH05', 'MH01', 'KA08']),
            'owned_by': temp_scenario['ownership'],
            'is_ownership_changed': temp_scenario['ownership_changed'],
            'previous_expiry_date': previous_expiry_date,
            'previous_insurer': previous_insurer,
            'previous_tp_expiry_date': previous_tp_expiry_date,
            'previous_tp_insurer': previous_tp_insurer,
            'not_sure': not_sure,
            'know_previous_tp_expiry_date': know_previous_tp_expiry_date,
            'claim_taken': claim if temp_scenario['journey_type'] not in ['new_journey', 'without_registration'] else '',
            'previous_ncb': ncb_value,
            'product_code': product['code'],
            'customer_name': customer_data['name'],
            'contact_number': customer_data['phone_number'],
            'idv': idv,
            'idv_min': idv_min,
            'idv_max': idv_max,
            'addons': json.dumps(addons),
            'discounts': json.dumps(discounts),
            'select_tab': temp_scenario['policy_type'],
            'email': customer_data['email'],
            'kyc': json.dumps(kyc_details),
            'kyc_verification': kyc_ver,
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
                'proposal_occupation': fake.job() if temp_scenario['ownership'] == 'Individual' else 'Business Owner'
            }),
            'is_inspection_required': inspection_required,
            'carrier_name': product['carrier_name'],
            'payment_time': current_date.strftime('%d/%m/%Y %H:%M:%S'),
            'breakin_inspection_approval': 'Yes' if inspection_required == 'Yes' else 'No'
        }
        
        test_data_list.append(test_case)
        logging.info("Generated test data: Testcase_id=%s", test_case['Testcase_id'])
    
    return test_data_list

def save_results(test_data_list, input_scenario):
    if not test_data_list:
        logging.error("No test data generated for scenario: %s", input_scenario)
        return None
    df = pd.DataFrame(test_data_list)
    output_file = f"test_data_{input_scenario.replace(' ', '_')}.xlsx"
    df.to_excel(output_file, index=False)
    logging.info("Results saved to %s with %d test cases", output_file, len(test_data_list))
    return output_file

def main():
    log_file = setup_logging()
    input_scenario = input("Enter the scenario (e.g., 1_NB_comp, Custom_break-in, XYZ_addons): ").strip()
    scenario, description = infer_scenario_details(input_scenario)
    test_data_list = generate_test_data(input_scenario, scenario, description)
    output_file = save_results(test_data_list, input_scenario)
    if output_file:
        print(f"Test data generated and saved to {output_file}, logs saved to {log_file}")
    else:
        print("No test data generated. Check logs for details.")

if __name__ == "__main__":
    main()