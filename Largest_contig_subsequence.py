#To start off this file I define a bunch of lists for us to demonstrate
#   the functions on
#case where largest sum in middle
list1 = [-5, 1, 15, -44, 2, 3]
#case where largest sum at beginning
list2 = [55, 60, -40, 2, 5, -300, 61]
#case where largest sum is at the end
list3 = [-2, -4, -1, -15, 1]
#case where all entries are negative
list4 = [-2, -4, -1, -5, -3, -8]
#case from homework 3 question 1 /contains a negative in the sum
list5 = [26, -15, 5, -7, -12, 8, -5, 10, 14, -5]
#case with one list entry
list6 = [-5]


#This function finds the largest subsequence using one 'for' loop and some
#   variables. This takes linear time.
def FindLargestSubsequenceLinear(list):
    largest_sum = list[0]
    curr_sum = list[0]
    for i, x in enumerate(list):
        #skip adding the sum of the first index, since we already do
        #   that before starting the for loop
        if i != 0:
            #add the current index to the current_sum at every index
            curr_sum += x
        #update the largest sum found whenever we find a new largest sum
        if curr_sum > largest_sum:
            largest_sum = curr_sum
        #whenever the current sum goes negative, it can't be included in the
        #   largest contiguous sum unless all array values are negative.
        if curr_sum < 0:
            curr_sum = 0
    return largest_sum

#This function also finds the largest subsequence in linear time, but does
#   it recursively to better demonstrate the subproblem in the DP solution.
def FindLargestSubsequenceRecursive(list, index, largest_sum, curr_sum):
    #base case where array is only one element (the last element in list)
    if index+1 == len(list):
        return max(largest_sum, curr_sum)
    #recursive case, where current sum is the max between the ith index value
    #   and the running sum from the last negative plus the ith index value
    #   and largest_sum just keeps track of the largest curr_sum so far
    return FindLargestSubsequenceRecursive(list, index+1, max(largest_sum, curr_sum), max(curr_sum + list[index+1], list[index+1]))

#There probably is already a function that will do this,
#   But I wanted to make sure the lists got printed exactly
#   how I wanted. This function just does that - prints out
#   lists cleanly on one line
def printList(list):
    print("[", end="")
    for i, x in enumerate(list):
        if i < len(list) - 1:
            print(x, end=", ")
        else:
            print(x, end="")
    print("]", end="\n")

#Much like the function above, this function just prints out the solution
#   in a (relatively) pretty, standardized way
def printSolution(list):
    print("IN THE LIST - ")
    printList(list)
    print("\nTHE LONGEST CONTIGUOUS SUBSEQUENCE HAS A SUM OF")
    print(FindLargestSubsequenceLinear(list))
    print("When solved with a for loop\n\n")
    print("AND A LARGEST CONTIGUOUS SUBSEQUENCE SUM OF")
    print(FindLargestSubsequenceRecursive(list, 0, list[0], list[0]))
    print("When solved recursively (both sums should be the same)\n\n")
    print("########################################################\n\n")

#This is where all the functions defined above get called
print("########################################################\n\n")
printSolution(list1)
printSolution(list2)
printSolution(list3)
printSolution(list4)
printSolution(list5)
printSolution(list6)
