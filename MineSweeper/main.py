from random import randint

class GameStart():
    def __init__(self, row, col, difficulty):
        self.row = row
        self.col = col
        self.mines = randint(10, 20) if difficulty == 0 else randint(20, 30) if difficulty == 1 else randint(30, 40) if difficulty == 2 else randint(10, 40)
        self.game = ['*' for _ in range(row*col)]
        self.lst = []

    def basic_print(self):
        print("Mines: ", self.mines)
        print(self.lst)
        for i in range(len(self.game)):
            print() if i%self.row==0 else None
            print(self.game[i], end=' ')


    def check(self, x):
        if x not in self.lst:
            return True
        return False

    def position_mines(self):
        i = 0
        while(i<self.mines):
            x = randint(0, self.row*self.col-1)
            if not self.check(x):
                continue
            self.lst.append(x)
            i = i + 1      

    def replace_star_with_mines(self):
        # self.game[45] = 'M'
        # self.game[44] = 'M'
        for i in range(0, len(self.game)):
            if i in self.lst:
                self.game[i] = 'M'

    def test(self):
        for place in self.lst:
            count = 0
            #print("PLace ", place)
            if place < self.row:
                for i in [-1, 1, 10, 11, 9]:
                    try:
                        if self.game[place+i] == '*':
                            count += 1
                    except:
                        pass
                self.game[place] = count

            elif place%self.col== 0:
                for i in [1, 10, -9, -10, 11]:
                    try:

                        if self.game[place+i] == '*':
                            count += 1
                    except:
                        pass
                self.game[place] = count
            
            elif (place % self.col)-9 == 0:
                for i in [-1, 10, 9, -10, -11]:
                    try:
                        if self.game[place+i] == '*':
                            count += 1
                    except:
                        pass
                self.game[place] = count

            else:
                for i in [-1, 1, -10, -11, -9, 10, 11, 9]:
                    try:
                        if self.game[place+i] == '*':
                            count += 1
                    except:
                        pass
                self.game[place] = count

if __name__ == '__main__': 
    # Passing Size of the Game and Difficulty
    # If difficulty 0 then mines range 10-20
    # If difficulty 1 then mines range 20-30
    # If difficulty 2 then mines range 30-40
    game = GameStart(10, 10, 1)
    game.position_mines()
    game.replace_star_with_mines()
    game.test()
    game.basic_print()