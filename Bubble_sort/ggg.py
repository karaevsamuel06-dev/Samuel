def bubble_sort(spisok):
    n = len(spisok)
    for i in range(n):
        for a in range(0, n - i - 1):
            if spisok[a] > spisok[a + 1]:
                spisok[a], spisok[a + 1] = spisok[a + 1], spisok[a]
    return spisok
            
def bynary_search(spisok, target):
    left = 0
    right = len(spisok) - 1

    while left <= right:
        mid = (left + right) // 2

        if spisok[mid] == target:
            print("Элемент найден :", mid)
            return
        elif spisok[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Элемент не найден")

numbers = [2, 5, 9, 1, 7]

sorted_numbers = bubble_sort(numbers)
print("Отсортированный список", sorted_numbers)

bynary_search(sorted_numbers, 7)

