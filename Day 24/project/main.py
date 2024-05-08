PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)


with open("input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name.strip())

        with open(f"./outputs/ready_to_send/{name.strip()}_letter.txt", "w") as name_letter:
            name_letter.write(new_letter)


