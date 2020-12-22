from random import randint


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def generate_otp():
    return random_with_N_digits(6)
    # digits = "0123456789"
    # OTP = ""
    # for i in range(6):
    #     OTP += digits[math.floor(random.random() * 10)]

    # return OTP


otp_code = generate_otp()
