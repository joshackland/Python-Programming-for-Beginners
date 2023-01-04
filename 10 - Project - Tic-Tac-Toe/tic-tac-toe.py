class Player():
    def __init__(self, name):
        self.name = name
        self.wins = 0

class TicTacToe():

    def __init__(self):
        self.ROWS = 3
        self.COLUMNS = 3
        self.EMPTY_CELL = " "
        self.NAUGHT = "O"
        self.CROSS = "X"


        self.player_one = Player(input("Enter player one's name: "))
        self.player_two = Player(input("Enter player two's name: "))
        self.total_games = -1

    def draw(self):
        draw_rows = []
        for row in self.board:
            draw_rows.append('|'.join(row))
        print('\n'+'\n------\n'.join(draw_rows)+'\n')

    def initialise_game_state(self):
        self.board = [[self.EMPTY_CELL for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
        self.current_turn = 0
        self.total_games += 1

    def display_score(self):
        print(f"\nTotal Games: {self.total_games}\n{self.player_one.name}: {self.player_one.wins}\n{self.player_two.name}: {self.player_two.wins}\nDraws: {self.total_games - self.player_one.wins - self.player_two.wins}\n")

    def check_if_winner(self):
        results = {
            "winner_found": False,
            "player": None
        }

        for row in self.board:
            row_value = row[0]
            if row_value != self.EMPTY_CELL:
                results["winner_found"] = True
                for column in row:
                    if column != row_value:
                        results["winner_found"] = False
                        break

                if results["winner_found"]:
                    results["player"] = self.player_crosses if row_value == self.CROSS else self.player_naughts
                    return results

        for column in range(self.COLUMNS):
            column_value = self.board[0][column]
            if column_value != self.EMPTY_CELL:
                results["winner_found"] = True
                for row in self.board:
                    if column_value != row[column]:
                        results["winner_found"] = False
                        break

                if results["winner_found"]:
                    results["player"] = self.player_crosses if column_value == self.CROSS else self.player_naughts
                    return results

        row_num = 0
        column_num = 0
        top_left_bottom_right_diagonal_value = self.board[row_num][column_num]

        if top_left_bottom_right_diagonal_value != self.EMPTY_CELL:
            results["winner_found"] = True
            while row_num < self.ROWS and column_num < self.COLUMNS:
                if self.board[row_num][column_num] != top_left_bottom_right_diagonal_value:
                    results["winner_found"] = False
                    break

                row_num += 1
                column_num += 1
            
            if results["winner_found"]:
                results["player"] = self.player_crosses if column_value == self.CROSS else self.player_naughts
                return results

        row_num = self.ROWS - 1
        column_num = 0
        bottom_left_top_right_diagonal_value = self.board[row_num][column_num]

        if bottom_left_top_right_diagonal_value != self.EMPTY_CELL:
            results["winner_found"] = True
            while row_num >= 0 and column_num < self.COLUMNS:
                if self.board[row_num][column_num] != bottom_left_top_right_diagonal_value:
                    results["winner_found"] = False
                    break

                row_num -= 1
                column_num += 1
            
            if results["winner_found"]:
                results["player"] = self.player_crosses if column_value == self.CROSS else self.player_naughts
                return results
        
        return results

    def valid_rows(self):
        rows = []

        for row_num, row in enumerate(self.board):
            for column in row:
                if column == self.EMPTY_CELL:
                    rows.append(row_num)
                    break

        return rows
    
    def valid_columns(self, row):
        columns = []

        for column_num, column in enumerate(self.board[row]):
            if column == self.EMPTY_CELL:
                columns.append(column_num)
        
        return columns


    def play(self):
        self.initialise_game_state()
        self.display_score()

        if self.total_games % 2 == 0:
            self.player_naughts = self.player_one
            self.player_crosses = self.player_two
        else:
            self.player_naughts = self.player_two
            self.player_crosses = self.player_one


        while self.current_turn < 9:
            current_player = self.player_naughts if self.current_turn % 2 == 0 else self.player_crosses
            self.draw()
            print(f"It is {current_player.name}'s turn!")
            valid_rows = self.valid_rows()

            selected_row = -1
            row_input = input(f"Select a row - {valid_rows}: ")

            while selected_row not in valid_rows:
                try:
                    selected_row = int(row_input)
                    if selected_row not in valid_rows:
                        row_input = input(f"'{selected_row}' is not a valid row. Please enter a valid row {valid_rows}: ")
                except:         
                    row_input = input(f"'{selected_row}' is not a valid row. Please enter a valid row {valid_rows}: ")

            valid_columns = self.valid_columns(selected_row)
            selected_column = -1
            column_input = input(f"Select a column - {valid_columns}: ")

            while selected_column not in valid_columns:
                try:
                    selected_column = int(column_input)
                    if selected_column not in valid_columns:
                        column_input = input(f"'{selected_column}' is not a valid row. Please enter a valid row: {valid_columns}")
                except:         
                    column_input = input(f"'{selected_column}' is not a valid row. Please enter a valid row: {valid_columns}")   

            self.board[selected_row][selected_column] = self.NAUGHT if self.current_turn % 2 == 0 else self.CROSS

            winner_check = self.check_if_winner()

            if winner_check["winner_found"]:
                self.draw()
                winner_check['player'].wins += 1
                print(f"{winner_check['player'].name} is the winner!!!")
                break

            self.current_turn += 1

        if self.current_turn == 9:
            self.draw()
            print("The game has ended in a draw!")


        return input("Do you want to play again? (y/Y)") in ['y','Y']



tictactoe = TicTacToe()

play_again = True

while play_again:
    play_again = tictactoe.play()
    
