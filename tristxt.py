from tris import Scacchiera,Computer,Player

class GameTxt():
    def __init__(self,s,p1,p2):
        self.s = s
        self.players = [p1, p2]
        self.turno = 0

    def print(self):
        for r in self.s.s:
            print(r)
        print()

    def cambia_turno(self):
        self.turno = 1 - self.turno


    def run(self):
        while True:

            self.print()

            if not self.players[self.turno].cpu:
                ok = False
                while not ok:
                    i,j = input('Inserisci i,j ').split(',')
                    i,j = [int(i),int(j)]
                    #ok = self.s.gioca(i,j,self.players[self.turno].symbol)
                    ok = self.players[self.turno].gioca(i,j)
            else:
                ok = False
                while not ok:
                    ok = self.players[self.turno].gioca()

            if s.tris(self.players[self.turno].symbol):
                print('Vice giocatore ',self.players[self.turno].symbol)
                break
            if not s.cespazio():
                print('Pareggio')
                break

            self.cambia_turno()




if __name__ == '__main__':
    s = Scacchiera()
    g = GameTxt(s,Computer(s,'X'),Player(s,'O'))
    g.run()