import random
class Word_Generator:
    def __init__(self):
        self._words = ["dog", "cat", "bunny", "moon", "sun", "flower", "perfume", "white", "colors", "black", "sweater", "shirt", "skirt", "shoe", "red", "butterfly", "chocolate", "movie", "character"]
        self._word_location = random.randint(0, len(self._words) - 1)
        self._word = ""
    def _generate_word(self):#private method that chooses a random word from a txt file.
        self._word = self._words[self._word_location]
    def get_word(self):#public method that calls the private method _generate_word() and returns the word.
        self._generate_word()
        return self._word
    def _word_as_list(self):#Private method that converts the random word string into a list of letters.
        word_as_list = []
        word = self.get_word()
        for letter in word:
            word_as_list.append(letter)
        return word_as_list
    def get_word_as_list(self):#Public method that calls the private method _word_as_list() and returns the random wod as a list.
        return self._word_as_list() 
        
