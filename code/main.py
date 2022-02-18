from anagram_finder import Anfind
from helpers import show_results

if __name__ == "__main__":

    # prompt user for a word
    keyword = input("what is the dutch word you want to find anagrams of?'\nenter word here: ")
    # clean user input
    keyword = keyword.lower().strip()
    # make class object of word 
    word_ana = Anfind(keyword)
    # use class object method to find anagrams
    anagrams = word_ana.find_anagrams()
    # show results 
    show_results(anagrams)