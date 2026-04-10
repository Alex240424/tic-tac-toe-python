import csv
import time

# Handles the saving and retrieving of game history
class History:
    def __init__(self, a = '', b = ''):     #Stores the player names
        self.a = a # Player 1
        self.b = b # Player 2
    
    def csv_maker(self):
        f = open('history.csv', 'w', newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Game no.', 'Winner', 'Loser', 'Draw', 'Time']) # Writes the header row
        f.close()
    def csv_winloss(self):
        n = open('history.csv', 'r' , newline = '')
        csv_reader = csv.reader(n)
        l = len(list(csv_reader)) # Gets the number of rows already present in the CSV file
        n.close()
        f = open('history.csv', 'a', newline = '')
        local = time.localtime()
        full_time = time.strftime("%B %d %Y %H:%M:%S", local) # Formats the time into storable string
        csv_writer = csv.writer(f)
        csv_writer.writerow([l, self.a, self.b, 'NA', full_time]) # l is used for game number
        f.close()
    def csv_draw(self):
        n = open('history.csv', 'r', newline = '')
        csv_reader = csv.reader(n)
        l = len(list(csv_reader))
        n.close()
        f = open('history.csv', 'a', newline = '')
        local = time.localtime()
        full_time = time.strftime("%B %d %Y %H:%M:%S", local)
        csv_writer = csv.writer(f)
        new_l=[l, 'NA', 'NA', f'{self.a}, {self.b}', full_time]
        csv_writer.writerow(new_l)
        f.close()
    def checkhistory(self):
        f = open('history.csv', 'r', newline = '')
        csv_reader = csv.reader(f)
        next(csv_reader) # Skips the header row
        return list(csv_reader)