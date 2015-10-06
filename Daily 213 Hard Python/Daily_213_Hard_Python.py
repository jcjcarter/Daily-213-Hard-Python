def maxSubstring(s):
    n = len(s)

    A, pA = [0] * n, [0] * n
    
    A[0] = 1 if s[0] == 'a' else -1

    pA[0] = 0

    for i in range(1,n):
        curr = 1 if s[i] == 'a' else -1
        extend = A[i - 1] + curr

        if curr > extend:
            A[i], pA[i] = curr, i
        else:
            A[i], pA[i] = curr, i


    B, pB = [0] * n, [0] * n
    B[0] = 1 if s[0] == 'b' else -1
    pB[0] = 0
    for i in range(1,n):
        curr = 1 if s[i] == 'b' else -1
        extend = B[i - 1] + curr
        if curr > extend:
            B[i], pB[i] = curr, i
        else:
            B[i], pB[i] = extend, pB[i - 1]

    maxIndex, maxSub, maxParent = -1, -1, -1
    for i in range(n):
        if A[i] > maxSub:
            maxIndex, maxSub, maxParent = i, A[i], pA[i]

        if B[i] > maxSub:
            maxIndex, maxSub, maxParent = i, B[i], pB[i]

    return maxIndex, maxSub, maxParent


def maxDiscrepancy(s):
    maxDisc = 1
    n = len(s)
    k = 1
    maxX, maxK, maxIndex, maxParent = -1, -1, -1, -1

    while maxDisc < (n - 1) // k + 1:
        for x in range(k):
            index, candidate, parent = maxSubstring(s[x::k])
            if candidate > maxDisc:
                maxX, maxK, maxIndex, maxDisc, maxParent \
                    = x, k, index, candidate, parent
        k += 1

    return maxDisc, maxParent * maxK + maxX, (maxIndex + 1)*maxK, maxK

# Read the input.
with open("input.txt", "r") as f:
    rows = f.read().split("\n")

for row in rows:
    print("{:<3} s[{}:{}:{}]".format(*maxDiscrepancy(row)))