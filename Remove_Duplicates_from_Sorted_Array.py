class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        #n=len(nums)
        while(i<len(nums)):
            try:
                if(nums[i]==nums[i+1]):
                    nums.pop(i+1)
                    i=0
                    continue
                i=i+1
            except:
                break
        return(len(nums))
