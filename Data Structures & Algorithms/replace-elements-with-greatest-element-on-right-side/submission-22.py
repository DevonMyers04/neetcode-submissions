class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far=-1
        saved_value=0
        for i in range(len(arr)-1,-1,-1):
            saved_value=arr[i]
            arr[i]=max_so_far

            max_so_far= max(max_so_far,saved_value)
            

            if i==len(arr)-1:
             arr[i]=-1


        return arr
        