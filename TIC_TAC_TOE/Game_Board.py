from tkinter import *
from TicTacToe import *
class Game_Board:
    def __init__(self, a = '', b = ''):
        self.player = 0 # Keeps track of whose turn it is (0 means X, 1 means O)
        self.counter = 0 # Keeps track of the number of moves made
        p1 = a
        p2 = b
        self.logic = TicTacToe(self, p1, p2)
        self.Board = Tk() # Creates a Tkinter window
        self.Board.title("TIC-TAC-TOE")
        self.Board.config(background="black")
        self.Board.geometry("560x430") # Set window size (not too big since some screens are smaller)

        # Creates the grid of 9 buttons
        self.button1=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button1))
        self.button2=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button2))
        self.button3=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button3))
        self.button4=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button4))
        self.button5=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button5))
        self.button6=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button6))
        self.button7=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button7))
        self.button8=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button8))
        self.button9=Button(self.Board,text='',height=8,width=16,bg='white',font=('Courier',10),command=lambda: self.logic.check(self.button9))
        self.button1.grid(row=0, column=0, padx=1, pady=0)
        self.button2.grid(row=0, column=1, padx=1, pady=0)
        self.button3.grid(row=0, column=2, padx=1, pady=0)
        self.button4.grid(row=1, column=0, padx=1, pady=0)
        self.button5.grid(row=1, column=1, padx=1, pady=0)
        self.button6.grid(row=1, column=2, padx=1, pady=0)
        self.button7.grid(row=2, column=0, padx=1, pady=0)
        self.button8.grid(row=2, column=1, padx=1, pady=0)
        self.button9.grid(row=2, column=2, padx=1, pady=0)

        # Creates the Restart button
        self.button10=Button(self.Board, text='Restart', height=5, width=15, bg='white', font=('Courier', 10),command=self.restart)
        self.button10.grid(row=1, column=10, pady=0, padx=5)
    def restart(self):
        confirm_window = Toplevel(self.Board) # Create a popup (Toplevel window) to confirm restart
        confirm_window.title("Confirm Restart")
        confirm_window.geometry("300x150")
        label = Label(confirm_window, text = "Are you sure you want to restart the game?", font = ('Arial', 12))
        label.pack(pady = 10)

        # Function to restart the game (clears buttons and resets variator/finder)
        def confirm_restart():
            # Reset the game board
            self.button1['text'] = ''
            self.button1['bg'] = 'white'
            self.button2['text'] = ''
            self.button2['bg'] = 'white'
            self.button3['text'] = ''
            self.button3['bg'] = 'white'
            self.button4['text'] = ''
            self.button4['bg'] = 'white'
            self.button5['text'] = ''
            self.button5['bg'] = 'white'
            self.button6['text'] = ''
            self.button6['bg'] = 'white'
            self.button7['text'] = ''
            self.button7['bg'] = 'white'
            self.button8['text'] = ''
            self.button8['bg'] = 'white'
            self.button9['text'] = ''
            self.button9['bg'] = 'white'
            self.player = 0
            self.counter = 0
            confirm_window.destroy()  # Close the confirmation window after restart

        def cancel_restart():
            confirm_window.destroy()  # Close the confirmation window to resume the game

        confirm_button = Button(confirm_window, text = "Confirm", command = confirm_restart, width = 10)
        confirm_button.pack(side = LEFT, padx = 20, pady = 20)

        cancel_button = Button(confirm_window, text = "Cancel", command = cancel_restart, width = 10)
        cancel_button.pack(side = RIGHT, padx = 20, pady = 20)
    def Start_Game(self):
        self.Board.mainloop()