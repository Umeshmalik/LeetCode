class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        sl, ft, ch, num = 1, 1, 1, arr[0]
        while ft < len(arr):
            if arr[ft] == num:
                ch += 1
                arr[sl] = arr[ft]
                sl += 1
                ft += 1
                if ch == 2 and ft < len(arr):
                    while ft < len(arr) and arr[ft] == num:
                        ft += 1
                    if ft == len(arr):
                        return sl
                    ch = 1
                    num = arr[ft]
                    arr[sl] = num
                    sl += 1
                    ft += 1
            else:
                ch = 1
                num = arr[ft]
                arr[sl] = num
                sl += 1
                ft += 1
        return sl