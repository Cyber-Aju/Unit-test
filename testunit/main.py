import re

# Question 1: -----------------------------------
regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'


def check_email(email):
    if (re.search(regex, email)):
        return True
    else:
        return False


def check_psw_upper(psw):
    result = any(char.isupper() for char in psw)
    return result


def check_psw_digit(psw):
    result = any(char.isdigit() for char in psw)
    return result


def check_psw_lower(psw):
    result = any(char.islower() for char in psw)
    return result


def check_psw_alphaNumeric(psw):
    result = psw.isalnum()
    return result


def check_psw(psw):
    if (check_psw_alphaNumeric(psw) and check_psw_digit(psw)
            and check_psw_upper(psw) and check_psw_lower(psw)
            and check_psw_digit(psw) and len(psw) >= 7):
        print("Valid password")
        return True
    else:
        print("Invalid password")
        return False


check_psw("QWERt55")
check_psw("QWERT55")
check_psw("Qwert5@")


# New functions: ------------------------------------
def check_psw_equal(psw1, psw2):
    return psw1 == psw2


def check_credentials(email, psw1, psw2):
    return check_email(email) and check_psw(psw1) and check_psw_equal(
        psw1, psw2)
