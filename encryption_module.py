

def encode(plain_text,opt_letters,alphabet_to_number,number_to_alphabet):
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