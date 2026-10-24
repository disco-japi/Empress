import random

#N-Queens-Puzzle
N = 5 #N >= 4
valid_sets = []


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
    _fr = fr
    if not _fr:
        set[n] = 0
    for i in range(0, N):
        if n < N-1:
            Calc(n+1, set, _fr)
        _fr = False
        if checkSet(set):
            return
        if(i is not N-1):
            set[n] += 1

#Game-gen
seed = random.randint(0,N ** N)

queens = []
for i in range(N):
    queens.append(seed % N)
    if seed > 0:
        seed = int(seed / N)

Calc(0, queens, True)
if not checkSet(queens):
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
for i in gameset:
    print(i)

def PaintAdj(set, x, y): # Randomly paints adjacent tile 
    q = set[y][x] # q: queen
    painted = False
    att = 0
    while att < 4 or painted == False:
        dir = random.randint(0,3) # 0: up, 1, right, 2, down, 3, left
        if dir == 0:
            if y > 0:
                if set[x, y-1] == 0:
                    set[x, y-1] = q
                    painted = True
        elif dir == 1:
            if x < N-1:
                if set[x+1, y] == 0:
                    set[x+1, y] = q
                    painted = True
        elif dir == 2:
            if x < N-1:
                if set[x, y+1] == 0:
                    set[x, y+1] = q
                    painted = True
        elif dir == 3:
            if x > 0:
                if set[x-1, y] == 0:
                    set[x-1, y] = q
                    painted = True
        att += 1
        return painted
    
def PaintSet(gameset):
    _gameset = gameset
    while True:
        for i in range(N):
            pass
        break
    return _gameset

painted_set = PaintSet