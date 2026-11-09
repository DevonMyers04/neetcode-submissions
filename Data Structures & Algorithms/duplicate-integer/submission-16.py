class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =[]
        for x in nums:
          print(x)
          if x in seen:
            return True
          else:
            seen.append(x)
            print(x)
        return False