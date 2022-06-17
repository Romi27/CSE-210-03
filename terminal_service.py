from word_generator import Word_Generator
class Terminal:
    
    """Class Terminal will receive the word generated on the class Word and show the number of underscores needed to guess the word. Then it will ask for the user for an input.
    It will compare if the input of the user is included in the word generated, then it will print his input inside of the word. If it is wrong it will tell the director that
     it was wrong, and will show the underscores. 
   
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    def __init__(self):
        self._hidden_word = ""
        self._hidden_word_list = []
        self._word = Word_Generator()
        self._guessed_letter = ""
        self._check_guess = True
        self._check_win = False
        self._full_word = ""
    def set_word(self, word):
        self._word = word
        self._create_hidden_word_list()
        self._create_hidden_word()
    def set_guessed_letter(self, guessed_letter):
        self._guessed_letter = guessed_letter
        self._add_guessed_letter()
        word = self._word.get_word()
        if self._full_word == word:
            self._check_win = True
        

    def _add_guessed_letter(self):
        word_list = self._word.get_word_as_list()
        index = -1
        check_letter = ""
        for letter in word_list:
            index += 1
            if self._guessed_letter == letter:
                self._hidden_word_list[index] = self._guessed_letter + " "
                check_letter = self._guessed_letter
        self._create_hidden_word()
        if check_letter == self._guessed_letter:
            self._check_guess = True
        elif check_letter != self._guessed_letter:
            self._check_guess = False
        full_word = ""
        for i in self._hidden_word.split():
            full_word += i
        self._full_word = full_word


    def _create_hidden_word_list (self):
        '''It will get the word created on class Word and change every letter for underscores, creating a new list with underscores.

        Arguments:
        self: An instance of terminal service.
        list: A single  word in a list.
        Returns: a list with underscores.
        '''
        word_list = self._word.get_word_as_list()
        for letter in word_list:
            letter = '_ '
            self._hidden_word_list.append(letter)
    def _create_hidden_word(self):
        hidden_word = ""
        for letter in self._hidden_word_list:
            hidden_word += letter
        self._hidden_word = hidden_word
    def get_guess(self):
        return self._check_guess
    def get_hidden_word(self):
        return self._hidden_word
    def get_hidden_word_list(self):
        return self._hidden_word_list
    def get_condition(self):
        return self._check_win
