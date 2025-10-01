# Trying Brute Force Approach first
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        my_set = set()
        for i in range (0,n):
            for j in range (i+1,n):
                for k in range (j+1,n):
                    if(nums[i]+nums[j]+nums[k] == 0):
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        my_set.add(tuple(temp))
        return [list(ans) for ans in my_set ]
# Time Complexity: O(n^3)
#A Better Approach will try to do it in O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        my_set = set()
        for i in range (0,n):
            check_set = set()
            for j in range (i+1,n):
                third = -(nums[i]+nums[j])
                if(third in check_set):
                    temp=[nums[i],nums[j],third]
                    temp.sort()
                    my_set.add(tuple(temp))
                check_set.add(nums[j])
        return [list(ans) for ans in my_set]

# Now a Better Approach 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range (n):
            if (i!=0 and nums[i] == nums[i-1]):
                continue
            j = i+1
            k = n-1
            while(j<k):
                total_sum = nums[i] +nums[j] +nums[k]
                if total_sum<0 :
                    j+=1
                elif total_sum>0 :
                    k-=1
                else : 
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return ans        