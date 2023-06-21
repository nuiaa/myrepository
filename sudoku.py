import argparse
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

#oyunu tasarlarkenki global değişiklikler: zorluk,yükseklik,genişlik,pixel,renk

BOARDS=[debug,easy,medium,hard]
MARGIN=20 #pixel
SIDE=50 #genişlik
WIDTH=HEIGHT=MARGIN*2+SIDE #yükseklik ve genişlik

class sudoku_error(Exception):
    """
    sudoku hatalari burada
    """
    pass
class sudoku_board(object):
    """
    sudoku tahta sunumu
    """
    
    def __init__(self,board_file): #Yeni bir platform oluşturulduğunda, bu platform .sudoku dosyası olarak oluşturulmalıdır.
        self.board=__create_board(board_file)
        pass
    def __create_board(self,board_file):
       #matrix yap

        board=[]
        #her line iter edilsin
        for line in board:
            line=line.strip()
        if len(line) !=9:
            board=[]
            raise sudoku_error("Sudokudaki her satır 9 karakter olmalıdır.")
        #line oluştur
        board.append([])
        
		#iterate
        for c in line:
		# 9 line yoksa hata fırlat
            if not c.isdigit():
                raise sudoku_error("Sudokuda 0-9 rakamları geçerlidir")
        
        board[-1].append(int(c))
        # 9 line yoksa hata fırlat

        if len(board) !=9:
            raise sudoku_error("Sudokuda 9 satır uzunluğunda olmalıdır")

		
        return board


class SudokuGame(object):
    """
    sudoku oyunu tahtasinin hikayesinin bitip bitmediğini kontrol eder
    """
    def __init__(self,board_file):
        self.board_file=board_file
        self.start_puzzle=sudoku_board(board_file).board
    
    def start(self):
        self.gameover=False
        self.puzzle=[]
        
        for i in xrange(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append(self.start_puzzle[i][j])

    def check_win(self):
        for row in xrange(9):
            if not self.__check_row(row):
                return False
        for column in xrange(9):
            if not self.__check_column(column):
                return False
        for row in xrange(3):
            for column in xrange(3):
                if not self.check_square(row,column):
                    return False
        self.gameover= True
        return True
    def __check_block(self,block):
        return set(block) == set(range(1,10))
    def __check_row(self,row):
        return self.__check_block(self.puzzle[row])
    def __check_column(self,column):
        return self.__check_block([self.puzzle[row][column]for row in xrange(9)])
    def __check_square(self,row,column):
        return self.__check_block([self.puzzle[r][c]
                                   for r in xrange(row*3, (row+1) * 3)
                                   for c in xrange(column*3,(column+1) * 3)
                                   ])
    
class sudokuUI(Frame):
    pass




