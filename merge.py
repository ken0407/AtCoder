def merge(left, right):
    res = []
    i,j = 0,0
    len_left = len(left)
    len_right = len(right)

    while (i<len_left) & (j<len_right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1

    return res + left[i:] + right[j:]

def merge_sort(array):
    if len(array)<=1:
        return array
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    return merge(merge_sort(left), merge_sort(right))

if __name__=='__main__':
    x = [11, 32, 1, 5, 3, 4, 7, 12]
    sorted_list_ = merge_sort(x)
    print(sorted_list_)