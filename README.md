# <p align="center">Tiling Puzzle Solver</p>
<p align="center">University of Virginia</p>
<p align="center">December 2019</p>  

---  

## 1. Background
This project entails implementing a program that will solve arbitrary tiling puzzles. The purpose of this project is to introduce a rich branch of discrete mathematics and combinatorics that involves tilings, symmetry, counting, solution space searching, branch-and-bound pruning, etc.

## 2. Puzzle Introduction
An interesting set of puzzles consists of pieces corresponding to the twelve "pentominoes" (i.e., all of the 12 non-isomorphic combinations of five connected unit squares).

<div align=center>
  <img width="50%" height="50%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/tiles5*5.jpg"/></div>

The above 12 pentominoes (collectively having a total area of 12*5=60 square units) can be fitted into a 60-square-unit rectangle of dimensions (a) 3x20, (b) 4x15, (c) 5x12, or (d) 6x10:

<div align=center>
  <img width="75%" height="75%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/pentominoes.jpg"/></div>

In our real world, the puzzles might look like these:
<div align="center">
  <img width="40%" height="40%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/real1.jpg">
  <img width="40%" height="40%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/real2.jpg">
</div>

<br/>
The 12 pentominoes can also be fitted into each of the following nine 8x8 boards with 4 squares missing from each, as indicated:

<div align=center>
  <img width="60%" height="60%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/missing.jpg"/></div>
  
  
All known combinations of four holes in an 8x8 board can be tiled with the twelve pentominoes (it is in fact unknown whether there exists any four-holed 8x8 board that is not thus tilable).
  
Yet another 8x8 tiling puzzle is as follows:

<div align=center>
  <img width="70%" height="70%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/tiles8*8.jpg"/></div>

In our real world, the puzzle setting is namde IQ creator and it looks like this:

<div align=center>
  <img width="30%" height="30%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/IQ_creator.jpg"/></div>

The following tiling puzzle is marketed by [www.bitsandpieces.com](http://www.bitsandpieces.com) under the name "Lucky Thirteen":

<div align=center>
  <img width="75%" height="75%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/lucky_13.jpg"/></div>

Interestingly, "Lucky Thirteen" is also a three-dimensional puzzle, with each solid piece having a height of one unit, and all thirteen pieces can be assembled into a three-dimensional 4x4x4 cube. In addition, six of the thirteen pieces can be assembled into a three-dimensional 3x3x3 cube.

<div align="center">
  <img width="40%" height="40%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/real_lucky_13_1.jpg">
  <img width="40%" height="40%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/real_lucky_13_2.jpg">
</div>

The 12 pentominoes can be fitted into the following irregular board with 13 holes in it.

<div align=center>
  <img width="75%" height="75%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/thirteen_holes.jpg"/>
</div>

Sometimes not all the tiles are needed for a solution, as is the case here when using the set of 12 pentominoes to cover a cross-shaped board (only 9 of the 12 pentominoes suffice to cover the board in this example):

<div align=center>
  <img width="75%" height="75%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/partial_cross.jpg"/>
</div>

In cases such as this, your program should print a warning that not all the tiles are used, and proceed to solve the puzzle. This instance is a special case of the "pentominoe triplication" problem, where for each pentominoe, we can use 9 of the other pentominoes to create a three-times-normal-size image of the original pentominoe.

## 3. Modeling
### 3.1. Loading Data
- ASCII input files are read line by line into the program.
- The string are converted into numpy matrix.
- Use connected algorithm to find connected components.
- The largest component is the board and the rest are tiles stord in a tile list.

### 3.2. Brief Description of Algorithm

- The main method of tiling is backtracking algorithm. The backtracking algorithm works by finding the first cell that should not be empty and putting the tiles into it from left to right, top to bottom.

- Each time you place a tile, check its validity: make sure that the tile you place does not go out of bounds or intersect with another tile. Besides, only a vacancy with a multiple of n4 cells can be formed where n equals to the number of cells formed a tile if all the tiles are formed with the same number of cells, otherwise it equals to the minimum cell number that formed the tile from the tile list.

- After the valid location is found, place the tile in and remove the tile from the list of all tiles.

- Whenever found a success tiling mechanism, record the mechanism and go back to its last condition and move on to the next trial until the last tile.

- After finding all the successful results, we should move the rotated and reflected versions of the same solution to get the non-isomorphic solutions.

## 4. Optimization
### 4.1. Tile Rotation
Each tile has a maximum of eight  ipped and rotated states, which are first placed into the tiles list by the rotation algorithm. Next, we need to clear the tiles repeat state in the tile list. This can reduce the number of rotations and flips that needed to be searched and thus improve the speed of the algorithm. For the purposes of this optimization, we check the symmetry of each tile: if the tile is symmetric, we remove half of the duplicate states; if it is asymmetrical, we keep  ipping and rotating it.

### 4.2. Board Rotation
The point of rotating the board is to find the location of invalid cells more quickly. For example, in our fill order we go from left to right, from top to bottom. Therefore, it is more advantageous for a wide board. Rotate the vertical plate 90 degrees when it encounters it, and the result will be even faster.


## 5. Sample Results
![The First Solution of `pentominoes3x20.txt'](https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/sample_solutions/pentominoes3x20_1.png)













