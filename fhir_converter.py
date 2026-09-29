def convert_to_fhir(patient):

    # Create FHIR Patient
    fhir_patient = {
        "resourceType": "Patient",
        "id": "patient-001",
        "name": [
            {
                "use": "official",
                "family": patient["family_name"],
                "given": [patient["given_name"]]
            }
        ],
        "birthDate": patient["date_of_birth"]
    }


    # Create FHIR Conditions
    fhir_conditions = []

    for index, condition in enumerate(
        patient["conditions"],
        start=1
    ):

        fhir_condition = {
            "resourceType": "Condition",
            "id": f"condition-{index}",
            "subject": {
                "reference": "Patient/patient-001"
            },
            "code": {
                "text": condition
            }
        }

        fhir_conditions.append(fhir_condition)


    # Create FHIR Blood Pressure Observation
    systolic = patient["blood_pressure"]["systolic"]
    diastolic = patient["blood_pressure"]["diastolic"]

    fhir_observation = {
        "resourceType": "Observation",
        "id": "blood-pressure-001",
        "status": "final",
        "code": {
            "text": "Blood pressure"
        },
        "subject": {
            "reference": "Patient/patient-001"
        },
        "component": [
            {
                "code": {
                    "text": "Systolic blood pressure"
                },
                "valueQuantity": {
                    "value": systolic,
                    "unit": "mmHg"
                }
            },
            {
                "code": {
                    "text": "Diastolic blood pressure"
                },
                "valueQuantity": {
                    "value": diastolic,
                    "unit": "mmHg"
                }
            }
        ]
    }


    # Create FHIR Bundle
    entries = [
        {
            "resource": fhir_patient
        }
    ]

    for condition in fhir_conditions:
        entries.append({
            "resource": condition
        })

    entries.append({
        "resource": fhir_observation
    })


    fhir_bundle = {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": entries
    }

    return fhir_bundle

Save/commit as "fhir_converter.py".

Then next → "deidentifier.py", the last Python file.
