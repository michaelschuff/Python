def solvemaze(x,y,maze):
    directions=[[0,1],[1,0],[0,-1],[-1,0]]
    for d in directions:
        if(x+d[0]>=0 and x+d[0]<=19 and y+d[1]>=0 and y+d[1]<=19):
            if(maze[y+d[1]][x+d[0]]=="L"):
                return(True)
            if(maze[y+d[1]][x+d[0]]=="*"):
                maze[y][x]="X"
                if(solvemaze(x+d[0],y+d[1],maze)):
                    return(True)
    return(False)

