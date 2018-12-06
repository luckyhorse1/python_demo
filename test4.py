def maxSequence(li):
    if len(li) <= 0:
        print("n is <= 0")
        return
    if len(li) == 1:
        print("val: %d" % li[0])
        return li[0]
    for item in li:
        print("item:%d" % item)
    print("---------------------------")
    half = len(li) // 2
    left = li[:half]
    right = li[half:]
    leftV = maxSequence(left)
    rightV = maxSequence(right)

    borderV = maxBorder(li)
    print("left: %d, right: %d, mid: %d" % (leftV, rightV, borderV))
    print("---------------------------")
    return max((leftV, rightV, borderV))


def maxBorder(li):
    half = len(li) // 2
    maxLeft, maxRight, thisSum = 0, 0, 0
    for item in li[half-1::-1]:
        thisSum += item
        if thisSum > maxLeft:
            maxLeft = thisSum

    thisSum = 0
    for item in li[half:]:
        thisSum += item
        if thisSum > maxRight:
            maxRight = thisSum
    print("mid:%d" % (maxLeft + maxRight))
    return maxLeft + maxRight


def process(li):
    thisSum, maxSum = 0, 0
    for item in li:
        thisSum += item
        if thisSum > maxSum:
            maxSum = thisSum
        elif thisSum < 0:
            thisSum = 0
    return maxSum


a = [4, -3, 5, -2, -1, 2, 6, -2]
b = [-1, 3, -2, 4, -6, 1, 6, -1]

print(maxSequence(b))
print(process(b))
