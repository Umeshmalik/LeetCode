class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, k in enumerate(flowerbed):
            if i == 0:
                if k == 0 and (len(flowerbed) == 1 or flowerbed[i+1] == 0):
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if k == 0 and flowerbed[i-1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        return True if n < 1 else False
                