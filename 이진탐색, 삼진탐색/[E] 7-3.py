def binary_search(arr,t,start,end):
    while start <= end :
        mid = (start+end)//2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t :
            end = mid -1
        else :
            end = start +1

#탐색 범위가 2000만을 넘어가면 이진탐색을 고려
#처리해야할 데이터의 값이나 개수가 1000만개 이상일 때도!
