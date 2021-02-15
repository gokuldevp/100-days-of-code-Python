import pandas as pd

# read the csv file and create a dict from it of format {"letter": "code"}
PATH = "nato_phonetic_alphabet.csv"
nato_df = pd.read_csv(PATH)
nato_phonetic_alphabet_dict = {row["letter"]: row["code"] for (index, row) in nato_df.iterrows()}

# compare each letter from users input to the dict and print the phonetic code for the letter
start = True
while start:
    user_input = input("What is the word? :").upper()
    try:
        phonetic_code = [nato_phonetic_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Only work with letters, Try again")
    else:
        print(phonetic_code)
        start = False
