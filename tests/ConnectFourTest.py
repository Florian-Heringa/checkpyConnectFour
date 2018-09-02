import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import ConnectFourSource as CF

############################## Test functions

def fillsBoardTestFunction():
    board = CF.emptyBoard.copy()
    for i in range(CF.BOARDWIDTH * CF.BOARDHEIGHT):
        while True:
            # Give copy of the board so it cannot be edited by the student
            column = lib.getFunction("make_move", _fileName)(board.copy())
            if CF.isValidMove(board, column):
                break

    makeMove(board, CF.PLAYERTILE, column)

    return CF.isBoardFull(CF.emptyBoard)
    
def canWinAGameTestFunction():
    won = 0
    for game in range(100):
        print(game)
        board = CF.emptyBoard.copy()

        while not CF.isBoardFull(board):

            while True:
                move = lib.getFunction("make_move", _fileName)(board.copy())
                if move.lower().startswith('q'):
                    sys.exit()
                if not move.isdigit():
                    continue
                move = int(move) - 1
                if CF.isValidMove(board, move):
                    break
            CF.makeMove(board, PLAYERTILE, move)

            if CF.isWinner(mainBoard, PLAYERTILE):
                winner = winner + 1
                break

            CF.getComputerMove()
            CF.makeMove(mainBoard, CF.COMPUTERTILE, move)
            if CF.isWinner(mainBoard, CF.COMPUTERTILE):
                break

    return won >= 1, won

###################### Tests
@t.test(0)
def containsCorrectFunction(test):

    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "make_move")
    test.description = lambda : "Correct function found in source"
    test.fail = lambda info : "Check if your function has the correct name: make_move"

@t.passed(containsCorrectFunction)
@t.test(10)
def fillsBoard(test):

    test.test = lambda : fillsBoardTestFunction
    test.description = lambda : "Fills board completely when playing alone"
    test.fail = lambda info : "Check if your function completely fills the board when no opponent is present"
    test.timeout = lambda : 30

@t.passed(fillsBoard)
@t.test(20)
def canWinAGame(test):

    test.test = lambda : canWinAGameTestFunction
    test.description = lambda : "Your algorithm can win a game"
    test.fail = lambda info : "Check your algorithm for mistakes"
    test.success = lambda info : "You won {0} games out of 100".format(info)
    test.timeout = lambda : 1
