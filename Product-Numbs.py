test0 = [1,2,3,4,5]

def productNumbers(array):
    #size of array is n
    n = len(array)

    direct_multiply = list([0]*n)
    direct_multiply[0] = array[0]
    for i in range(1,n):
        direct_multiply[i] = direct_multiply[i-1]*array[i]

    reverse_multiply = list([0]*n)
    reverse_multiply[n-1] = array[n-1]
    for i in range(n - 2,-1,-1):
        reverse_multiply[i] = reverse_multiply[i+1]*array[i]

    array[0] = reverse_multiply[1]
    array[n - 1] = direct_multiply[n-2]
    for i in range(1,n -1):
        array[i] = direct_multiply[i - 1]*reverse_multiply[i+1]
    return array
print(productNumbers(test0))