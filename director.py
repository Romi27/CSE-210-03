from terminal_service import Terminal
from word_generator import Word_Generator
from Jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        Word Generator (Word Generator): The game's Word generator.
        is_playing (boolean): Whether or not to keep playing.
        jumper (Seeker): The game's jumper.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word_Generator()
        self._jumper = Jumper()
        self._terminal = Terminal()
        self._letter_guess = ""
        self._guess_is_right = True
        self._is_playing = True
        self._message = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal.set_word(self._word)
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            print()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """guess the letter from A to Z 
        Args:
            self (Director): An instance of Director.
        """
        self._letter_guess = input("Guess a letter [A-Z]: ")

    def _do_updates(self):
        ""
        """Keeps watch on where the seeker is moving.
        Args:
            self (Director): An instance of Director.
        """
        self._terminal.set_guessed_letter(self._letter_guess)
        self._guess_is_right = self._terminal.get_guess()
        self._jumper.set_guess(self._guess_is_right)
        if self._jumper.get_condition() == False:
            self._is_playing = False
            self._message = "Game over"
        elif self._terminal.get_condition() == True:
            self._is_playing = False
            self._message = "You found the word!"

    def _do_outputs(self):
        """Provides a hint for the jumper to use.
        Args:
            self (Director): An instance of Director.
        """
        if self._is_playing == True:
            print(self._jumper.get_jumper())
            print(self._terminal.get_hidden_word())
        elif self._is_playing == False:
            print(self._jumper.get_jumper())
            print(self._message)
            print("The word was " + self._word.get_word())

