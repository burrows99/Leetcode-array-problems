class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=list()
        Ans=list()
        nums.sort()
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            else:
                left=i+1
                right=len(nums)-1
                while(left<right):
                    total=nums[i]+nums[left]+nums[right]
                    if(total==0):
                        ans.append([nums[i],nums[left],nums[right]])
                        left=left+1
                        right=right-1
                    else:
                        if(total<0):
                            left=left+1
                        else:
                            right=right-1
        for i in ans:
            if(i not in Ans):
                Ans.append(i)
        return(Ans)
