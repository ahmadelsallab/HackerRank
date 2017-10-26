# Write a function that takes a binary search tree and an offset k, and returns the kth smallest node in the tree.

#          15
#    12          18
# 10   14      16    22

# k  out
# 1  10
# 2  12
# 3  14
# 4  15

class node:
    def __init__(self):
        self.val = 0
        self.left = node()
        self.right = node()

def findMin(rootNode, minVal, lastKMin):
    if node == None:
        return node.val
    else:
        leftMin = findMin(rootNode.left, lastKMin)
        rightMin = findMin(rootNode.right, lastKMin)
        currentMinVal = min(leftMin, rightMin)
        if (currentMinVal < minVal and currentMinVal > lastKMin):
            return minVal


def findKthMin(node, k):
    minNode = node
    for min_offset in range(k):
        kMinNode = findMin(node, minNode, kMinNode)

    return minNode
