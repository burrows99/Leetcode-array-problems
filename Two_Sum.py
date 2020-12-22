class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol=list()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]+nums[j]==target):
                    sol.append([i,j])
        if(len(sol)==1):
            return(sol[0])
        else:
            for i in sol:
                if(i[0]!=i[1]):
                    return(i)
