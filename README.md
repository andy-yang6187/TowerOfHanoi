# TowerOfHanoi
Python ASCII visualization of Tower of Hanoi Algorithm

This program serves as a test for the recursive algorithm to solve Tower of Hanoi. 

Users can insert any number of rings, and the algorithm will solve the game. 

## Tower of Hanoi

Tower of Hanoi is a game where you have three pegs, and you have a bunch of distinct rings, each of different radii, that can be put on a peg. The starting position is as shown in the image below, with all of the rings in order based on radius, starting on peg A.

![tower of hanoi example](https://github.com/andy-yang6187/TowerOfHanoi/blob/main/images/towerofhanoi.PNG)

The goal of the game is to move the rings into the same configuration, except on peg C by moving the rings one by one according to the following rules:

* You can only move one ring each time you make a move.
* Smaller radius rings can never be below larger radius rings.
* When you move a ring, you can only take the ring at the top of the peg and drop it to the top of another peg.

This game is traditionally done with three rings, but as you might guess from the diagram, the problem generalizes to n rings.

The problem is optimally sovled with 2^^n -1

## How to run

Simply execute the tower_of_hanoi.py file 

