class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        i, j = 0, len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            biggest = max(biggest, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
            
        return biggest


        #i at start iterate till end
        #j at end iterate at start
        # stop both when they meet
        # keep comparing final output of both until biggest appears, until i and j meet