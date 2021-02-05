class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(mat)
        Mat=[[-1]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                Mat[i][j]=mat[n-1-j][i]
        for i in range(n):
            mat[i]=Mat[i]
