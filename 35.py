class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(arr, low, high, x): 
            if(high>=low): 
                mid=(high+low)//2
                if arr[mid]==x: 
                    return(mid)
                elif arr[mid]>x: 
                    return(binary_search(arr,low,mid-1,x))
                else: 
                    return(binary_search(arr, mid + 1, high, x)) 
            else:
                return(-1)
        def f(array,element):
            flag=0
            while(True):
                index=binary_search(array,0,len(array)-1,element)
                if(index!=-1):
                    return(index+flag)
                else:
                    if(element<array[-1]):
                        element=element+1
                    else:
                        flag=1
                        element=element-1
        return(f(nums,target))
