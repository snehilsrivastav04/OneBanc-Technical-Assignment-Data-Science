import pytest
from main_code import check_mpin  


common_mpins = [
    ("1234", "1990", "1988", "2015", "WEAK", ["COMMONLY_USED"]),
    ("0000", "1992", "1990", "2018", "WEAK", ["COMMONLY_USED"]),
    ("1111", "1995", "1993", "2020", "WEAK", ["COMMONLY_USED"]),
    ("123456", "1998", "1999", "2021", "WEAK", ["COMMONLY_USED"]),
    ("654321", "2000", "2002", "2022", "WEAK", ["COMMONLY_USED"]),
    ("999999", "1987", "1986", "2010", "WEAK", ["COMMONLY_USED"]),
]


demographic_mpins = [
    ("2000", "1995", "2000", "2018", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("5102", "1993", "1995", "2015", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),  # Reversed 2015
    ("5991", "1995", "2000", "2018", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),  # Reversed 1995
    ("95", "1995", "2000", "2018", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("00", "1995", "2000", "2018", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("18", "1993", "1995", "2018", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("39", "1993", "1995", "2018", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),  # Reversed '93'
]


multi_reason_mpins = [
    ("1990", "1990", "1990", "1990", "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]),
    ("9001", "1990", "2001", "2010", "WEAK", ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_ANNIVERSARY"]),  # Reversed 1990
]


strong_mpins = [
    ("374829", "1992", "1993", "2015", "STRONG", []),
    ("981276", "1980", "1985", "2010", "STRONG", []),
    ("573810", "2003", "2005", "2025", "STRONG", []),
    ("258369", "1993", "1995", "2022", "STRONG", []),
]


invalid_mpins = [
    ("12AB", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("123", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("1234567", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("abcdef", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
    ("@#$%!", "1995", "1990", "2015", "Error", "Invalid MPIN!"),
]


test_cases = common_mpins + demographic_mpins + multi_reason_mpins + strong_mpins + invalid_mpins

@pytest.mark.parametrize("mpin, birth_year_self, birth_year_spouse, anniversary_year, expected_strength, expected_reasons", test_cases)
def test_check_mpin(mpin, birth_year_self, birth_year_spouse, anniversary_year, expected_strength, expected_reasons):
    print(f"\nRunning test for MPIN: {mpin}")
    
    result = check_mpin(mpin, birth_year_self, birth_year_spouse, anniversary_year)
    print(f"Result: {result}")

    if expected_strength == "Error":
        assert "Error" in result and result["Error"] == expected_reasons
    else:
        assert result["Strength"] == expected_strength
        assert set(result["Reasons"]) == set(expected_reasons)  # Use set to avoid order mismatches
