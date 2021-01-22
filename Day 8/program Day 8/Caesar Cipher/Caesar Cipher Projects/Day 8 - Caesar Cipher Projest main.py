import cipherarts

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(text, shift):

    for i in range(len(text)):
        if text[i] in alphabet:
            code = alphabet.index(text[i])

            if direction == "encode":

                if code + shift >= 26:
                    code = (code - 26) + shift

                else:
                    code = code + shift

            elif direction == "decode":

                if code + shift >= 26:
                    code = code + 26 - shift

                else:
                    code = code - shift
            changed_text = alphabet[code]

        else:
            changed_text = text[i]
        print(f"{changed_text}", end = "")


try_again = True

print(cipherarts.logo)
print("WELCOME TO CAESAR CIPHER ENCODER AND DECODER!!!\n")

while try_again == True:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    if direction == "encode" or "decode":
        print(f"\nThe {direction} Word is :")
        cipher(text, shift)

    else:
        print("\nYou didn't select 'encode' or 'decode'!")

    again = input("\n\nDo You Want to try again? 'Yes' or 'No'? \n").lower()

    if again == "no":
        try_again = False
        print("\nCome again Later!!!")
