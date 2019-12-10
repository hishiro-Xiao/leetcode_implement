class ShellSort:
    def ShellSort(self, arr):
        gap = len(arr) // 2 
        while gap > 0:
            for i in range(gap):
                for j in range(i, len(arr), gap):
                    
            gap = gap // 2
        return arr
        
if __name__ == '__main__':

    arr1 = [x for x in range(5,0,-1)]+[x for x in range(6,11)]+[x for x in range(20,10,-1)]
    print(arr1)

    sln = ShellSort()
    res = sln.ShellSort(arr1)
    print(res)
