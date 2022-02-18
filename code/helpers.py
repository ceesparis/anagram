def is_anagram(searchword: str, otherword: str) -> bool:
    '''
    takes in two words
    checks if words are anagrams
    '''
    # if the sorted letters of two words are equivalent, they are anagrams
    if sorted(searchword) == sorted(otherword):
        return True
    else:
        return False 

def show_results(anagrams: list) -> None:
    if not anagrams:
        print('\nno anagrams were found\n')
    elif len(anagrams) == 1:
        print(f'\nthe following anagram was found:\n\n{anagrams[0]}\n')
    else:
        print('\nthe following anagrams were found:\n')
        for anagram in anagrams: 
            print (anagram)
        print('\n')

