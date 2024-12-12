def total(n):
    totalOrtog = 0
    totalElse = 0

    for i in range(1, n + 1):
        condition = False
        for j in range(n):
            if i == 2 ** j:
                totalOrtog += i
                condition = True

        if condition == False: 
            totalElse += 1

    return totalOrtog, totalElse

n = 10
ortog, other = total(n)
print(ortog, other)