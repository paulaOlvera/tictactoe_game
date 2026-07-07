from copy import deepcopy
# Define board
class Board: 
    def __init__(self):
        # Initialize the board in blank
        self.cells = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def display(self):
        # Displays the board
        print("    0    1    2  ")
        # for row in self.cells:
        for i in range(3):
            print(f"{i} {self.cells[i]}")
            

    def place_mark(self,row, col,mark):
        self.cells[row][col]=mark

# class Player:
#     def get_move(self,game):
#         pass
    
# class HumanPlayer(Player):
#     def get_move(self,game):
#         row = int(input())
#         col = int(input())
#         return row, col

# class MinimaxPlayer(Player):
#     def get_move(self,game):
#         return game.best_move(game)

class Game:
    def __init__(self):
        self.board = Board()
        self.player_x='X'
        self.player_o='O'
        self.current_player=self.player_x

    # Minimax functions ####################################
    def clone(self):
        return deepcopy(self)
    
    def minimax(self,maximizing):
        score = self.score()
        if score is not None:
            return score
        
        if maximizing:
            best = -100
            for move in self.get_moves():
                child = self.clone()
                child.set_move(*move)
                child.switch_turns()
                value = child.minimax(False)
                best = max(best,value)
            return best
            
        else:
            best = 100
            for move in self.get_moves():
                child = self.clone()
                child.set_move(*move)
                child.switch_turns()
                value = child.minimax(True)
                best = min(best,value)
            return best
        
    def best_move(self):
        best_score = 100
        best = None
        for move in self.get_moves():
            child = self.clone()
            child.set_move(*move)
            child.switch_turns()
            score = child.minimax(True)
            print(f"move {move} with score {score}")
            if score< best_score:
                best_score = score
                best = move
        return best
    
    #######################################################


    def switch_turns(self):
        if self.current_player == self.player_x:
            self.current_player = self.player_o
            
        else:
            self.current_player = self.player_x
    
    def get_player(self):
        return f"The current player is {self.current_player}"
    
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
        
        self.board.place_mark(row,col,self.current_player)
        return True
            # if self.current_player == self.player_x:
            #     self.board.place_mark(row,col,"X")
            #     return True
            # if self.current_player == self.player_o:
            #     self.board.place_mark(row,col,"O")
            #     return True
        
    def check_winner(self):
        # check rows
        for row in self.board.cells:
            if row[0] != ' ' and row[0] == row[1] == row[2]:
                # print(f"One of the rows where the same")
                # print(f"{self.current_player} wins")
                return row[0]
        # check columns
        for i in range(3):
            if self.board.cells[0][i]!= ' ' and self.board.cells[0][i] == self.board.cells[1][i] == self.board.cells[2][i]:
                # print(f"All elements in column {i} where the same")
                # print(f"{self.current_player} wins")
                return self.board.cells[0][i]
        # check diagonal
        if self.board.cells[0][0]!= ' ' and self.board.cells[0][0] == self.board.cells[1][1] == self.board.cells[2][2]:
            # print("The first diagonal is the same")
            # print(f"{self.current_player} wins")
            return self.board.cells[0][0]
        # check other diagonal
        if self.board.cells[2][0] != ' ' and self.board.cells[2][0] == self.board.cells[1][1] == self.board.cells[0][2]:
            # print("The second diagonal is the same")
            # print(f"{self.current_player} wins")
            return self.board.cells[2][0]
        return None
    def check_draw(self):
        count = 0
        for row in self.board.cells:
            for cell in row:
                if cell != ' ':
                    count+=1
        if count==9:
            return True
        
        return False

    def get_moves(self):
        moves = []
        for i in range(len(self.board.cells)):
            for j in range(len(self.board.cells[0])):
                if self.board.cells[i][j]==' ':
                    moves.append((i,j))
        return moves

    def is_over(self):
        if self.check_winner()!=None or self.check_draw()!=False:
            return True
    
    def score(self):
        winner = self.check_winner()
        if winner=='X':
            return 1
        if winner=='O':
            return -1
        if self.check_draw()==True:
            return 0
        return None
    
if __name__ == "__main__":
    game = Game()
    game.board.display()

    while True: 
        print("***********************************************")
        if game.current_player == 'X':
            row = int(input("Set move row: "))
            col = int(input("Set move column: "))
        else:
            row,col = game.best_move()
        
        game.set_move(row,col)
        game.board.display()
        if game.is_over():
            score = game.score()
            if score==0:
                print("DRAW")
            if score==1:
                print("Player X wins")
            if score==-1:
                print("Player 0 wins")
            # print(game.score())
            break
        game.switch_turns()


