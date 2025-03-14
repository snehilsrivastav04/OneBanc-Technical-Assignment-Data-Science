# OneBanc-Technical-Assignment-Data-Science by Snehil Srivastav
MPIN Strength Validator
Overview
This project implements a MPIN  Strength Validator in Python. It evaluates MPINs based on common security weaknesses such as commonly used numbers, demographic relevance (birth years, anniversaries), and length constraints.

Features
Strength Classification: MPINs are categorized as STRONG or WEAK based on predefined rules.
Common Patterns Detection: Identifies commonly used MPINs like 1234, 0000, 1111, etc.
Demographic Checks: Detects if MPINs match personal information like birth years or anniversaries.
Validation for Invalid Inputs: Rejects MPINs that are too short, contain non-numeric characters, or exceed valid length.
Test Coverage
We implemented 40+ test cases using pytest, covering:
✅ Commonly used MPINs (weak)
✅ MPINs based on personal data (weak)
✅ Secure, randomized MPINs (strong)
✅ Invalid MPIN formats (errors)

To Run it , requires
pip install pytest
and after this run
!pytest C:/Users/snehi/Downloads/bnac/test_mpin.py -v 
to evaluate the file.
    Checks the strength of an MPIN based on common patterns and demographic data.
  
Parameters:
- mpin (str): The MPIN to be checked.
- birth_year_self (str): The user's birth year.
- birth_year_spouse (str): The spouse's birth year.
- anniversary_year (str): The wedding anniversary year.

Returns:
- dict: A dictionary with MPIN strength and reasons for weakness (if any).
  
