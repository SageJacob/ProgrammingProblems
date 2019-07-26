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
