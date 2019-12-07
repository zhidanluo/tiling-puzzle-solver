import numpy as np
import copy
import matplotlib.pyplot as plt
import rotate


"""Matrix ratator."""
rot90 = rotate.MaxtrixRotator(90)
rot180 = rotate.MaxtrixRotator(180)
rot270 = rotate.MaxtrixRotator(270)
flipper = rotate.MaxtrixRotator()


def _init_(boardBlank, tiles):
    board = copy.copy(boardBlank)
    tilesC = copy.copy(tiles)
    history = []
    count = 0
    successCount = 0
    countTile = 0
    countRot = 0
    return board, tilesC, history, count, successCount, countTile, countRot


def getPoints(tile, position):
    nrow = np.shape(tile)[0]
    ncol = np.shape(tile)[1]
    
    startPoint = position
    stopPoint = [position[0]+nrow-1, position[1]+ncol-1]
    
    return startPoint, stopPoint


def getFirstOnePoints(tile, position):
    nrow = np.shape(tile)[0]
    ncol = np.shape(tile)[1]
    
    allOneIndex = np.nonzero(tile)
    firstOneIndex = [allOneIndex[0][0], allOneIndex[1][0]]

    startPoint = [position[0]-firstOneIndex[0], position[1]-firstOneIndex[1]]
    stopPoint = [position[0]+nrow-1-firstOneIndex[0], position[1]+ncol-1-firstOneIndex[1]]
    
    return startPoint, stopPoint


def tryPutTile(tile, board, position):
    startPoint, stopPoint = getFirstOnePoints(tile, position)
                  
    for i in range(startPoint[0], stopPoint[0]+1):
        for j in range(startPoint[1], stopPoint[1]+1):
            board[i,j] += tile[i-startPoint[0], j-startPoint[1]]
    
    return board


def tileRotator(tile):
    tile90 = rot90.rotation(tile)
    tile180 = rot180.rotation(tile)
    tile270 = rot270.rotation(tile)
    tileF = flipper.flip(tile)
    tileF90 = rot90.rotation(tileF)
    tileF180 = rot180.rotation(tileF)
    tileF270 = rot270.rotation(tileF)
    
    return list([tile, tile90, tile180, tile270,
                 tileF, tileF90, tileF180, tileF270])
   

def printTile(tile):
    tile_str = ''.join(str(x) for x in tile)
    tile_str = tile_str.replace('[', '')
    tile_str = tile_str.replace(']', "\n")
    tile_str = tile_str.replace('0', ' ')
    tile_str = tile_str.replace('1', 'O')
    return tile_str

    
def showRot(tiles, rotateFlag, flipFlag):
    count = 0
    for tile in tiles:
        tileRotList = tileRotator(tile)
        tileRotList, n = testRot(tileRotList, rotateFlag, flipFlag)
#            print(count)
        print("%d kinds:" % n)
        for t in tileRotList:
            print(printTile(t))
        count += 1
        

def testRot(tileRotList, rotateFlag, flipFlag):
    if (not rotateFlag) and not (flipFlag):  # neither flip nor rotate
        return list([tileRotList[0]]), 1
    
    elif flipFlag and (not rotateFlag):  # only flip no rotate
        if (tileRotList[0] == tileRotList[4]).all():
            return list([tileRotList[0]]), 1
        else:
            return list([tileRotList[0], tileRotList[4]]), 2
                
    elif (not flipFlag) and rotateFlag:  # only rotate no flip
        shapeflag = (tileRotList[0].shape == tileRotList[1].shape == tileRotList[2].shape)
        if shapeflag:
            if (tileRotList[0] == tileRotList[1]).all():
                return list([tileRotList[0]]), 1
            elif (tileRotList[0] == tileRotList[2]).all():
                return list([tileRotList[0], tileRotList[1]]), 2
            else:
                return list([tileRotList[0], tileRotList[1], tileRotList[2], tileRotList[3]]), 4
        else:
            if (tileRotList[0] == tileRotList[2]).all():
                return list([tileRotList[0], tileRotList[1]]), 2
            else:
                return list([tileRotList[0], tileRotList[1], tileRotList[2], tileRotList[3]]), 4
    
    else:   # both rotate and flip
        shapeflag = (tileRotList[0].shape == tileRotList[1].shape == tileRotList[2].shape)
        if shapeflag:
            if (tileRotList[0] == tileRotList[1]).all():
                return list([tileRotList[0]]), 1
            elif (tileRotList[0] == tileRotList[2]).all() and (tileRotList[0] == tileRotList[4]).all():
                return list([tileRotList[0], tileRotList[1]]), 2
            elif (tileRotList[0] == tileRotList[2]).all():
                return list([tileRotList[0], tileRotList[1], tileRotList[4], tileRotList[5]]), 4
            elif (
                (tileRotList[0] == tileRotList[4]).all() 
                or (tileRotList[0] == tileRotList[5]).all() 
                or (tileRotList[0] == tileRotList[6]).all() 
                or (tileRotList[0] == tileRotList[7]).all()):
                return list([tileRotList[0], tileRotList[1], tileRotList[2], tileRotList[3]]), 4
            else:
                return tileRotList, 8
        else:
            if (tileRotList[0] == tileRotList[2]).all() and (tileRotList[0] == tileRotList[4]).all():
                return list([tileRotList[0], tileRotList[1]]), 2
            elif (tileRotList[0] == tileRotList[2]).all():
                return list([tileRotList[0], tileRotList[1], tileRotList[4], tileRotList[5]]), 4
            elif (tileRotList[0] == tileRotList[4]).all() or (tileRotList[0] == tileRotList[6]).all():
                return list([tileRotList[0], tileRotList[1], tileRotList[2], tileRotList[3]]), 4
            else:
                return tileRotList, 8

 
def getSolution(history, boardShow, boardFlag, show = True):
    board = boardShow
        
    for subhistory in history:
        position = [subhistory[4], subhistory[5]]
        tile = subhistory[1]
        I, J = np.nonzero(board, )
        for n in range(len(I)):
            board[I[n], J[n]] += 1
        board = tryPutTile(tile, board, position)
        
    if boardFlag:
        board = rot270.rotation(board)
    
    board = board.astype(int)
    
    if show:
        plt.matshow(board)
        plt.show()
    return board

           
def uniqueSolution(solutions, n, squareFlag, rotateFlag, flipFlag, show = False):
    finalS = copy.copy(solutions)    
    count = 0
    
    if (not rotateFlag) and not (flipFlag):  # neither flip nor rotate
        pass
    
    elif flipFlag and (not rotateFlag):  # only flip no rotate
        while count < len(finalS):
            solution = finalS[count]
            solution_all_list = tileRotator(solution)   
#            idx = [len(np.nonzero(s - subsolution)[0]) for subsolution in finalS]
            idx = [np.sum(np.abs(solution_all_list[4] - subsolution)) for subsolution in finalS]
            finalS.pop(idx.index(min(idx)))          
            count += 1

    elif (not flipFlag) and rotateFlag:  # only rotate no flip  
        if not squareFlag:
            while count < len(finalS):
                solution = finalS[count]                
                solution_all_list = tileRotator(solution)
#                idx = [len(np.nonzero(s - subsolution)[0]) for subsolution in finalS]
                idx = [np.sum(np.abs(solution_all_list[2] - subsolution)) for subsolution in finalS]
                finalS.pop(idx.index(min(idx)))          
                count += 1          
        else:
            while count < len(finalS):
                solution = finalS[count]
                
                solution_all_list = tileRotator(solution)
                solution_check_list = solution_all_list[1:4]            
                for s in solution_check_list:
    #                idx = [len(np.nonzero(s - subsolution)[0]) for subsolution in finalS]
                    idx = [np.sum(np.abs(s - subsolution)) for subsolution in finalS]
                    finalS.pop(idx.index(min(idx)))         
                count += 1
    else:   # both rotate and flip
        if not squareFlag:
            while count < len(finalS):
                solution = finalS[count]                
                solution_all_list = tileRotator(solution)
                solution_check_list = []    
                solution_check_list.append(n - solution_all_list[2])
                solution_check_list.append(n - solution_all_list[4])
                solution_check_list.append(solution_all_list[6])        
                for s in solution_check_list:
    #                idx = [len(np.nonzero(s - subsolution)[0]) for subsolution in finalS]
                    idx = [np.sum(np.abs(s - subsolution)) for subsolution in finalS]
                    finalS.pop(idx.index(min(idx)))          
                count += 1          
        else:
            while count < len(finalS):
                solution = finalS[count]                
                solution_all_list = tileRotator(solution)
                solution_check_list = solution_all_list[1:]            
                for s in solution_check_list:
    #                idx = [len(np.nonzero(s - subsolution)[0]) for subsolution in finalS]
                    idx = [np.sum(np.abs(s - subsolution)) for subsolution in finalS]
                    finalS.pop(idx.index(min(idx)))         
                count += 1        

    # whether to show solutions
    if show: 
        for b in finalS:
            plt.matshow(b)
            plt.show()
    
    return finalS