def fiborec(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fiborec(num-1) + fiborec(num-2)

def fibodp(num):
    arr = [0,1]
    for i in range(2,num+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[num]

ar1 = [fiborec(i) for i in range(0,10)]
ar2 = [fibodp(i) for i in range(0,10)]

print(ar1)
print(ar2)