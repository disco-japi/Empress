class Queen:
    x = 0
    def __init__(self, x):
        self.x = x

#N-Queens-Puzzle
N = 8 #N >= 4
valid_sets = []


def checkSet(set):
    check = []
    prev = N+2
    for i in set:
        if abs(prev-i.x) <= 1:
            return False
        if i.x not in check:
            check.append(i.x)
        else:
            return False
        prev = i.x
    return True




def printSet(set):
    pos = [None]*len(set)
    n = 0
    for i in set:
        temp = ""
        for j in range(i.x):
            temp= temp+ "x"
        temp = temp + "o"
        for j in range(N-i.x-1):
            temp = temp +  "x"
        pos[n] = temp
        n+= 1
    for i in pos:
        print(i)
    print("")
    

queens = []
for i in range(N):
    queens.append(Queen(0))

def Calc(n, set): # n: y recorrido, enfoque Bottom-Up recursivo
    if n == N:
        return
    set[n].x = 0
    for i in range(0, N):
        Calc(n+1, set)
        if checkSet(set):
            printSet(set)
        if(i is not N-1):
            set[n].x += 1

Calc(0, queens)

#for i in valid_sets:
 #   printSet(i)
    
print(len(valid_sets))