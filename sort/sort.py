def quick_sort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return quick_sort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + quick_sort([x for x in arr[1:] if x>=arr[0]])

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]   #slice
        right = arr[mid:]   #slice

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        x = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[x] = left[i]
                i += 1
            else:
                arr[x] = right[j]
                j += 1
            x += 1

        while i < len(left):
            arr[x] = left[i]
            i += 1
            x += 1
        while j < len(right):
            arr[x] = right[j]
            j += 1
            x += 1

def radix_sort(arr):
    rang = 10
    length = len(str(max(arr)))
    tmp = arr
    for i in range(length):
        arr_rang = [[] for j in range(rang)]
        for j in tmp:
            figure = j // 10**i % 10
            arr_rang[figure].append(j)  
        tmp = []
        for j in range(rang):
            tmp = tmp + arr_rang[j]
    for i in range(len(arr)):
        arr[i] = tmp[i]

def main():
    sort = {'1':quick_sort, '2':merge_sort, '3':radix_sort}
    arr = list(map(int, input().split()))
    print('1.quick_sort\n2.merge_sort\n3.radix_sort')
    sort_number = input()
    print(sort[sort_number](arr))



if __name__ == "__main__":
    main()

