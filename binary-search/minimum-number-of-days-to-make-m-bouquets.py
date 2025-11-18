class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def get_count_bouquets(dayAt) -> int:
            cntBouquets = 0
            cntAdjFlowers = 0
            for d in bloomDay:
                if d <= dayAt:
                    cntAdjFlowers += 1
                else:
                    cntBouquets += cntAdjFlowers // k
                    cntAdjFlowers = 0
            cntBouquets += cntAdjFlowers // k
            
            return cntBouquets
        
        left = 0
        right = max(bloomDay)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if get_count_bouquets(mid) >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans