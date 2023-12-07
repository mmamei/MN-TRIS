# classe scacchiera 2
class Scacchiera():
    def __init__(self):
        self.s = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    def gioca(self,i,j,p):
        if i < 3 and j < 3 and self.s[i][j] == 0:
            self.s[i][j] = p
            return True
        return False
    def cespazio(self):
        for i in range(3):
            for j in range(3):
                if self.s[i][j] == 0:
                    return True
        return False
    def tris(self,p):
        r0 = self.s[0][0] == p and self.s[0][1] == p and self.s[0][2] == p
        r1 = self.s[1][0] == p and self.s[1][1] == p and self.s[1][2] == p
        r2 = self.s[2][0] == p and self.s[2][1] == p and self.s[2][2] == p
        c0 = self.s[0][0] == p and self.s[1][0] == p and self.s[2][0] == p
        c1 = self.s[0][1] == p and self.s[1][1] == p and self.s[2][1] == p
        c2 = self.s[0][2] == p and self.s[1][2] == p and self.s[2][2] == p
        d1 = self.s[0][0] == p and self.s[1][1] == p and self.s[2][2] == p
        d2 = self.s[0][2] == p and self.s[1][1] == p and self.s[2][0] == p
        return r0 or r1 or r2 or c0 or c1 or c2 or d1 or d2


import random

class Computer():
    def __init__(self,s, symbol):
        self.s = s
        self.symbol = symbol
        self.cpu = True

    def gioca(self):
        while True:
            i = random.randint(0,2)
            j = random.randint(0,2)
            if self.s.gioca(i,j,self.symbol):
                return [i,j]

class Player():
    def __init__(self, s, symbol):
        self.s = s
        self.symbol = symbol
        self.cpu = False

    def gioca(self,i,j):
        if self.s.gioca(i,j,self.symbol):
            return [i,j]
        else:
            return False


from guizero import *

class GameGUI():
    def __init__(self,s,p1,p2):
        self.s = s
        self.players = [p1,p2]
        self.app = App('tris', layout='grid')
        self.p = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                self.p[i][j] = PushButton(self.app,text=' ',grid=[i,j],
                                          command=self.gioca,args=[i,j],
                                          enabled=False, width=5)
        self.ris = TextBox(self.app,'gioca',grid=[0,3,3,1],width=20)
        self.turno = 0


    def buttons(self,val):
        for i in range(3):
            for j in range(3):
                self.p[i][j].enabled = val

    def cambia_turno(self):
        self.turno = 1 - self.turno

    def move(self):
        print('move')
        if not self.players[self.turno].cpu:
            self.buttons(True)

        if self.players[self.turno].cpu:
            self.buttons(False)
            i,j = self.players[self.turno].gioca()
            self.p[i][j].text = self.players[self.turno].symbol

            if self.s.tris(self.players[self.turno].symbol):
                self.ris.value = f'VINCE Giocatore {self.players[self.turno].symbol}'
            elif not self.s.cespazio():
                self.ris.value = f'PAREGGIO'
            else:
                self.cambia_turno()
                self.app.after(1000,self.move)

    def gioca(self, i, j):
        r = self.players[self.turno].gioca(i,j)
        if r == False:
            return
        self.p[i][j].text = self.players[self.turno].symbol

        if self.s.tris(self.players[self.turno].symbol):
            self.ris.value = f'VINCE Giocatore {self.players[self.turno].symbol}'
            self.buttons(False)
        elif not self.s.cespazio():
            self.ris.value = f'PAREGGIO'
            self.buttons(False)
        else:
            self.cambia_turno()
            self.move()

    def run(self):
        self.app.after(1,self.move)
        self.app.display()

if __name__ == '__main__':
    s = Scacchiera()
    g = GameGUI(s,Computer(s,'X'),Player(s,'O'))
    g.run()