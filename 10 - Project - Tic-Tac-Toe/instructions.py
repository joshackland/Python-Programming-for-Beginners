class Player():
    def __init__(self, name):
        self.name = name
        self.wins = 0


class TicTacToe():
    def __init__(self):
        #create player one and player two
        #create the 3x3 grid

    #print out the current state of the board
    def draw(self):
        #e.g.
        #X| |O
        #-----
        # |X| 
        #-----
        #O| |O
    
    #check to see if there is a 3 in a row
    def check_if_winner(self):
        #check vertical

        #check horizontal

        #check diagonal

        #return if winner found
    
    #find the rows which can be played on
    def valid_rows(self):
        #iterate through rows to find any unplayed positions
        
        #return list of valid rows

    #for a given row, find the columns which can be played on
    def valid_columns(self, row):
        #iterate through the columns of a row to find which can be played on
        
        #return list of valid columns

    #function to run to play game
    def play(self):
        self.initialise_game_state()

        #while loop for game
            #each player takes turn place X or O

            valid_rows = self.valid_rows()

            #allow player to enter the row.
            selected_row = input()
            #if not a valid row, have player re-enter row

            valid_columns = self.valid_columns(selected_row)

            #allow player to select column to play on
            #if not a valid column, have player re-enter column

            #once valid position selected, place X or O on grid

            if self.check_if_winner():
                #display who winner is
                #give player +1 to wins
                #end game
            
tictactoe = TicTacToe()

play_again = True

while play_again:
    tictactoe.play()
    #give option to play again or exit