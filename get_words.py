import csv
from bs4 import BeautifulSoup
import requests
import time

file="page1.html"

def get_all_words():
    def get_words_from_page(page_object):
        words = page_object.find_all("span", class_="word")
        for i in range(len(words)):
            words[i] = words[i].get_text()
        descriptions = page_object.find("tbody").find_all("div", class_="description")
        for i in range(len(descriptions)):
            descriptions[i] = descriptions[i].get_text().replace("\xa0", " ")
        if len(descriptions) != len(words):
            raise Exception("not every word has exactly one matching description")
        else:
            pairs = []
            for i in range(len(words)):
                pairs.append([words[i], descriptions[i]])
        return(pairs)

    alphabet = ["a", "b", "c", "č", "ć", "d", "dž", "đ", "e",
     "f", "g", "h", "i", "j", "k", "l", "lj", "m", "n", "nj", "o",
      "p", "r", "s", "š", "t", "u", "v", "z", "ž"]
    list_of_words = []

    for letter in alphabet:
        print("letter: " + letter)
        for i in range(200):
            page = requests.get("http://xn--rjenik-k2a.hr/" + "?letter=" + str(letter) + "&page=" + str(i+1))
            soup = BeautifulSoup(page.content, "html.parser")
            current_page_words = get_words_from_page(soup)
            if current_page_words == []:
                break
            else:
                list_of_words += current_page_words
                with open("words.csv", "a", newline="") as f: # TODO: fix adding to the end of the file if it already exists
                    thewriter = csv.writer(f)
                    for word in current_page_words:
                        thewriter.writerow(word)
                print("current page:" + str(i+1))
                time.sleep(1)
    return(list_of_words)
"""
with open(file, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

#print(get_words_from_page(soup))
get_all_words(soup)
"""

get_all_words()
