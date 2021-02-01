class Solution:
    def searchRange(self, array: List[int], e: int) -> List[int]:
        def bs(array,element):
            a=0
            b=len(array)-1
            mid=int((a+b)/2)
            while(a<b):
                if(element<array[mid]):
                    b=mid
                    mid=int((a+b)/2)
                elif(element>array[mid]):
                    a=mid+1
                    mid=int((a+b)/2)
                else:
                    return(mid)
            return(-1)
        def f(array,element):
            try:
                i=array.index(element)
            except:
                i=-1
            if(i==-1):
                return([-1,-1])
            else:
                x=i-1
                y=i+1
                ans=list()
                while(x>=0):
                    if(array[x]==element):
                        x=x-1
                    else:
                        break
                ans.append(x+1)
                while(y<len(array)):
                    if(array[y]==element):
                        y=y+1
                    else:
                        break
                ans.append(y-1)
                return(ans)
        return(f(array,e))
