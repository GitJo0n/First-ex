def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # 반환값이 없을 경우 -1 반환(에러를 쉽게 찾음)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(find_element(arr, 7))  # O(n)


