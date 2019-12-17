class HeapSort:
    def HeapSort(self, arr):
        for i in range(len(arr), 0, -1):
            arr[0: i] = self.Heap(arr[0: i])
        return arr

    def Heap(self, arr):
        # 将数组的下标映射到树，arr[i]的又子树为(i+1)*2，因为i从0开始
        # 大顶堆：将值大的节点“升到”堆的顶部
        for i in range(len(arr) // 2 - 1, -1, -1):
            if (i+1)*2-1 >= len(arr) or (i+1)*2 >= len(arr):
                continue
            if arr[(i+1)*2] > arr[i] and arr[(i+1)*2] > arr[(i+1)*2 - 1]:
                arr[(i+1)*2], arr[i] = arr[i], arr[(i+1)*2]
            elif arr[(i+1)*2 - 1] > arr[i] and arr[(i+1)*2 - 1] > arr[(i+1)*2]:
                arr[(i+1)*2 - 1], arr[i] = arr[i], arr[(i+1)*2 - 1]
        arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]

        return arr

if __name__ == '__main__':

    arr1 = [x for x in range(5,0,-1)]+[x for x in range(6,11)]+[x for x in range(20,10,-1)]
    arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(arr1)

    sln = HeapSort()
    res = sln.HeapSort(arr1)
    print(res)