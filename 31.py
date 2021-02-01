class Solution:
    def nextPermutation(self, array: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def get_index(array,n):
            i=n-1
            while(i-1>=0):
                if(array[i-1]<array[i]):
                    return(i-1)
                i=i-1
            return(-1)
        def greater(array,element,n):
            i=n-1
            while(i>=0):
                if(array[i]>element):
                    return(i)
                i=i-1
            return(-1)
        def swap(array,i,j):
            z=array[i]
            array[i]=array[j]
            array[j]=z
        def reverse_after_index(array,i,n):
            new_array=array[i+1:]
            new_array=new_array[::-1]
            for x in range(len(new_array)):
                array[x+i+1]=new_array[x]
        def check_decreasing(array,n):
            i=0
            while(i+1<n):
                if(array[i]>=array[i+1]):
                    pass
                else:
                    return(0)
                i=i+1
            return(1)
        def f(array):
            n=len(array)
            status=check_decreasing(array,n)
            if(status==1):
                array.sort()
                return(array)
            i=get_index(array,n)
            g=greater(array,array[i],n)
            swap(array,i,g)
            reverse_after_index(array,i,n)
        return(f(array))
