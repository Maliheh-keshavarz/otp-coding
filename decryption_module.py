

def decode(ciphertext, opt_letters, alphabet_to_number, number_to_alphabet):
    """
    Decrypts ciphertext using a one-time pad (OTP).

    This function takes a ciphertext message, a list of one-time pad (OTP) letters, and dictionaries for mapping
    between alphabet letters and numbers. It decrypts the ciphertext message using the OTP.

    Parameters:
        ciphertext (str): The ciphertext message to be decrypted.
        opt_letters (list of str): A list of OTP letters used for decryption.
        alphabet_to_number (dict): A dictionary mapping alphabet letters to numbers.
        number_to_alphabet (dict): A dictionary mapping numbers to alphabet letters.

    Returns:
        str: The decrypted plain text message.
    
    """
    

    decoded_text = []

    for i in range(len(ciphertext)):
        cipher_number = alphabet_to_number.get(ciphertext[i], 0)
        opt_number = alphabet_to_number.get(opt_letters[i], 0)
        total = (cipher_number - opt_number) % 26
        decoded_text.append(number_to_alphabet.get(total, ' '))

    return ''.join(decoded_text)

