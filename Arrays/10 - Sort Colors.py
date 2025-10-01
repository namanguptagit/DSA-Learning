class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        x,y,z = 0,0,n-1
        while(y<=z):
            if nums[y] == 0:
                nums[x], nums[y] = nums[y], nums[x]
                x+=1
                y+=1
            elif nums[y] == 1:
                y+=1
            elif nums[y] == 2:
                nums[y], nums[z] = nums[z], nums[y]
                z-=1
