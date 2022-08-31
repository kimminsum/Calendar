from tkinter import *
from tkcalendar import Calendar
import datetime

class Window:
    def __init__(self):
        ### Crawling today date ###
        today = datetime.date.today()
        self.date = {"year":today.year, 
                    "month":today.month, 
                    "day":today.day}
        self.main() # __main__

    def main(self):
        self.root = Tk()
        self.root.geometry("300x200") # Window size [width, height]
        ### Add calendar object ###
        cal = Calendar(self.root, selectmode = 'day',
                    year = self.date["year"],
                    month = self.date["month"],
                    day = self.date["day"])
        cal.pack(pady = 20)

        self.root.mainloop() # Excute root

if __name__ == "__main__": 
    window = Window()