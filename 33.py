class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr, x): 
            low = 0
            high = len(arr) - 1
            mid = 0
            while low <= high:
                mid = (high + low) // 2
                if(arr[mid] < x): 
                    low = mid + 1
                elif(arr[mid] > x): 
                    high = mid - 1
                else: 
                    return(mid) 
            return(-1)
        def f(array,num):
            n=len(array)
            ind=array.index(min(array))
            a1=array[ind:]
            a2=array[:ind]
            if(a1[0]<=num<=a1[-1]):
                b=binary_search(a1,num)
                if(b==-1):
                    return(b)
                else:
                    return(ind+b)
            else:
                return(binary_search(a2,num))
        return(f(nums,target))
