class SelectSort:
    #原始实现
    def SelectSort(self, arr):
        for i in range(len(arr) - 1):
            minpos = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minpos]:
                    minpos = j
            if minpos != i:
                arr[i], arr[minpos] = arr[minpos], arr[i]
        return arr
    
    #每次不光找最小值，还找最大值(节省一半时间)
    def SelectSort_optimize1(self, arr):
        for i in range(len(arr)//2 - 1):
            minpos = i
            maxpos = len(arr) - i -1
            for j in range(i, maxpos+1):
                if arr[j] < arr[minpos]:
                    minpos = j
                elif arr[j] > arr[maxpos]:
                    maxpos = j
            if minpos != i:
                arr[i], arr[minpos] = arr[minpos], arr[i]
            if maxpos != len(arr) - i -1:
                arr[i], arr[maxpos] = arr[maxpos], arr[i]
        return arr
    
     # 每次不光找最小值，最大值，还有第二小的值(节省三分之二的时间)
     # 其实是错误的，第二小值需要第三小值的信息，这是做不到的
     # 所以说，一次遍历，最多只能找到数组中的最大值和最小值
    def SelectSort_optimize2(self, arr):
        for i in range(0,len(arr)//2 - 1,2):
            minpos = i
            maxpos = len(arr) - i -1
            secmin = i+1
            for j in range(i, maxpos+1):
                if arr[j] < arr[minpos]:
                    minpos = j
                elif arr[j] > arr[maxpos]:
                    maxpos = j
                elif arr[minpos] < arr[j] < arr[secmin]:
                    secmin = j
            if minpos != i:
                arr[i], arr[minpos] = arr[minpos], arr[i]
            if maxpos != len(arr) - i -1:
                arr[i], arr[maxpos] = arr[maxpos], arr[i]
            if secmin != i+1:
                arr[i], arr[secmin] = arr[secmin], arr[i]
        return arr

    # 既然可以一次找出最大最小和第二小值，那为什么不能一次找出所有值呢
    # 结果：错误，因为上面第二小值是做不到的
    def SelectSort_optimize3(self, arr):
        pos = [x for x in range(len(arr))]  #记录第k小的值的下标
        print(pos)
        
        for j in range(len(pos)-1):
            for i in range(len(arr)):
                if j == 0 and arr[i] < arr[pos[j]]:
                    pos[j] = i
                elif arr[pos[j-1]] < arr[i] <= arr[pos[j]]:
                    pos[j] = i
        print(pos)
        return [arr[x] for x in pos]

if __name__ == '__main__':

    arr1 = [x for x in range(5,0,-1)]+[x for x in range(6,11)]
    print(arr1)

    sln = SelectSort()
    res = sln.SelectSort_optimize2(arr1)
    print(res)
