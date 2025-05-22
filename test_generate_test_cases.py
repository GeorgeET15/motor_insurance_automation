import pytest
import json
from generate_test_cases import generate_test_case

def test_ncb_zero_for_claims():
    scenario = {
        'name': 'NB_Not_Sure_No_TP',
        'category': 'four_wheeler',
        'journey_type': 'new_journey',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'Yes',
        'policy_type': 'comprehensive'
    }
    test_case = generate_test_case(scenario, 1)
    assert test_case['previous_ncb'] == 0, "NCB should be 0 when claim is taken"

def test_ncb_zero_for_ownership_change():
    scenario = {
        'name': 'NB_Not_Sure_No_TP',
        'category': 'four_wheeler',
        'journey_type': 'new_journey',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'comprehensive'
    }
    test_case = generate_test_case(scenario, 1)
    assert test_case['previous_ncb'] == 0, "NCB should be 0 when ownership has changed"

def test_inspection_required_for_break_in():
    scenario = {
        'name': 'RO_2018_09_Expired_Exp_GT_90D',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': '>90D',
        'od_status': '>90D',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09'
    }
    test_case = generate_test_case(scenario, 1)
    assert test_case['is_inspection_required'] == 'Yes', "Inspection should be required for break-in >90 days"

def test_no_inspection_for_active_policy():
    scenario = {
        'name': 'RO_2018_09_Active_OD_T_TP_T',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': 'today',
        'od_status': 'today',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09'
    }
    test_case = generate_test_case(scenario, 1)
    assert test_case['is_inspection_required'] == 'No', "No inspection should be required for active policy expiring today"

def test_vehicle_age_rejection():
    scenario = {
        'name': 'RO_2018_09_Expired_Exp_GT_90D',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': '>90D',
        'od_status': '>90D',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '<2018-09'
    }
    import random
    original_randint = random.randint
    random.randint = lambda a, b: 2008
    test_case = generate_test_case(scenario, 1)
    random.randint = original_randint
    assert test_case is None, "Test case should be None for vehicles >15 years old"

def test_addons_for_comprehensive():
    scenario = {
        'name': 'NB_Not_Sure_No_TP',
        'category': 'four_wheeler',
        'journey_type': 'new_journey',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive'
    }
    test_case = generate_test_case(scenario, 1)
    addons = json.loads(test_case['addons'])
    assert len(addons) > 0, "Comprehensive policy should include add-ons"

def test_customer_data_keys():
    scenario = {
        'name': 'NB_Not_Sure_No_TP',
        'category': 'four_wheeler',
        'journey_type': 'new_journey',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive'
    }
    test_case = generate_test_case(scenario, 1)
    assert all(key in test_case for key in ['customer_name', 'contact_number', 'email', 'registration_number']), "Customer data should include all required keys"
    assert all(key in json.loads(test_case['proposal_questions'])['address'] for key in ['address_line_1', 'pincode', 'city', 'state']), "Address should include all required keys"
