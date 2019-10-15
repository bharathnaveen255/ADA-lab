sol = [[0 for i in range(4)] for j in range(4)]

def solve_maze(maze,r,c):
            row = len(maze)
            col = len(maze[0])
            if r == row or c == col:
                        return False
            if (r,c) == (row-1,col-1):
                        sol[r][c] = 1
                        return True
            if maze[r][c] == 0:
                        return False
            if solve_maze(maze,r+1,c) or solve_maze(maze,r,c+1):
                        sol[r][c] = 1
                        return True
            return False

maze = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
solve_maze(maze,0,0)
print(sol)

            
            
            
                        
            
            
                        
