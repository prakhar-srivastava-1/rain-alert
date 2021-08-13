def will_it_rain(code_list):
    for code in code_list:
        if code < 700:
            return True
    return False
