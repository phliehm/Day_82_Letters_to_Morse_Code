# 1. Greet user, tell the user what the program can do
# 2. Get text input
# 3. parse into single letters (how does morse code seperate letters and words?) --> list
# (Is this needed? Can I not just go through the input string?)
# 4. make a dictionary {letter: morse code} (once)
# 5. build new string by looping through the letters
# 6. output new string


import pandas as pd


# 4. make a dictionary {letter: morse code} (once)
morse_df = pd.read_csv("morse.csv", header=None)
morse_df = morse_df.rename(columns={0:"letters",1: "Morse"})
#print(morse_df.head())
letter_morse_dict = dict(morse_df.values)
morse_letter_dict = {v: k for k, v in letter_morse_dict.items()}        # other direction
print(letter_morse_dict)
print(morse_letter_dict)

'''
letter_morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
                      'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
                          '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
'''

'''
morse_letter_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K',
                      '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V',
                        '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                          '-....': '6', '--...': '7', '---..': '8', '----.': '9'}
'''

# 1. Greet user, tell the user what the program can do

direction = input('''This is a MORSE CODE - Converter!!
                  
Type "c" if you want to write text and translate it to morse code, type "d" if you want to decode morse code: ''')

      

# 2. Get text input

input_str = input('''Morse Code: Letters are seperated by 3 spaces, words are seperated by 7 spaces.
Type your message, hit ENTER and then you will get the translated message. 

                                                Enjoy!
                  
"Your message: ''')

# 5. build new string by looping through the letters
def convert_from_letters_to_morse(letters):
    coded_message  =""
    for c in letters.upper():     # convert to uppercase letters
        try:
            coded_message +=letter_morse_dict[c]
            coded_message +='   ' # 3 spaces to seperate letters
        except KeyError:
            coded_message +='       ' # 7 spaces to seperate words, here also used fo symbols not knownH
    
    # 6. output new string
    return coded_message



# build new string by looping through space seperated morse code letters
def convert_from_morse_to_letters(morse):
    decoded_message  =""
    morse = morse.replace("       ", " # ") # replace 7 spaces with a special character which will be decoded later as a space, 
                                                    #the additional spaces are needed for the split
    morse = morse.replace("   ", " ") # replace letter seperation of 3 spaces with only one space                                                
    morse = morse.split()
    print(morse)
    for c in morse:
        try:
            decoded_message +=morse_letter_dict[c]
        except KeyError:
            decoded_message += ' '
    return decoded_message


# function to convert the message
def conversion(message):
    if direction == "c":
        result = convert_from_letters_to_morse(message)
    elif direction == "d":
        result = convert_from_morse_to_letters(message)
    print(f"Your converted message is: {result}")


conversion(input_str)
