class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        i, j = 0, len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            biggest = max(biggest, area)
            if i == j:
                break
        return biggest


        #i at start iterate till end
        #j at end iterate at start
        # stop both when they meet
        # keep comparing final output of both until biggest appears, until i and j meet