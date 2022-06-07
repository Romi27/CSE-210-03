from word_generator import Word_Generator


class Jumper:
    def __init__(self):
        """ Creating the library and list to be printed later. This allows the lines of the library to be adjusted
        by adding the blank text "" later.
        """
       
        self.wrong_letter = 0
        self.jumper_library_1 = "  ___  "
        self.jumper_library_2 = " /___\ "
        self.jumper_library_3 = " \   / "
        self.jumper_library_4 = "  \ /  "
        self.jumper_library_5="0"
        self.jumper_library_5_error="X"
        self.man_list = [
            "  /|\  ",
            "  / \  ",
            "",
            "^^^^^^^"]

    def get_drawing(self):
        """Using the Library and List to print image if guess is correct
        """
        draw = self.jumper_library_1
        draw = self.jumper_library_2
        draw=self.jumper_library_3
        draw = self.jumper_library_4
        draw=self.jumper_library_5
        draw = self.man_list

        if self.wrong_letter== 1:
            draw = self.jumper_library_2
            draw = self.jumper_library_3
            draw = self.jumper_library_4
            draw = self.jumper_library_5
            draw = self.man_list
        if self.wrong_letter == 2:
            draw = self.jumper_library_3
            draw = self.jumper_library_4
            draw = self.jumper_library_5
            draw = self.man_list
        if self.wrong_letter == 3:
            
            draw = self.jumper_library_4
            draw = self.jumper_library_5
            draw = self.man_list
        if self.wrong_letter == 4:
          
            draw = self.jumper_library_5
            draw = self.man_list
        if self.wrong_letter == 5:
         
            draw = self.jumper_library_5_error
            draw = self.man_list
            return draw

    def wrongletter(self):
        if self.wrong_letter not in Word_Generator.get_word:
            self.wrong_letter=self.wrong_letter+1
        return self.wrong_letter
