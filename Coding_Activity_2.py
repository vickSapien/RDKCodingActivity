'''
FUNCTION sortAndFindMedian(numbers)
CALL sort(numbers)
DEFINE n AS length of numbers
IF n MOD 2 = 0
RETURN (numbers[n/2 - 1] + numbers[n/2 ) / 2
ELSE
RETURN numbers[n/2]
ENDIF
ENDFUNCTION
FUNCTION sort(numbers)
// Implement a sorting algorithm (e.g., bubble sort, selection sort, etc.)
// Sort the 'numbers' array in ascending order
// Pseudocode for the sorting algorithm is not provided; implement as per your
understanding
ENDFUNCTION
'''

def sortAndFindMedian(numbers):
    insertionSort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return numbers[n/2 - 1]  + numbers[n/2] / 2
    else:
        return numbers[int(n/2)]


def insertionSort(numbers):
    for i in range(1, len(numbers)):
        temp = numbers[i]
        j = i
        while j > 0 and numbers[j-1] > temp:
            numbers[j] = numbers[j-1]
            j -= 1
        numbers[j] = temp

    return numbers