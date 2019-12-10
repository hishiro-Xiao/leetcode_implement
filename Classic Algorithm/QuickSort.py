class QuickSort:
    def QuickSort(self, arr):
        if len(arr) == 1 or len(arr) == 0:
            return arr

        privot = arr[0]
        low, high = 0, len(arr) - 1
        while low < high:
            while  low < high and arr[high] > privot:
                high -= 1
            arr[low] = arr[high]
            while  low < high and arr[low] < privot:
                low += 1
            arr[high] = arr[low]
        arr[low] = privot

        left = self.QuickSort(arr[0: low])
        right = self.QuickSort(arr[low + 1: len(arr)])

        return left + [privot] + right

if __name__ == '__main__':

    arr1 = [x for x in range(5,0,-1)]+[x for x in range(6,11)]+[x for x in range(20,10,-1)]
    arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(arr2)

    sln = QuickSort()
    res = sln.QuickSort(arr2)
    print(res)