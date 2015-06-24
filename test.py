def merge_sort(lst):
    if len(lst) == 1:
       return lst
    middle = len(lst) / 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    # print 'left', left
    # print 'right', right
    return merge(left, right)

def merge(left, right):
    merged = []
    while left and right:
          if left[0] <= right[0]:
             merged.append(left.pop(0))
          else:
             merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged

if __name__ == '__main__':
   print merge_sort([1, 4, 2, 3, 6, 9, 0, 5, 10])