def quick_sort(array): 
    if len(array) <= 1:
        return array
    else:
        lefthalf = quick_sort([x for x in array[1:] if x<array[0]])
        righthalf = quick_sort([x for x in array[1:] if x>=array[0]])
        return lefthalf + [array[0]] + righthalf

def merge_sort(array):

    def merge(left, right):
        Res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                Res.append(left[i])
                i += 1
            else:
                Res.append(right[j])
                j += 1
        Res += left[i:] + right[j:]
        return Res

    if len(array) <= 1:
        return array
    else:
        L = array[:len(array) // 2]
        R = array[len(array) // 2:]
    return merge(merge_sort(L), merge_sort(R))

def radix_sort(array):
    rang = 10
    length = len(str(max(array)))
    for i in range(length):
        array_rang = [[] for j in range(rang)]
        for j in array:
            figure = j // 10**i % 10
            array_rang[figure].append(j)  
        array = []
        for j in range(rang):
            array = array + array_rang[j]
    return array

def main():
    sort = {'1':quick_sort, '2':merge_sort, '3':radix_sort}
    array = list(map(int, input().split()))
    print('1.quick_sort\n2.merge_sort\n3.radix_sort')
    sort_number = input()
    print(sort[sort_number](array))



if __name__ == "__main__":
    main()

