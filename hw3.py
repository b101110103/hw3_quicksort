def QuickSort(arr, start, end):
    
    if start >= end:
        return
    
    benchmark = arr[start] #先選第一個元素當作基準點
    left = start
    right = end
    
    while left < right:
        #先跑右側，直到右指標<=基準點
        while left < right and arr[right] >= benchmark: 
            right -= 1
        #再跑左側，直到左指標>=基準點
        while left < right and arr[left] <= benchmark: 
            left += 1
        #交換左右指標，只要左右指標重疊，while迴圈就結束
        arr[left], arr[right] = arr[right], arr[left] 
    
    #交換基準點跟右指標（左指標也可以反正左右指標重疊了）
    arr[start], arr[right] = arr[right], arr[start]
    
    #因為要輸出排序過程，所以在此階段先print出來
    print("排序過程：", arr)
    
    #基準點的左邊跟右邊再繼續進行快速排序，直到start和end重合，就return
    QuickSort(arr, start, right-1)
    QuickSort(arr, right+1, end)

arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("初始陣列：", arr)
QuickSort(arr, 0, len(arr)-1)
print("排序後的陣列：", arr)