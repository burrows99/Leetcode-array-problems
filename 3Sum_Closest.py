class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        a=list()
        b=list()
        for i in range(n):
            left=i+1
            right=n-1
            while(left<right):
                total=nums[i]+nums[left]+nums[right]
                if(total<target):
                    left=left+1
                    a.append(total)
                    b.append(abs(total-target))
                elif(total>target):
                    right=right-1
                    a.append(total)
                    b.append(abs(total-target))
                else:
                    return(total)
        x=b.index(min(b))
        return(a[x])
