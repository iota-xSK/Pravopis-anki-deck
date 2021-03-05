import csv
import os

file = "words.csv"
file_cleaned = "words_cleaned.csv"
letters_file = "accented_letters"

def unaccent(accented_word, accent_file):
    with open(accent_file) as f:
        Lines = f.read().splitlines()
        #print(Lines)
        accented_letters_list = []
        for line in Lines:
            chars = []
            for letter in line:
                chars.append(letter.lower())
            accented_letters_list.append(chars)
    for letters in accented_letters_list:
        for letter in letters:
            accented_word = accented_word.replace(letter, letters[0])
    return(accented_word)

with open(file, "r") as f:
    read = csv.reader(f)
    if os.path.exists(file_cleaned):
        with open(file_cleaned, "w") as g:
            g.write("")
    else:
        open(file_cleaned, "x")
    with open(file_cleaned, "a") as g:
        written = csv.writer(g)
        for row in read:
            row[0] = unaccent(row[0], letters_file)
            declentions_position = [row[1].find("〈"), row[1].find("〉")]
            definition = ""
            for i in range(len(row[1])):
                if i < declentions_position[0] or i > declentions_position[1]:
                    definition += row[1][i]
            row[1] = definition
            written.writerow(row)
