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
  
The 12 pentominoes can also be fitted into each of the following nine 8x8 boards with 4 squares missing from each, as indicated:

<div align=center>
  <img width="60%" height="60%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/missing.jpg"/></div>
  
  
All known combinations of four holes in an 8x8 board can be tiled with the twelve pentominoes (it is in fact unknown whether there exists any four-holed 8x8 board that is not thus tilable).
