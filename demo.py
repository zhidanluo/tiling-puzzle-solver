# -*- coding: utf-8 -*-
"""

author: luozhidan

Tiling Puzzle Solver

Project for CS6161 - Algorithms
"""


__author__ = 'Zhidan Luo'


from puzzleSolver import main
import os

# change this path to your own
puzzleDataSetsDirectoryFullPath = "puzzles/"

# whether to allow tiles to be rotated or flipped
rotate = True
flip = True

# if demo == True, only to find first two solutions and to be graphically shown
demo = True

# ignored if demo == True.
# if True, all solutions will be graphically shown
show = False

# this test mode is to test the symmetry of tiles in given conditions
test = False

for fileName in sorted(os.listdir(puzzleDataSetsDirectoryFullPath)):
	if fileName != '.DS_Store':
		solutions = main(puzzleDataSetsDirectoryFullPath, fileName, 
				 rotate = rotate, flip = flip, 
				 demo = demo, show = show, 
				 testMode = test)



# fileName = 'IQ_creator.txt'
# fileName = 'lucky13.txt'
# fileName = 'partial_cross.txt'
# fileName = 'pentominoes3x20.txt'
# fileName = 'pentominoes4x15.txt'
# fileName = 'pentominoes5x12.txt'
# fileName = 'pentominoes6x10.txt'
# fileName = 'pentominoes8x8_corner_missing.txt'
# fileName = 'pentominoes8x8_four_missing_corners.txt'
# fileName = 'pentominoes8x8_four_missing_diagonal.txt'
# fileName = 'pentominoes8x8_four_missing_near_corners.txt'
# fileName = 'pentominoes8x8_four_missing_near_middle.txt'
# fileName = 'pentominoes8x8_four_missing_offset_near_corners.txt'
# fileName = 'pentominoes8x8_four_missing_offset_near_middle.txt'
# fileName = 'pentominoes8x8_middle_missing.txt'
# fileName = 'pentominoes8x8_side_missing.txt'
# fileName = 'pentominoes8x8_side_offset_missing.txt'
# fileName = 'test1.txt'
# fileName = 'test2.txt'
# fileName = 'thirteen_holes.txt'



# solutions = main(puzzleDataSetsDirectoryFullPath, fileName, 
# 				rotate = rotate, flip = flip, 
# 				demo = demo, show = show, 
# 				testMode = test)
