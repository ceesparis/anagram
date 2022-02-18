import csv
from helpers import is_anagram

class Anfind():
    '''
    takes in word, finds anagrams of this word
    '''
    def __init__(self, word):
        self.word = word 
    
    def find_anagrams(self) -> list:
        # create list to store anagrams
        anagrams = []
        # open csv with dutch words
        with open('../data/clean_woorden.csv', 'r') as file:
            csv_reader = csv.reader(file)
            # check for each word if it is an anagram 
            for line in csv_reader:
                dict_word = line[0]
                # if so, add to anagrams
                if is_anagram(self.word, dict_word) and dict_word != self.word: 
                    anagrams.append(dict_word)
        # return list of anagrams
        return anagrams
    

                    
    

    