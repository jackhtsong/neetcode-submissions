class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            if i == 0:
                hashTable[nums[0]] = 0
                continue
            
            if target - nums[i] in hashTable:
                return [hashTable[target - nums[i]], i]
            else:
                hashTable[nums[i]] = i