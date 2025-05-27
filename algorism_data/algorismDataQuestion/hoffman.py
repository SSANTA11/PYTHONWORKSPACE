def insertSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

class Node:
    def __init__ (self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
nodes=[]
input=[('A',20),('B',30)]
for data,freq in input:
    nodes.append(Node(data,freq))
mindex=0
sum=0
for i in range(1, len(input)):
    if input[mindex].freq<input[i].freq: