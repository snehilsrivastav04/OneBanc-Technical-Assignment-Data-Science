def is_common_mpin(mpin):
    """Checks if the MPIN is commonly used."""
    common_mpins = {'1234', '0000', '1111', '123456', '654321', '999999',
                   "1234", "0000", "1111", "2580", "1212", "7777", "1004", "2000", "4444", "2222",
        "6969", "9999", "3333", "5555", "6666", "0852", "1998", "2001", "2002", "2003",
        "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "0123",
        "9876", "1122", "1230", "1990", "1991", "1992", "1993", "1994", "1995", "1996",
        "1997", "1999", "0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008",
        "0009", "0101", "0202", "0303", "0404", "0505", "0606", "0707", "0808", "0909",
        "1010", "1111", "1212", "1313", "1414", "1515", "1616", "1717", "1818", "1919",
        "2020", "2121", "2222", "2323", "2424", "2525", "2626", "2727", "2828", "2929",
        "3030", "3131", "3232", "3333", "3434", "3535", "3636", "3737", "3838", "3939",
        "4040", "4141", "4242", "4343", "4444", "4545", "4646", "4747", "4848", "4949",
        "5050", "5151", "5252", "5353", "5454", "5555", "5656", "5757", "5858", "5959",
        "6060", "6161", "6262", "6363", "6464", "6565", "6666", "6767", "6868", "6969",
        "7070", "7171", "7272", "7373", "7474", "7575", "7676", "7777", "7878", "7979",
        "8080", "8181", "8282", "8383", "8484", "8585", "8686", "8787", "8888", "8989",
        "9090", "9191", "9292", "9393", "9494", "9595", "9696", "9797", "9898", "9999",
        "1234", "4321", "1020", "2010", "1001", "1100", "0110", "0101", "1010", "2200",
        "0022", "1122", "2211", "1337", "1945", "2023"
        "123456", "000000", "111111", "654321", "121212", "777777", "100400", "200000",
        "444444", "222222", "696969", "999999", "333333", "555555", "666666", "085208",
        "199819", "200120", "200220", "200320", "200420", "200520", "200620", "200720",
        "200820", "200920", "201020", "201120", "201220", "012345", "987654"
    
}
    return mpin in common_mpins

def check_mpin(mpin, birth_year_self, birth_year_spouse, anniversary_year):
  

    # Validate MPIN format
    if not isinstance(mpin, str) or not mpin.isdigit() or len(mpin) < 4 or len(mpin) > 6:
        return {"Error": "Invalid MPIN!"}

    # Default result
    strength = "STRONG"
    reasons = []

    # Check if MPIN is commonly used
    if is_common_mpin(mpin):
        strength = "WEAK"
        reasons.append("COMMONLY_USED")

    # Function to check if MPIN contains any variation of a given year
    def contains_year_variations(mpin, year, reason_label):
        if year:
            year_str = str(year)  # Full 4-digit year
            year_short = year_str[-2:]  # Last two digits
            if year_str in mpin or year_short in mpin:
                return reason_label
        return None

    # Check for weak MPINs due to demographic years
    for year, label in [
        (birth_year_self, "DEMOGRAPHIC_DOB_SELF"),
        (birth_year_spouse, "DEMOGRAPHIC_DOB_SPOUSE"),
        (anniversary_year, "DEMOGRAPHIC_ANNIVERSARY"),
    ]:
        reason = contains_year_variations(mpin, year, label)
        if reason:
            strength = "WEAK"
            reasons.append(reason)

    return {"Strength": strength, "Reasons": reasons}
