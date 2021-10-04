input_str = input('Enter elements of a list separated by space ')
print("\n")
list1 = input_str.split()   #to convert the input string to list

print('list: ', list1)

for i in range(len(list1)):     #to convert each element to integer type
    list1[i] = int(list1[i])



#function definition
def binary_search(list1,n):


    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if list1[mid] < n:
            low = mid + 1


        elif list1[mid] > n:
            high = mid - 1


        else:
            return mid

    return 0

n = input("enter the number to be searched:")
result = binary_search(list1, int(n)) #function call

if result != 0:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")
