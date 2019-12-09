class InsertSort:
    def InsertSort(self, arr):
        for i in range(1, len(arr)):
            insertpos = i
            insertval = arr[i]
            for j in range(i-1,-1,-1):
                if insertval < arr[j]:
                    arr[insertpos] = arr[j]
                    insertpos -= 1
                else:
                    break
            arr[insertpos] = insertval
        return arr

    # 优化，在左边有序数组中查找插入位置时，可以使用二分查找来减少查找次数
    

if __name__ == '__main__':

    arr1 = [x for x in range(5,0,-1)]+[x for x in range(6,11)]+[x for x in range(20,10,-1)]
    print(arr1)

    sln = InsertSort()
    res = sln.InsertSort(arr1)
    print(res)