def binary_to_ascii(binary_item):
    """
    Convert a binary number to an ASCII char.
    """
    str_number = str(binary_item)

    if str_number == '':
        return -1
    
    decimal_number = int(str_number, 2)
    decoded = chr(decimal_number)
    return decoded

def binary_list_to_string(binary_list):
    """
    Convert a binary list to an ASCII string.
    """
    string = ''

    for binary_ch in binary_list:
        result = binary_to_ascii(binary_ch)

        if result == -1:
            break

        else:
            string += result

    return string
