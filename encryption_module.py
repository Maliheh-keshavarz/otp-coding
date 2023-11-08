

def encode(plain_text,opt_letters,alphabet_to_number,number_to_alphabet):
    """
    Encrypts plain text using a one-time pad (OTP).

    This function takes a plain text message, a list of one-time pad (OTP) letters, and dictionaries for mapping
    between alphabet letters and numbers. It encrypts the plain text message using the OTP.

    Parameters:
        plain_text (str): The plain text message to be encrypted.
        opt_letters (list of str): A list of OTP letters for encryption.
        alphabet_to_number (dict): A dictionary mapping alphabet letters to numbers.
        number_to_alphabet (dict): A dictionary mapping numbers to alphabet letters.

    Returns:
        str: The encrypted ciphertext.
    
    Raises:
        ValueError: If the length of the plain text and OTP letters do not match.
    """



    initial_total = []
    ciphertext = []

    if len(plain_text) != len(opt_letters):
        raise ValueError("plain_text and opt_letters must have the same length.")
    
    for i in range(len(plain_text)):
        plain_number = alphabet_to_number.get(plain_text[i], 0)
        opt_number = alphabet_to_number.get(opt_letters[i], 0)
        total = (plain_number + opt_number) % 26
        initial_total.append(total)

    for total in initial_total:
        letter = number_to_alphabet.get(total, ' ')
        ciphertext.append(letter)


    return ''.join(ciphertext)


