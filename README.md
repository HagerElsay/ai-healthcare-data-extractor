AI Healthcare Data Extractor

A Python healthcare data extraction tool that converts unstructured patient text into structured data, validates the extracted information, de-identifies patient identifiers, and generates FHIR output.

Features

- Extracts patient names
- Extracts date of birth
- Extracts medical conditions
- Extracts blood pressure
- Validates extracted healthcare data
- De-identifies direct patient identifiers
- Converts structured data into FHIR resources
- Generates a FHIR Bundle
- Uses Python standard libraries

Workflow

Unstructured Patient Text
          ↓
      Extraction
          ↓
       Validation
          ↓
   Structured Patient Data
          ↓
    De-identification
          ↓
      FHIR Conversion
          ↓
       FHIR Bundle

Project Structure

ai-healthcare-data-extractor/
│
├── main.py
├── extractor.py
├── validator.py
├── fhir_converter.py
└── deidentifier.py

Example Input

Ahmed Ali, born 12 June 1995, has diabetes and asthma. BP: 140/90

Example Output

The tool extracts:

Name: Ahmed Ali
Date of Birth: 1995-06-12
Conditions: diabetes, asthma
Blood Pressure: 140/90

It then creates:

- Structured patient data
- De-identified patient data
- FHIR Patient resource
- FHIR Condition resources
- FHIR Blood Pressure Observation
- FHIR Bundle

Technology

- Python
- Regular expressions
- JSON
- HL7 FHIR concepts

Current Limitations

This is a Version 1 prototype using rule-based extraction. It is designed for learning, experimentation, and healthcare AI development.

It is not intended for clinical decision-making or production healthcare use.

Future Improvements

- NLP/LLM-based extraction
- Support for clinical documents
- More healthcare data types
- Standard medical coding
- Batch document processing
- API integration
- More advanced de-identification
- Production-grade FHIR validation

Goal

The project explores how AI and software can help transform unstructured healthcare information into structured, interoperable, and privacy-aware data.
