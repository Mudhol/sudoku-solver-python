import numpy as np
grid=[[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,7,9]]
def canAdd(grid,y,x,n,rows):
    for i in range(rows**2):
        if grid[y][i]==n:
            return False
    for i in range(rows**2):
        if grid[i][x]==n:
            return False
    x0=(x//rows)*rows
    y0=(y//rows)*rows
    for j in range(rows):
        for i in range(rows):
            if grid[j+y0][i+x0]==n:
                return False
    return True
def solve(grid):
    rows=np.matrix(grid).shape[0]
    for y in range(rows):
        for x in range(rows):
            if grid[y][x]==0:
                for n in range(1,10):
                    if canAdd(grid,y,x,n,int(rows**0.5)):
                        grid[y][x]=n
                        solve(grid)
                        grid[y][x]=0
                return
    print(np.matrix(grid))
