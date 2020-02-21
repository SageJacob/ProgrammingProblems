'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        Left = 0
        Right = len(height)-1
        maxArea = 0
        """
         Left -= 1 and Right += 1 because the max height has been reached for the current
         state of Left and Right. If the smaller height didn't change, any future values would
         result in a smaller area
        """
        while Left < Right:
            if height[Left] > height[Right]:
                tempArea = height[Right]*(Right-Left)
                Right -= 1
            else:
                tempArea = height[Left]*(Right-Left)
                Left += 1
            if tempArea > maxArea:
                maxArea = tempArea
        return maxArea
