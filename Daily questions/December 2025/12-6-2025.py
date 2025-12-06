class Solution:
    def countPartitions(self, nums, k):
        n=len(nums)
        MOD=10**9+7

        sum=[0]*(n+2)
        sum[1]=1

        qMax=deque()  
        qMin=deque() 

        l=0
        cnt=0

        for r, x in enumerate(nums):

            # max queue 
            while qMax and qMax[-1]<x:
                qMax.pop()
            qMax.append(x)

            # min queue 
            while qMin and qMin[-1]>x:
                qMin.pop()
            qMin.append(x)

            # shrink window
            while qMax[0]-qMin[0]>k:
                y=nums[l]
                if qMax[0]==y:
                    qMax.popleft()
                if qMin[0]==y:
                    qMin.popleft()
                l+=1

            #  update cnt & sum[r+2]
            cnt=(sum[r+1]-sum[l])%MOD
            sum[r+2]=(sum[r+1]+cnt)%MOD

        return cnt
        # INSERT_YOUR_CODE
if __name__ == "__main__":
    from collections import deque
    import copy
    
    sol = Solution()
    test_cases = [
        # (nums, k, expected_output)
        ([1,2,3], 2, 3),      # partitions are [1], [2], [3]; each partition difference <=2
        ([1,5,6,2], 3, 2),    # [5,6,2] diff = 4>3 so can't take as one, needs careful windowing
        ([1,3,6], 1, 0),      # no subarray of len>=2 with max-min <=1
        ([2,2,2], 0, 4),      # all partitions of [2], [2], [2] possible, sliding uniqueness
        ([1], 0, 1),          # single element = always one way as no window to split
        ([10,20,12,15], 10, 3), # needs careful windowing
        ([1,3,5,7], 2, 3),    # Each pair-only windows possible
        ([], 10, 0),          # empty array, no output
    ]
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        out = sol.countPartitions(copy.deepcopy(nums), k)
        print(f"Test {i}: countPartitions({nums}, {k}) -> {out}")
        assert out == expected, f"Failed on test {i}"
    print("All tests passed for countPartitions")