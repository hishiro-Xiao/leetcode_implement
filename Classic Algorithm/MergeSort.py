class MergeSort:
    def MergeSort(self, arr):
        if len(arr) == 1 or len(arr) == 0:
            return arr
        
        left = self.MergeSort(arr[0: len(arr) // 2])
        right = self.MergeSort(arr[len(arr) // 2: len(arr)])

        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        
        return res

if __name__ == '__main__':

    arr1 = [x for x in range(5,0,-1)]+[x for x in range(6,11)]+[x for x in range(20,10,-1)]
    arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(arr2)

    sln = MergeSort()
    res = sln.MergeSort(arr2)
    print(res)