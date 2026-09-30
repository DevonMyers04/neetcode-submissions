class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_ones=0
        true_max=0
        for num in nums:
            if num==1:
                consecutive_ones+=1
                if true_max < consecutive_ones:
                     true_max=consecutive_ones
            else:
                consecutive_ones=0
        return true_max
        