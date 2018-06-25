# Dict of all the morse code characters
morse_code = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
              "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
              "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
              "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
              "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
              "8": "---..", "9": "----.", "Ä": ".-.-", "Á": ".--.-", "Å": ".--.-", "Ch": "----",
              "É": "..-..", "Ñ": "--.--", "Ö": "---.", "Ü": "..--"}

# Function for converting morse code into english
def mortoeng():
    # lists are created: full_message is to print over all message, coded_message is to allow print of each morse code one by one
    full_message = []
    coded_message = []
    print("We will now ask you to input one code at a time, when you're done type DONE!")
    while True:
        #Asking users to input each morse code
        section = input("Please put in your code: ").lower()
        if section == "done":
            print("Ok, we will now convert your code!")
            break
        else:
            coded_message.append(section)

    # Using items loop to append the key into full_message
    for key, value in morse_code.items():
        for message in coded_message:
            # Message has to exactly equal the value or you will print out multiple values with the same item in it.
            if message == value:
                full_message.append(key)

    print(full_message)


def engtomor():
    full_message = []
    code = input("Please state your message to convert: ").upper()
    for char in code:
        if char in morse_code.keys():
            full_message.append(morse_code[char])

    print(full_message)


choice_conversion = input("""
                        Please choose the following:
                        A) Morse code to English
                        B) English to morse code""").lower()
if choice_conversion == "a":
    mortoeng()
else:
    engtomor()