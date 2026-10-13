class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            key = nums[i]
            value = i
            hashTable[key] = value

        solution = []
        for i in range(len(nums)):
            if target - nums[i] in hashTable and hashTable[target - nums[i]] != i:
                solution = [i, hashTable[target - nums[i]]]
                break
        return solution