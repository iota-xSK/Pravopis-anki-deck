import csv
import re

file="words_cleaned.csv"
deck_file="deck.csv"

with open(file, "r") as f:
    read = csv.reader(f)
    words = []
    for row in read:
        words.append(row)


list_of_hard_parts = ["ć", "č", "dž", "đ", "ije", "je"]
hard_part_reference = {
"č": "č ili ć",
"ć": "č ili ć",
"dž": "dž ili đ",
"đ": "dž ili đ",
"ije": "ije ili je",
"je": "ije ili je"}

def where_is_part(word, part):
    found_positions = []
    for i in range(len(word)-(len(part)-1)):
        buffer = ""
        for j in range(len(part)):
            buffer += word[j+i]
        if buffer == part:
            found_positions.append((i, i+len(part)-1))
    return(found_positions)

def make_cards(_words, parts, reference):
	cards = []
	for _word in _words:
		working_word = _word
		for part in parts:
			positions = where_is_part(_word[0], part)
			for position in positions:
				#print(position)
				#print(_word[0][position[0]-1:position[1]+1])
				if _word[0][position[0]-1:position[1]+1] == "ije":
					break
				#print("print 2", _word)
				#working_word[0] = working_word[0][0:position[0]] + "_"*(position[1]-position[0]+1) + working_word[0][position[1]+1:len(working_word[0])]
				#working_word[0] = working_word[0][0:position[0]] + "_" + working_word[0][position[1]+1:len(working_word[0])]
				#print("print 3", _word)
				word_q = _word[0][0:position[0]] + "_" + _word[0][position[1]+1:len(_word[0])]
				card = [_word[0], _word[1], word_q, reference[part] + "?", reference[part]]
				#card = [word_old[0].replace("_", part), word_old[1], word_q, reference[part] + "?", reference[part]]
				cards.append(card)
				#print("---------------")
	return(cards)

deck = make_cards(words, list_of_hard_parts, hard_part_reference)

with open(deck_file, "w", newline='') as f:
    written = csv.writer(f, delimiter="	")
    for card in deck:
        written.writerow(card)
