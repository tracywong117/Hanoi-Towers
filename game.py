# Hanoi Tower Game

import argparse

parser = argparse.ArgumentParser(description='Hanoi Tower Game')
parser.add_argument('--num_disk', type=int, default=3, help='Number of disks in the game')

args = parser.parse_args()
num_disks = args.num_disk

class HanoiTower:
    def __init__(self, num_disks=3):
        self.towers = [[], [], []]
        self.selected_disk = None
        self.selected_disk_tower = None
        self.moves = 0
        self.num_disks = num_disks

    def reset(self):
        self.towers = [[], [], []]
        self.selected_disk = None
        self.selected_disk_tower = None
        self.moves = 0

        for i in range(self.num_disks, 0, -1):
            self.towers[0].append(i)
        
    def select_disk(self, tower):
        if len(self.towers[tower]) > 0:
            self.selected_disk = self.towers[tower][-1]
            self.selected_disk_tower = tower

    def move_disk(self, tower):
        if self.selected_disk is not None:
            if len(self.towers[tower]) == 0 or self.selected_disk < self.towers[tower][-1]:
                self.towers[self.selected_disk_tower].pop()
                self.towers[tower].append(self.selected_disk)
                self.moves += 1
            self.selected_disk = None
            self.selected_disk_tower = None

    def is_game_over(self):
        return len(self.towers[0]) == 0 and len(self.towers[1]) == 0
    
    def get_top_disk(self, tower):
        if len(self.towers[tower]) > 0:
            return self.towers[tower][-1]
        else:
            return None
    
    def draw(self):
        tower_height = self.num_disks

        for level in range(tower_height, 0, -1):
            for tower in self.towers:
                if len(tower) >= level:
                    print(" "*(self.num_disks-tower[level - 1]) + "*" * (tower[level - 1]*2-1) + " "*(self.num_disks-tower[level - 1]), end=" | ")
                else:
                    print(" "*(self.num_disks*2-1), end=" | ")
            print()
                
        spacing = " "*(self.num_disks-1)
        print(spacing+"0"+"   "+spacing*2+"1"+spacing*2+"   "+"2")

    def user_move(self):
        select_disk = int(input("Select disk: "))
        move_disk = int(input("Move disk: "))
        self.select_disk(select_disk)
        self.move_disk(move_disk)

    def play(self):
        self.reset()
        while not self.is_game_over():
            self.draw()
            self.user_move()
            if self.is_game_over():
                self.draw()
                print("You win!")
                print("Moves:", self.moves)
                break
    
game = HanoiTower(num_disks=num_disks) # 3 disks in the game
game.play()

