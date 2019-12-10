# -*- coding: utf-8 -*-
"""

author: luozhidan

Tiling Puzzle Solver

Project for CS6161 - Algorithms
"""

__author__ = 'Zhidan Luo'


# General imports
import numpy as np
import copy
import time


# Local imports
import utils
import helper
import recorder
from rotate import MaxtrixRotator


"""Matrix ratator."""
rot90 = MaxtrixRotator(90)
rot180 = MaxtrixRotator(180)
rot270 = MaxtrixRotator(270)
flipper = MaxtrixRotator()


"""Checker function."""
def overlapCheck(board):
    if np.max(board) < 2:
        return True
    else:
        return False


def holeNumToCheck(tiles):

    tilesCheck = copy.copy(tiles)
    length = []
    for tile in tilesCheck:
        length.append(np.sum(tile))

    if len(set(length)) == 1:
        return length[0], True
    else:
        return min(length), False


def holeCheck(board, ref):
    boardCheck = copy.copy(board)
    boardCheck = np.abs(boardCheck-1)
    _, labels = utils.findConnectedComponents(boardCheck)
    
    length = []
    for i in range(np.max(labels)+1):
        index = np.where(labels==i)[0]
        length.append(len(index))
    
    holeChecker = []
    length[0] = length[0] - ref
    for lenthi in length:
        if holeEqualFlag:
            if lenthi % holeNum != 0:
                holeChecker.append(False)
            else:
                holeChecker.append(True)
        else:
            if lenthi < holeNum:
                holeChecker.append(False)
            else:
                holeChecker.append(True)

    if all(holeChecker):
        return True
    else:
        return False


def boardCheck(board, ref):
    if overlapCheck(board):
        # return True
        if holeCheck(board, ref):
            return True
        else:
            return False
    else:
        return False


def edgeCheck(tile, board, position):
    boardShape = board.shape
    startPoint, stopPoint = helper.getFirstOnePoints(tile, position)
    if (stopPoint[0] < boardShape[0] 
        and stopPoint[1] < boardShape[1] 
        and startPoint[0] >= 0 
        and startPoint[1] >= 0):
        return True
    else:
        return False
 
    
def boardRotateCheck(boardBlank):
    if len(boardBlank[0]) > len(boardBlank):
        return True
    else:
        return False


def squareCheck(board):
    if not board.shape[0] == board.shape[1]:
        return False
    else:
        boardRot_1 = rot90.rotation(board)
        boardRot_4 = flipper.flip(board)
        if (
            len(np.nonzero(boardRot_1 - board)[0]) > 0
            or len(np.nonzero(boardRot_4 - board)[0]) > 0):
            return False
        else:
            return True
        
        
"""Put function."""
def putSingleTile(tile, board, position, ref): 
    flag = False                                              
    old_board = copy.copy(board)
    new_board = helper.tryPutTile(tile, board, position)
    if boardCheck(new_board, ref):
        board = new_board
        flag = True
    else:
        board = old_board
        
    return board, old_board, flag


def putRotTile(tile, board, position, countTile, countRot, tilesC, ref):
    tileRotList = helper.tileRotator(tile)
    tileRotList, n = helper.testRot(tileRotList, rotateFlag, flipFlag)
    
    old_board = copy.copy(board)
    checker = []
    while countRot < n:   
        tile = tileRotList[countRot]
        if edgeCheck(tile, board, position):
            board, old_board, flag = putSingleTile(tile, board, position, ref)
            checker.append(flag)
        else:
            checker.append(False)

        if any(checker): break
        countRot += 1
    
    if any(checker):
        return board, old_board, countTile, countRot, n, tile
    else:
        countTile += 1
        countRot = 0
        return board, old_board, countTile, countRot, n, tile


"""Main solver."""
def solvePuzzle(tiles, boardBlank, startTime):
    successHistory = []
    board, tilesC, history, count, successCount, countTile, countRot = helper._init_(boardBlank, tiles)
    ref = np.sum(boardBlank)
    numOnes = boardBlank.shape[0] * boardBlank.shape[1]
    
    i = 0
    while i < board.shape[0]:
        j = 0
        while j < board.shape[1]:
            position = [i, j]
            if board[i,j] == 0:
                while board[i,j] == 0:
                    if countTile < len(tilesC):
                        tile = tilesC[countTile]
                        board, old_board, countTile, countRot, n, tile = putRotTile(tile, board, position, countTile, countRot, tilesC, ref)
                    else:
                        if not history:
                            if len(successHistory) > 0:
                                return successHistory
                            else:
                                print("No solution!!!")
                                return None
                        board, tile, tilesC, countTile, i, j, countRot, n = recorder.recallHistory(history)
                        position = [i,j]
                history = recorder.record(history, old_board, tile, tilesC, countTile, i, j, countRot, n)
                tilesC.pop(countTile)

                countTile = 0
                countRot = 0
                count += 1
                j += 1
            else:
                j += 1
        i = position[0]
        i += 1
        if np.sum(board) == numOnes:
            board, tile, tilesC, countTile, i, j, countRot, n, successCount, successHistory = recorder.success(board, count, successCount, history, startTime, successHistory)
            if demoFlag:
                if successCount > 1:
                    return successHistory
    return successHistory
    

"""Main function."""
def main(path, fileName, rotate, flip, demo, show, testMode = False):

    global rotateFlag, flipFlag, demoFlag, boardFlag, holeNum, holeEqualFlag, squareFlag
    boardFlag = True
    
    rotateFlag = True if rotate else False
    flipFlag = True if flip else False
    demoFlag = True if demo else False
    
    tiles, boardBlank = utils.loadTileBoard(path, fileName)
    
    squareFlag = squareCheck(boardBlank)
    holeNum, holeEqualFlag = holeNumToCheck(tiles)    
    boardFlag = boardRotateCheck(boardBlank)
    
    if boardFlag:
        boardBlank = rot90.rotation(boardBlank)

    if testMode:
        helper.showRot(tiles, rotateFlag, flipFlag)
        return None
        
        
    startTime = time.time()
    successHistory = solvePuzzle(tiles, boardBlank, startTime)
    endTime = time.time()
    print("\ntotal time used: %.6f sec" % (endTime - startTime))

    solutions = []

    if demoFlag:
        if not successHistory:
            return None
        for history in successHistory:
            boardShow = np.zeros(boardBlank.shape)
            board = helper.getSolution(history, boardShow, boardFlag)
            solutions.append(board)
    else:
        if not successHistory:
            return None
        for history in successHistory:
            boardShow = np.zeros(boardBlank.shape)
            board = helper.getSolution(history, boardShow, boardFlag, show = False)
            solutions.append(board)
    
    if demoFlag or (not fileName.find('test') == -1):
        finalSolutions = solutions
        if (not fileName.find('test') == -1):
            print("number of unique solutions: %d" % len(finalSolutions)) 
        return finalSolutions
    else:
        finalSolutions = helper.uniqueSolution(solutions, len(tiles)+1, squareFlag, 
                                               rotateFlag, flipFlag, show)
        print("check unique solution time: %.4f sec" % (time.time() - endTime))
        print("number of unique solutions: %d" % len(finalSolutions)) 
        return finalSolutions    
    
