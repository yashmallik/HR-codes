# Objective
# # Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the Tutorial tab for learning materials and an instructional video!
# Task
# Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above.
# Once sorted, print the following 3 lines:
# for (int i = 0; i < n; i++) {
#     // Track number of elements swapped during a single array traversal
#     int numberOfSwaps = 0;
    
#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#             numberOfSwaps++;
#         }
#     }
    
#     // If no elements were swapped during a traversal, array is sorted
#     if (numberOfSwaps == 0) {
#         break;
#     }
# }

# Array is sorted in numSwaps swaps.
# where numSwap is the number of swaps that took place.
# First Element: firstElement
# where firstElement is the first element in the sorted array.
# Last Element: lastElement
# where secondElement is the last element in the sorted array.
# Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.




for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
