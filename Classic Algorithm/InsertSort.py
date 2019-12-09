class InsertSort:
    def InsertSort(self, arr):
        for i in range(1, len(arr)):
            insertpos = i
            insertval = arr[i]
            for j in range(i,0,-1):
                if arr[i] < arr[j]:
                    arr[insertpos] = arr[j]
                else:
                    break
            arr[insertpos] = arr[] 

if __name__ == '__main__':

    arr1 = [x for x in range(5,0,-1)]+[x for x in range(6,11)]
    print(arr1)

    sln = SelectSort()
    res = sln.SelectSort_optimize2(arr1)
    print(res)