import pandas as pd
from google import genai
from faker import Faker
from datetime import datetime, timedelta
import random
import json
import itertools
from tqdm import tqdm
import os
from dotenv import load_dotenv
import sys
import backoff




load_dotenv()


fake = Faker('en_IN')

try:
    client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"Failed to initialize Gemini API client: {e}")
    sys.exit(1)

# Define the 18 provided scenarios with unique names
scenarios = [
    {'name': 'NB_Not_Sure_No_TP', 'category': 'four_wheeler', 'journey_type': 'new_journey', 'tp_status': 'no_tp', 'od_status': 'not_sure', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive'},
    {'name': 'NB_Not_Sure_TP_3D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '<3D', 'od_status': 'not_sure', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive'},
    {'name': 'NB_Not_Sure_TP_60D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '<60D', 'od_status': 'not_sure', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive'},
    {'name': 'NB_Not_Sure_TP_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '>90D', 'od_status': 'not_sure', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive'},
    {'name': 'RO_2018_09_Active_Exp_T', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': 'today', 'od_status': 'today', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '<2018-09'},
    {'name': 'RO_2018_09_Active_Exp_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '>90D', 'od_status': '>90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '<2018-09'},
    {'name': 'RO_2018_09_Expired_Exp_LT_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '<90D', 'od_status': '<90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '<2018-09'},
    {'name': 'RO_2018_09_Expired_Exp_GT_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '>90D', 'od_status': '>90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '<2018-09'},
    {'name': 'RO_2018_09_Active_OD_T_TP_T', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': 'today', 'od_status': 'today', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Active_OD_T_TP_60D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '<60D', 'od_status': 'today', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Active_OD_T_TP_60D_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '60D-90D', 'od_status': 'today', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Active_OD_T_TP_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '>90D', 'od_status': 'today', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Active_OD_90D_TP_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '>90D', 'od_status': '>90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Expired_OD_90D_TP_T', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': 'today', 'od_status': '<90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Expired_OD_90D_TP_60D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '<60D', 'od_status': '<90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Expired_OD_90D_TP_60D_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '60D-90D', 'od_status': '<90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Expired_OD_90D_TP_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '>90D', 'od_status': '<90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
    {'name': 'RO_2018_09_Expired_OD_GT_90D_TP_90D', 'category': 'four_wheeler', 'journey_type': 'without_registration', 'tp_status': '>90D', 'od_status': '>90D', 'ownership': 'Individual', 'ownership_changed': 'No', 'claim_taken': 'No', 'policy_type': 'comprehensive', 'manufacturing_year': '>2018-09'},
]


carriers = [
    'Reliance Motor',
    'Future Generali India',
    'Royal Sundaram General Insurance Co. Ltd',
    'ICICI Lombard General Insurance',
    'GoDigit',
    'SBI General Insurance',
    'HDFC Ergo General Insurance',
    'Cholamandalam MS General Insurance'
]

vehicles = [
    {'category': 'two_wheeler', 'make_model': 'BAJAJ PULSAR', 'variant': '200 NS BSIV (CC - 200 Seat Cap - 2 Fuel - Petrol)'},
    {'category': 'two_wheeler', 'make_model': 'HONDA ACTIVA', 'variant': '5G (CC - 109 Seat Cap - 2 Fuel - Petrol)'},
    {'category': 'four_wheeler', 'make_model': 'MARUTI SUZUKI ALTO', 'variant': 'LXi (CC - 796 Seat Cap - 5 Fuel - CNG)'},
    {'category': 'four_wheeler', 'make_model': 'HONDA CITY', 'variant': '1.5 V MT (CC - 1497 Seat Cap - 5 Fuel - Petrol)'}
]


@backoff.on_exception(
    backoff.expo,
    Exception,
    max_tries=3,
    max_time=60
)
def generate_customer_data():
    prompt = """
    Generate a realistic Indian customer profile for a motor insurance test case, including:
    - name (e.g., Siddarth Sharma)
    - phone_number (10-digit, e.g., 9876543210)
    - email (e.g., siddarth.sharma@gmail.com)
    - registration_number (format: XX##XX####, e.g., KA01JK1234)
    - address (JSON object with address_line_1, pincode, city, state, e.g., {"address_line_1": "123 MG Road", "pincode": "560001", "city": "Bangalore", "state": "Karnataka"})
    Ensure the data is consistent with Indian demographics and formats.
    Return the response as a JSON object.
    """
    required_keys = ['name', 'phone_number', 'email', 'registration_number', 'address']
    address_keys = ['address_line_1', 'pincode', 'city', 'state']
    fallback_data = {
        'name': fake.name(),
        'phone_number': fake.phone_number()[:10],
        'email': fake.email(),
        'registration_number': fake.bothify(text='??##??####'),
        'address': {
            'address_line_1': fake.street_address(),
            'pincode': fake.postcode(),
            'city': fake.city(),
            'state': fake.state()
        }
    }

    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash-001',
            contents=prompt
        )
        response_text = response.text.strip()

       
        if response_text.startswith('```json'):
            response_text = response_text[7:-3].strip()
        elif response_text.startswith('```'):
            response_text = response_text[3:-3].strip()

     
        try:
            customer_data = json.loads(response_text)
        except json.JSONDecodeError:
            return fallback_data

        
        if not isinstance(customer_data, dict):
            return fallback_data

        
        missing_keys = [key for key in required_keys if key not in customer_data]
        if missing_keys:
            return fallback_data

       
        if not isinstance(customer_data['address'], dict):
            customer_data['address'] = fallback_data['address']
        else:
            missing_address_keys = [key for key in address_keys if key not in customer_data['address']]
            if missing_address_keys:
                customer_data['address'] = fallback_data['address']

      
        if not isinstance(customer_data['phone_number'], str) or not customer_data['phone_number'].isdigit() or len(customer_data['phone_number']) != 10:
            customer_data['phone_number'] = fallback_data['phone_number']
        if not isinstance(customer_data['registration_number'], str) or not len(customer_data['registration_number']) == 10:
            customer_data['registration_number'] = fallback_data['registration_number']
        if '@' not in customer_data['email']:
            customer_data['email'] = fallback_data['email']

        return customer_data
    except Exception:
        return fallback_data


def generate_test_case(scenario, testcase_id):
    vehicle = random.choice([v for v in vehicles if v['category'] == scenario['category']])
    carrier = random.choice(carriers)
    manufacturing_year = random.randint(2010, 2023) if scenario.get('manufacturing_year', '') == '>2018-09' else random.randint(2010, 2018)

    
    ncb = 0
    inspection_required = 'Yes'
    if scenario['claim_taken'] == 'Yes' or scenario['ownership_changed'] == 'Yes':
        ncb = 0
    elif scenario['od_status'] in ['today', '<90D'] and scenario['tp_status'] in ['today', '<3D', '<60D']:
        ncb = random.choice([0.2, 0.25, 0.35, 0.45, 0.5])
        inspection_required = 'No' if scenario['od_status'] == 'today' and scenario['tp_status'] == 'today' else 'Yes'

 
    current_year = 2025
    if manufacturing_year < 2010:
        print(f"Vehicle manufactured in {manufacturing_year} is >15 years old, not eligible for quotes")
        return None

    
    current_date = datetime(2025, 5, 22)
    previous_expiry_date = ''
    previous_tp_expiry_date = ''
    if scenario['od_status'] == '>90D':
        previous_expiry_date = (current_date - timedelta(days=random.randint(91, 365))).strftime('%d/%m/%Y')
    elif scenario['od_status'] == '<90D':
        previous_expiry_date = (current_date - timedelta(days=random.randint(1, 89))).strftime('%d/%m/%Y')
    elif scenario['od_status'] == 'today':
        previous_expiry_date = current_date.strftime('%d/%m/%Y')

    if scenario['tp_status'] == '>90D':
        previous_tp_expiry_date = (current_date - timedelta(days=random.randint(91, 365))).strftime('%d/%m/%Y')
    elif scenario['tp_status'] == '<60D':
        previous_tp_expiry_date = (current_date - timedelta(days=random.randint(4, 59))).strftime('%d/%m/%Y')
    elif scenario['tp_status'] == '<3D':
        previous_tp_expiry_date = (current_date - timedelta(days=random.randint(1, 3))).strftime('%d/%m/%Y')
    elif scenario['tp_status'] == 'today':
        previous_tp_expiry_date = current_date.strftime('%d/%m/%Y')
    elif scenario['tp_status'] == '60D-90D':
        previous_tp_expiry_date = (current_date - timedelta(days=random.randint(60, 89))).strftime('%d/%m/%Y')

   
    try:
        customer_data = generate_customer_data()
    except Exception as e:
        print(f"Critical error in generate_customer_data: {e}. Stopping execution.")
        sys.exit(1)

    
    addons = []
    discounts = []
    if scenario['policy_type'] == 'comprehensive':
        addons = [{'insurance_cover_code': random.choice(['ZERO_DEPRECIATION_COVER', 'ROAD_SIDE_ASSISTANCE', 'PERSONAL_ACCIDENT', 'LL_PAID_DRIVER', 'ENGINE_PROTECTOR'])}]
        discounts = [{'discount_code': random.choice(['ANTI_THEFT_DISCOUNT', 'TPPD_DISCOUNT', 'VOLUNTARY_DEDUCTIBLE'])}]

    return {
        'Testcase_id': f"{carrier.upper().replace(' ', '_')}_{scenario['category'].upper()}_{scenario['name']}_{testcase_id:03d}",
        'category': scenario['category'],
        'journey_type': scenario['journey_type'],
        'registration_number': customer_data['registration_number'] if scenario['journey_type'] == 'without_registration' else '',
        'make_model': vehicle['make_model'],
        'variant': vehicle['variant'],
        'registration_date': fake.date_between(start_date='-15y', end_date='today').strftime('%d/%m/%Y') if manufacturing_year >= 2010 else '',
        'rto': random.choice(['KA01', 'MH05', 'MH01', 'KA08']),
        'owned_by': scenario['ownership'],
        'is_ownership_changed': scenario['ownership_changed'],
        'previous_expiry_date': previous_expiry_date,
        'previous_insurer': random.choice(['Bajaj Allianz General Insurance Co. Ltd.', 'Tata AIG General Insurance']) if previous_expiry_date else '',
        'previous_tp_expiry_date': previous_tp_expiry_date,
        'previous_tp_insurer': random.choice(['Bajaj Allianz General Insurance Co. Ltd.', 'Tata AIG General Insurance']) if previous_tp_expiry_date else '',
        'not_sure': 'Yes' if scenario['od_status'] == 'not_sure' or scenario['tp_status'] == 'not_sure' else 'No',
        'know_previous_tp_expiry_date': 'No' if scenario['tp_status'] == 'not_sure' else 'Yes',
        'claim_taken': scenario['claim_taken'],
        'previous_ncb': ncb,
        'product_code': f"{carrier.upper().replace(' ', '_')}_{scenario['category'].upper()}_{scenario['policy_type'].upper()}",
        'customer_name': customer_data['name'],
        'contact_number': customer_data['phone_number'],
        'idv': random.choice(['Max', 'Min', 500000, 250000]) if scenario['journey_type'] == 'without_registration' else '',
        'ncb_two': random.choice([0, 0.2, 0.25, 0.35]) if scenario['category'] == 'two_wheeler' and ncb > 0 else 0,
        'addons': json.dumps(addons),
        'discounts': json.dumps(discounts),
        'select_tab': scenario['policy_type'],
        'email': customer_data['email'],
        'kyc': json.dumps([{'PAN': {'pan': fake.bothify(text='?????####?'), 'dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')}}]),
        'kyc_verification': 'Yes',
        'proposal_questions': json.dumps({
            'manufacturing_year': str(manufacturing_year),
            'registration_number': customer_data['registration_number'] if scenario['journey_type'] == 'without_registration' else '',
            'engine_number': fake.bothify(text='##########'),
            'chassis_number': fake.bothify(text='#################'),
            'proposer_first_name': customer_data['name'].split()[0],
            'proposer_last_name': customer_data['name'].split()[-1] if len(customer_data['name'].split()) > 1 else '',
            'proposer_dob': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
            'proposer_gender': random.choice(['Male', 'Female']),
            'proposer_email': customer_data['email'],
            'proposer_phone_number': customer_data['phone_number'],
            'address': customer_data['address']
        }),
        'is_inspection_required': inspection_required,
        'carrier_name': carrier
    }


def expand_scenarios():
    categories = ['two_wheeler', 'four_wheeler']
    journey_types = ['new_journey', 'without_registration']
    policy_types = ['comprehensive', 'third_party', 'OD']
    ownerships = ['Individual', 'Corporate']
    ownership_changes = ['Yes', 'No']
    claims = ['Yes', 'No']
    manufacturing_years = ['<2018-09', '>2018-09']

    additional_scenarios = []
    combinations = itertools.product(categories, journey_types, policy_types, ownerships, ownership_changes, claims, manufacturing_years)
    for i, combo in enumerate(combinations, len(scenarios) + 1):
        additional_scenarios.append({
            'name': f'ADDITIONAL_{i}',
            'category': combo[0],
            'journey_type': combo[1],
            'tp_status': random.choice(['no_tp', '<3D', '<60D', '>90D', 'today', '60D-90D']),
            'od_status': random.choice(['not_sure', 'today', '<90D', '>90D']),
            'ownership': combo[3],
            'ownership_changed': combo[4],
            'claim_taken': combo[5],
            'policy_type': combo[2],
            'manufacturing_year': combo[6]
        })
    return additional_scenarios


test_cases = []
all_scenarios = scenarios + expand_scenarios()[:50]
total_scenarios = len(all_scenarios)

try:
    with tqdm(total=total_scenarios, desc="Generating test cases", unit="scenario") as pbar:
        for i, scenario in enumerate(all_scenarios, 1):
            try:
                test_case = generate_test_case(scenario, i)
                if test_case:
                    test_cases.append(test_case)
                pbar.update(1)
            except Exception as e:
                print(f"Error generating test case for scenario {scenario['name']}: {e}")
                if any(keyword in str(e).lower() for keyword in ['resourceexhausted', 'quota', 'memory']):
                    print("Resource exhaustion detected. Stopping execution.")
                    sys.exit(1)
                continue
except KeyboardInterrupt:
    print("Process interrupted by user. Saving progress...")
except Exception as e:
    print(f"Unexpected error: {e}. Saving progress...")


try:
    df = pd.DataFrame(test_cases)
    df.to_excel('automation_data_table_generated.xlsx', index=False)
    print("Excel file generated: automation_data_table_generated.xlsx")
except Exception as e:
    print(f"Error saving Excel file: {e}")
    sys.exit(1)
