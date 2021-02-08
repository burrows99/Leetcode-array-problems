class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        def one_traversal(mat,i,n,m):
            ans=list()
            c1=mat[i][m-i-1]
            c2=mat[n-i-1][m-i-1]
            c3=mat[n-i-1][i]
            for x in range(i,m-i-1):
                ans.append(mat[i][x])
            ans.append(c1)
            for x in range(i+1,n-i-1):
                ans.append(mat[x][m-i-1])
            ans.append(c2)
            for x in range(m-i-2,i,-1):
                ans.append(mat[n-i-1][x])
            ans.append(c3)
            for x in range(n-i-2,i,-1):
                ans.append(mat[x][i])
            return(ans)
        def f(mat):
            ans=list()
            n=len(mat)
            m=len(mat[0])
            i=min(int(n/2),int(m/2))
            for level in range(i+1):
                ans=ans+one_traversal(mat,level,n,m)
            return(ans[:n*m])
        return(f(mat))
