import cProfile

class BubbleSort:
    #原始实现
    def BubbleSort(self, arr):
        len_arr = len(arr)

        for i in range(len_arr-1):
            for j in range(i+1, len_arr):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        
        return arr
    
    #全局有序
    def BubbleSort_optimized1(self, arr):
        len_arr = len(arr)

        for i in range(len_arr-1):
            sorted = False
            for j in range(i+1, len_arr):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                    sorted = True
            if not sorted:
                return arr
        
        return arr
    
    #局部有序
    def BubbleSort_optimized2(self, arr):
        pass


if __name__ == '__main__':

    arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    sln = BubbleSort()
    res = sln.BubbleSort_optimized1(arr1)
    print(res)
