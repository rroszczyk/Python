import sys


class NumberError(ValueError):
    pass


def substitue(separator, number):
    if len(number) not in [9, 11]:
        return None
    replaced = number.replace(separator, "", 2)
    if len(replaced) == 9 and replaced.isdigit():
        return replaced
    return None


def get_local_type(local_number, separators=["", " ", "-"]):
    for separator in separators:
        replaced = substitue(separator, local_number)
        if replaced is not None:
            return replaced
    return None


def validate_number(phone_number):
    if phone_number[0:2] == "0-":
        replaced = get_local_type(phone_number[2:], [" "])
        if replaced is None:
            raise NumberError("Expected 0-XXX XXX XXX")
        return replaced
    if phone_number[0:5] == "0048 ":
        replaced = get_local_type(phone_number[5:], [" "])
        if replaced is None:
            raise NumberError("Expected 0048 XXX XXX XXX")
        return "+48" + replaced
    if phone_number[0:4] == "+48 ":
        replaced = get_local_type(phone_number[4:], ["-"])
        if replaced is None:
            raise NumberError("Expected +48 XXX-XXX-XXX")
        return "+48" + replaced
    if phone_number[0:3] == "+48":
        replaced = get_local_type(phone_number[3:], [""])
        if replaced is None:
            raise NumberError("Expected +48XXXXXXXXX")
        return "+48" + replaced
    replaced = get_local_type(phone_number)
    if replaced is None:
        raise NumberError("Expected XXXXXXXXX or XXX XXX XXX or XXX-XXX-XXX")
    return replaced  


if __name__ == "__main__":
    try:
        number = validate_number(sys.argv[1])
    except NumberError as error:
        sys.stderr.write("Invalid number format: {}.\n".format(error))
        sys.exit(1)
    else:
        print(number)