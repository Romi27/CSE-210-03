class Jumper:
    def __init__(self):
        """ Creating the library and list to be printed later. This allows the lines of the library to be adjusted
        by adding the blank text "" later.
        """
        #self.guess = "Y"
        self.wrong_letter = 0
        self.jumper_library = {
        "1": ["  ___  "],
        "2": [" /___\ "],
        "3": [" \   / "],
        "4": ["  \ /  "]}
        self.man_list = [
        "  /|\  ",
        "  / \  ",
        "",
        "^^^^^^^"]
    def _falling_man(self):
        """Using the Library and List to print image if guess is correct
        """
        while self.guess.capitalize() == True:
            a = self.jumper_library["1"]
            b = self.jumper_library["2"]
            c = self.jumper_library["3"]
            d = self.jumper_library["4"]
            print (a[0])
            print (b[0])
            print (c[0])
            print (d[0])
            print("   0   ")
            for line in self.man_list:
                print(line)
                print()
            """Adjusting the image for each missed guess"""
        if not self.guess.capitalize() == True:
            self.wrong_letter += 1
            z = str(self.wrong_letter)
            wrong_guess = self.jumper_library[z]
            w = wrong_guess[0]
            w = ""
            empty_line = [w]
            self.jumper_library[z] = empty_line
            a = self.jumper_library["1"]
            b = self.jumper_library["2"]
            c = self.jumper_library["3"]
            d = self.jumper_library["4"]
            if self.attempt != 5:
                print (a[0])
                print (b[0])
                print (c[0])
                print (d[0])
                print("   0   ")
                for line in self.man_list:
                    print(line)
                    print()
            else:
                print (a[0])
                print (b[0])
                print (c[0])
                print (d[0])
                print("   X   ")
                for line in self.man_list:
                    print(line)
                    print()
                self.IsPlaying = False