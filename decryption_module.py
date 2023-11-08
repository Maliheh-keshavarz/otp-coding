

def decode(ciphertext, opt_letters, alphabet_to_number, number_to_alphabet):
    
    

    decoded_text = []

    for i in range(len(ciphertext)):
        cipher_number = alphabet_to_number.get(ciphertext[i], 0)
        opt_number = alphabet_to_number.get(opt_letters[i], 0)
        total = (cipher_number - opt_number) % 26
        decoded_text.append(number_to_alphabet.get(total, ' '))

    return ''.join(decoded_text)

