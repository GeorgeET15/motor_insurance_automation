# Sample data for test case generation

# Carriers
carriers = [
    'Go Digit Motor',
    'HDFC Ergo',
    'ICICI Lombard',
    'Reliance General',
    'Future Generali',
    'Bajaj Allianz',
    'Tata AIG',
    'Royal Sundaram',
    'Chola MS',
    'IFFCO Tokio',
    'SBI General',
    'Bharti AXA',
    'Oriental Insurance',
    'United India',
    'National Insurance',
    'Universal Sompo',
]

available_addons = [
            'PERSONAL_ACCIDENT', 'RIM_PROTECTION', 'RETURN_TO_INVOICE', 'ENGINE_PROTECTOR_COVER',
            'COST_OF_CONSUMABLE', 'TYRE_SECURE_COVER', 'PERSONAL_BELONGING', 'ROAD_SIDE_ASSISTANCE',
            'ZERO_DEPRECIATION_COVER', 'LOSS_OF_USE', 'PA_PAID_DRIVER', 'PA_UNNAMED',
            'ELECTRICAL_ACCESSORIES_IDV', 'LIABILITY_TO_EMPLOYEES', 'LL_PAID_DRIVER',
            'NON_ELECTRICAL_ACCESSORIES_IDV', 'KEY_LOCK_REPLACEMENT', 'BATTERY_PROTECTION',
            'NCB_PROTECTION'
]


# Products
products = [
    {'code': 'GODIGIT_MOTOR_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Go Digit Motor'},
    {'code': 'HDFC_ERGO_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'Comprehensive', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_PC_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'TP Only', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_PC_OD_ONLY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'OD Only', 'carrier_name': 'HDFC Ergo'},
    {'code': 'GODIGIT_MOTOR_OWN_DAMAGE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Go Digit Motor'},
    {'code': 'GODIGIT_MOTOR_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Go Digit Motor'},
    {'code': 'ICICI_LOMBARD_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'ICICI Lombard'},
    {'code': 'HDFC_ERGO_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'Comprehensive', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'TP Only', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_TW_OD_ONLY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'OD Only', 'carrier_name': 'HDFC Ergo'},
    {'code': 'FG_MOTOR_COMPREHENSIVE_P1', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': '6', 'product_class': 'Comprehensive', 'carrier_name': 'Future Generali'},
    {'code': 'GODIGIT_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Go Digit Motor'},
    {'code': 'GODIGIT_TW_OWN_DAMAGE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Go Digit Motor'},
    {'code': 'GODIGIT_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Go Digit Motor'},
    {'code': 'RELIANCE_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'RELIANCE_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Reliance General'},
    {'code': 'RELIANCE_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'RELIANCE_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Reliance General'},
    {'code': 'RELIANCE_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'RELIANCE_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Reliance General'},
    {'code': 'FG_MOTOR_COMPREHENSIVE_P2', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': '6', 'product_class': 'Comprehensive', 'carrier_name': 'Future Generali'},
    {'code': 'FG_MOTOR_OD_ONLY_P1', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': '6', 'product_class': 'OD Only', 'carrier_name': 'Future Generali'},
    {'code': 'FG_MOTOR_OD_ONLY_P2', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': '6', 'product_class': 'OD Only', 'carrier_name': 'Future Generali'},
    {'code': 'FG_MOTOR_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': '6', 'product_class': 'TP Only', 'carrier_name': 'Future Generali'},
    {'code': 'ICICI_LOMBARD_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'ICICI Lombard'},
    {'code': 'ICICI_LOMBARD_PC_OD_ONLY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'ICICI Lombard'},
    {'code': 'ICICI_LOMBARD_PC_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'ICICI Lombard'},
    {'code': 'ICICI_LOMBARD_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'ICICI Lombard'},
    {'code': 'ICICI_LOMBARD_TW_OD_ONLY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'ICICI Lombard'},
    {'code': 'IFFCO_TOKIO_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'IFFCO_TOKIO', 'product_class': 'Comprehensive', 'carrier_name': 'IFFCO Tokio'},
    {'code': 'RSA_MOTOR_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ROYAL_SUNDARAM', 'product_class': 'Comprehensive', 'carrier_name': 'Royal Sundaram'},
    {'code': 'IFFCO_TOKIO_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'IFFCO_TOKIO', 'product_class': 'TP Only', 'carrier_name': 'IFFCO Tokio'},
    {'code': 'IFFCO_TOKIO_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'IFFCO_TOKIO', 'product_class': 'OD Only', 'carrier_name': 'IFFCO Tokio'},
    {'code': 'RSA_MOTOR_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ROYAL_SUNDARAM', 'product_class': 'TP Only', 'carrier_name': 'Royal Sundaram'},
    {'code': 'RSA_MOTOR_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ROYAL_SUNDARAM', 'product_class': 'OD Only', 'carrier_name': 'Royal Sundaram'},
    {'code': 'RSA_MOTOR_TW_NEW_BUNDLED', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ROYAL_SUNDARAM', 'product_class': 'Comprehensive', 'carrier_name': 'Royal Sundaram'},
    {'code': 'RSA_MOTOR_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ROYAL_SUNDARAM', 'product_class': 'Comprehensive', 'carrier_name': 'Royal Sundaram'},
    {'code': 'RSA_MOTOR_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ROYAL_SUNDARAM', 'product_class': 'OD Only', 'carrier_name': 'Royal Sundaram'},
    {'code': 'RSA_MOTOR_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ROYAL_SUNDARAM', 'product_class': 'TP Only', 'carrier_name': 'Royal Sundaram'},
    {'code': 'CHOLA_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'CHOLA', 'product_class': 'Comprehensive', 'carrier_name': 'Chola MS'},
    {'code': 'CHOLA_PC_OD_ONLY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'CHOLA', 'product_class': 'OD Only', 'carrier_name': 'Chola MS'},
    {'code': 'CHOLA_PC_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'CHOLA', 'product_class': 'TP Only', 'carrier_name': 'Chola MS'},
    {'code': 'RSA_MOTOR_PC_NEW_BUNDLED', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ROYAL_SUNDARAM', 'product_class': 'Comprehensive', 'carrier_name': 'Royal Sundaram'},
    {'code': 'CHOLA_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'CHOLA', 'product_class': 'Comprehensive', 'carrier_name': 'Chola MS'},
    {'code': 'CHOLA_TW_OD_ONLY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'CHOLA', 'product_class': 'OD Only', 'carrier_name': 'Chola MS'},
    {'code': 'CHOLA_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'CHOLA', 'product_class': 'TP Only', 'carrier_name': 'Chola MS'},
    {'code': 'IFFCO_TOKIO_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'IFFCO_TOKIO', 'product_class': 'Comprehensive', 'carrier_name': 'IFFCO Tokio'},
    {'code': 'IFFCO_TOKIO_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'IFFCO_TOKIO', 'product_class': 'OD Only', 'carrier_name': 'IFFCO Tokio'},
    {'code': 'IFFCO_TOKIO_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'IFFCO_TOKIO', 'product_class': 'TP Only', 'carrier_name': 'IFFCO Tokio'},
    {'code': 'FG_MOTOR_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': '6', 'product_class': 'Comprehensive', 'carrier_name': 'Future Generali'},
    {'code': 'FUTURE_GENERALI_MOTOR_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'FG_MOTOR_1', 'product_class': 'Comprehensive', 'carrier_name': 'Future Generali'},
    {'code': 'FUTURE_GENERALI_MOTOR_PC_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'FG_MOTOR_1', 'product_class': 'TP Only', 'carrier_name': 'Future Generali'},
    {'code': 'FUTURE_GENERALI_MOTOR_PC_OD_ONLY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'FG_MOTOR_1', 'product_class': 'OD Only', 'carrier_name': 'Future Generali'},
    {'code': 'FUTURE_GENERALI_MOTOR_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'FG_MOTOR_1', 'product_class': 'Comprehensive', 'carrier_name': 'Future Generali'},
    {'code': 'FUTURE_GENERALI_MOTOR_TW_OD_ONLY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'FG_MOTOR_1', 'product_class': 'OD Only', 'carrier_name': 'Future Generali'},
    {'code': 'FUTURE_GENERALI_MOTOR_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'FG_MOTOR_1', 'product_class': 'TP Only', 'carrier_name': 'Future Generali'},
    {'code': 'RELIANCE_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'RELIANCE_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Reliance General'},
    {'code': 'RELIANCE_PC_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'RELIANCE_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Reliance General'},
    {'code': 'RELIANCE_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'RELIANCE_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Reliance General'},
    {'code': 'SBI_MOTOR_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'SBI_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'SBI General'},
    {'code': 'SBI_MOTOR_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'SBI_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'SBI General'},
    {'code': 'SBI_MOTOR_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'SBI_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'SBI General'},
    {'code': 'SBI_MOTOR_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'SBI_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'SBI General'},
    {'code': 'SBI_MOTOR_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'SBI_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'SBI General'},
    {'code': 'SBI_MOTOR_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'SBI_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'SBI General'},
    {'code': 'TATA_AIG_MOTOR_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'TATA_AIG', 'product_class': 'Comprehensive', 'carrier_name': 'Tata AIG'},
    {'code': 'TATA_AIG_MOTOR_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'TATA_AIG', 'product_class': 'OD Only', 'carrier_name': 'Tata AIG'},
    {'code': 'TATA_AIG_MOTOR_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'TATA_AIG', 'product_class': 'TP Only', 'carrier_name': 'Tata AIG'},
    {'code': 'TATA_AIG_MOTOR_PC_NEW_BUNDLED', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'TATA_AIG', 'product_class': 'Comprehensive', 'carrier_name': 'Tata AIG'},
    {'code': 'TATA_AIG_MOTOR_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'TATA_AIG', 'product_class': 'Comprehensive', 'carrier_name': 'Tata AIG'},
    {'code': 'TATA_AIG_MOTOR_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'TATA_AIG', 'product_class': 'OD Only', 'carrier_name': 'Tata AIG'},
    {'code': 'TATA_AIG_MOTOR_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'TATA_AIG', 'product_class': 'TP Only', 'carrier_name': 'Tata AIG'},
    {'code': 'BAJAJ_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'BAJAJ_ALLIANZ_GENERAL', 'product_class': 'Comprehensive', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'BAJAJ_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'BAJAJ_ALLIANZ_GENERAL', 'product_class': 'OD Only', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'BAJAJ_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'BAJAJ_ALLIANZ_GENERAL', 'product_class': 'TP Only', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'BAJAJ_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'BAJAJ_ALLIANZ_GENERAL', 'product_class': 'Comprehensive', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'BAJAJ_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'BAJAJ_ALLIANZ_GENERAL', 'product_class': 'OD Only', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'BAJAJ_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'BAJAJ_ALLIANZ_GENERAL', 'product_class': 'TP Only', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'HDFC_ERGO_NEW_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'Comprehensive', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_NEW_PC_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'TP Only', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_NEW_PC_OD_ONLY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'OD Only', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_NEW_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'Comprehensive', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_NEW_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'TP Only', 'carrier_name': 'HDFC Ergo'},
    {'code': 'HDFC_ERGO_NEW_TW_OD_ONLY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'HDFC_ERGO', 'product_class': 'OD Only', 'carrier_name': 'HDFC Ergo'},
    {'code': 'TD_BAJAJ_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'BAGIC_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'TD_BAJAJ_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'BAGIC_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'TD_BAJAJ_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'BAGIC_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'TD_BAJAJ_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'BAGIC_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'TD_BAJAJ_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'BAGIC_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'TD_BAJAJ_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'BAGIC_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Bajaj Allianz'},
    {'code': 'TD_ICICI_LOMBARD_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'ICICI Lombard'},
    {'code': 'TD_ICICI_LOMBARD_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'ICICI Lombard'},
    {'code': 'TD_ICICI_LOMBARD_TW_OD_ONLY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'ICICI Lombard'},
    {'code': 'TD_ICICI_LOMBARD_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'ICICI Lombard'},
    {'code': 'TD_ICICI_LOMBARD_PC_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'ICICI Lombard'},
    {'code': 'TD_ICICI_LOMBARD_PC_OD_ONLY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ICICI_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'ICICI Lombard'},
    {'code': 'TD_AIG_MOTOR_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'TD_AIG_PC', 'product_class': 'Comprehensive', 'carrier_name': 'Tata AIG'},
    {'code': 'TD_AIG_MOTOR_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'TD_AIG_PC', 'product_class': 'OD Only', 'carrier_name': 'Tata AIG'},
    {'code': 'TD_AIG_MOTOR_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'TD_AIG_PC', 'product_class': 'TP Only', 'carrier_name': 'Tata AIG'},
    {'code': 'TD_AIG_MOTOR_PC_NB', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'TD_AIG_PC', 'product_class': 'Comprehensive', 'carrier_name': 'Tata AIG'},
    {'code': 'TD_AIG_MOTOR_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'TD_TATA_AIG', 'product_class': 'OD Only', 'carrier_name': 'Tata AIG'},
    {'code': 'TD_AIG_MOTOR_COMP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'TD_TATA_AIG', 'product_class': 'Comprehensive', 'carrier_name': 'Tata AIG'},
    {'code': 'TD_AIG_MOTOR_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'TD_TATA_AIG', 'product_class': 'TP Only', 'carrier_name': 'Tata AIG'},
    {'code': 'TD_AIG_MOTOR_NB', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'TD_TATA_AIG', 'product_class': 'Comprehensive', 'carrier_name': 'Tata AIG'},
    {'code': 'ORIENTAL_GIC_MOTOR_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ORIENTAL_GIC_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Oriental Insurance'},
    {'code': 'ORIENTAL_GIC_MOTOR_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ORIENTAL_GIC_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Oriental Insurance'},
    {'code': 'ORIENTAL_GIC_MOTOR_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ORIENTAL_GIC_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Oriental Insurance'},
    {'code': 'ORIENTAL_GIC_MOTOR_TW_NEW_BUNDLED', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'ORIENTAL_GIC_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Oriental Insurance'},
    {'code': 'ORIENTAL_GIC_MOTOR_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ORIENTAL_GIC_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Oriental Insurance'},
    {'code': 'ORIENTAL_GIC_MOTOR_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ORIENTAL_GIC_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Oriental Insurance'},
    {'code': 'ORIENTAL_GIC_MOTOR_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ORIENTAL_GIC_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Oriental Insurance'},
    {'code': 'ORIENTAL_GIC_MOTOR_PC_NEW_BUNDLED', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'ORIENTAL_GIC_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Oriental Insurance'},
    {'code': 'UNIVERSAL_SOMPO_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'UNIVERSAL_SOMPO', 'product_class': 'Comprehensive', 'carrier_name': 'Universal Sompo'},
    {'code': 'UNIVERSAL_SOMPO_TW_OD_ONLY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'UNIVERSAL_SOMPO', 'product_class': 'OD Only', 'carrier_name': 'Universal Sompo'},
    {'code': 'UNIVERSAL_SOMPO_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'UNIVERSAL_SOMPO', 'product_class': 'TP Only', 'carrier_name': 'Universal Sompo'},
    {'code': 'GODIGIT_MOTOR_NEW_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Go Digit Motor'},
    {'code': 'GODIGIT_MOTOR_NEW_OWN_DAMAGE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Go Digit Motor'},
    {'code': 'GODIGIT_MOTOR_NEW_THIRD_PARTY', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Go Digit Motor'},
    {'code': 'GODIGIT_NEW_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Go Digit Motor'},
    {'code': 'GODIGIT_NEW_TW_OWN_DAMAGE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Go Digit Motor'},
    {'code': 'GODIGIT_NEW_TW_THIRD_PARTY', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'GO_DIGIT_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Go Digit Motor'},
    {'code': 'RENEWAL_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'RENEWAL_MOTOR', 'product_class': 'Comprehensive', 'carrier_name': 'Renewal Motor'},
    {'code': 'RENEWAL_PC_SAOD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'RENEWAL_MOTOR', 'product_class': 'OD Only', 'carrier_name': 'Renewal Motor'},
    {'code': 'RENEWAL_PC_SATP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'RENEWAL_MOTOR', 'product_class': 'TP Only', 'carrier_name': 'Renewal Motor'},
    {'code': 'UNITED_INDIA_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'UNITED_INDIA', 'product_class': 'Comprehensive', 'carrier_name': 'United India'},
    {'code': 'UNITED_INDIA_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'UNITED_INDIA', 'product_class': 'OD Only', 'carrier_name': 'United India'},
    {'code': 'UNITED_INDIA_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'UNITED_INDIA', 'product_class': 'TP Only', 'carrier_name': 'United India'},
    {'code': 'UNITED_INDIA_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'UNITED_INDIA', 'product_class': 'TP Only', 'carrier_name': 'United India'},
    {'code': 'UNITED_INDIA_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'UNITED_INDIA', 'product_class': 'OD Only', 'carrier_name': 'United India'},
    {'code': 'UNITED_INDIA_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'UNITED_INDIA', 'product_class': 'Comprehensive', 'carrier_name': 'United India'},
    {'code': 'NATIONAL_PC_COMPREHENSIVE', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'NATIONAL_INSURANCE', 'product_class': 'Comprehensive', 'carrier_name': 'National Insurance'},
    {'code': 'NATIONAL_PC_OD', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'NATIONAL_INSURANCE', 'product_class': 'OD Only', 'carrier_name': 'National Insurance'},
    {'code': 'NATIONAL_PC_TP', 'category_code': 'MOTOR_RETAIL', 'insurance_company_code': 'NATIONAL_INSURANCE', 'product_class': 'TP Only', 'carrier_name': 'National Insurance'},
    {'code': 'NATIONAL_TW_COMPREHENSIVE', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'NATIONAL_INSURANCE', 'product_class': 'Comprehensive', 'carrier_name': 'National Insurance'},
    {'code': 'NATIONAL_TW_OD', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'NATIONAL_INSURANCE', 'product_class': 'OD Only', 'carrier_name': 'National Insurance'},
    {'code': 'NATIONAL_TW_TP', 'category_code': 'TWO_WHEELER_RETAIL', 'insurance_company_code': 'NATIONAL_INSURANCE', 'product_class': 'TP Only', 'carrier_name': 'National Insurance'},
]

# Sample scenarios
scenarios = [
    {
        'name': 'NEW_FOUR_WHEELER_COMP',
        'category': 'four_wheeler',
        'journey_type': 'new_journey',
        'policy_type': 'comprehensive',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'manufacturing_year': '>2018-09'
    },
    {
        'name': 'ROLLOVER_TWO_WHEELER_TP_OWNERSHIP_CHANGED',
        'category': 'two_wheeler',
        'journey_type': 'rollover',
        'policy_type': 'third_party',
        'ownership': 'Company',
        'ownership_changed': 'Yes',
        'claim_taken': 'Yes',
        'tp_status': '>90D',
        'od_status': 'today',
        'kyc_verification': 'No',
        'kyc_type': 'CKYC',
        'manufacturing_year': '<2018-09'
    },
    {
        'name': 'WITHOUT_REGISTRATION_FOUR_WHEELER_OD',
        'category': 'four_wheeler',
        'journey_type': 'without_registration',
        'policy_type': 'OD',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'No',
        'tp_status': 'no_tp',
        'od_status': 'not_sure',
        'kyc_verification': 'Yes',
        'kyc_type': 'AADHAR',
        'manufacturing_year': '>2018-09'
    },
    {
        'name': 'ROLLOVER_FOUR_WHEELER_COMP',
        'category': 'four_wheeler',
        'journey_type': 'rollover',
        'policy_type': 'comprehensive',
        'ownership': 'Individual',
        'ownership_changed': 'No',
        'claim_taken': 'Yes',
        'tp_status': '<60D',
        'od_status': '<90D',
        'kyc_verification': 'Yes',
        'kyc_type': 'PAN',
        'manufacturing_year': '>2018-09'
    }
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