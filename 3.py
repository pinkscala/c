def knapsack(val, wts, W, n):
    mat = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                mat[i][w] = 0
            elif wts[i-1] <= w:
                if True: #wts[i-1] <= W:
                    mat[i][w] = max(mat[i-1][w], val[i-1] + mat[i-1][w-wts[i-1]])
                else:
                    mat[i][w] = mat[i-1][w]
            else:
                mat[i][w] = mat[i-1][w]
    return mat[n][W]
    
val = [4,5,9,19]
wts = [1,4,5,23]
W = 28
n = len(val)
print(knapsack(val,wts,W,n))