class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        [1,1,1,1,2,1]
        map = {
            1: [0, 1, 2, 3, 5], total = 11
        }
        i=0 -> (0) + ((0-1)+(0-2)+(0-3)+(0-5)) = 0 + (0*4-sum(1,2,3,5))
        i=1 -> (1-0) + ((1-2)+(1-3)+(1-5)) = 1 + (1*3-sum(2,3,5))
        i=2 -> ((2-0)+(2-1)) + ((2-3)+(2-5)) = (2*2-sum(0,1)) + (2*2-sum(3,5))
        i=3 -> ((3-0)+(3-1)+(3-2)) + (3-5) = (3*3-sum(0,1,2)) + (3*1-sum(5))
        i=5 -> ((5-0)+(5-1)+(5-2)+(5-3)) + (0) = (5*4-sum(0,1,2,3)) + 0
        ==> Pattern: prefix sum
        i=idx -> left + right = (idx*cnt_left-sum_left) + (idx*cnt_right-sum_right)
        """
        n = len(nums)
        arr = [0]*n
        hashmap = defaultdict(list)

        for i, num in enumerate(nums):
            hashmap[num].append(i)

        for num in hashmap.keys():
            idx_list = hashmap[num]

            cnt_left, sum_left = 0, 0
            cnt_right, sum_right = len(idx_list), sum(idx_list)
            for j, idx in enumerate(idx_list):
                cnt_right -= 1
                sum_right -= idx
                
                left = abs(idx*cnt_left - sum_left)
                right = abs(idx*cnt_right - sum_right)
                arr[idx] = left + right

                cnt_left += 1
                sum_left += idx
                

        return arr