# List of commonly used 4-digit and 6-digit MPINs
common_mpin_list = {
    "1234", "0000", "1111", "2222", "3333", "4444", "5555",
    "6666", "7777", "8888", "9999", "1212", "6969", "2000",
    "4321", "1010", "2580", "5683", "123456", "654321", "000000",
    "111111", "222222", "333333", "444444", "555555", "666666",
    "777777", "888888"
}

def check_mpin(mpin, birth_year_self, birth_year_spouse, anniversary_year):
    reasons = []  # List to store reasons for weak MPIN

    if not mpin.isdigit() or len(mpin) not in [4, 6]:
        return {"Error": "Invalid MPIN! Please enter a 4-digit or 6-digit number."}

    if mpin in common_mpin_list:
        reasons.append("COMMONLY_USED")

    # Check if MPIN matches user's birth year (full year or last two digits)
    if mpin == birth_year_self or (len(mpin) == 2 and mpin == birth_year_self[-2:]):
        reasons.append("DEMOGRAPHIC_DOB_SELF")

    if mpin == birth_year_spouse or (len(mpin) == 2 and mpin == birth_year_spouse[-2:]):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")

    # Check if MPIN matches anniversary year
    if mpin == anniversary_year or (len(mpin) == 2 and mpin == anniversary_year[-2:]):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    strength = "WEAK" if reasons else "STRONG"

    return {"Strength": strength, "Reasons": reasons}


mpin_input = input("Enter a 4-digit or 6-digit MPIN: ").strip()
birth_year_self = input("Enter your birth year (YYYY): ").strip()
birth_year_spouse = input("Enter your spouse's birth year (YYYY) or press Enter to skip: ").strip() or "0000"
anniversary_year = input("Enter your anniversary year (YYYY) or press Enter to skip: ").strip() or "0000"


result = check_mpin(mpin_input, birth_year_self, birth_year_spouse, anniversary_year)
print(result)
