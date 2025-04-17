class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        copied_flowerbed = [2] + flowerbed + [2]
        for i in range(1, len(copied_flowerbed) - 1):
            if n == 0: break
            if copied_flowerbed[i] == 1: continue
            if copied_flowerbed[i-1] != 1 and copied_flowerbed[i+1] != 1:
                copied_flowerbed[i] = 1
                n -= 1

        return True if n == 0 else False
