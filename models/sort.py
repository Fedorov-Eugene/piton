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

def quick_sort_test(txt): 
    return quick_sort(list(map(int, txt.split(" "))))

def merge_sort_test(txt): 
    return merge_sort(list(map(int, txt.split(" "))))

def radix_sort_test(txt): 
    return radix_sort(list(map(int, txt.split(" "))))


def main(str):
    pass

if __name__ == "__main__":
    main()

