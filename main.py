import json

from extractor import extract_patient_data
from validator import validate_patient_data
from fhir_converter import convert_to_fhir
from deidentifier import deidentify_patient


print("==============================")
print(" AI HEALTHCARE DATA EXTRACTOR")
print("==============================")


# Get input
text = input("\nEnter patient information:\n")


# ==============================
# 1. EXTRACTION
# ==============================

patient = extract_patient_data(text)


# ==============================
# 2. VALIDATION
# ==============================

errors = validate_patient_data(patient)

print("\n==============================")
print(" VALIDATION")
print("==============================")

if len(errors) == 0:
    print("VALIDATION PASSED")
else:
    print("VALIDATION FAILED")

    for error in errors:
        print("-", error)


# ==============================
# 3. STRUCTURED DATA
# ==============================

print("\n==============================")
print(" STRUCTURED DATA")
print("==============================")

print(json.dumps(patient, indent=4))


# Save structured data
with open("structured_patient.json", "w") as file:
    json.dump(patient, file, indent=4)


# ==============================
# 4. DE-IDENTIFICATION
# ==============================

deidentified_patient = deidentify_patient(patient)

print("\n==============================")
print(" DE-IDENTIFIED DATA")
print("==============================")

print(json.dumps(deidentified_patient, indent=4))


# Save de-identified data
with open("deidentified_patient.json", "w") as file:
    json.dump(deidentified_patient, file, indent=4)


# ==============================
# 5. FHIR CONVERSION
# ==============================

if len(errors) == 0:

    fhir_data = convert_to_fhir(patient)

    print("\n==============================")
    print(" FHIR OUTPUT")
    print("==============================")

    print(json.dumps(fhir_data, indent=4))


    # Save FHIR output
    with open("patient_fhir.json", "w") as file:
        json.dump(fhir_data, file, indent=4)


    print("\n==============================")
    print(" FILES SAVED")
    print("==============================")

    print("structured_patient.json")
    print("deidentified_patient.json")
    print("patient_fhir.json")

else:

    print("\nFHIR conversion skipped because validation failed.")

Put this in GitHub as "main.py".

Then tell me “done” and I'll give you the latest "extractor.py" next.
