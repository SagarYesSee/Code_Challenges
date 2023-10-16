def getRow(rowIndex):
    if rowIndex < 0:
        return []
    res = [1]
    for i in range(1, rowIndex + 1):
        next_row = [0] * (len(res) + 1)
        for j in range(len(res)):
            next_row[j] += res[j]
            next_row[j+1] += res[j]
        res = next_row
    return res


rowIndex = int(input('Enter Row Index :- '))
print(getRow(rowIndex))