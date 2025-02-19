# Kadana Algo

import sys

def largestSubayyarSum(givenNums):
	maxSum = -sys.maxsize -1
	currSum = 0
	start = 0
	end = 0

	n = len(givenNums)

	while end < n:
		while currSum <0:
			currSum -= givenNums[start]
			start += 1

		currSum += givenNums[end]
		end += 1

		maxSum = max(maxSum, currSum)
	
	return maxSum

givenNums = [1,4,-3,10,-20,12]
print(largestSubayyarSum(givenNums))