import datetime

def is_common_mpin(mpin):
   
    common_mpins_4 = [
        "1234", "0000", "1111", "2580", "1212", "7777", "1004", "2000", "4444", "2222",
        "6969", "9999", "3333", "5555", "6666", "0852", "1998", "2001", "2002", "2003",
        "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "0123",
        "9876", "1122", "1230", "1990", "1991", "1992", "1993", "1994", "1995", "1996",
        "1997", "1999", "0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008",
        "0009", "0101", "0202", "0303", "0404", "0505", "0606", "0707", "0808", "0909",
        "1010", "1111", "1212", "1313", "1414", "1515", "1616", "1717", "1818", "1919",
        "7070", "7171", "7272", "7373", "7474", "7575", "7676", "7777", "7878", "7979",
        "8080", "8181", "8282", "8383", "8484", "8585", "8686", "8787", "8888", "8989",
        "9090", "9191", "9292", "9393", "9494", "9595", "9696", "9797", "9898", "9999",
        "1234", "4321", "1020", "2010", "1001", "1100", "0110", "0101", "1010", "2200",
        "0022", "1122", "2211", "1337", "1945", "2023"
    ]
    common_mpins_6 = [
        "123456", "000000", "111111", "654321", "121212", "777777", "100400", "200000",
        "444444", "222222", "696969", "999999", "333333", "555555", "666666", "085208",
        "199819", "200120", "200220", "200320", "200420", "200520", "200620", "200720",
        "200820", "200920", "201020", "201120", "201220", "012345", "987654"
    ]

    if len(mpin) == 4:
        return mpin in common_mpins_4
    elif len(mpin) == 6:
        return mpin in common_mpins_6
    else:
        return False

def check_mpin_strength(mpin, dob_self=None, dob_spouse=None, anniversary=None):

    reasons = []
    strength = "STRONG"

    if is_common_mpin(mpin):
        strength = "WEAK"
        reasons.append("COMMONLY_USED")

    if dob_self:
        dob_self_str = dob_self.strftime("%d%m")
        dob_self_str_reversed = dob_self.strftime("%m%d")
        dob_self_year_str = dob_self.strftime("%y%m")
        dob_self_year_str_reversed = dob_self.strftime("%m%y")

        if dob_self_str in mpin or dob_self_str_reversed in mpin or dob_self_year_str in mpin or dob_self_year_str_reversed in mpin:
            strength = "WEAK"
            reasons.append("DEMOGRAPHIC_DOB_SELF")

    if dob_spouse:
        dob_spouse_str = dob_spouse.strftime("%d%m")
        dob_spouse_str_reversed = dob_spouse.strftime("%m%d")
        dob_spouse_year_str = dob_spouse.strftime("%y%m")
        dob_spouse_year_str_reversed = dob_spouse.strftime("%m%y")

        if dob_spouse_str in mpin or dob_spouse_str_reversed in mpin or dob_spouse_year_str in mpin or dob_spouse_year_str_reversed in mpin:
            strength = "WEAK"
            reasons.append("DEMOGRAPHIC_DOB_SPOUSE")

    if anniversary:
        anniversary_str = anniversary.strftime("%d%m")
        anniversary_str_reversed = anniversary.strftime("%m%d")
        anniversary_year_str = anniversary.strftime("%y%m")
        anniversary_year_str_reversed = anniversary.strftime("%m%y")

        if anniversary_str in mpin or anniversary_str_reversed in mpin or anniversary_year_str in mpin or anniversary_year_str_reversed in mpin:
            strength = "WEAK"
            reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    return {"strength": strength, "reasons": reasons}

def get_date_input(prompt):
    
    while True:
        try:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")
            

while True:
    mpin = input("Enter your 4 or 6 digit MPIN: ")
    if mpin.isdigit() and (len(mpin) == 4 or len(mpin) == 6):
        break
    else:
        print("Invalid MPIN.")


dob_self = None
dob_spouse = None
anniversary = None

if input("Do you want to enter your date of birth? (yes/no): ").lower() == "yes":
    dob_self = get_date_input("Enter your date of birth")

if input("Do you want to enter your spouse's date of birth? (yes/no): ").lower() == "yes":
    dob_spouse = get_date_input("Enter spouse's date of birth")

if input("Do you want to enter your anniversary date? (yes/no): ").lower() == "yes":
    anniversary = get_date_input("Enter anniversary date")


result = check_mpin_strength(mpin, dob_self, dob_spouse, anniversary)

print(f"MPIN Strength: {result['strength']}")
if result["strength"] == "WEAK":
    print("Reasons for weakness:")
    for reason in result["reasons"]:
        print(f"- {reason}")
