class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        def invert(bit):
            return bit ^ 1

        def flip(img):
            for row in img:
                l, r = 0, len(row)-1
                while l <= r:
                    # swap + invert
                    row[l], row[r] = invert(row[r]), invert(row[l])
                    l += 1
                    r -= 1
            return img

        return flip(image)