"""
Minesweeper problem

Read in stars and dots for mines and non-mines
Output mines and adjacent count
"""

import file_reader as fr
import file_writer as fw

class Problem2:

    def __init__(self, game_board):
        self.game_board = game_board
        self.rows = len(self.game_board)
        self.cols = len(self.game_board[0])-1
        self.top_pad = [0 for i in range(self.cols)]
        self.bottom_pad = [0 for i in range(self.cols)]
        self.game_space = [[] for i in range(self.rows)]
        self.output_data = [[] for i in range(self.rows)]
        self.return_string = ""

    #calculate adjacent count
    def surrouding_update(self, list_location, row, col):
        list_location[row-1][col-1] += 1
        list_location[row][col-1] += 1
        list_location[row+1][col-1] += 1
        list_location[row-1][col] += 1
        list_location[row+1][col] += 1
        list_location[row-1][col+1] += 1
        list_location[row][col+1] += 1
        list_location[row+1][col+1] += 1

    def process_gameboard(self, input_game):

        #convert strings to ints, use 88 as the sentinal for *
        for index, row in enumerate(input_game):
            for char in row:
                if char == "*":
                    self.game_space[index].append(88)
                elif char == ".":
                    self.game_space[index].append(0)
                else:
                    None
        
        #add padding for calculation
        self.game_space.insert(0,self.top_pad)
        self.game_space.append(self.bottom_pad)
        
        for k in range(len(self.game_space)):
            self.game_space[k].insert(0,0)
            self.game_space[k].insert(self.cols+2,0)
        
        #process the adjacent values
        for index, num_row in enumerate(self.game_space):
            for index2, num_val in enumerate(num_row):
                if num_val == 88:
                    self.surrouding_update(self.game_space, index, index2)

        #remove pads
        del self.game_space[0]
        del self.game_space[-1]
        for index, row in enumerate(self.game_space):
            del row[0]
            del row[-1]

        #loop through game space again to process into a string for file writing
        for index, num_row in enumerate(self.game_space):
            for index2, num_val in enumerate(num_row):
                if num_val == 88:
                    self.output_data[index].append("*")
                elif num_val == 0:
                    self.output_data[index].append("0")
                else:
                    self.output_data[index].append(str(num_val))
        
        for num_row in self.output_data:
            self.return_string += " ".join(num_row)
            self.return_string += "\n"
        
        return self.return_string

def execute_main():
    input_file = fr.FileReader("inputFile.txt")
    game_input = input_file.file_read_all_str_list()
    
    exe_problem2 = Problem2(game_input)
    answer = exe_problem2.process_gameboard(game_input)
    print(answer)
    output_file = fw.FileWriter("PyProblem2-Output.txt")
    output_file._file_write_all_str(answer)

if __name__ == "__main__":
    execute_main()