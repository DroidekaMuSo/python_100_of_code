print("Welcome to Morse translator, ")
sentence = input("Please, type what you what to translate into Morse").upper()

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


def translator(sentence):
    sentence_dict = list(sentence)
    translate = []

    for let in sentence_dict:

        if let == ' ':
            translate.append(' ')
        elif let in morse_code_dict:
            translate.append(morse_code_dict[let])
        else:
            translate.append("?")

    translated_sentence = " ".join(translate)

    print(f"""
    What you wrote: {sentence}
    What you got: {translated_sentence}
    """)


translator(sentence)
