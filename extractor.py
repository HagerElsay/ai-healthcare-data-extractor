import re


def extract_patient_data(text):

    # ==============================
    # NAME
    # ==============================

    name_match = re.search(
        r"^([A-Za-z]+)\s+([A-Za-z]+)",
        text
    )

    if name_match:
        given_name = name_match.group(1)
        family_name = name_match.group(2)
    else:
        given_name = None
        family_name = None


    # ==============================
    # DATE OF BIRTH
    # ==============================

    dob_match = re.search(
        r"born\s+(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})",
        text,
        re.IGNORECASE
    )

    months = {
        "january": "01",
        "february": "02",
        "march": "03",
        "april": "04",
        "may": "05",
        "june": "06",
        "july": "07",
        "august": "08",
        "september": "09",
        "october": "10",
        "november": "11",
        "december": "12"
    }

    if dob_match:

        day = dob_match.group(1)
        month_name = dob_match.group(2).lower()
        year = dob_match.group(3)

        month = months.get(month_name)

        if month:
            date_of_birth = f"{year}-{month}-{int(day):02d}"
        else:
            date_of_birth = None

    else:
        date_of_birth = None


    # ==============================
    # CONDITIONS
    # ==============================

    condition_match = re.search(
        r"has\s+(.+?)(?:\.|blood pressure|BP)",
        text,
        re.IGNORECASE
    )

    if condition_match:

        condition_text = condition_match.group(1)

        conditions = [
            condition.strip()
            for condition in re.split(
                r"\s+and\s+|,",
                condition_text
            )
            if condition.strip()
        ]

    else:
        conditions = []


    # ==============================
    # BLOOD PRESSURE
    # ==============================

    bp_match = re.search(
        r"(\d{2,3})\s*/\s*(\d{2,3})",
        text
    )

    if bp_match:

        systolic = int(bp_match.group(1))
        diastolic = int(bp_match.group(2))

    else:

        systolic = None
        diastolic = None


    # ==============================
    # RETURN DATA
    # ==============================

    return {
        "given_name": given_name,
        "family_name": family_name,
        "date_of_birth": date_of_birth,
        "conditions": conditions,
        "blood_pressure": {
            "systolic": systolic,
            "diastolic": diastolic
        }
    }

Save/commit it as "extractor.py".

Then say done → I'll give you "validator.py".
