N = 5

def main(frow, fcol):
    mat = [[0 for i in range(N)] for j in range(N)]
    mat[frow][fcol] = 1
    if solver(mat,frow,fcol,0) == False:
        print("no valid config")
    else:
        printmat(mat)

def solver(mat,frow,fcol,col):
    if col >= N:
        return True
    if col == fcol:
        return solver(mat,frow,fcol,col+1)
    
    for row in range(N):
        if row == frow:
            continue
        if check(mat,row,col):
            mat[row][col] = 1
            if solver(mat,frow,fcol,col+1) == True:
                return True
            mat[row][col] = 0
    return False

def check(mat,row,col):
    for i in range(N):
        if mat[row][i] == 1 or mat[i][col] == 1:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if mat[i][j] == 1:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,N,1)):
        if mat[i][j] == 1:
            return False
        
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if mat[i][j] == 1:
            return False
    
    for i,j in zip(range(row,N,1),range(col,N,1)):
        if mat[i][j] == 1:
            return False
        
    return True

def printmat(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end='   ')
        print("\n")
            
main(1,3)