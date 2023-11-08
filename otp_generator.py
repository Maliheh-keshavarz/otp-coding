



import secrets

def otp(text,number_to_alphabet):

    """
    Generates a one-time pad (OTP) for encrypting text.

    Parameters:
        text (str): The input text to be encrypted.
        number_to_alphabet (dict): A dictionary that maps numbers to alphabet letters.

    Returns:
        letters(list of str): A list of letters representing the one-time pad (OTP).
    """



    key=[]
    letters=[]


    for i in range (len((text))):
        random_number = secrets.randbelow(26)
        key.append(random_number)
    
   

    for number in key:
        letter = number_to_alphabet.get(number, '')
        letters.append(letter)

    
    return letters
