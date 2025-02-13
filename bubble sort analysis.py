#Write a function to compute the number	of comparisons in Bubble Sort for a given array	size.

#writing a bubble sort algorithm 
array = [3, 9, 5, 6, 1]
for i in range(len(array)-1):
    for j in range(len(array)-1-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)

#analysing the bubble sort
array = [3, 9, 5, 6, 1]
comparisons = 0
swaps = 0
for i in range(len(array)-1):
    for j in range(len(array)-1-i):
        comparisons += 1
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            swaps += 1
            

print(array)
print("Comparisons: " , comparisons)
print("Swaps: " , swaps)

#number of comparisons / worst-case scenario of number of swaps
n = len(array)
expected_comparisons = (n * (n - 1)) // 2  
print("Expected Number of Comparisons:", expected_comparisons)