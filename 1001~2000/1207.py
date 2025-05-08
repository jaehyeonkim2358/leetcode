class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}
        for n in arr:
            count_map[n] = count_map.get(n, 0) + 1
        reverse_count_map = {}
        for k, v in count_map.items():
            if v in reverse_count_map:
                return False
            else:
                reverse_count_map[v] = k

        return True
