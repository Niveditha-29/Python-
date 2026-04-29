n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
largest = arr[0]
for num in arr:
    if num >  second  largest:
        largest = num

print(" Largest element is:", largest)

