class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [1,1,1,2,2,3]
        ->[(1),1,1,2,2,3], cnt+1 <= LIMIT -> cnt=1, num=prev_num=1, swap ptr1 vs i
        ->[1,(1),1,2,2,3], cnt+1 <= LIMIT -> cnt=2, num=prev_num=1, swap ptr1 vs i (resulting in same num)
        ->[1,1,(1),2,2,3], cnt+1 > LIMIT, num=prev_num=1
            --> increase i until num(2) != prev_num(1) --> swap ptr1 (2) vs i (3)
            --> ans += cnt, set cnt=1, prev_num = num (2)
            -->[1,1,(2, ptr1),(1, i),2,3]
        ->[1,1,2,(1, ptr1),(2, i),3], cnt+1 <= LIMIT -> cnt=2, num=prev_num=2, swap ptr1 vs i -> [1,1,2,(2),(1),3]
        ->[1,1,2,2,(1, ptr1),(3, i)], cnt=1, num!=prev_num, swap ptr1 vs i ->[1,1,2,2,(3),(1)]

        [0,0,1,1,1,1,2,3,3]
        ->[0,0,1,1,(2),1,(1),3,3]
        ->[0,0,1,1,2,(1),1,(3),3] (find next number and check valid)
        """
        n = len(nums)
        i = 1
        j = 1
        count = 1
        while i < n:
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    i += 1
                    continue
            else:
                count = 1

            nums[j] = nums[i]
            i+=1
            j+=1
        return j
