import pytest
from main_code import check_mpin  

# Define test cases
test_cases = [
    # Weak MPINs 
    ("1234", "1990", "1988", "2015", "WEAK", ["COMMONLY_USED"]),
    ("0000", "1992", "1990", "2018", "WEAK", ["COMMONLY_USED"]),
    ("1111", "1995", "1993", "2020", "WEAK", ["COMMONLY_USED"]),
    ("123456", "1998", "1999", "2021", "WEAK", ["COMMONLY_USED"]),
    ("654321", "2000", "2002", "2022", "WEAK", ["COMMONLY_USED"]),
    ("999999", "1987", "1986", "2010", "WEAK", ["COMMONLY_USED"]),


    ("2000", "1995", "2000", "2018", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("2015", "1993", "1995", "2015", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("1990", "1990", "1990", "1990", "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]),
   

    # Strong MPINs 
    ("374829", "1992", "1993", "2015", "STRONG", []),
    ("981276", "1980", "1985", "2010", "STRONG", []),
    ("573810", "2003", "2005", "2025", "STRONG", []),

    # Invalid MPINs
    ("12AB", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("123", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("1234567", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("abcdef", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("@#$%!", "1995", "1990", "2015", "Error", "Invalid MPIN!"),

    # More test cases for additional coverage
    ("258369", "1993", "1995", "2022", "STRONG", []),
    ("741852", "1985", "1987", "2000", "STRONG", []),
    ("369258", "1975", "1978", "1995", "STRONG", []),



]

@pytest.mark.parametrize("mpin, birth_year_self, birth_year_spouse, anniversary_year, expected_strength, expected_reasons", test_cases)
def test_check_mpin(mpin, birth_year_self, birth_year_spouse, anniversary_year, expected_strength, expected_reasons):
    print(f"Running test for MPIN: {mpin}")
    
    result = check_mpin(mpin, birth_year_self, birth_year_spouse, anniversary_year)
    print(f"Result: {result}")

    if expected_strength == "Error":
        assert "Error" in result and result["Error"] == expected_reasons
    else:
        assert result["Strength"] == expected_strength
        assert result["Reasons"] == expected_reasons
