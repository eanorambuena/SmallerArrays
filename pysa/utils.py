def binary_to_ascii(binary_item):
    """
    Convert a binary string to an ASCII char.
    """
    str_number = str(binary_item)
    decimal_number = int(str_number, 2)
    decoded = chr(decimal_number)
    return decoded

def binary_to_string(binary_list):
    """
    Convert a binary string to an ASCII string.
    """
    return "".join([binary_to_ascii(binary_ch) for binary_ch in binary_list])
