def validate_patient_data(patient):

    errors = []

    # Check name
    if not patient["given_name"] or not patient["family_name"]:
        errors.append("Patient name not found.")

    # Check date of birth
    if not patient["date_of_birth"]:
        errors.append("Date of birth not found.")

    # Check conditions
    if len(patient["conditions"]) == 0:
        errors.append("No medical condition found.")

    # Check blood pressure
    systolic = patient["blood_pressure"]["systolic"]
    diastolic = patient["blood_pressure"]["diastolic"]

    if systolic is None or diastolic is None:

        errors.append("Blood pressure not found.")

    else:

        if systolic < 50 or systolic > 250:
            errors.append(
                "Systolic blood pressure is outside the accepted range."
            )

        if diastolic < 30 or diastolic > 150:
            errors.append(
                "Diastolic blood pressure is outside the accepted range."
            )

    return errors

Save/commit as "validator.py".

Then say next.
