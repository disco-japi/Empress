import random

#N-Queens-Puzzle
N = 9 #N >= 4

def checkSet(set):
    check = []
    prev = N+2
    for i in set:
        if abs(prev-i) <= 1 or i > N-1:
            return False
        if i not in check:
            check.append(i)
        else:
            return False
        prev = i
    return True

def printSet(set):
    pos = [None]*N
    n = 0
    for i in set:
        temp = ""
        for j in range(i):
            temp= temp+ "x"
        temp = temp + "o"
        for j in range(N-i-1):
            temp = temp +  "x"
        pos[n] = temp
        n+= 1
    for i in pos:
        print(i)
    print("")
    

def Calc(n, set, fr): # n: y recorrido, fr: first-run, enfoque Bottom-Up recursivo
    if not fr:
        set[n] = 0
    for i in range(0, N):
        if n < N-1 and Calc(n+1, set, fr):
            return True
        fr = False
        if checkSet(set):
            return True
        if(i is not N-1):
            set[n] += 1

#Game-gen
seed = random.randint(0,N ** N)

queens = []

for i in range(N):
    queens.append(seed % N)
    if seed > 0:
        seed = int(seed / N)

if not Calc(0, queens, True):
    Calc(0, queens, False)

#Color-Flooding
def SetGen(set):
    gameset = []
    n = 0
    for i in set:
        gameset.append([])
        for j in range(i):
            gameset[n].append(0)
        gameset[n].append(n+1)
        for j in range(N-i-1):
            gameset[n].append(0)
        n+= 1
    return gameset

gameset = SetGen(queens)

def PaintAdj(set, x, y): # Randomly paints adjacent tile 
    q = set[y][x] # q: queen
    painted = False
    att = 0
    while att < 4 or painted == False:
        dir = random.randint(0,3) # 0: up, 1, right, 2, down, 3, left
        if dir == 0 and y > 0 and set[y-1][x] == 0:
            set[y-1][x] = q
            painted = True
            y-= 1
        elif dir == 1 and x < N-1 and set[y][x+1] == 0:
            set[y][x+1]= q
            painted = True
            x+= 1
        elif dir == 2 and y < N-1 and set[y+1][x] == 0:
            set[y+1][x] = q
            painted = True
            y+=1
        elif dir == 3 and  x > 0 and set[y][x-1] == 0:
            set[y][x-1] = q
            painted = True
            x-= 1
        att += 1
        return (painted, x, y)

def SpreadPaint(set, x, y, q, d, c): # q: queen; d: direction = 0: up, 1, right, 2, down, 3, left; c: counter
    c+= 1
    if set[y][x] == 0:
        set[y][x] = q
    else:
        q = set[y][x]
    if c<=2*N:
        if y > 0 and d != 0:
            SpreadPaint(set, x,y-1, q,2,c)
        if x < N-1 and d != 3:
            SpreadPaint(set, x+1,y, q,1,c)
        if y < N-1 and d != 2:
            SpreadPaint(set, x,y+1, q,0,c)
        if x > 0 and d != 1:
            SpreadPaint(set, x-1,y, q,3,c)
    
def PaintSet(gameset):
    pointers = []
    for i in range(N):
        pointers.append([(queens[i], i)])
    for j in range(N):
        for i in range(N):
            x, y = pointers[i][random.randint(0,len(pointers[i])-1)]
            painted, x, y = PaintAdj(gameset, x, y)
            if painted:
                pointers[i].append((x, y))
    for i in range(N):
        if gameset[i] != 0:
            SpreadPaint(gameset, i, 0, gameset[0][i],2,0)
            break

PaintSet(gameset)

for i in gameset:
    print(i)