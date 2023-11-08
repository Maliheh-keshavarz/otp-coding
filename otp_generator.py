import secrets

def otp(text,number_to_alphabet):
    key=[]
    letters=[]


    for i in range (len((text))):
        random_number = secrets.randbelow(26)
        key.append(random_number)
    
   

    for number in key:
        letter = number_to_alphabet.get(number, '')
        letters.append(letter)

    
    return letters
