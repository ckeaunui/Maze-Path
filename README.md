# Maze-Path

This project is designed to find a path through any maze which starts at the top and ends at the bottom. To enter a maze, edit the Maze.txt file with the following rules:

1. The maze must be of dimensions m:int x n:int and consist of 1's and 0's.  1 represents a path tile and 0 represents a wall
2. The maze must have one start tile in the top row and one exit tile in the bottom row. 
3. Each rows element must be separated with a single comma

ex.

0,0,0,1,0,0,0  
0,0,0,1,1,1,0  
0,0,0,0,0,1,0  
      .  
      .  
      .  
0,1,1,1,1,1,0  
0,1,0,0,0,1,0  
0,0,0,0,0,1,0  
