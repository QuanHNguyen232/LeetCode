class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt_plantable = 0
        for i, bed in enumerate(flowerbed):
            if bed == 1: continue
            can_left = False if (i-1>=0 and flowerbed[i-1] == 1) else True
            can_right = False if (i+1<len(flowerbed) and flowerbed[i+1] == 1) else True
            if can_left and can_right:
                cnt_plantable += 1
                flowerbed[i] = 1

        return cnt_plantable >= n