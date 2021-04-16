PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", 'w') as file:
            file.write(new_letter)