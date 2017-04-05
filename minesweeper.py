"""Gavin Franklin
   Final Minesweeper
   4/3/16"""
#This code imports the two librarys I will use
from tkinter import *
from random import *

#This is needed so recursion does not have a limit
import sys
sys.setrecursionlimit(100000) 

#This code uses the tkinter library to create the main gui
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        #This code creates the origional gui
        self.lblrows = Label(self, text = "Rows:")
        self.lblrows.grid(row = 1, column = 0)

        self.lblcol = Label(self, text  = "Col:")
        self.lblcol.grid(row = 1, column = 1)

        self.lblmin = Label(self, text = "Mines:")
        self.lblmin.grid(row = 1, column = 2)

        self.textrow = Entry(self)
        self.textrow.grid(row = 2, column = 0)

        self.textcol = Entry(self)
        self.textcol.grid(row = 2, column = 1)

        self.textmin = Entry(self)
        self.textmin.grid(row = 2, column = 2)

        self.lstlbl = Label(self, text = "", bg = "#fff", anchor = "w", relief = "groove")
        self.lstlbl.grid(row = 4, column = 1)

        self.winper = Label(self, text = "Win %")
        self.winper.grid(row = 5, column = 0)

        self.wintxt = Label(self, text = " ", bg = "#fff", anchor = "w", relief = "groove")
        self.wintxt.grid(row = 5, column = 1)

        #These variables help keep track of the win percentage
        self.winnum = 0

        self.numgame = 0

        self.esbut =Button(self,text = "Easy", command = self.easymod)
        self.esbut.grid(row = 0, column = 0)

        self.medbut = Button(self,text = "Medium", command = self.medmod)
        self.medbut.grid(row = 0, column = 1)

        self.hardbut = Button(self,text = "Hard", command = self.harmod)
        self.hardbut.grid(row = 0, column = 2)

        
        #This button runs the command turncheck which checks to see if it's a repeat game that way it clears the left overs
        self.start = Button(self, text = "Make Game", command = self.cust)
        self.start.grid(row = 3, column = 1)

        self.playerwon = False

    def easymod(self):
        self.type = 1
        self.turncheck()
    def medmod(self):
        self.type = 2
        self.turncheck()
    def harmod(self):
        self.type = 3
        self.turncheck()
    def cust(self):
        self.type = 4
        self.turncheck()

    #This function clears the leftover buttons and labels from the previous game    
    def turncheck(self):

        #This variable keeps track of the number of games that were played
        self.numgame = self.numgame + 1
        if self.numgame > 1:
            #These booleans are set to false so when the board is cleared the program does not run it like an actual game
            self.loseclear = False
            self.winclear = False
            self.playerwon = False
            clearpos = -1
            self.radcle.invoke()
            self.lstlbl["text"] = ""#This reseats the win lose label so it doesn't stick around
            self.rules.destroy()
            for i in range (self.Height):
                for i in range (self.Width):
                    clearpos = clearpos + 1
                    if self.gamebut[clearpos] != ("n"):
                        self.gamebut[clearpos].invoke()
                        self.lstlbl["text"] = ""
                    if self.lblsto[clearpos] != 0:
                        self.lblsto[clearpos].destroy()
        self.loseclear = True                
        self.winclear = True            
        self.gameS()
    
    #This function starts the game by calling the asignmine function and making the gui
    def gameS(self):
        #this creates the radio button that allows you to flag
        self.radVar = IntVar()
        self.radcle = Radiobutton(self, text = "Clear",variable = self.radVar, value = 1)
        self.radcle.grid(row = 4, column = 0)
        
        self.radfla = Radiobutton(self, text = "Flag",variable = self.radVar, value = 2)
        self.radfla.grid(row = 4, column = 2)

        

        #This creates all the variables I will need for my project based on the Button that was clicked
        if self.type == 1:
            self.Height = 9
            self.Width = 9
            self.Mines = 10
        if self.type == 2:
            self.Height = 16
            self.Width = 16
            self.Mines = 40
        if self.type == 3:
            self.Height = 17
            self.Width = 17
            self.Mines = 50
        if self.type == 4:
            self.Height = self.hwCheck(int(self.textrow.get()))
            self.Width = self.hwCheck(int(self.textcol.get()))
            self.Area = self.Height * self.Width
            self.Mines = self.mnCheck(int(self.textmin.get()))
        
        self.Area = self.Height * self.Width    
        self.Squa = self.Area - self.Mines

        #These lists are where all of my data is being stord
        self.flagLoc = [0]* self.Area #If the buttons were flaged
        self.col = ["000000","0000ff","008000","ff0000","000099","a52a2a","ffff00","ffa500","ffcccc"] #Colors
        self.lblsto = [0] * self.Area #labels
        #self.MineA = [0] * (self.Width + 2)
        #self.mineH = [self.MineA] * (self.Height + 2) This code did not work for some reason
        self.mineH = [[0 for i in range (self.Width +2)]for i in range(self.Height +2)] #These double for loops create a two demensional list
        self.gamebut=[0]*self.Area#Buttons
        
        #This label simply explains the ruls of minesweeper
        self.rules = Label(self, text = "Minesweeper \n After clicking a a button a number will appear \n that represents the mines located around that specific square \n if you click on a mine you lose \n clear them all and you win good luck!")
        self.rules.grid(row = 6, rowspan = self.Height, columnspan = 3)
        

        #This is a two deminsional list sorting an apropriate amount of zeros
        
        self.asignMines()
        
        self.spot = -1
        for i in range (self.Height):
            holder = i
            for i in range (self.Width):
                self.spot = self.spot +1
                hold = self.spot
                self.gamebut[hold] = Button(self, text = " ", command = lambda hold=hold, i=i, holder=holder: self.flagcheck(holder, i, hold))
                self.gamebut[hold].grid(row = holder + 7, column = i+3)
   
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
            while keepgoing == True: #The loop is neccecary so the mines are not put in the same location
                up = randint(1,self.Height)
                side = randint(1,self.Width)
                if self.mineH[up][side] != 1:
                    self.mineH[up][side] = 1
                    keepgoing = False

    #This function checks to see if recursion is needed when a specific button is clicked. I had to make a new function because I set the counter = to 0 in the previous function    
    def zerochecker(self, counts, checkspot, climb, crawl):
         if counts == 0 :
            self.lblsto[checkspot] = Label(self, text = "  ", anchor = "w", relief = "ridge")
            self.lblsto[checkspot].grid(row = climb+6, column = crawl+2, sticky = "ns")
            self.recurser(checkspot)

    #This function sets up the recursion by manipulating the list around to check for all four sides 
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
        
    #This invoker function calls the recursion of all the squares surrounding a zero tile. There is a lot of if statements but each one refreces a sepcific list to see if it's ok to clear
    def invoker(self, midbut, arounds):
        if arounds[0] == 0:
            if self.gamebut[midbut - self.Width - 1] != ("n"): #This if statment makes sure the space is not already cleared because you can't clear a button that does not exist
                if self.flagLoc[midbut - self.Width - 1] != ("f"):#This if statment checks to see if the square is flaged because you do not want to clear a flaged square
                    self.gamebut[midbut - self.Width - 1].invoke() #This acually invokes the recursion
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
        if self.playerwon == False:
            flagval = self.radVar.get()
            if flagval == 2:
                self.flager(positioner,position,whichone)
            else:
                self.remover(positioner,position,whichone)
    #This function replaces the "button" with a flaged button
    def flager(self,fplace,fpos,fwhich):
        self.gamebut[fwhich].destroy()
        self.gamebut[fwhich] = Button(self,text = "f", fg = "#{}".format(self.col[3]),  command = lambda fwhich=fwhich, fpos=fpos, fplace=fplace: self.unflag(fplace, fpos, fwhich))
        self.gamebut[fwhich].grid(row = fplace + 7, column = fpos+3)
        self.flagLoc[fwhich] = "f"
    def unflag(self, uplace, upos, uwhich):
        self.gamebut[uwhich].destroy()
        self.gamebut[uwhich] = Button(self,text = " ", command = lambda uwhich=uwhich, upos=upos, uplace=uplace: self.flagcheck(uplace, upos, uwhich))
        self.gamebut[uwhich].grid(row = uplace + 7, column = upos+3) 
        self.flagLoc[uwhich] = 0
    #This function is ran when a square is first clicked and check to see if it's a mine
    def remover(self, down, over, passer):
        self.gamebut[passer].grid_forget()
        self.gamebut[passer] = "n"
        down = down +1 
        over = over + 1
        self.Squa = self.Squa - 1
        if self.mineH[down][over] == 1:
            self.gameover(down, over)
        if self.mineH[down][over] != 1:
            self.remover2(down, over, passer)
    #This functions checks to see if the user won
    def remover2(self, slide, move, r2passer):
        if self.Squa == 0:
            self.gameover2()
            self.remover3(slide,move,r2passer)
        if self.Squa != 0:
            self.remover3(slide, move ,r2passer)
    #This function removes the square from the gui and replaces it with a label
    def remover3(self, climb, crawl, r3passer):

        #This code checks to see if the corosponding gui placemnts are surrounded by mines in the mineH two demensional list
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
        self.zerochecker(counter,r3passer, climb, crawl)

        #This if statments prevents the program from printing the zeros because that could get very anoying
        if counter != 0:
            self.lblsto[r3passer] = Label(self, text = "{}".format(counter), anchor = "w", fg = "#{}".format(self.col[counter]), relief = "ridge")
            self.lblsto[r3passer].grid(row = climb+6, column = crawl+2, sticky = "ns")
            
    #This funcion is ran when the player loses
    def gameover(self, climb, crawl):
        clearpos = -1
        #This boolean is set to False so the program does not say the player won once all the squares are cleared
        self.winclear = False
        if self.loseclear == True:
            self.wintxt["text"] = "{}".format((round((self.winnum/self.numgame),2))*100)
        #These for loops clear the remaining squares and display what was beneath them
        for i in range (self.Height):
            holder = i
            for i in range (self.Width):
                clearpos = clearpos + 1
                if self.gamebut[clearpos] != ("n"):
                    #Also a small example of recursion
                    self.gamebut[clearpos].invoke()
                    self.lstlbl["text"] = "you lose"
                if self.mineH[holder + 1][i + 1] == 1:
                    self.lblsto[clearpos] = Label(self, text = "x", relief = "ridge")
                    self.lblsto[clearpos].grid(row = climb + 6, column = crawl + 2)

    #this function is ran if the player wins!
    def gameover2(self):
        if self.winclear == True: #This is the same boolean from the losing function so this is not ran if the player lost and the board is clearing
            self.lstlbl["text"] = "you win"
            self.playerwon = True
            self.winnum = self.winnum + 1
            self.wintxt["text"] = "{}".format((round((self.winnum/self.numgame),2))*100)
        
def main():
    real = App()
    real.mainloop()

if __name__ == "__main__":
    main()
