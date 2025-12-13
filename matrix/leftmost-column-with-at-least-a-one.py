# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        nrows, ncols = binaryMatrix.dimensions()

        def is_target_col(col) -> bool:
            for row in range(nrows):
                val = binaryMatrix.get(row, col)
                if val == 1:
                    return True
            return False
        
        # left-bound binary search
        left = 0
        right = ncols - 1
        while left < right:
            mid = left + (right-left)//2
            if is_target_col(mid):
                right = mid
            else:
                left = mid+1
        
        # post-process
        if is_target_col(left):
            return left
        return -1