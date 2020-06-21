def quick_sort(array):
    if len(array)<=1:
        return array
    p = array[-1]
    left =[]
    pivot = []
    right = []

    for v in array:
        if v<p:
            left.append(v)
        elif v==p:
            pivot.append(v)
        else:
            right.append(v)
    return quick_sort(left) + pivot + quick_sort(right)

if __name__=='__main__':
    x = [11, 32, 1, 5, 3, 4, 7, 12]
    sorted_list_ = quick_sort(x)
    print(sorted_list_)