class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        # for each unique first num, find 2sum that adds up to 0
        sol = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                ans = nums[i] + nums[l] + nums[r]
                if ans == 0:
                    sol.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    r-=1
                elif ans < 0:
                    l += 1
                elif ans > 0:
                    r -= 1

        return sol

            