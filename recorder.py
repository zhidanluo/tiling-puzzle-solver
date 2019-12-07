import prettytable as pt
import copy
import time
import helper


"""History stuff."""
def hisInfo(history):
    tb = pt.PrettyTable()
    tb.field_names = ["id", "i", "j", "tile", "countRot", "nRot"]
    countTable = 0
    for subhistory in history:
        tb.add_row([countTable, subhistory[4], subhistory[5], 
                    helper.printTile(subhistory[1]), subhistory[6], subhistory[7]])
        countTable += 1
    print(tb)


def hisPlainInfo(history):
    oldHistory = history[0]
    countTile = oldHistory[3]
    print("countTile: %d" % countTile)


def record(history, old_board, tile, tilesC, countTile, i, j, countRot, n):
    history.append([old_board, tile, copy.copy(tilesC), countTile, i, j, countRot, n])
    return history


def recall(history):
    lastHistory = history[-1]
    board = lastHistory[0]
    tile = lastHistory[1]
    tilesC = lastHistory[2]
    countTile = lastHistory[3]
    i = lastHistory[4]
    j = lastHistory[5]
    countRot = lastHistory[6]
    n = lastHistory[7]
    history.pop(-1)
    
    return board, tile, tilesC, countTile, i, j, countRot, n


def recallHistory(history):
    board, tile, tilesC, countTile, i, j, countRot, n = recall(history)
    
    countRot += 1
    if countRot > n - 1:
        countTile += 1
        countRot = 0

    return board, tile, tilesC, countTile, i, j, countRot, n


def success(board, count, successCount, history, startTime, successHistory):
    historyRec = copy.copy(history)
    successHistory.append(historyRec)
    successCount += 1
    # print("count: %d" % count)
    if successCount < 3:
        print("success number: %d" % successCount)
        print("time used: %.6f sec\n" % (time.time() - startTime))
        hisInfo(history)
    elif successCount < 6:
        print("success number: %d" % successCount)
        print("time used: %.6f sec\n" % (time.time() - startTime))              
        # hisPlainInfo(history)
    elif successCount == 7:
        print("still calculating...\nplease wait...")
    else:
        pass
    board, tile, tilesC, countTile, i, j, countRot, n = recallHistory(history)
    # input("Press Enter to continue...")
    return board, tile, tilesC, countTile, i, j, countRot, n, successCount, successHistory