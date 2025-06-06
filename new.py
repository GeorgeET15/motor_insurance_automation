import pandas as pd
from datetime import datetime, timedelta
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import csv

# Define proposal_questions_dict and base_data as before
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

def generate_test_case(scenario, index, make_model, variant, kyc):
    test_case = base_data.copy()
    test_case["Testcase_id"] = f"ICICI_LOMBARD_PC_{scenario.replace(' ', '_').upper()}_{index:02d}"
    test_case["product_code"] = f"ICICI_LOMBARD_PC_{'COMPREHENSIVE' if 'Rollover' in scenario else 'THIRD_PARTY'}"
    test_case["select_tab"] = "comprehensive" if "Rollover" in scenario else "third_party"
    test_case["make_model"] = make_model
    test_case["variant"] = variant
    test_case["kyc"] = kyc

    if "Rollover < 2018-09" in scenario:
        test_case["manufacturing_year"] = "2017"
        test_case["registration_date"] = "28/08/2017"
    else:
        test_case["manufacturing_year"] = "2023"
        test_case["registration_date"] = "28/08/2023" if "Rollover > 2018-09" in scenario else ""

    test_case["journey_type"] = "new_journey" if "New Business" in scenario else "without_registration"

    if "New Business" in scenario or "Not Sure" in scenario:
        test_case["kyc"] = kyc if kyc else json.dumps([{
            "OVD": {
                "proposer_poi_document_type": "PAN Card",
                "proposer_poa_document_type": "Aadhaar Card",
                "proposer_phone_number": "8970985822",
                "proposer_email": "nisha.kalpathri@riskcovry.com"
            }
        }])
    elif "Rollover < 2018-09" in scenario:
        test_case["kyc"] = kyc if kyc else json.dumps([{
            "PAN": {
                "pan": "GTTPK1088Q",
                "dob": "28/10/1994"
            }
        }])
    elif "Rollover > 2018-09" in scenario:
        test_case["kyc"] = kyc if kyc else json.dumps([{
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

# Tkinter GUI
class InsuranceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Motor Insurance Automation")
        self.root.geometry("400x300")
        self.root.configure(bg="#FFFFFF")  # White background

        # Style configuration
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", font=("Helvetica", 14), background="#FFFFFF", foreground="#D32F2F")  # Red text
        style.configure("TEntry", font=("Helvetica", 12))

        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(expand=True, fill="both")

        # Title
        self.title_label = ttk.Label(self.main_frame, text="Motor Insurance Automation", style="TLabel")
        self.title_label.pack(pady=20)

        # Question label
        self.question_label = ttk.Label(self.main_frame, text="Would you like to edit the fields?", style="TLabel")
        self.question_label.pack(pady=10)

        # Buttons
        self.yes_button = ttk.Button(self.main_frame, text="Yes", command=self.show_edit_window, style="TButton")
        self.yes_button.pack(pady=5, fill="x")

        self.no_button = ttk.Button(self.main_frame, text="No", command=self.process_and_show_preview, style="TButton")
        self.no_button.pack(pady=5, fill="x")

        # Variables to store user inputs
        self.make_model = tk.StringVar(value="HONDA CITY")
        self.variant = tk.StringVar(value="1.3 LXi (CC - 1343 Seat Cap - 5 Fuel - Petrol)")
        self.kyc_poi = tk.StringVar(value="PAN Card")
        self.kyc_poa = tk.StringVar(value="Aadhaar Card")
        self.kyc_phone = tk.StringVar(value="8970985822")
        self.kyc_email = tk.StringVar(value="nisha.kalpathri@riskcovry.com")

    def show_edit_window(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Fields")
        edit_window.geometry("400x500")
        edit_window.configure(bg="#FFFFFF")

        # Edit frame
        edit_frame = ttk.Frame(edit_window, padding="20")
        edit_frame.pack(expand=True, fill="both")

        # Labels and Entries
        ttk.Label(edit_frame, text="Edit Fields", font=("Helvetica", 14), background="#FFFFFF", foreground="#D32F2F").pack(pady=10)

        # Make Model
        ttk.Label(edit_frame, text="Make Model:", font=("Helvetica", 12), background="#FFFFFF", foreground="#1976D2").pack(anchor="w")  # Blue text
        ttk.Entry(edit_frame, textvariable=self.make_model, font=("Helvetica", 12)).pack(fill="x", pady=5)

        # Variant
        ttk.Label(edit_frame, text="Variant:", font=("Helvetica", 12), background="#FFFFFF", foreground="#1976D2").pack(anchor="w")
        ttk.Entry(edit_frame, textvariable=self.variant, font=("Helvetica", 12)).pack(fill="x", pady=5)

        # KYC Details
        ttk.Label(edit_frame, text="KYC POI Document:", font=("Helvetica", 12), background="#FFFFFF", foreground="#1976D2").pack(anchor="w")
        ttk.Entry(edit_frame, textvariable=self.kyc_poi, font=("Helvetica", 12)).pack(fill="x", pady=5)

        ttk.Label(edit_frame, text="KYC POA Document:", font=("Helvetica", 12), background="#FFFFFF", foreground="#1976D2").pack(anchor="w")
        ttk.Entry(edit_frame, textvariable=self.kyc_poa, font=("Helvetica", 12)).pack(fill="x", pady=5)

        ttk.Label(edit_frame, text="KYC Phone Number:", font=("Helvetica", 12), background="#FFFFFF", foreground="#1976D2").pack(anchor="w")
        ttk.Entry(edit_frame, textvariable=self.kyc_phone, font=("Helvetica", 12)).pack(fill="x", pady=5)

        ttk.Label(edit_frame, text="KYC Email:", font=("Helvetica", 12), background="#FFFFFF", foreground="#1976D2").pack(anchor="w")
        ttk.Entry(edit_frame, textvariable=self.kyc_email, font=("Helvetica", 12)).pack(fill="x", pady=5)

        # Submit button
        ttk.Button(edit_frame, text="Submit", command=self.process_and_show_preview, style="TButton").pack(pady=20, fill="x")

    def process_and_show_preview(self):
        # Construct KYC JSON
        kyc_data = json.dumps([{"OVD": {
            "proposer_poi_document_type": self.kyc_poi.get(),
            "proposer_poa_document_type": self.kyc_poa.get(),
            "proposer_phone_number": self.kyc_phone.get(),
            "proposer_email": self.kyc_email.get()
        }}])

        # Generate test cases
        test_cases = [generate_test_case(scenario, i + 1, self.make_model.get(), self.variant.get(), kyc_data) for i, scenario in enumerate(scenarios)]

        # Create DataFrame
        df = pd.DataFrame(test_cases)

        # Reorder columns
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

        # Ensure output directory exists
        os.makedirs("data", exist_ok=True)

        # Save to CSV
        output_file = "data/icici_4w_test_results.csv"
        try:
            df.to_csv(output_file, index=False)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save CSV: {e}")
            return

        # Show preview window
        preview_window = tk.Toplevel(self.root)
        preview_window.title("CSV Preview")
        preview_window.geometry("800x600")
        preview_window.configure(bg="#FFFFFF")

        # Preview frame
        preview_frame = ttk.Frame(preview_window, padding="20")
        preview_frame.pack(expand=True, fill="both")

        ttk.Label(preview_frame, text="CSV Preview", font=("Helvetica", 14), background="#FFFFFF", foreground="#D32F2F").pack(pady=10)

        # Text area for preview
        text_area = scrolledtext.ScrolledText(preview_frame, wrap=tk.WORD, font=("Helvetica", 10), bg="#F5F5F5", fg="#1976D2")
        text_area.pack(expand=True, fill="both", pady=10)

        # Load CSV content into text area
        with open(output_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                text_area.insert(tk.END, ",".join(row) + "\n")

        text_area.configure(state="disabled")

        # Close button
        ttk.Button(preview_frame, text="Close", command=preview_window.destroy, style="TButton").pack(pady=10, fill="x")

        # Disable main window buttons
        self.yes_button.configure(state="disabled")
        self.no_button.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = InsuranceApp(root)
    root.mainloop()