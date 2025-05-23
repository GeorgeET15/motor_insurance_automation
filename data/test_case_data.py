# Scenarios, carriers, and vehicles for motor insurance test cases

scenarios = [
    # New Business (No Inspection Required)
    {
        'name': 'NB_INDIVIDUAL',
        'category': 'four_wheeler',
        'journey_type': 'new_journey',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'No'
    },
    {
        'name': 'NB_COMPANY',
        'category': 'four_wheeler',
        'journey_type': 'new_journey',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'third_party',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'CKYC',
        'inspection_required': 'No'
    },
    # Not Sure (Inspection Depends on Ownership Change)
    {
        'name': 'NS_NO_TP',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '<2018-09',
        'kyc_verification': 'No',
        'kyc_type': 'AADHAR',
        'inspection_required': 'Yes'
    },
    {
        'name': 'NS_TP_3D',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': '<3D',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'third_party',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'No'
    },
    {
        'name': 'NS_TP_60D',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': '<60D',
        'od_status': 'not_sure',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'third_party',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'AADHAR',
        'inspection_required': 'No'
    },
    {
        'name': 'NS_TP_90D',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': '>90D',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'third_party',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'No',
        'kyc_type': 'CKYC',
        'inspection_required': 'Yes'
    },
    # New Not Sure Scenarios (Non-Expired, Active TP)
    {
        'name': 'NS_TP_TODAY_OWNERSHIP_CHANGED',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': 'today',
        'od_status': 'not_sure',
        'ownership': 'Company',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'third_party',
        'manufacturing_year': '<2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'Yes'
    },
    {
        'name': 'NS_TP_90D_NO_OWNERSHIP_CHANGE',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'tp_status': '>90D',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'third_party',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'AADHAR',
        'inspection_required': 'No'
    },
    # Rollover < 2018-09
    {
        'name': 'RO_PRE_2018_ACTIVE_EXP_T',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': 'today',
        'od_status': 'today',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '<2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_PRE_2018_ACTIVE_EXP_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': '>90D',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '<2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'CKYC',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_PRE_2018_EXPIRED_EXP_LT_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '<60D',
        'od_status': '<90D',
        'ownership': 'Individual',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '<2018-09',
        'kyc_verification': 'No',
        'kyc_type': 'AADHAR',
        'inspection_required': 'Yes'
    },
    {
        'name': 'RO_PRE_2018_EXPIRED_EXP_GT_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': '>90D',
        'ownership': 'Company',
        'ownership_changed': 'Yes',
        'claim_taken': 'Yes',
        'policy_type': 'comprehensive',
        'manufacturing_year': '<2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'Yes'
    },
    # Rollover > 2018-09
    {
        'name': 'RO_POST_2018_OD_T_TP_T',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': 'today',
        'od_status': 'today',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_POST_2018_OD_T_TP_60D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '<60D',
        'od_status': 'today',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'OD',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'AADHAR',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_POST_2018_OD_T_TP_60D_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '60D-90D',
        'od_status': 'today',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'No',
        'kyc_type': 'CKYC',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_POST_2018_OD_T_TP_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': 'today',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_POST_2018_OD_90D_TP_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': '>90D',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'Yes',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'AADHAR',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_POST_2018_EXPIRED_OD_90D_TP_T',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': 'today',
        'od_status': '<90D',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'Yes'
    },
    {
        'name': 'RO_POST_2018_EXPIRED_OD_90D_TP_60D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '<60D',
        'od_status': '<90D',
        'ownership': 'Company',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'No',
        'kyc_type': 'CKYC',
        'inspection_required': 'Yes'
    },
    {
        'name': 'RO_POST_2018_EXPIRED_OD_90D_TP_60D_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '60D-90D',
        'od_status': '<90D',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'AADHAR',
        'inspection_required': 'Yes'
    },
    {
        'name': 'RO_POST_2018_EXPIRED_OD_90D_TP_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': '<90D',
        'ownership': 'Individual',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'Yes'
    },
    {
        'name': 'RO_POST_2018_EXPIRED_OD_GT_90D_TP_90D',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': '>90D',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'CKYC',
        'inspection_required': 'No'
    },
    # New Rollover Scenarios (Non-Expired, Active Policies)
    {
        'name': 'RO_PRE_2018_ACTIVE_OD_T_TP_90D_OWNERSHIP_CHANGED',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': 'today',
        'ownership': 'Individual',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '<2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'Yes'
    },
    {
        'name': 'RO_PRE_2018_ACTIVE_OD_90D_TP_T',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': 'today',
        'od_status': '>90D',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'OD',
        'manufacturing_year': '<2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'AADHAR',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_POST_2018_ACTIVE_OD_T_TP_90D_OWNERSHIP_CHANGED',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': 'today',
        'ownership': 'Individual',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'No',
        'kyc_type': 'CKYC',
        'inspection_required': 'Yes'
    },
    {
        'name': 'RO_POST_2018_ACTIVE_OD_90D_TP_T',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': 'today',
        'od_status': '>90D',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'No'
    },
    {
        'name': 'RO_POST_2018_ACTIVE_THIRD_PARTY_OWNERSHIP_CHANGED',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': 'today',
        'od_status': 'not_sure',
        'ownership': 'Individual',
        'ownership_changed': 'Yes',
        'claim_taken': 'No',
        'policy_type': 'third_party',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'AADHAR',
        'inspection_required': 'Yes'
    },
    {
        'name': 'RO_POST_2018_ACTIVE_OD_90D_TP_90D_NO_CHANGE',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': '>90D',
        'ownership': 'Company',
        'ownership_changed': 'No',
        'claim_taken': 'Yes',
        'policy_type': 'comprehensive',
        'manufacturing_year': '>2018-09',
        'kyc_verification': 'Yes',
        'kyc_type': 'CKYC',
        'inspection_required': 'No'
    },
    # Edge Case
    {
        'name': 'VEHICLE_AGE_GT_15Y',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'tp_status': '>90D',
        'od_status': '>90D',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'policy_type': 'comprehensive',
        'manufacturing_year': '<2010',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'inspection_required': 'No'
    }
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
    # Four-wheeler vehicles
    {
        'category': 'four_wheeler',
        'make_model': 'MARUTI SUZUKI ALTO',
        'variant': 'LXi (CC - 796 Seat Cap - 5 Fuel - CNG)'
    },
    {
        'category': 'four_wheeler',
        'make_model': 'HONDA CITY',
        'variant': '1.5 V MT (CC - 1497 Seat Cap - 5 Fuel - Petrol)'
    },
    {
        'category': 'four_wheeler',
        'make_model': 'HYUNDAI CRETA',
        'variant': 'SX Diesel (CC - 1493 Seat Cap - 5 Fuel - Diesel)'
    },
    {
        'category': 'four_wheeler',
        'make_model': 'TATA NEXON',
        'variant': 'XZ Plus (CC - 1199 Seat Cap - 5 Fuel - Petrol)'
    },
    {
        'category': 'four_wheeler',
        'make_model': 'MAHINDRA SCORPIO',
        'variant': 'S5 (CC - 2179 Seat Cap - 7 Fuel - Diesel)'
    },
    {
        'category': 'four_wheeler',
        'make_model': 'FORD ECOSPORT',
        'variant': 'Titanium (CC - 1499 Seat Cap - 5 Fuel - Petrol)'
    },
    {
        'category': 'four_wheeler',
        'make_model': 'TOYOTA FORTUNER',
        'variant': '2.8 4x4 MT (CC - 2755 Seat Cap - 7 Fuel - Diesel)'
    },
    {
        'category': 'four_wheeler',
        'make_model': 'KIA Seltos',
        'variant': 'HTX (CC - 1493 Seat Cap - 5 Fuel - Petrol)'
    },
    {
        'category': 'four_wheeler',
        'make_model': 'BMW X5',
        'variant': 'xDrive30d (CC - 2993 Seat Cap - 5 Fuel - Diesel)'
    },

    # Two-wheeler vehicles
    {
        'category': 'two_wheeler',
        'make_model': 'HONDA ACTIVA',
        'variant': '5G (CC - 109 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'BAJAJ PULSAR',
        'variant': '150 (CC - 149 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'TVS JUPITER',
        'variant': 'Classic (CC - 109.7 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'ROYAL ENFIELD CLASSIC',
        'variant': '350 (CC - 346 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'YAMAHA FZ-S',
        'variant': 'V3 (CC - 149 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'SUZUKI ACCESS',
        'variant': '125 (CC - 124 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'KTM DUKE',
        'variant': '200 (CC - 199.5 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'HONDA CB SHINE',
        'variant': 'SP (CC - 124.7 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'Bajaj Dominar',
        'variant': '400 (CC - 373.3 Seat Cap - 2 Fuel - Petrol)'
    },
    {
        'category': 'two_wheeler',
        'make_model': 'HARLEY DAVIDSON IRON 883',
        'variant': 'Iron 883 (CC - 883 Seat Cap - 2 Fuel - Petrol)'
    }
]

# City-State Mapping for India (simplified example, expand as needed)
city_state_mapping = {
    'Dibrugarh': 'Assam',
    'Erode': 'Tamil Nadu',
    'Guntakal': 'Andhra Pradesh',
    'Amravati': 'Maharashtra',
    'Shimla': 'Himachal Pradesh',
    'Fatehpur': 'Uttar Pradesh',
    'Mangalore': 'Karnataka',
    'Kolhapur': 'Maharashtra',
    'Nadiad': 'Gujarat',
    'Ludhiana': 'Punjab',
    'Jamalpur': 'Bihar',
    'Malegaon': 'Maharashtra',
    'Bidar': 'Karnataka',
    'Mumbai': 'Maharashtra',
    'Mau': 'Uttar Pradesh',
    'Agartala': 'Tripura',
    'Suryapet': 'Telangana',
    'Mysore': 'Karnataka',
    'Jhansi': 'Uttar Pradesh',
    'North Dumdum': 'West Bengal',
    'Srikakulam': 'Andhra Pradesh',
    'Rohtak': 'Haryana',
    'Rewa': 'Madhya Pradesh',
    'Anantapuram': 'Andhra Pradesh',
    'Baranagar': 'West Bengal',
    'Tiruchirappalli': 'Tamil Nadu',
    'Ghaziabad': 'Uttar Pradesh',
    'Mehsana': 'Gujarat',
    'Madhyamgram': 'West Bengal',
    'Ratlam': 'Madhya Pradesh',
    'Kharagpur': 'West Bengal'
}

# Base IDV ranges for vehicles
base_idv_ranges = {
    'MARUTI SUZUKI ALTO': (200000, 400000),
    'HONDA CITY': (700000, 1200000),
    'HYUNDAI CRETA': (1000000, 1800000),
    'TATA NEXON': (800000, 1400000),
    'MAHINDRA SCORPIO': (1200000, 2000000),
    'FORD ECOSPORT': (700000, 1200000),
    'TOYOTA FORTUNER': (2500000, 4000000),
    'KIA Seltos': (900000, 1600000),
    'BMW X5': (3000000, 6000000),
    'HONDA ACTIVA': (50000, 100000),
    'BAJAJ PULSAR': (70000, 120000),
    'TVS JUPITER': (60000, 110000),
    'ROYAL ENFIELD CLASSIC': (150000, 250000),
    'YAMAHA FZ-S': (80000, 130000),
    'SUZUKI ACCESS': (60000, 110000),
    'KTM DUKE': (150000, 250000),
    'HONDA CB SHINE': (60000, 110000),
    'Bajaj Dominar': (150000, 250000),
    'HARLEY DAVIDSON IRON 883': (800000, 1200000)
}