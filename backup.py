import pandas as pd
from datetime import datetime, timedelta
import json

proposal_questions_dict = {
    "manufacturing_year": "2023",
    "registration_number": "",
    "engine_number": "234we32432",
    "chassis_number": "78u781678936y6789",
    "financier_name": "",
    "financier_type": "",
    "gstin": "27AAUFM1756H1ZT",
    "company_name": "UMBO IDTECH PRIVATE LIMITED",
    "proposer_email": "nisha.kalpathri@riskcovry.com",
    "proposer_phone_number": "8970985822",
    "address": json.dumps({
        "address_line_1": "D/O SUBBARAO",
        "address_line_2": "SHIVAJI NAGAR",
        "pincode": "590001",
        "city": "Belgaum",
        "state": "Karnataka"
    })
}

base_data = {
    "Testcase_id": "ICICI_LOMBARD_PC_THIRD_PARTY_01",
    "category": "four_wheeler",
    "journey_type": "new_journey",
    "registration_number": "",
    "make_model": "HONDA CITY",
    "variant": "1.3 LXi (CC - 1343 Seat Cap - 5 Fuel - Petrol)",
    "registration_date": "",
    "rto": "KA01",
    "owned_by": "Individual",
    "is_ownership_changed": "No",
    "previous_expiry_date": "",
    "offset_previous_expiry_date": "",
    "previous_insurer": "",
    "previous_tp_expiry_date": "",
    "offset_previous_tp_expiry_date": "",
    "previous_tp_insurer": "",
    "not_sure": "",
    "know_previous_tp_expiry_date": "",
    "not_sure_previous_tp_expiry_date": "",
    "claim_taken": "",
    "previous_ncb": "0%",
    "product_code": "ICICI_LOMBARD_PC_THIRD_PARTY",
    "customer_name": "Nisha",
    "contact_number": "8970985822",
    "idv": "",
    "NCB_two": "",
    "addons": "",  
    "discounts": "",  
    "select_tab": "third_party",
    "email": "nisha.kalpathri@riskcovry.com",
    "kyc": json.dumps([{"OVD": {
        "proposer_poi_document_type": "PAN Card",
        "proposer_poa_document_type": "Aadhaar Card",
        "proposer_phone_number": "8970985822",
        "proposer_email": "nisha.kalpathri@riskcovry.com"
    }}]),  
    "kyc_verification": "Yes",
    "proposal_questions": json.dumps(proposal_questions_dict),
    "is_inspection_required": "No",
    "carrier_name": "ICICI Lombard General Insurance",
    "Expected Output": "Policy created successfully",
    "Status": "Pass",
    "Comments": ""
}

scenarios = [
    "New Business",
    "Not Sure about previous policy & no TP",
    "Not Sure about previous policy & with TP < 3D",
    "Not Sure about previous policy & with TP < 60D",
    "Not Sure about previous policy & with TP > 90D",
    "Rollover < 2018-09 & Active & Exp: T",
    "Rollover < 2018-09 & Active & Exp > 90D",
    "Rollover < 2018-09 & Expired & Exp < 90D",
    "Rollover < 2018-09 & Expired & Exp > 90D",
    "Rollover > 2018-09 & Active & OD:T & TP: T",
    "Rollover > 2018-09 & Active & OD:T & TP < 60D",
    "Rollover > 2018-09 & Active & OD:T & TP 60D - 90D",
    "Rollover > 2018-09 & Active & OD:T & TP > 90D",
    "Rollover > 2018-09 & Active & OD > 90D & TP > 90D",
    "Rollover > 2018-09 & Expired & OD < 90D & TP: T",
    "Rollover > 2018-09 & Expired & OD < 90D & TP < 60D",
    "Rollover > 2018-09 & Expired & OD < 90D & TP 60D - 90D",
    "Rollover > 2018-09 & Expired & OD < 90D & TP > 90D",
    "Rollover > 2018-09 & Expired & OD > -90D & TP > 90D"
]


current_date = datetime(2025, 5, 26)
ncb_values = [0.20, 0.25, 0.35, 0.45, 0.50]


addon_mapping = {
    "Zero Depreciation": {"insurance_cover_code": "ZERO_DEPRECIATION_COVER"},
    "Roadside Assistance": {"insurance_cover_code": "ROAD_SIDE_ASSISTANCE"},
    "Engine Protection": {"insurance_cover_code": "ENGINE_PROTECTION"},
    "Consumables Cover": {"insurance_cover_code": "COST_OF_CONSUMABLE"}
}

def generate_test_case(scenario, index):
    test_case = base_data.copy()
    test_case["Testcase_id"] = f"ICICI_LOMBARD_PC_{scenario.replace(' ', '_').upper()}_{index:02d}"
    test_case["product_code"] = f"ICICI_LOMBARD_PC_{'COMPREHENSIVE' if 'Rollover' in scenario else 'THIRD_PARTY'}"
    test_case["select_tab"] = "comprehensive" if "Rollover" in scenario else "third_party"

    
    if "Rollover < 2018-09" in scenario:
        test_case["manufacturing_year"] = "2017"
        test_case["registration_date"] = "28/08/2017"
    else:
        test_case["manufacturing_year"] = "2023"
        test_case["registration_date"] = "28/08/2023" if "Rollover > 2018-09" in scenario else ""

    
    test_case["journey_type"] = "new_journey" if "New Business" in scenario else "without_registration"

    
    if "New Business" in scenario or "Not Sure" in scenario:
        test_case["kyc"] = json.dumps([{
            "OVD": {
                "proposer_poi_document_type": "PAN Card",
                "proposer_poa_document_type": "Aadhaar Card",
                "proposer_phone_number": "8970985822",
                "proposer_email": "nisha.kalpathri@riskcovry.com"
            }
        }])
    elif "Rollover < 2018-09" in scenario:
        test_case["kyc"] = json.dumps([{
            "PAN": {
                "pan": "GTTPK1088Q",
                "dob": "28/10/1994"
            }
        }])
    elif "Rollover > 2018-09" in scenario:
        test_case["kyc"] = json.dumps([{
            "CKYC Number": {
                "ckyc_number": "60061639446221",
                "dob": "28/10/1994"
            }
        }])

    
    if "Not Sure about previous policy" in scenario:
        test_case["not_sure"] = "Yes"
        test_case["previous_expiry_date"] = ""
        test_case["offset_previous_expiry_date"] = ""
        test_case["previous_insurer"] = ""
        test_case["is_inspection_required"] = "Yes"
        test_case["Expected Output"] = "Inspection required"
        test_case["previous_ncb"] = "0%"
        test_case["claim_taken"] = "Yes"
        test_case["addons"] = ""  
    else:
        test_case["previous_insurer"] = "Bajaj Allianz General Insurance Co. Ltd."
        test_case["previous_tp_insurer"] = "Bajaj Allianz General Insurance Co. Ltd."
        test_case["Expected Output"] = "Policy created successfully" if "Active" in scenario else "Inspection required, policy issuance depends on pre-inspection"

    
    if "Exp: T" in scenario or "OD:T" in scenario or "TP: T" in scenario:
        test_case["previous_expiry_date"] = current_date.strftime("%d/%m/%Y")
        test_case["offset_previous_expiry_date"] = "0"
        test_case["previous_tp_expiry_date"] = current_date.strftime("%d/%m/%Y")
        test_case["offset_previous_tp_expiry_date"] = "0"
        test_case["is_inspection_required"] = "No" if "Active" in scenario else "Yes"
    elif "Exp < 90D" in scenario or "OD < 90D" in scenario or "TP < 60D" in scenario:
        test_case["previous_expiry_date"] = (current_date - timedelta(days=45)).strftime("%d/%m/%Y")
        test_case["offset_previous_expiry_date"] = "-45"
        test_case["previous_tp_expiry_date"] = (current_date - timedelta(days=30)).strftime("%d/%m/%Y")
        test_case["offset_previous_tp_expiry_date"] = "-30"
        test_case["is_inspection_required"] = "Yes" if "Expired" in scenario else "No"
    elif "TP 60D - 90D" in scenario:
        test_case["previous_expiry_date"] = (current_date - timedelta(days=45)).strftime("%d/%m/%Y")
        test_case["offset_previous_expiry_date"] = "-45"
        test_case["previous_tp_expiry_date"] = (current_date - timedelta(days=75)).strftime("%d/%m/%Y")
        test_case["offset_previous_tp_expiry_date"] = "-75"
        test_case["is_inspection_required"] = "Yes" if "Expired" in scenario else "No"
    elif "Exp > 90D" in scenario or "OD > 90D" in scenario or "TP > 90D" in scenario or "OD > -90D" in scenario:
        test_case["previous_expiry_date"] = (current_date - timedelta(days=120)).strftime("%d/%m/%Y")
        test_case["offset_previous_expiry_date"] = "-120"
        test_case["previous_tp_expiry_date"] = (current_date - timedelta(days=120)).strftime("%d/%m/%Y")
        test_case["offset_previous_tp_expiry_date"] = "-120"
        test_case["is_inspection_required"] = "Yes" if "Expired" in scenario else "No"

    
    if "no TP" in scenario:
        test_case["previous_tp_expiry_date"] = ""
        test_case["offset_previous_tp_expiry_date"] = ""
        test_case["previous_tp_insurer"] = ""
        test_case["is_inspection_required"] = "Yes"
    elif "TP < 3D" in scenario:
        test_case["previous_tp_expiry_date"] = (current_date - timedelta(days=2)).strftime("%d/%m/%Y")
        test_case["offset_previous_tp_expiry_date"] = "-2"
        test_case["previous_tp_insurer"] = "Bajaj Allianz General Insurance Co. Ltd."
        test_case["is_inspection_required"] = "Yes"

    
    if "Not Sure" in scenario or "Expired" in scenario:
        test_case["previous_ncb"] = "0%"
        test_case["claim_taken"] = "Yes"
    elif "Active" in scenario:
        
        ncb_index = (index - 6) % len(ncb_values)  
        test_case["previous_ncb"] = f"{int(ncb_values[ncb_index] * 100)}%"  
        test_case["claim_taken"] = "No"
    else:
        
        test_case["previous_ncb"] = "0%"
        test_case["claim_taken"] = ""
        test_case["addons"] = ""  

    
    addons = []
    if "Rollover < 2018-09" in scenario:
        if index in [6, 7]:  
            addons = [
                addon_mapping["Zero Depreciation"],
                addon_mapping["Roadside Assistance"]
            ]
        elif index in [8, 9]:  
            addons = [addon_mapping["Roadside Assistance"]]
    elif "Rollover > 2018-09" in scenario:
        if index in [10, 11, 12, 13, 14]:  
            addons = [
                addon_mapping["Zero Depreciation"],
                addon_mapping["Roadside Assistance"],
                addon_mapping["Engine Protection"]
            ]
        elif index in [15, 16, 17, 18, 19]:  
            addons = [addon_mapping["Consumables Cover"]]
    test_case["addons"] = json.dumps(addons) if addons else ""  

    
    if "Rollover" in scenario and "Active" in scenario:
        test_case["discounts"] = json.dumps([{"discount_code": "ANTI_THEFT_DISCOUNT", "sa": ""}])
    else:
        test_case["discounts"] = "" 

    
    try:
        proposal_questions = json.loads(test_case["proposal_questions"])
        proposal_questions["manufacturing_year"] = test_case["manufacturing_year"]
        proposal_questions["registration_number"] = test_case["registration_number"]
        proposal_questions["previous_policy_expiry_date"] = test_case["previous_expiry_date"]
        proposal_questions["previous_tp_policy_expiry_date"] = test_case["previous_tp_expiry_date"]
        test_case["proposal_questions"] = json.dumps(proposal_questions)
    except json.JSONDecodeError as e:
        
        raise

    
    test_case["Status"] = "Pass"
    test_case["Comments"] = ""
    return test_case


try:
    test_cases = [generate_test_case(scenario, i + 1) for i, scenario in enumerate(scenarios)]
except Exception as e:
    
    raise


df = pd.DataFrame(test_cases)


columns = [
    "Testcase_id", "category", "journey_type", "registration_number", "make_model", "variant",
    "registration_date", "rto", "owned_by", "is_ownership_changed", "previous_expiry_date",
    "offset_previous_expiry_date", "previous_insurer", "previous_tp_expiry_date",
    "offset_previous_tp_expiry_date", "previous_tp_insurer", "not_sure",
    "know_previous_tp_expiry_date", "not_sure_previous_tp_expiry_date", "claim_taken",
    "previous_ncb", "product_code", "customer_name", "contact_number", "idv", "NCB_two",
    "addons", "discounts", "select_tab", "email", "kyc", "kyc_verification",
    "proposal_questions", "is_inspection_required", "carrier_name", "Expected Output",
    "Status", "Comments"
]
df = df[columns]


import os
os.makedirs("data", exist_ok=True)


try:
    df.to_excel("data/icici_4w_test_results.xlsx", index=False, engine="openpyxl")
    
except Exception as e:
    
    raise