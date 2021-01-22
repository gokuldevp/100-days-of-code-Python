
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):

    print("The Cipher Text is :")
    for i in range(len(text)):
        if text[i] in alphabet:
            encrypt_code = alphabet.index(text[i])
            if encrypt_code + shift >= 26:
                encrypt_code = (encrypt_code - 26) + shift
            else:
                encrypt_code = encrypt_code + shift
            encrypt_text = alphabet[encrypt_code]
        else:
            encrypt_text = text[i]
        print(f"{encrypt_text}", end = "")

def decrypt(text, shift):
    print("The Plain Text is :")


  # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  # e.g.
  # cipher_text = "mjqqt"
  # shift = 5
  # plain_text = "hello"
  # print output: "The decoded text is hello"

    for i in range(len(text)):
        if text[i] in alphabet:
            decrypt_code = alphabet.index(text[i])
            if decrypt_code + shift >= 26:
                decrypt_code = decrypt_code + 26 - shift
            else:
                decrypt_code = decrypt_code - shift
            plain_text = alphabet[decrypt_code]
        else:
            plain_text = text[i]
        print(f"{plain_text}", end = "")

# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.


try_again = True

while try_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "decode":
        decrypt(text, shift)
    elif direction == "encode":
        encrypt(text, shift)
    else:
        print("You didn't select 'encode' or 'decode'!")
    again = input("\nDo You Want to try again? 'Yes' or 'No'? \n").lower()

    if again == "no":
        try_again = False
        print("\nCome again Later!!!")
