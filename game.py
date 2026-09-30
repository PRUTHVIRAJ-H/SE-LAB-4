from board import Board


class Minesweeper:
    def __init__(self):
        print("Minesweeper")
        self.n = int(input("Please enter n (used for n*n grid) :"))
        print("Please select mode :")
        print("E : Easy(n*n grid and n mines)")
        print("M : Medium(n*n grid and (n*n)/3 mines)")
        print("H : Hard(n*n grid and (n*n)/2 mines)")
        self.mode = ""
        while(self.mode not in ("E","M","H")):
            self.mode = input("Please enter your choice:")
        
        self.mode_n = {"E":self.n,"M":(self.n*self.n)//3,"H":(self.n*self.n)//2}
        self.board = Board(self.n,self.n,self.mode_n[self.mode])

    def display(self, reveal_mines=False):
        b = self.board
        print("\n   " + " ".join(str(c + 1) for c in range(b.cols)))
        for r in range(b.rows):
            cells = []
            for c in range(b.cols):
                pos = (r, c)
                if reveal_mines and pos in b.mines:
                    ch = "*"
                elif pos in b.flags:
                    ch = "F"
                elif pos not in b.revealed:
                    ch = "#"
                elif pos in b.mines:
                    ch = "*"
                else:
                    ch = str(b.adjacent_mines(r, c))
                cells.append(ch)
            print(f"{r + 1:2} " + " ".join(cells))

    def run(self):
        print("Minesweeper")
        print('Your Mode:'+self.mode+" Your Grid Size:"+str(self.n*self.n)+" Mines: "+str(self.mode_n[self.mode]))
        
        while True:
            self.display()
            raw = input("> ").strip().lower()
            if raw == "q":
                return
            parts = raw.split()
            if len(parts) != 3 or parts[0] not in {"r", "f"}:
                print("Use r row col or f row col.")
                continue
            try:
                r, c = int(parts[1]) - 1, int(parts[2]) - 1
            except ValueError:
                print("Coordinates must be numbers.")
                continue

            if not self.board.in_bounds(r, c):
                print("Outside the board.")
                continue

            if parts[0] == "f":
                self.board.toggle_flag((r, c))
                continue

            if self.board.reveal((r, c)):
                self.display(reveal_mines=True)
                print("BOOM! You hit a mine.")
                return

            if self.board.won():
                self.display()
                print("You cleared the board!")
                return
