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
        self._word_generator = Word_Generator()
        self._is_playing = True
        self._Jumper = Jumper()
        self._terminal_service = Terminal()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """guess the letter from A to Z 
        Args:
            self (Director): An instance of Director.
        """
        
        guess_letter = self._terminal_service.compare_lists("\nGuess a letter [A-Z: ]")
        self._.word_generator.get_word(guess_letter)

    def _do_updates(self):
        ""
        """Keeps watch on where the seeker is moving.
        Args:
            self (Director): An instance of Director.
        """
        self._jumper.get_word_as_list(self._Word_Generator)

    def _do_outputs(self):
        """Provides a hint for the jumper to use.
        Args:
            self (Director): An instance of Director.
        """
        play = self._Jumper.falling_man()
        self._terminal_service.compare_lists(play)

            
