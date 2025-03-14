def check_mpin(mpin, birth_year_self, birth_year_spouse, anniversary_year):
  
    
    if not isinstance(mpin, str) or not mpin.isdigit() or len(mpin) < 4 or len(mpin) > 6:
        return {"Error": "Invalid MPIN!"}
    
    
    result = {
        "Strength": "STRONG",
        "Reasons": []
    }
    
    # Check if MPIN is commonly used
    common_mpins = ['1234', '0000', '1111', '123456', '654321', '999999']
    if mpin in common_mpins:
        result["Strength"] = "WEAK"
        result["Reasons"].append("COMMONLY_USED")
    

    if birth_year_self in mpin or mpin in birth_year_self:
        result["Strength"] = "WEAK"
        if "DEMOGRAPHIC_DOB_SELF" not in result["Reasons"]:
            result["Reasons"].append("DEMOGRAPHIC_DOB_SELF")
    

    if birth_year_spouse in mpin or mpin in birth_year_spouse:
        result["Strength"] = "WEAK"
        if "DEMOGRAPHIC_DOB_SPOUSE" not in result["Reasons"]:
            result["Reasons"].append("DEMOGRAPHIC_DOB_SPOUSE")
    

    if anniversary_year in mpin or mpin in anniversary_year:
        result["Strength"] = "WEAK"
        if "DEMOGRAPHIC_ANNIVERSARY" not in result["Reasons"]:
            result["Reasons"].append("DEMOGRAPHIC_ANNIVERSARY")
    
    return result