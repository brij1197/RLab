""" Objective: Develop an algorithm, accompanied by unit tests, that fulfills the following
requirements:
1. The algorithm should be capable of searching a matrix (of dimensions m x n) for a
specified number. If the target number is found within the matrix, the algorithm should
return true; otherwise, it should return false.
2. The time complexity of the algorithm should be logarithmic, i.e., O(log(N)), or better.
3. The algorithm should accurately log its execution time in microseconds.
4. The matrix for this task has the following characteristics:
• Each row within the matrix is sorted in ascending order.
• The first number of each row is larger than the last number of the preceding row.
5. You may use any programming language and unit testing framework of your choice. """

import time

class MatrixSearch:
    def __init__(self,matrix):
        self.matrix=matrix
        self.execution_time=None
        
    def search(self, target):
        if not self.matrix or not self.matrix[0]:
            return False

        rows=len(self.matrix)
        columns=len(self.matrix[0])
        
        left,right=0,(rows*columns)-1
        
        start_time=time.time()
        while left<=right:
            mid=(left+right)//2
            mid_value=self.matrix[mid//columns][mid%columns]
            
            if(mid_value==target):
                self.execution_time=(time.time()-start_time)*1000
                return True
            elif (mid_value<target):
                left=mid+1
            else:
                right=mid-1
        
        self.execution_time=(time.time()-start_time)*1000
        return False

    def get_execution_time(self):
        return self.execution_time