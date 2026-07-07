
# Define board
class Board: 
    def __init__(self):
        # Initialize the board in blank
        self.cells = [['','',''],['','',''],['','','']]

    def display(self):
        # Displays the board
        for row in self.cells:
            print(row)

    def place_mark(self,row, col,mark):
        self.cells[row][col]=mark

class Game:
    def __init__(self,name1,name2):
        self.board = Board()
        self.player_x=name1
        self.player_o=name2
        self.current_player=self.player_x

    def switch_turns(self):
        if self.current_player == self.player_x:
            self.current_player = self.player_o
            
        else:
            self.current_player = self.player_x
    
    def get_player(self):
        print(self.current_player)
    
    def set_move(self,row,col):
        # check move before setting it
        if row not in range(3):
            print("Row out of range")
            return False
        if col not in range(3):
            print("Column out of range")
            return False
        if self.board.cells[row][col]=="X" or self.board.cells[row][col]=="O":
            print(f"There is already an element in row {row} and column {col}")
            return False
        else:
            if self.current_player == self.player_x:
                self.board.place_mark(row,col,"X")
            if self.current_player == self.player_o:
                self.board.place_mark(row,col,"O")
        return True
    def check_winner(self):
        # check rows
        for row in self.board.cells:
            if row[0] != '' and row[0] == row[1] == row[2]:
                print(f"One of the rows where the same")
                print(f"{game1.current_player} wins")
                return True
        # check columns
        for i in range(3):
            if self.board.cells[0][i]!= '' and self.board.cells[0][i] == self.board.cells[1][i] == self.board.cells[2][i]:
                print(f"All elements in column {i} where the same")
                print(f"{game1.current_player} wins")
                return True
        # check diagonal
        if self.board.cells[0][0]!= '' and self.board.cells[0][0] == self.board.cells[1][1] == self.board.cells[2][2]:
            print("The first diagonal is the same")
            print(f"{game1.current_player} wins")
            return True
        # check other diagonal
        if self.board.cells[2][0] != '' and self.board.cells[2][0] == self.board.cells[1][1] == self.board.cells[0][2]:
            print("The second diagonal is the same")
            print(f"{game1.current_player} wins")
            return True
        count = 0
        for row in self.board.cells:
            for cell in row:
                if cell != '':
                    count+=1
        if count==9:
            print(f"Player {self.player_x} and player {self.player_o} draw")
            return True
        print("No winner still")
        return False

    def get_moves(self):
        moves = []
        pass
if __name__ == "__main__":
    game1 = Game("Paula","Anthony")
    while True: 
        print("***********************************************")
        game1.get_player()
        a = int(input("Set move row: "))
        b= int(input("Set move column: "))
        while game1.set_move(a,b) == False:
            print("You cannot do that moves try again")
            a = int(input("Set move row: "))
            b= int(input("Set move column: "))
        game1.board.display()
        if game1.check_winner()==True:
            break
        game1.switch_turns()


