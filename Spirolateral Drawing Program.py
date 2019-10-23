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
        """Defines all GUI frames, widgets, turtle, and constants.
        """

        COLOUR_BG = "pale green"
        PAD_LX = 20
        PAD_LY = 10
        PAD_BX = 3
        PAD_BY = 3
        WIDTH = 10

        self.master = master
        self.frame_menu = Frame(master, bg = COLOUR_BG)
        self.frame_menu.grid(row = 0, column = 0, columnspan = 2,
                             sticky = 'nesw')

        self.label_menu = Label(self.frame_menu, text = "Menu", bg = COLOUR_BG)

        self.button_add = Button(self.frame_menu, text = "Add a spirolateral",
                                 command = self.spiro_add)
        self.button_remove = Button(self.frame_menu, text = "Remove a spiro"
                                    + "lateral", command = self.spiro_remove)
        self.button_draw = Button(self.frame_menu, text = "Draw a spirolateral"
                                  , command = self.spiro_draw)
        self.button_save = Button(self.frame_menu, text = "Save spirolateral "
                                  + "list", command = self.save)
        self.button_load = Button(self.frame_menu, text = "Load spirolateral "
                                  + "list", command = self.load)
        self.button_info = Button(self.frame_menu, text = "Information",
                                  command = self.display_information)

        self.label_menu.grid(row = 0, column = 0, rowspan = 2, padx = PAD_LX)

        self.button_add.grid(row = 0, column = 1, padx = PAD_BX, pady = PAD_BY,
                             sticky = EW)
        self.button_remove.grid(row = 1, column = 1, padx = PAD_BX,
                                pady = PAD_BY, sticky = EW)
        self.button_draw.grid(row = 1, column = 2, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_save.grid(row = 0, column = 2, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_load.grid(row = 0, column = 3, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_info.grid(row = 1, column = 3, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)

        self.frame_secondary = Frame(master)
        self.frame_secondary.grid(row = 1, column = 1, sticky = NW)

        self.label_prompt1 = Label(self.frame_secondary, pady = PAD_LY)
        self.label_prompt2 = Label(self.frame_secondary, pady = PAD_LY)
        self.label_prompt3 = Label(self.frame_secondary, pady = PAD_LY)

        self.label_response1 = Label(self.frame_secondary, padx = PAD_LX)
        self.label_response2 = Label(self.frame_secondary, padx = PAD_LX)
        self.label_response3 = Label(self.frame_secondary, padx = PAD_LX)

        self.button_enter = Button(self.frame_secondary, text = "Enter",
                                   width = WIDTH)
        self.button_yes = Button(self.frame_secondary, text = "Yes",
                                 width = WIDTH, command = root.destroy)
        self.button_draw2 = Button(self.frame_secondary, text = "Draw",
                                   width = WIDTH, command = self.start_draw)
        self.button_stop = Button(self.frame_secondary, text = "Stop",
                                  width = WIDTH, command = self.stop_draw)

        self.entry1 = Entry(self.frame_secondary)
        self.entry2 = Entry(self.frame_secondary)
        self.entry3 = Entry(self.frame_secondary)

        self.frame_spiro = Frame(master)
        self.frame_spiro.grid(row = 1, column = 0, rowspan = 2, sticky = NW)

        self.label_spiro = Label(self.frame_spiro, text = "Spirolaterals:")
        self.label_spiro.grid(row = 0, column = 0, padx = PAD_LX,
                              pady = PAD_LY, sticky = NW)

        self.label_spiros = Label(self.frame_spiro, justify = LEFT)
        self.label_spiros.grid(row = 1, column = 0, padx = PAD_LX,
                               sticky = NW)

        self.frame_draw = Frame(master)

        self.canvas = Canvas(self.frame_draw, width = 500, height = 500)
        self.canvas.grid(row = 0, column = 0)

        self.turtle = turtle.RawTurtle(self.canvas)

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

    def display_information(self):
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
