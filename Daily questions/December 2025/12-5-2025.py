class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        par = nums.pop() & 1
        for c in nums:
            par ^= (c & 1)
        return len(nums) * (par ^ 1)

# --- Simple tests consistent with repository style (print + assert) ---
if __name__ == "__main__":
    from typing import List
    import copy

    sol = Solution()
    test_cases = [
        # (nums, expected_output)
        ([1, 2, 3], 0),           # Odd total sum, cannot partition equally
        ([1, 2, 3, 4], 4),        # Even sum (10), can partition, returns n*1 = 4
        ([2, 2, 2, 2], 4),        # Even sum, all even, can partition, n*1 = 4
        ([1, 3, 5, 7], 0),        # All odd, sum is even, but split not possible for two equal sum (16/2=8, but all numbers odd)
        ([1, 1], 2),              # [1,1], sum=2, possible to partition, n*1 = 2
        ([2], 0),                 # Only one number, can't partition, output is 0
        ([1, 1, 1, 1], 4),        # [1,1,1,1], sum=4, can partition, n*1 = 4
        ([1, 2], 0),              # sum=3, odd, cannot partition, returns 0
        ([10000, 10000, 10000, 10000], 4), # All even, n*1 = 4
        ([1, 10000], 0),          # Odd+even=odd sum, cannot partition
    ]
    for i, (nums, expected) in enumerate(test_cases, 1):
        out = sol.countPartitions(copy.deepcopy(nums))
        print(f"Test {i}: countPartitions({nums}) -> {out}")
        assert out == expected
    print("All tests passed for countPartitions")