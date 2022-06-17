class Jumper:
    def __init__(self):
        """ Creating the library and list to be printed later. This allows the lines of the library to be adjusted
        by adding the blank text "" later.
        """
        self._parachute = ["  ___  \n", " /___\ \n", " \   / \n", "  \ /  \n"]
        self._jumper = ["   0  \n", "  /|\  \n", "  / \  \n", "^^^^^^^"]
        self._guess_is_right = True
        self._is_alive = True

    def set_guess(self, guess):
        """Using the Library and List to print image if guess is correct
        """
        self._guess_is_right = guess
        self._check_guess()

    def _check_guess(self):
        if len(self._parachute) > 1:
            if self._guess_is_right == False:
                self._parachute.pop(0)
        elif len(self._parachute) == 1:
            if self._guess_is_right == False:
                self._parachute.pop(0)
                self._jumper[0] = "   x  \n"
                self._is_alive = False

    def _draw_parachute(self):
        parachute = ""
        for line in self._parachute:
            parachute += line
        return parachute
    def _draw_jumper(self):
        parachute = self.get_parachute()
        jumper = parachute 
        for line in self._jumper:
            jumper += line
        return jumper 
    def get_parachute(self):
        return self._draw_parachute()
    def get_jumper(self):
        return self._draw_jumper()
    def get_condition(self):
        return self._is_alive
