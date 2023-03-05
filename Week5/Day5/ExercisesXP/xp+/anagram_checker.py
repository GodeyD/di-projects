import re
import numpy as np

class AnagramChecker():
    not_english = ''
    def __init__(self) -> None:
        'should load the word list file (text file) into a variable, so that it can be searched later on in the code'
        with open("sowpods.txt") as f:
            words = f.readlines()
        self.new_words = [x[:-1] for x in words]
        
        

    def is_valid_word(word):
        valid_words = re.compile(r'(?<!\S)[A-Za-z]+(?!\S)')
        if valid_words.match(f'{word}'): 
            return True
        else:
            return False
        

    def get_anagrams(self, word):
        word_letters = []
        txt_word_letters = []
        anagrams_list = []
        
        for _ in word:
            word_letters.append(_.lower())
        word_letters.sort()   

        for w in self.new_words:  
            txt_word_letters.clear()          
            for _ in w:                
                txt_word_letters.append(_.lower())
            txt_word_letters.sort()
            if txt_word_letters == word_letters:
                anagrams_list.append(w)
        try:        
            anagrams_list.remove(word.upper())
            self.not_english = ''
        except:            
            ValueError()
            self.not_english = 'not'           
        return anagrams_list

def is_anagram(word1, word2):
    'that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.'
    word_a = []
    word_b = []

    for l in word1.lower():
        word_a.append(l)
    for l in word2.lower():
        word_b.append(l)

    if word_a != word_b:
        word_b.sort()
        word_a.sort()
        if word_a == word_b:
            return True
        else:
            return False
    else:
        return False


    