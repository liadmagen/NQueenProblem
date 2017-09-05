#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:07:32 2017

@author: liadmagen

the queen problem actually fills the board with horse-moves

optimization:
    instead of a a sparse matrix - single-dimension array according to the 
    row count, where the array value is the corresponding col number
"""


import numpy as np

def getEmptyBoard(n):
    # Creates a 0-filled chess board nxn
    return np.zeros((n,n))

def markthreats(mat, x,y, markOriginalLocation=False):
    # Given a board mat, and a location x,y -> r,c
    # marks all the area of the queen's threat
    n = mat.shape[0]
    # fill vertical/horizotal
    mat[x,:] = 1
    mat[:,y] = 1
    
    # fill diagonal threat
    k1 = y-x
    k2 = x+y+1-n #(x+1)-(n-y)
    
    print(k2)
    mat = np.logical_or(mat, np.eye(n, k=k1))
    mat = np.logical_or(mat, np.flipud(np.eye(n, k=k2)))

    mat = mat.astype(float)
    
    if (markOriginalLocation):
        mat[x,y] = 2.
    
    return mat

def placeQueen(mat, x,y):
    n = mat.shape[0]
    if(x<0 or y<0 or x>n or y>n):
        return (False, mat)
    else:
        if(mat[x,y] == 1):
            return (False, mat)
        else:
            mat[x,y] = 1.
            return (True, markthreats(mat))

def getHorseMovesFor(n, x, y):
    horseMoves = [(x-2, y-1),(x-2, y+1),(x+2, y-1),(x+2, y+1),(x-1, y-2),(x-1, y+2),(x+1, y-2),(x+1, y+2)]
    hm = [t for t in horseMoves if t[0]>0 and t[1]> 0]
    return hm

def printBoard(mat):
    n = mat.shape[0]
    for i in range(n):
      for j in range(n):
        if mat[j] == i:
          # There is a queen in column j, row i.
          print("Q", end=" ")
        else:
          print("_", end=" ")
      print()
    print()


def fillBoard(n):
    """
    - Fill one location
    - move to next horse-move location from that position
    - repeat until no more options left - then back
    """
    mat = getEmptyBoard(n)
    for i in range(n**2):
        c = i%n
        r = (i-c)/n
        newMat = placeQueen(r,c)
            
    
