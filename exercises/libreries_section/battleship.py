class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, board, start_row, start_col, direction):
        if start_row > 10 and start_row < 0:
            print(f"The ship does not fit in the row at the start position: {start_row}") 
            return False
        if start_col > 10 and start_col < 0:
            print(f"The ship does not fit in the column at the start position: {start_col}") 
        possible_postions = []
        for i in range(self.size):
            if direction == 'v':
                item = board[start_row + i][start_col]
                print("🤖",item)
                if item == '':
                    possible_postions.append([start_row + i, start_col])
                else: 
                    return False
            if direction == 'h':
                item = board[start_row][start_col + i]
                if item == '':
                    possible_postions.append([start_row, start_col + i])
                else: 
                    return False
        self.position = possible_postions
        for i in range(len(possible_postions)):
            board[possible_postions[i][0]][possible_postions[i][1]] = self.name[0]
        return True
    
    def hit(self):
        self.hits += 1
        if self.hits == self.size:
            return True
        else:
            return False
        
class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destroyer",2)

class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine",3)

class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship",4)


class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.board = [['' for _ in range(10)] for _ in range(10)]
            # [
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',]
            # ]
        self.ships = []
        self.hits = [['' for _ in range(10)] for _ in range(10)]
            # [
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',],
            #     ['','','','','','','','','','',]
            # ]

    def place_ships(self):
        ships = [Destroyer(), Submarine(), Battleship()]
        count = len(ships)
        print("You'll need to enter the position for your 3 ships: ")
        print("-----------------------------------------------------")
        while count > 0:
            if count == 1:
                print("---Destroyer---")
            if count == 2:
                print("---Submarine---")
            if count == 3:
                print("---Battleship---")
            start_row = int(input("--> Start row:"))
            start_col = int(input("--> Start column:"))
            direction = input("--> Directions (V or H): ").lower()
            wassuccessful = ships[count - 1].place_ship(self.board, start_row - 1, start_col - 1, direction)
            if wassuccessful:
                count -= 1
                self.ships.append(ships)
                print(f"---{self.user_name} ships---")
                for row in self.board:
                    print(" ".join(row))
                print()
                if count == 0:
                    print(f"{self.user_name}, all your ships are ready.")
            else:
                print("This position is not valid, please try again.")
    
    def print_board(self, board):
        for row in board:
            print(" ".join(row))
        print()

    def attack(self, opponent):
        while True:
            print(f"{self.user_name}, slect a position to attack.")
            row = int(input("Row: "))
            col = int(input("Column: "))
            if 0 <= row < 10 and 0 <= col < 10:
                if opponent.board[row][col] == '':
                    print("Water")
                    self.hits[row][col] = 'W'
                    opponent.board[row][col] = 'W'
                    break
                elif opponent.board[row][col] != 'W':
                    print("Direct hit")
                    self.hits[row][col] = 'X'
                    for ship in opponent.ships:
                        if (row, col) in ship.positions:
                            if ship.hit():
                                print(f"Ship was sunk, {ship.name}.")
                            break
                    opponent.board[row][col] = 'X'
                    break
                else:
                    print("You already has attacked this postition")
            else:
                print("Position is not valid. Try again.")

    def all_ships_sunk(self):
        return all(ship.hits == ship.size for ship in self.ships)

class BattleshipGame:
    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def play(self):
        print("Welcome to Naval Battleship")
        print("Player 1, enter your ships.")
        self.player1.place_ships()
        print("Player 2, enter your ships.")
        self.player2.place_ships()
        
        current_player = self.player1
        opponent = self.player2

        while True:
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print(f"{current_player.user_name} has win the game")
                break
            current_player, opponent = opponent, current_player

game = BattleshipGame()
game.play()