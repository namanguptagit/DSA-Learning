class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        j , k = 0 , n-1
        pos = n-1
        while (j <= k):
            if abs(nums[j]) > abs(nums[k]):
                res[pos] = nums[j]*nums[j]
                j+=1
            else:
                res[pos] = nums[k]*nums[k]
                k-=1
            pos-=1
        return res