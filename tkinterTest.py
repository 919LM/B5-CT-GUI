from tkinter import * 

top = Tk()
songList = []

def addTrack():
    
    songList.append(E1.get())
def printList():    
    print(songList)

L1 = Label(top, text="Playlist Generator")
L1.grid(column = 0, row = 1 )

E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

B1 = Button (text = "Add to Playlist", bg = "white", command = addTrack)
B1.grid(column = 1, row = 2)

B2 = Button(text = "Print Playlist", bg = "sky blue", command = printList)
B2.grid(column = 1, row = 1)
print(E1.get())
top.mainloop()