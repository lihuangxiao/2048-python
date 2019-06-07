import math


class Game2048:

    def __init__(self, board = None):
        if not board:
            board = [
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0
            ]
        self.game_board = board


    def get_board_value(self):
        board_value = 0
        for i in range(16):
            tile_display = self.game_board[i]
            tile_value = math.log2(tile_display) * 2**i if tile_display else 0
            board_value += tile_value
        return board_value

    def get_board_score(self):
        score = 0
        for tile_display in self.game_board:
            score += tile_display
        return score

    def squash_four(self, array_of_four):
        if array_of_four[2] == array_of_four[3]:
            array_of_four[3] *= 2
            array_of_four[2] = 0
        if array_of_four[1] == array_of_four[2]:
            array_of_four[2] *= 2
            array_of_four[1] = 0
        if array_of_four[0] == array_of_four[1]:
            array_of_four[1] *= 2
            array_of_four[0] = 0
        non_zeros = [i for i in array_of_four if i]
        return [0 for _i in range(4 - len(non_zeros))] + non_zeros


    def right(self):
        self.game_board[0:4] = self.squash_four(self.game_board[0:4])
        self.game_board[4:8] = self.squash_four(self.game_board[4:8])
        self.game_board[8:12] = self.squash_four(self.game_board[8:12])
        self.game_board[12:16] = self.squash_four(self.game_board[12:16])


    def rotation_90_right(self):
        new_board = [*self.game_board]
        new_board[3] = self.game_board[0]
        new_board[7] = self.game_board[1]
        new_board[11] = self.game_board[2]
        new_board[15] = self.game_board[3]
        new_board[2] = self.game_board[4]
        new_board[6] = self.game_board[5]
        new_board[10] = self.game_board[6]
        new_board[14] = self.game_board[7]
        new_board[1] = self.game_board[8]
        new_board[5] = self.game_board[9]
        new_board[9] = self.game_board[10]
        new_board[13] = self.game_board[11]
        new_board[0] = self.game_board[12]
        new_board[4] = self.game_board[13]
        new_board[8] = self.game_board[14]
        new_board[12] = self.game_board[15]
        self.game_board = new_board


    def up(self):
        self.rotation_90_right()
        self.right()
        self.rotation_90_right()
        self.rotation_90_right()
        self.rotation_90_right()


    def down(self):
        self.rotation_90_right()
        self.rotation_90_right()
        self.rotation_90_right()
        self.right()
        self.rotation_90_right()


    def left(self):
        self.rotation_90_right()
        self.rotation_90_right()
        self.right()
        self.rotation_90_right()
        self.rotation_90_right()
