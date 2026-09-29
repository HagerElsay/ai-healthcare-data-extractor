def deidentify_patient(patient):

    deidentified_patient = {
        "given_name": "[DE-IDENTIFIED]",
        "family_name": "[DE-IDENTIFIED]",
        "date_of_birth": "[DE-IDENTIFIED]",
        "conditions": patient["conditions"],
        "blood_pressure": patient["blood_pressure"]
    }

    return deidentified_patient
