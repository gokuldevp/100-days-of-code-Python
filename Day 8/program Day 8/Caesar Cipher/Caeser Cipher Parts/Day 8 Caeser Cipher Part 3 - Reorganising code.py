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


while try_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode" or "decode":
        print(f"The {direction} Word is :")
        cipher(text, shift)
    else:
        print("\nYou didn't select 'encode' or 'decode'!")
    again = input("\nDo You Want to try again? 'Yes' or 'No'? \n").lower()

    if again == "no":
        try_again = False
        print("\nCome again Later!!!")
