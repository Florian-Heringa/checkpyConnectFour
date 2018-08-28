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
