class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #cant sort because O(n) is not the same as O(n) + O(nlogn)
        #two pointers, move inwards the pointer with smaller height
        curr_max = 0
        l, r = 0, len(heights) - 1
        while l < r:
            val = (r - l) * min(heights[l], heights[r])

            if  val > curr_max:
                curr_max = val
                continue
            
            elif heights[l] < heights[r]:
                l += 1
            
            elif heights[l] > heights[r]:
                r -= 1

            elif heights[l] == heights[r]:
                l += 1
                r -= 1
            
        
        return curr_max

