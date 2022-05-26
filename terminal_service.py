class Terminal:
    
    """Class Terminal will receive the word generated on the class Word and show the number of underscores needed to guess the word. Then it will ask for the user for an input.
    It will compare if the input of the user is included in the word generated, then it will print his input inside of the word. If it is wrong it will tell the director that
     it was wrong, and will show the underscores. 
   
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    def get_word (self, random_list):
        '''It will get the word created on class Word and change every letter for underscores, creating a new list with underscores.
        
        Arguments: 
        self: An instance of terminal service.
        list: A single  word in a list.

        Returns: a list with underscores.
        '''
        num_letters = len(random_list)
        editable_list =[]
        for letter in random_list:
            letter = '_ '
            editable_list.append(letter)
        print(letter,end='')

    def read_guess(self, guess):
        """Gets the text input from the terminal.  
        Args: 
            self (TerminalService): An instance of TerminalService.
            guess (string): A string of one letter. 

        Returns:
            string: The user's input as text.
        """
        return input(guess)

    def compare_lists(self,editable_list, random_list, guess):
        """Compares if the user's guess is included in the random_list (random word generated). 
        If it is included it will print the new underscored word with the user's guess.
        If not, it will tell the director that it was a wrong guess. 
        

        Args: 
            self (TerminalService): An instance of TerminalService.
            guess (string): The user's input. 
            random_list (list with the random word): generated in the class Word
            editable_list (list with underscores ) : Hiding the letters of the random list.
                    Returns:
            editable_list (list with underscores and user's  positive guess)
        """
                 

        for i in range(len(random_list)):
            if random_list[i] == guess:
                editable_list[i] = guess
        print (*editable_list)
        return editable_list
            
        
    