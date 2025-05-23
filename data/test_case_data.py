# Scenarios, carriers, and vehicles for motor insurance test cases

scenarios = [
    # New Business
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
        'kyc_type': 'PAN'
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
        'kyc_type': 'CKYC'
    },
    # Not Sure
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
        'kyc_type': 'AADHAR'
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
        'kyc_type': 'PAN'
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
        'kyc_type': 'AADHAR'
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
        'kyc_type': 'CKYC'
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
        'kyc_type': 'PAN'
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
        'kyc_type': 'CKYC'
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
        'kyc_type': 'AADHAR'
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
        'kyc_type': 'PAN'
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
        'kyc_type': 'PAN'
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
        'kyc_type': 'AADHAR'
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
        'kyc_type': 'CKYC'
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
        'kyc_type': 'PAN'
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
        'kyc_type': 'AADHAR'
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
        'kyc_type': 'PAN'
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
        'kyc_type': 'CKYC'
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
        'kyc_type': 'AADHAR'
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
        'kyc_type': 'PAN'
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
        'kyc_type': 'CKYC'
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
        'kyc_type': 'PAN'
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
