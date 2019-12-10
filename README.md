# <p align="center">Tiling Puzzle Solver</p>
<p align="center">University of Virginia</p>
<p align="center">December 2019</p>  

---  

## 1. Background
This project entails implementing a program that will solve arbitrary tiling puzzles. The purpose of this project is to introduce a rich branch of discrete mathematics and combinatorics that involves tilings, symmetry, counting, solution space searching, branch-and-bound pruning, etc.

## 2. Puzzle Introduction
An interesting set of puzzles consists of pieces corresponding to the twelve "pentominoes" (i.e., all of the 12 non-isomorphic combinations of five connected unit squares).

<div align=center><img width="50%" height="50%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/tiles5*5.jpg"/></div>

The above 12 pentominoes (collectively having a total area of 12*5=60 square units) can be fitted into a 60-square-unit rectangle of dimensions (a) 3x20, (b) 4x15, (c) 5x12, or (d) 6x10:

<div align=center><img width="50%" height="50%" src="https://github.com/Dan-Animenz/tilingPuzzleSolver/blob/master/pictures/pentominoes.jpg"/></div>

