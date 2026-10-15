class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0
        if not nums:
            return 0
        for num in elements:
            if num - 1 not in elements:
                current = num
                counter = 1
                while current + 1 in elements:
                    counter += 1
                    current += 1
                if counter >= longest:
                    longest = counter
        return longest
                    
