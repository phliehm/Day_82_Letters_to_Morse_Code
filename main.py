# 1. Greet user, tell the user what the program can do
# 2. Get text input
# 3. parse into single letters (how does morse code seperate letters and words?) --> list
# (Is this needed? Can I not just go through the input string?)
# 4. make a dictionary {letter: morse code} (once)
# 5. build new string by looping through the letters
# 6. output new string


import pandas as pd

# 1. Greet user, tell the user what the program can do

print('''This is a MORSE CODE - Converter!!
      Type your message, hit ENTER and then you will see the OUTPUT as Morse Code.
      Enjoy!''')

# 2. Get text input

input_str = input("Your message: ").upper()

# 3. parse into single letters (how does morse code seperate letters and words?) --> list
# (Is this needed? Can I not just go through the input string?)
# 4. make a dictionary {letter: morse code} (once)

morse_df = pd.read_csv("morse.csv", header=None)
morse_df = morse_df.rename(columns={0:"letters",1: "Morse"})
#print(morse_df.head())
letter_morse_dict = dict(morse_df.values)
morse_letter_dict = {v: k for k, v in letter_morse_dict.items()}        # other direction
print(letter_morse_dict)
print(morse_letter_dict)
# 5. build new string by looping through the letters
# 6. output new string

def convert_from_letters_to_morse(letters):
    coded_message  =""
    for c in input_str:
        coded_message +=letter_morse_dict[c]
        coded_message +=' '
    print(f"Your message in morse code is: {coded_message}")

convert_from_letters_to_morse(input_str)


### not done!!!
def convert_from_morse_to_letters(morse):
    coded_message  =""
    for c in input_str:
        coded_message +=morse_letter_dict[c]
        coded_message +=' '
    print(f"Your message in morse code is: {coded_message}")

