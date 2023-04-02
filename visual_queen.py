"""Show the Answer in a Visual form"""

import numpy as np

def matrix_render(arr):
    """ Creates a matrix version of chessboard where 1 denotes the queen places and 0 denoted empty box"""
    n = len(arr)
    chess = np.zeros((n, n), dtype=int)
    for row in range(n):
        chess[arr[row]][row]=1
    return chess

def image_render(arr):
    pass

def main():
    arr = [2, 5, 1, 4, 0, 3]
    print(matrix_render(arr))


if __name__=="__main__":
    main()