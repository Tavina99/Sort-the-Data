import random
import time
import copy
import sys


def SelectionSort(numbers):
    
    size = len(numbers)
    # Initialize a variable to count the number of comparisons
    comparisonAmount = 0

    for j in range(size):
        # Assume the current index is the minimum
        minimum = j

        # Iterate through the remaining elements to find the minimum
        for i in range(j + 1, size):
            comparisonAmount += 1
            # Compare and update the minimum index 
            if numbers[i] < numbers[minimum]:
                minimum = i

        # Swap the minimum value and the current index value
        (numbers[minimum], numbers[j]) = (numbers[j], numbers[minimum])

    return comparisonAmount



def MergeSort(numbers):
    # Recursive function to perform Merge Sort and count comparisons
    def mergeSortRecursive(nums):
        # Base case: If the list has 1 element or is empty, it's already sorted
        if len(nums) <= 1:
            return nums, 0  # Return both the sorted list and comparison count

        # Split the list into two halves
        mid = len(nums) // 2
        left, leftComparisons = mergeSortRecursive(nums[:mid])  # Recursive call on the left half
        right, rightComparisons = mergeSortRecursive(nums[mid:])  # Recursive call on the right half

        # Merge the sorted halves and count comparisons made during merging
        merged, mergeComparisons = merge(left, right)
        
        # Return the merged list and the total comparisons made
        return merged, leftComparisons + rightComparisons + mergeComparisons

    # Helper function to merge two sorted lists and count comparisons
    def merge(left, right):
        i = j = 0  # Initialize indices for left and right lists
        merged = []  # Initialize an empty list to store the merged result
        comparisons = 0  # Initialize the comparison count

        # Compare elements from both lists and merge in sorted order
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append remaining elements from both lists (if any)
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        # Return the merged list and the total comparisons made during merging
        return merged, comparisons

    # Start the recursive sorting process
    sortedNumbers, comparisons = mergeSortRecursive(numbers)

    # Return the sorted list and the total comparisons made during sorting
    return sortedNumbers, comparisons




#QuickSort (with code in Python/C++/Java/C) (no date) Programiz.com. Available at: https://www.programiz.com/dsa/quick-sort (Accessed: December 12, 2023). 
def QuickSort(numbers, lowest, highest):
    comparisonAmount = 0
    def partition(numbers, lowest, highest):
        nonlocal comparisonAmount#This allows partition function to use the same comparisonAmount variable in QuickSort Function
        """
        generateUniqueRandomArray Function gives us a random, evenly distributed numbers array so to 
        keep up the efficiency of quick sort algorithm, random number will be chosen as pivot and will assign it as the
        rightmost element 
        """
        pivot_index = random.randint(lowest, highest)
        (numbers[pivot_index], numbers[highest]) = (numbers[highest], numbers[pivot_index])
        pivot = numbers[highest]
        # pointer for greater element
        j = lowest - 1

        for i in range(lowest, highest): 
            comparisonAmount += 1
            if numbers[i] <= pivot:
                j = j + 1
                if j !=i:
                    (numbers[j], numbers[i]) = (numbers[i], numbers[j])

        (numbers[j + 1], numbers[highest]) = (numbers[highest], numbers[j + 1])
        # return the position of pivot
        return j + 1

    if lowest < highest:
        p = partition(numbers, lowest, highest)
        # recursive call on the left side of pivot
        comparisonAmount+=QuickSort(numbers, lowest, p - 1)
        # recursive call on the right side of pivot
        comparisonAmount+=QuickSort(numbers, p + 1, highest)

    return comparisonAmount


def CalculateAverageTime(sortingFunction, numbers):
    #to calculate the average execution time, calculate execution time ten times and dividing it by ten
    tenTimes = 10
    executionTime = 0
    #doing a seperate if statement for quicksort because it's passing extra two parameters than other sorting algorithmes
    for i in range (tenTimes):
        if(sortingFunction == QuickSort):
            startingTime = time.perf_counter()
            sortingFunction(numbers,0,len(numbers)-1)
            
        else:
            startingTime = time.perf_counter()
            sortingFunction(numbers)
        endingTime = time.perf_counter()
        executionTime += (endingTime - startingTime) * 1000  # Convert to milliseconds
    averageExecutionTime = executionTime / tenTimes
    return averageExecutionTime

def generateUniqueRandomList(lowest, highest, size):
    # Ensure size is not greater than the range of unique values
    size = min(size, highest - lowest + 1)
    #range() generates a sequence of numbers from lowest to highest and  random.sample() is then used to select size unique elements from this sequence
    return random.sample(range(lowest, highest + 1), size)

def writeSortedArraysToFile(sortedArray, sortingMethod, arraySize, filePath):
    # This if condition will prevent appending newly sorted arrays  to previously sorted arrays
    if sortingMethod == 'Selection Sorting' and arraySize == 100:
        with open(filePath, 'w') as file:
            file.write('Sorted ' + str(arraySize) + ' numbers using ' + sortingMethod + ':\n')
            file.write(str(sortedArray) + '\n\n')
    else:
        with open(filePath, 'a') as file:
            file.write('Sorted ' + str(arraySize) + ' numbers using ' + sortingMethod + ':\n')
            file.write(str(sortedArray) + '\n\n')

lowestNumber = 100000
highestNumber = 999999
sizeHundred = 100
sizeThousand = 1000
sizeTenThousand = 10000

hundredList = generateUniqueRandomList(lowestNumber, highestNumber, sizeHundred)
thousandList = generateUniqueRandomList(lowestNumber, highestNumber, sizeThousand)
tenThousandList = generateUniqueRandomList(lowestNumber, highestNumber, sizeTenThousand)


#copy.deepcopy() function will copy the list and the modifications done to the copied list won't affect the original list
selectionSortingHundredList = copy.deepcopy(hundredList)
selectionSortingThousandList = copy.deepcopy(thousandList)
selectionSortingTenThousandList = copy.deepcopy(tenThousandList)
quickSortingHundredList = copy.deepcopy(hundredList)
quickSortingThousandList = copy.deepcopy(thousandList)
quickSortingTenThousandList = copy.deepcopy(tenThousandList)
mergeSortingHundredList = copy.deepcopy(hundredList)
mergeSortingThousandList = copy.deepcopy(thousandList)
mergeSortingTenThousandList = copy.deepcopy(tenThousandList)


sortedArrayListFilePath = 'sortedArrayList.txt'

SelectionSort(selectionSortingHundredList)
writeSortedArraysToFile(selectionSortingHundredList, 'Selection Sorting', sizeHundred ,sortedArrayListFilePath )
SelectionSort(selectionSortingThousandList)
writeSortedArraysToFile(selectionSortingThousandList, 'Selection Sorting', sizeThousand ,sortedArrayListFilePath )
SelectionSort(selectionSortingTenThousandList)
writeSortedArraysToFile(selectionSortingTenThousandList, 'Selection Sorting', sizeTenThousand,sortedArrayListFilePath )

MergeSort(mergeSortingHundredList)
writeSortedArraysToFile(mergeSortingHundredList, 'Merge Sorting', sizeHundred ,sortedArrayListFilePath )
MergeSort(mergeSortingThousandList)
writeSortedArraysToFile(mergeSortingThousandList, 'Merge Sorting', sizeThousand ,sortedArrayListFilePath )
MergeSort(mergeSortingTenThousandList)
writeSortedArraysToFile(mergeSortingTenThousandList, 'Merge Sorting', sizeTenThousand ,sortedArrayListFilePath )

QuickSort(quickSortingHundredList,0,len(quickSortingHundredList)-1)
writeSortedArraysToFile(quickSortingHundredList, 'Quick Sorting', sizeHundred ,sortedArrayListFilePath )
QuickSort(quickSortingThousandList,0,len(quickSortingThousandList)-1)
writeSortedArraysToFile(quickSortingThousandList, 'Quick Sorting', sizeThousand ,sortedArrayListFilePath )
QuickSort(quickSortingTenThousandList,0,len(quickSortingTenThousandList)-1)
writeSortedArraysToFile(quickSortingTenThousandList, 'Quick Sorting', sizeTenThousand ,sortedArrayListFilePath )

selectionSortingHundredListTime = CalculateAverageTime(SelectionSort,selectionSortingHundredList)
print("Average execution time for 100 numbers using Selection Sort = ",selectionSortingHundredListTime)
selectionSortingThousandListTime = CalculateAverageTime(SelectionSort,selectionSortingThousandList)
print("Average execution time for 1000 numbers using Selection Sort = ",selectionSortingThousandListTime)
selectionSortingTenThousandListTime = CalculateAverageTime(SelectionSort,selectionSortingTenThousandList)
print("Average execution time for 10000 numbers using Selection Sort = ",selectionSortingTenThousandListTime)

mergeSortingHundredListTime = CalculateAverageTime(MergeSort,mergeSortingHundredList)
print("Average execution time for 100 numbers using Merge Sort = ",mergeSortingHundredListTime)
mergeSortingThousandListTime = CalculateAverageTime(MergeSort,mergeSortingThousandList)
print("Average execution time for 1000 numbers using Merge Sort = ",mergeSortingThousandListTime)
mergeSortingTenThousandListTime = CalculateAverageTime(MergeSort,mergeSortingTenThousandList)
print("Average execution time for 10000 numbers using Merge Sort = ",mergeSortingTenThousandListTime)

quickSortingHundredListTime = CalculateAverageTime(QuickSort,quickSortingHundredList)
print("Average execution time for 100 numbers using Quick Sort = ",quickSortingHundredListTime)
quickSortingThousandListTime = CalculateAverageTime(QuickSort,quickSortingThousandList)
print("Average execution time for 1000 numbers using Quick Sort = ",quickSortingThousandListTime)
quickSortingTenThousandListTime = CalculateAverageTime(QuickSort,quickSortingTenThousandList)
print("Average execution time for 10000 numbers using Quick Sort = ",quickSortingTenThousandListTime)


print("Number of comparisons for 100 numbers using Selection Sort = ", SelectionSort(selectionSortingHundredList))
print("Number of comparisons for 1000 numbers using Selection Sort = ", SelectionSort(selectionSortingThousandList))
print("Number of comparisons for 10000 numbers using Selection Sort = ", SelectionSort(selectionSortingTenThousandList))

#How do I add a comparison counter to merge sort in Python? (no date) Quora. Available at: https://www.quora.com/How-do-I-add-a-comparison-counter-to-merge-sort-in-Python (Accessed: December 24, 2023).
SortedHundredListMerge,hundredListComparisonAmount = MergeSort(mergeSortingHundredList)
print("Number of comparisons for 100 numbers using Merge Sort = ",hundredListComparisonAmount )
SortedThousandListMerge,thousandListComparisonAmount = MergeSort(mergeSortingThousandList)
print("Number of comparisons for 1000 numbers using Merge Sort = ", thousandListComparisonAmount)
SortedTenThousandListMerge,tenThousandListComparisonAmount = MergeSort(mergeSortingTenThousandList)
print("Number of comparisons for 10000 numbers using Merge Sort = ", tenThousandListComparisonAmount)

#Follow, S. S. (2018) Comparisons involved in modified quicksort using merge sort tree, GeeksforGeeks. Available at: https://www.geeksforgeeks.org/comparisons-involved-modified-quicksort-using-merge-sort-tree/ (Accessed: December 24, 2023).
print("Number of comparisons for 100 numbers using Quick Sort = ", QuickSort(quickSortingHundredList,0,len(quickSortingHundredList)-1))
print("Number of comparisons for 1000 numbers using Quick Sort = ", QuickSort(quickSortingThousandList,0,len(quickSortingThousandList)-1))
print("Number of comparisons for 10000 numbers using Quick Sort = ", QuickSort(quickSortingTenThousandList,0,len(quickSortingTenThousandList)-1))


#prernadec Follow, P. (2020) Line chart in matplotlib - python, GeeksforGeeks. Available at: https://www.geeksforgeeks.org/line-chart-in-matplotlib-python/ (Accessed: December 29, 2023).
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')  # Set the style of the plot to 'ggplot'

selectionSortDataSets = [sizeHundred, sizeThousand, sizeTenThousand]
selectionSortTimings = [selectionSortingHundredListTime,selectionSortingThousandListTime,selectionSortingTenThousandListTime]
mergeSortDataSets = [sizeHundred, sizeThousand, sizeTenThousand]
mergeSortTimings = [mergeSortingHundredListTime,mergeSortingThousandListTime,mergeSortingTenThousandListTime]
quickSortDataSets = [sizeHundred, sizeThousand, sizeTenThousand]
quickSortTimings = [quickSortingHundredListTime,quickSortingThousandListTime,quickSortingTenThousandListTime]
 
#Plotting a line chart for all algorithms to get an overall understanding  
plt.plot(selectionSortDataSets, selectionSortTimings, 'b', label='Selection Sort', linewidth=5)    
plt.plot(mergeSortDataSets, mergeSortTimings, 'r', label='Merge Sort', linewidth=5)   
plt.plot(quickSortDataSets, quickSortTimings, 'g', label='Quick Sort', linewidth=4)#reducing the width to see the merge sort line
plt.ylabel('Time(m/s)')  
plt.xlabel('Dataset Sizes')  
plt.title('Performance of sorting algorithms across various dataset sizes')   
plt.legend() # Displaying a legend to differentiate between the sorting algorithms
plt.show() # Display the plot

#jeeteshgavande30 Follow, J. (2020) Bar plot in matplotlib, GeeksforGeeks. Available at: https://www.geeksforgeeks.org/bar-plot-in-matplotlib/ (Accessed: December 29, 2023).

dataSets = ['100', '1000', '10000']
algorithms = ['Selection Sort', 'Merge Sort', 'Quick Sort']

# Plotting separate bar charts for each algorithm to get an explicit understanding
for i, algorithm in enumerate(algorithms):
    plt.figure()
    
    # Bar chart for Selection Sort
    if i == 0:
        plt.bar(dataSets, selectionSortTimings, color='blue', label='Selection Sort')
    
    # Bar chart for Merge Sort
    elif i == 1:
        plt.bar(dataSets, mergeSortTimings, color='orange', label='Merge Sort')
    
    # Bar chart for Quick Sort
    elif i == 2:
        plt.bar(dataSets, quickSortTimings, color='green', label='Quick Sort')
    
    # Adding labels and title
    plt.xlabel('Dataset Sizes')
    plt.ylabel('Time(m/s)')
    plt.title(f'Execution Times for {algorithm} ')
    plt.legend() # Displaying a legend to differentiate between the sorting algorithms
    plt.show() # Display the plot

    

