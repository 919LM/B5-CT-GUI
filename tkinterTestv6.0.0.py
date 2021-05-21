
from tkinter import Tk, font 
from tkinter.ttk import Button, Label, Entry
import random   


uniqueList = []
myList = []
songList = []
myRolls = []
rollTimes = 0
dieType = 0




    

           
class App:
    

    def __init__(self, master: Tk) -> None:
        self.master = master
  
        
        self.defaultFont = font.nametofont("TkDefaultFont")
  
        
        self.defaultFont.configure(family="Magneto",
                                   size=19,
                                   weight=font.BOLD)

        self.btn = Button(self.master, text = "Accept Terms\nand Conditions", command = lambda:[self.mainMenu()])
        self.btn.place(y = 120, x = 40)

        self.lbl = Label(self.master, text = "Kilometer GUI")
        self.lbl.pack()

        self.lbl2 = Label (self.master, text = "Terms and Conditions\n(Click here to accept)")
        self.lbl2.pack()
       

    def mainMenu(self): 
        self.clearWindow() 
        self.LMain = Label(self.master, text = "Block 5 GUI Projects")
        self.LMain.pack()
        self.B1Main = Button(self.master, text = "Week 1 Functions",  command = lambda: [self.week1()])
        self.B1Main.pack()
        self.B2Main = Button(self.master, text = "Week 2 Functions",  command = lambda:[self.week2()])
        self.B2Main.pack()


        
    def week1(self):

            self.clearWindow()
            def addTrack():
                 
            
                songList.append(self.E1.get())
                self.E1.delete(0, 10000)
            
            self.clearWindow() 
            self.L1 = Label(self.master, text = "yourTunes")
            self.L1.pack()

            self.E1 = Entry(self.master)
            self.E1.pack()

            self.B1 = Button (text = " + ", command = lambda: [addTrack()])
            self.B1.pack()

            self. B2 = Button(text = "Playlist", command = lambda:[self.printList()])
            self.B2.pack()

            self.B3 = Button(text = "Write to File", command = lambda: [self.exportList()])
            self.B3.pack()

            self.B4 = Button(text = "Main Menu", command = lambda: [self.mainMenu()])
            self.B4.pack()

            print(self.E1.get())




    def week2(self):
        
            
        def rollDice():
            
            rollTimes = self.E2W2.get()
            dieType = self.E1W2.get()  


                    
            global x     
            
            for x in range(0, int(rollTimes)):
                myRolls.append(random.randint(1, int(dieType)))
                print(myRolls)

        self.L4W2 = Label(self.master, text = "Here are your rolls!")
        self.L4W2.pack()
        self.L5W2 = Label(self.master, text = f"Your roll outputs are: {myRolls}")
        self.L5W2.pack()
        self.B2W2 = Button(self.master, text = "Main Menu", command = lambda: [self.mainMenu()])
        self.B2W2.pack()
        self.clearWindow()
        self.L1W2 = Label(self.master, text = "Dice Roller")
        self.L1W2.pack()
        self.L2W2 = Label(self.master, text = "# of Sides")
        self.L2W2.pack()
        self.L3W2 = Label(self.master, text = "# of Rolls")
        self.L3W2.pack()
        self.E1W2 = Entry(self.master)
        self.E1W2.pack()
        self.E2W2 = Entry(self.master)
        self.E2W2.pack()
        self.B1W2 = Button(self.master, text = "Roll 'em", command = lambda:[rollDice()])
        self.B1W2.pack()
        self.BMain = Button(self.master, text = "Main Menu", command = lambda:[self.mainMenu()])
        self.BMain.pack()


    def printList(self):

            print(songList)
    def exportList(self):
            with open("test.txt", "w") as f:
                for item in songList:
                    f.write("%s\n" % item)
    def clearWindow(self):
            
            for widget in self.master.winfo_children():
                widget.destroy()

    


if __name__ == "__main__":
    root = Tk()
    root.geometry("300x250")
    root.title("Block 5 GUI Projects")
    print(font.names())
    app = App(root)
root.mainloop()
        
