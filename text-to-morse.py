from morse_dict import MORSE_CODE_DICT as MCD

user_input = input("Enter text you want to convert: ")

morse_output = []
for letter in user_input:
    letter = letter.upper()
    if letter in MCD:
        morse_output.append(MCD[letter])
    else:
         morse_output.append(letter)
print(f'Your string in morse code: {morse_output}')
