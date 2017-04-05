"""Gavin Franklin
   Final Minesweeper
   4/3/16"""
#This code imports the two librarys I will use
from tkinter import *
from random import *
import sys
sys.setrecursionlimit(100000) 

#This code uses the tkinter library to create the main gui
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        #This code creates the origional
        self.lblrows = Label(self, text = "Rows:")
        self.lblrows.grid(row = 0, column = 0)

        self.lblcol = Label(self, text  = "Col:")
        self.lblcol.grid(row = 0, column = 1)

        self.lblmin = Label(self, text = "Mines:")
        self.lblmin.grid(row = 0, column = 2)

        self.textrow = Entry(self)
        self.textrow.grid(row = 1, column = 0)

        self.textcol = Entry(self)
        self.textcol.grid(row = 1, column = 1)

        self.textmin = Entry(self)
        self.textmin.grid(row = 1, column = 2)

        self.lstlbl = Label(self, text = "", bg = "#fff", anchor = "w", relief = "groove")
        self.lstlbl.grid(row = 3, columnspan = 3)

        self.numgame = 0

        self.start = Button(self, text = "Make Game", command = self.turncheck)
        self.start.grid(row = 2, columnspan = 2)
        
    def turncheck(self):
        
        self.numgame = self.numgame + 1
        if self.numgame > 1:
            clearpos = -1
            for i in range (self.Height):
                for i in range (self.Width):
                    clearpos = clearpos + 1
                    if self.gamebut[clearpos] != ("n"):
                        self.gamebut[clearpos].invoke()
                        self.lstlbl["text"] = ""
        self.gameS()
    
    #This function starts the game by calling the asignmine function and making the gui
    def gameS(self):
        #this creates the radio button that allows you to flag
        self.radVar = IntVar()
        self.radcle = Radiobutton(self, text = "Clear",variable = self.radVar, value = 1)
        self.radcle.grid(row = 3, column = 0)
        
        self.radfla = Radiobutton(self, text = "Flag",variable = self.radVar, value = 2)
        self.radfla.grid(row = 3, column = 2)

        #This creates all the variables I will need for my projext
        self.Height = self.hwCheck(int(self.textrow.get()))
        self.Width = self.hwCheck(int(self.textcol.get()))
        self.Area = self.Height * self.Width
        self.Mines = self.mnCheck(int(self.textmin.get()))
        self.Squa = self.Area - self.Mines
        self.flagLoc = [0]* self.Area
        self.col = ["000000","0000ff","008000","ff0000","000099","a52a2a","ffff00","ffa500","ffcccc"]
        

        #This is a two deminsional list sorting an apropriate amount of zeros
        self.mineH = [[0 for i in range (self.Width +2)]for i in range(self.Height +2)]
        self.asignMines()
        self.gamebut=[0]*self.Area
        self.spot = -1
        for i in range (self.Height):
            holder = i
            for i in range (self.Width):
                self.spot = self.spot +1
                hold = self.spot
                self.gamebut[hold] = Button(self, text = " ", command = lambda hold=hold, i=i, holder=holder: self.flagcheck(holder, i, hold))
                self.gamebut[hold].grid(row = holder + 5, column = i+3)
   
    #This code makes the setter functions for the hieght width and mines
    def hwCheck(self, tester):
        if tester <= 0:
            tester = 10
        if tester > 20:
            tester = 10
        return tester

    def mnCheck(self, mtester):
        if mtester > self.Area:
            mtester = 10
        return mtester 
    #This function asigns the mines to a specific location
    def asignMines(self):
        for i in range (self.Mines):
            keepgoing = True
            while keepgoing == True:
                up = randint(1,self.Height)
                side = randint(1,self.Width)
                if self.mineH[up][side] != 1:
                    self.mineH[up][side] = 1
                    keepgoing = False
        
    def zerochecker(self, counts, checkspot):
         if counts == 0 :
            self.recurser(checkspot)

    def recurser(self,midbut):
        around = [0] * 8
        if (midbut - self.Width + 1) <= 0:
            around[0] = 1
            around[1] = 1
            around[2] = 1
        if (midbut + self.Width + 1) > self.Area:
            around[5] = 1
            around[6] = 1
            around[7] = 1
        if (midbut % self.Width) == 0:
            around[0] = 1
            around[3] = 1
            around[5] = 1
        if (midbut % self.Width) == (self.Width -1):
            around[2] = 1
            around[4] = 1
            around[7] = 1
        #print("{}".format(around))    
        self.invoker(midbut, around)
        

    def invoker(self, midbut, arounds):
        if arounds[0] == 0:
            if self.gamebut[midbut - self.Width - 1] != ("n"):
                if self.flagLoc[midbut - self.Width - 1] != ("f"):
                    self.gamebut[midbut - self.Width - 1].invoke()
        if arounds[1] == 0:
            if self.gamebut[midbut - self.Width] != ("n"):
                if self.flagLoc[midbut - self.Width] != ("f"):
                    self.gamebut[midbut - self.Width].invoke()
                                
        if arounds[2] == 0:
            if self.gamebut[midbut - self.Width + 1] != ("n"):
                if self.flagLoc[midbut - self.Width + 1] != ("f"):
                    self.gamebut[midbut - self.Width + 1].invoke()
        if arounds[3] == 0:
            if self.gamebut[midbut - 1] != ("n"):
                if self.flagLoc[midbut - 1] != ("f"):
                    self.gamebut[midbut - 1].invoke()
        if arounds[4] == 0:
            if self.gamebut[midbut + 1] != ("n"):
                if self.flagLoc[midbut + 1] != ("f"):
                    self.gamebut[midbut + 1].invoke()
        if arounds[5] == 0:
            if self.gamebut[midbut + self.Width - 1] != ("n"):
                if self.flagLoc[midbut + self.Width - 1] != ("f"):
                    self.gamebut[midbut + self.Width - 1].invoke()
        if arounds[6] == 0:
            if self.gamebut[midbut + self.Width] != ("n"):
                if self.flagLoc[midbut + self.Width] != ("f"):
                    self.gamebut[midbut + self.Width].invoke()
        if arounds[7] == 0:
            if self.gamebut[midbut + self.Width + 1] != ("n"):
                if self.flagLoc[midbut + self.Width + 1] != ("f"):
                    self.gamebut[midbut + self.Width + 1].invoke()
        
        
    #This function checks to see if the flag radio button is clicked so it will flag it
    def flagcheck(self, positioner, position, whichone):
        flagval = self.radVar.get()
        if flagval == 2:
            self.flager(positioner,position,whichone)
        else:
            self.remover(positioner,position,whichone)
    #This function replaces the "button" with a flaged button
    def flager(self,fplace,fpos,fwhich):
        self.gamebut[fwhich].destroy()
        self.gamebut[fwhich] = Button(self,text = "f", fg = "#{}".format(self.col[3]),  command = lambda fwhich=fwhich, fpos=fpos, fplace=fplace: self.unflag(fplace, fpos, fwhich))
        self.gamebut[fwhich].grid(row = fplace + 5, column = fpos+3)
        self.flagLoc[fwhich] = "f"
    def unflag(self, uplace, upos, uwhich):
        self.gamebut[uwhich].destroy()
        self.gamebut[uwhich] = Button(self,text = " ", command = lambda uwhich=uwhich, upos=upos, uplace=uplace: self.flagcheck(uplace, upos, uwhich))
        self.gamebut[uwhich].grid(row = uplace + 5, column = upos+3) 
        self.flagLoc[uwhich] = 0
    #This function is ran when a square is first clicked and check to see if it's a mine
    def remover(self, down, over, passer):
        self.gamebut[passer].grid_forget()
        self.gamebut[passer] = "n"
        down = down +1 
        over = over + 1
        self.Squa = self.Squa - 1
        if self.mineH[down][over] == 1:
            self.gameover()
        if self.mineH[down][over] != 1:
            self.remover2(down, over, passer)
    #This functions checks to see if the user won
    def remover2(self, slide, move, r2passer):
        if self.Squa == 0:
            self.gameover2()
        if self.Squa != 0:
            self.remover3(slide, move ,r2passer)
    #This function removes the square from the gui and replaces it with a label
    def remover3(self, climb, crawl, r3passer):
        
        counter = 0
        if self.mineH[climb][crawl+1] == 1:
            counter = counter + 1
        if self.mineH[climb-1][crawl+1] == 1:
            counter = counter + 1
        if self.mineH[climb+1][crawl+1] == 1:
            counter = counter + 1
        if self.mineH[climb+1][crawl] == 1:
            counter = counter + 1
        if self.mineH[climb-1][crawl] == 1:
            counter = counter + 1
        if self.mineH[climb-1][crawl-1] == 1:
            counter = counter + 1
        if self.mineH[climb][crawl-1] == 1:
            counter = counter + 1
        if self.mineH[climb+1][crawl-1] == 1:
            counter = counter + 1
        self.zerochecker(counter,r3passer)
        
        self.newlbl = Label(self, text = "{}".format(counter), anchor = "w", fg = "#{}".format(self.col[counter]))
        self.newlbl.grid(row = climb+4, column = crawl+2, sticky = "ns")
    def gameover(self):
        self.lstlbl["text"] = "you lose"
        clearpos = -1
        for i in range (self.Height):
                for i in range (self.Width):
                    clearpos = clearpos + 1
                    if self.gamebut[clearpos] != ("n"):
                        self.gamebut[clearpos].invoke()
    def gameover2(self):
        self.lstlbl["text"] = "you win"
       
        
def main():
    real = App()
    real.mainloop()
main()
