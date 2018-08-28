import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import ConnectFourSource as CF

BOARDWIDTH = 7
BOARDHEIGHT = 6

PLAYERTILE = 'X'
COMPUTERTILE = 'O'

emptyBoard = [[' ' for y in range(BOARDWIDTH)] for x in range(BOARDHEIGHT)]
filledBoard = [[PLAYERTILE for y in range(BOARDWIDTH)] for x in range(BOARDHEIGHT)]

###################### Tests
@t.test(0)
def containsCorrectFunction(test):

    def test_method():
        return assertlib.fileContainsFunctionDefinitions(_fileName, "make_move")

    test.test = lambda : test_method
    test.description = lambda : "Correct function found in source"
    test.fail = lambda info : "Check if your function has the correct name: make_move"

@t.passed(containsCorrectFunction)
@t.test(10)
def fillsBoard(test):

    def test_method():
        board = emptyBoard.copy()
        for i in range(BOARDWIDTH * BOARDHEIGHT):
            while True:
                # Give copy of the board so it cannot be edited by the student
                column = lib.getFunction("make_move", _fileName)(board.copy())
                if CF.isValidMove(board, column):
                    break

        CF.makeMove(board, PLAYERTILE, column)

        return CF.isBoardFull(board)

    test.test = lambda : test_method
    test.description = lambda : "Fills board completely when playing alone"
    test.fail = lambda info : "Check if your function completely fills the board when no opponent is present"
    test.timeout = lambda : 30

@t.passed(fillsBoard)
@t.test(20)
def canWinAGame(test):

    # num_games_won = 0

    # def test_method():
    #     won = 0
    #     for _ in range(100):
    #         board = emptyBoard.copy()

    #         while not CF.isBoardFull(board):

    #             while True:
    #                 move = lib.getFunction("make_move", _fileName)(board.copy())
    #                 if move.lower().startswith('q'):
    #                     sys.exit()
    #                 if not move.isdigit():
    #                     continue
    #                 move = int(move) - 1
    #                 if CF.isValidMove(board, move):
    #                     break
    #             CF.makeMove(board, PLAYERTILE, move)

    #             if CF.isWinner(mainBoard, PLAYERTILE):
    #                 winner = winner + 1
    #                 break

    #             CF.getComputerMove()
    #             CF.makeMove(mainBoard, COMPUTERTILE, move)
    #             if CF.isWinner(mainBoard, COMPUTERTILE):
    #                 break

    #     return won > 1, 100

    # def testTest():
    #     return False, 0

    test.test = lambda : False
    test.description = lambda : "Your algorithm can win a game"
    test.fail = lambda info : "Check your algorithm for mistakes"
    test.success = lambda info : "You won {0} games out of 100".format(0)
    test.timeout = lambda : 60
