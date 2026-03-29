# TAGS: array,greedy

# Solution by counting number of zeros and handling edge cases

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return n == 0

        total = 0
        i = 0
        size = len(flowerbed)
        while i < size:
            while i < size and flowerbed[i] == 1:
                i += 1
            
            if i == size:
                break
            # i points to first 0
            j = i + 1
            while j < size and flowerbed[j] == 0:
                j += 1
            # j points to one past last 0
            num_zero = j - i
            can_place = (num_zero - 1) // 2
            if num_zero % 2 == 0 and (j == size or i == 0):
                can_place += 1
            elif num_zero % 2 == 1 and (j == size and i == 0):
                can_place += 1

            total += can_place

            i = j + 1

        return total >= n

# Solution with a single loop and actually planting the flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        for i in range(length):
            if flowerbed[i] == 1:
                continue

            left_ok = (i == 0 or flowerbed[i-1] == 0)
            right_ok = (i == length - 1 or flowerbed[i+1] == 0)
            if left_ok and right_ok:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
        
        return count >= n
