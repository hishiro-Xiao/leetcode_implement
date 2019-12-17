class ShellSort:
    def ShellSort(self, arr):
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                j = i
                while j-gap >= 0 and arr[j] < arr[j-gap]:
                    arr[j], arr[j-gap] = arr[j-gap], arr[j]
                    j -= gap
            gap //= 2 
        return arr
        
if __name__ == '__main__':

    arr1 = [x for x in range(5,0,-1)]+[x for x in range(6,11)]+[x for x in range(20,10,-1)]
    arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(arr1)

    sln = ShellSort()
    res = sln.ShellSort(arr1)
    print(res)
