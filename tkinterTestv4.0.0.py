from tkinter import * 

top = Tk()
songList = []

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()
        

def printList():    
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)
L1 = Label(top, text="yourTunes ", bg = "#d4850f")

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "Week 1 Functions", bg = "#d4850f", command = week1)
    B1Main.grid(column = 0, row = 2)
    B2Main = Button(text = "Week 2 Functions", bg = "#d4850f", command = week2)
    B2Main.grid(column = 0, row = 3)
    B3Main = Button(text = "Week 3 Functions", bg = "#d4850f")
    B3Main.grid(column = 0, row = 4) 



def week1():
    def addTrack():
    
        songList.append(E1.get())
        E1.delete(0, END)
    clearWindow() 
    L1 = Label(top, text = "yourTunes")
    L1.grid(column = 0, row = 1 )

    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    B1 = Button (text = " + ", bg = "#d4850f", command = addTrack)
    B1.grid(column = 1, row = 2)

    B2 = Button(text = "Playlist", bg = "#d4850f", command = printList)
    B2.grid(column = 1, row = 1)

    B3 = Button(text = "Write to File", bg = "#4940e6", command = exportList)
    B3.grid(column = 1, row = 3)

    Bclear = Button(text = "Clear", bg = "#4940e6")
    Bclear.grid(column = 2, row = 3)
    print(E1.get())




def week2():
    clearWindow()
    
    L1W2 = Label(top, text = "Dice Roller")
    L1W2.grid = (column = 0, row = 0)
    L2W2 = Label(top, text = "# of Sides")
    L2W2.grid = (column = 1, row = 1)
    L3W2 = Label(top, text = "# of Rolls")
    L3W2.grid = (column = 1, row = 3)
    E1W2 = Entry(top, bd = 5)
    E1W2.grid = (column = 2, row = 1)
    E2W2 = Entry(top, bd = 5)
    E2W2.grid = (column = 2, row = 1)
    B1W2 = Button(text = "Roll 'em'")


if __name__ == "__main__":
    mainMenu()
top.mainloop()