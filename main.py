
from otp_generator import otp



def main():

    alphabet_to_number = {chr(97 + i): i for i in range(26)}
    number_to_alphabet = {i: chr(97 + i) for i in range(26)}
    # number_to_alphabet = {val: k for k, val in alphabet_to_number.items()}  


    message= input("Enter the plain text: ")
    plain_text =message.lower()
    plain_text=plain_text.replace(" ", "")
    
    





if __name__ == "__main__":
    main()