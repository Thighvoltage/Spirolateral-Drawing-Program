from tkinter import *
import turtle
import pickle

class Spirolateral():
    def __init__(self, name, segment, angle):
        """A class has been made for spirolaterals so they can be easily be
        assigned multiple variables for the program to use later.
        """
        self.name = name
        self.segment = segment
        self.angle = angle


class GUI:
    def __init__(self, master):
        print(0)

    def spiro_add(self):
        print(1)

    def spiro_remove(self):
        print(2)

    def spiro_draw(self):
        print(3)

    def start_draw(self):
        print(4)

    def stop_draw(self):
        print(5)

    def save(self):
        print(6)

    def load(self):
        print(7)

    def quit(self):
        print(8)

    def spiro_print(self):
        print(9)

    def clear(self):
        print(10)

    def option_stop(self, num, text):
        print(11)


def check_num(entry, label, response, lower_limit, upper_limit, integer):
    print(12)

# Creates list of spiros for the program to add to
spiros = []
# Creates constant for the program to use. Defining here makes it easy to
# edit. Minimum choice used as constant because no input in the program should
# Require an input less than 1.
MIN_CHOICE = 1

def main():
    """Runs the GUI and assigns it a name
    """
    global root
    root = Tk()
    root.title("Spirolateral Drawing Program")
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    """Runs main() if this program hasn't been imported
    """
    main()
