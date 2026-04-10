from tkinter import *
from Game_Board import *
class GUI():
    def __init__(self):
        self.gui = Tk() # Create main window
        # self.gui.geometry('2000x796')
        self.gui.state('zoomed')  # Maximize the window to fill the screen
        self.gui.resizable(False, False)  # Disable window resizing (both horizontally and vertically)
        
        self.Bg = PhotoImage(file = "BackGround2.png")
        self.Gs = PhotoImage(file = "GameStart1.png")
        self.XoXo = PhotoImage(file = "XOXO2.png")
        self.Hist = PhotoImage(file = "History3.png")
        self.Ex = PhotoImage(file = "Exit.png")
        Lb = Label(self.gui, image = self.Bg) # Holds the self.bg image inside the self.gui window
        Lb.place(x = 0, y = 0, relheight = 1, relwidth = 1) # Center positions and stretches it to fill the whole screen
        PlyGm = Button(self.gui, image = self.Gs, background = "#48CCCD", command = lambda: self.Players()) # Start Game button
        PlyGm.place(x = 600, y = 500)
        Pic = Label(self.gui, image = self.XoXo, background = "#E238EC")
        Pic.place(x = 455, y = 20)
        Csv = Button(self.gui, image = self.Hist, bg = "#E238EC", command = lambda: self.checkhistory()) # History button
        Csv.place(x = 970, y = 500)
        Exit = Button(self.gui, image = self.Ex, bg = "#E238EC", command = lambda: self.Exit()) # Exit button
        Exit.place(x = 400, y = 500)
        self.gui.mainloop()
    def Players(self):
        self.gui.destroy() # Closes the main window
        self.PlayInfo=Tk() # Opens the pre-game window
        # self.PlayInfo.geometry('1000x796')
        self.PlayInfo.state('zoomed')  # Maximize the player info window
        self.PlayInfo.resizable(False, False)  # Disable resizing
        BgImg = PhotoImage(file = "BackGround2.png")
        P1 = PhotoImage(file = "Player1.png")
        P2 = PhotoImage(file = "Player2.png")
        Bg = Label(self.PlayInfo,image = BgImg)
        Bg.place(x = 0,y = 0,relheight = 1,relwidth = 1)
        pl1 = Label(self.PlayInfo, image = P1)
        pl2 = Label(self.PlayInfo, image = P2)
        pl1.place(x = 100, y = 100)
        pl2.place(x = 700, y = 100)

        # Input boxes to enter player names
        self.pe1 = Entry(self.PlayInfo,width = 50)
        self.pe2 = Entry(self.PlayInfo,width = 50)
        self.pe1.place(x = 55, y = 250)
        self.pe2.place(x = 655,y = 250)
        Gs=PhotoImage(file="GameStart1.png")
        Gsb=Button(self.PlayInfo, image = Gs, background = "#48CCCD", command = lambda: self.Play())
        Gsb.place(x = 400, y = 400)
        BackImg=PhotoImage(file = "Back.png")
        Back=Button(self.PlayInfo, image = BackImg, bg = "#E238EC", command = lambda: self.Back1())
        Back.place(x = 488, y = 500)
        self.PlayInfo.mainloop()
    def Play(self): # Starts the actual game
        game1 = Game_Board(self.pe1.get(), self.pe2.get()) # Creates a game board
        self.PlayInfo.destroy() # Closes the pre-game window
        game1.Start_Game() # Starts the game
    def Exit(self):
        self.gui.destroy() # Exits the game
    def checkhistory(self):
        Csv = History()
        self.gui.destroy() # closes the main window
        
        self.Hist = Tk()
        # self.Hist.geometry('1000x600')  # Set window size for history display
        self.Hist.state('zoomed')  # Maximize the history window
        self.Hist.resizable(False, False)  # Disable resizing
        self.Hist.title('Game History')
        
        # Add the background image
        bgpic = PhotoImage(file='test.png')
        bglabel = Label(self.Hist, image=bgpic)
        bglabel.place(x=0, y=0, relwidth=1, relheight=1)

        # Add a Back button
        BackImg = PhotoImage(file="Back.png")
        Back = Button(self.Hist, image=BackImg, bg="#48CCCD", command=lambda: self.Back2())
        Back.place(x=950, y=0)

        p = Csv.checkhistory() # Gets all past games' history from the CSV file

        headers = ['Game No', 'Winner', 'Loser', 'Draw', 'Time of Game']
        
        # Places the header columns in the window
        i = 0
        for header in headers:
            header_label = Label(self.Hist, text = header, width = 15, font = ('Arial', 12, 'bold'), bg = '#cccccc', relief = 'solid')
            header_label.grid(row = 0, column = i, padx = 5, pady = 5)
            i += 1

        row = 1  # Start at 1st row for the history rows
        for values in p:
            col = 0  # Resets the column index for each row
            for value in values:
                # Create cells to store data in each of them
                cell = Label(self.Hist, text = value, width =20, font = ('Arial', 10), relief = 'solid')
                cell.grid(row = row, column = col, padx = 5, pady = 5)
                col += 1  # Move to the next column
            row += 1  # Move to the next row

        self.Hist.mainloop()
    def Back2(self):
        self.Hist.destroy() # Closes the history window
        self.__init__() # Re-initializes the main window
    def Back1(self):
        self.PlayInfo.destroy() # Closes the pre-game window
        self.__init__() # Re-initializes the main window