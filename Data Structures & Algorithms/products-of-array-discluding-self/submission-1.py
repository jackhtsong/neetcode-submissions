import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # add the product of shit left of i with right of i
        # use prefix sum to calculate the product for all 
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        solution = [0] * len(nums)
        prefixpoint = 0
        postfixpoint = len(nums) - 1
        for i in range(len(nums)):
            j = len(nums)
            if i == 0:
                prefix[i] = nums[i]
                postfix[j - 1] = nums[len(nums) - 1]
                prefixpoint+= 1
                postfixpoint -= 1
            else:
                prefix[prefixpoint] = prefix[prefixpoint - 1] * nums[prefixpoint]
                prefixpoint += 1
                postfix[postfixpoint] = postfix[postfixpoint + 1] * nums[postfixpoint]
                postfixpoint -= 1

        for i in range(len(nums)):
            if i == 0:
                solution[0] = postfix[1]
                continue
            if i == len(nums) - 1:
                solution[len(nums) - 1] = prefix[len(nums) - 2]
                continue
            solution[i] = prefix[i - 1] * postfix[i + 1]
        return solution

                

    
