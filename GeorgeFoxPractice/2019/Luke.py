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
    
import os
path="/Users/eatdacarrot/ComputerScience/Python/GeorgeFoxPractice/2019/"
file=open(os.path.join(path+"Lukeinput.txt"),"r")
lines=file.read().splitlines()
size=int(lines[0])
mazes=int(lines[size+1])
del lines[size+1]
del lines[0]
maze=[]
for x in range(mazes):
    for y in range(size):
        maze.append(list(lines[y]))
    a=lines[x+size].split(" ")
    print(solvemaze(int(a[0]),int(a[1]),maze))
    maze=[]