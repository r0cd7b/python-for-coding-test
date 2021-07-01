# 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    left = start + 1
    right = end
    while True:
        while left < end and array[left] <= array[start]:
            left += 1
        while right > start and array[right] >= array[start]:
            right -= 1
        if left >= right:
            array[right], array[start] = array[start], array[right]
            break
        array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
