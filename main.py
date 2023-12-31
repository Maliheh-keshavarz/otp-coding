
from otp_generator import otp
from encryption_module import encode
from decryption_module import decode


def main():

    """
    Main function for encrypting and decrypting plain text using a one-time pad (OTP).

    This code takes user input for a plain text message and performs the following steps:
        1. Generates a one-time pad (OTP) consisting of random letters.
        2. Encrypts the plain text message using the OTP.
        3. Decrypts the ciphertext back to the original plain text.

 
    """

    alphabet_to_number = {chr(97 + i): i for i in range(26)}
    number_to_alphabet = {i: chr(97 + i) for i in range(26)}
    # number_to_alphabet = {val: k for k, val in alphabet_to_number.items()}  


    message= input("Enter the plain text: ")
    plain_text =message.lower()
    plain_text=plain_text.replace(" ", "")
    
    

    opt_letters= otp(plain_text,number_to_alphabet)
    print("OTP:", opt_letters)


    ciphertext = encode(plain_text,opt_letters,alphabet_to_number,number_to_alphabet)
    print(f"Encrypted Text (Ciphertext): {ciphertext}")

    decoded_text = decode(ciphertext, opt_letters, alphabet_to_number, number_to_alphabet)
    print(f"Decrypted Text (Plain Text): {decoded_text}")


if __name__ == "__main__":
    main()