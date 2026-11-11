class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_sum= []
        seen={}
        for i, x in enumerate(nums):
            need= target-x
            if need in seen:
                target_sum.append(seen[need])
                target_sum.append(i)
                return(target_sum)
            seen[x]=i


       