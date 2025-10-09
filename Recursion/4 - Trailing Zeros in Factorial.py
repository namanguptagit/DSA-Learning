class Solution:
    def trailingZeroes(self, n: int) -> int:
        countOfZero = 0
        powerOfFive = 5

        while n//powerOfFive:
            countOfZero+=n//powerOfFive
            powerOfFive*=5

        return countOfZero