from tkinter import *
from History import *
class TicTacToe:
    def __init__(self, game, a, b):     #Stores the player names
        self.game = game
        self.a = a # Player 1
        self.b = b # Player 2
    def check(self, button):
        if button['text'] == '' and self.game.player == 0: # If Player 1 clicks on an empty cell
            button['text'] = ('X')
            button['bg'] = 'red'
            self.game.counter += 1
            self.game.player = 1
            TicTacToe(self.game, self.a, self.b).check_the_winner()
        elif button['text'] == '' and self.game.player == 1: # If Player 2 clicks on empty cell
            button['text'] = 'O'
            button['bg'] = 'blue'
            self.game.counter += 1
            self.game.player = 0
            TicTacToe(self.game, self.a, self.b).check_the_winner()
    # Checks all possible winning combinations
    def check_the_winner(self):
        if self.game.button1['text']=='X' and self.game.button2['text']=='X' and self.game.button3['text']=='X':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.a}'
            t = History(self.a,self.b)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button1['text']=='X' and self.game.button5['text']=='X' and self.game.button9['text']=='X':
            root6=Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.a}'
            t = History(self.a, self.b)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button1['text'] == 'X' and self.game.button4['text'] == 'X' and self.game.button7['text'] == 'X':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.a}'
            t = History(self.a, self.b)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button2['text'] == 'X' and self.game.button5['text'] == 'X' and self.game.button8['text'] == 'X':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.a}'
            t = History(self.a, self.b)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button3['text'] == 'X' and self.game.button6['text'] == 'X' and self.game.button9['text'] == 'X':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.a}'
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            t = History(self.a, self.b)
            t.csv_winloss()
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button3['text'] == 'X' and self.game.button5['text'] == 'X' and self.game.button7['text'] == 'X':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.a}'
            t = History(self.a, self.b)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button4['text'] == 'X' and self.game.button5['text'] == 'X' and self.game.button6['text'] == 'X':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.a}'
            t = History(self.a, self.b)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button7['text'] == 'X' and self.game.button8['text'] == 'X' and self.game.button9['text'] == 'X':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.a}'
            t = History(self.a, self.b)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button1['text'] == 'O' and self.game.button2['text'] == 'O' and self.game.button3['text'] == 'O':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.b}'
            t = History(self.b, self.a)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button1['text'] == 'O' and self.game.button5['text'] == 'O' and self.game.button9['text'] == 'O':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.b}'
            t = History(self.b, self.a)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button1['text'] == 'O' and self.game.button4['text'] == 'O' and self.game.button7['text'] == 'O':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.b}'
            t = History(self.b, self.a)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button2['text'] == 'O' and self.game.button5['text'] == 'O' and self.game.button8['text'] == 'O':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.b}'
            t = History(self.b, self.a)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button3['text'] == 'O' and self.game.button6['text'] == 'O' and self.game.button9['text'] == 'O':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.b}'
            t = History(self.b, self.a)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button3['text'] == 'O' and self.game.button5['text'] == 'O' and self.game.button7['text'] == 'O':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.b}'
            t = History(self.b, self.a)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button4['text'] == 'O' and self.game.button5['text'] == 'O' and self.game.button6['text'] == 'O':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.b}'
            t = History(self.b, self.a)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.button7['text'] == 'O' and self.game.button8['text'] == 'O' and self.game.button9['text'] == 'O':
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            worder = f'CONGRATS {self.b}'
            t = History(self.b, self.a)
            t.csv_winloss()
            root6.config(background="black")
            won = PhotoImage(file="Youhavewon.png")
            k3 = Label(root6, text = worder,font=("Arial",50),bg="black",fg="#cc1e18",image=won,compound="bottom")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()
            return # To prevent _tkinter.TclError
        if self.game.counter == 9 :
            drawforcsv = History(self.a, self.b)
            drawforcsv.csv_draw()
            root6 = Tk()
            root6.title("TIC-TAC-TOE")
            root6.config(background="black")
            worder = 'Try Your Best On The Next Game'
            k4=Label(root6,text="DRAW!",font=("Bold",50),bg="black",fg="#00FF00")
            k4.pack()
            k3 = Label(root6, text=worder,font=("Arial",50),bg="black",fg="#00FF00")
            k3.pack()
            self.game.Board.destroy()
            root6.mainloop()