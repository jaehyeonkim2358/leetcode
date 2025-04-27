from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        mod_count = Counter([0])
        answer = 0
        prefix = 0
        for i in range(n):
            # 지금 숫자가 조건에 맞으면 누적합을 1 증가
            if nums[i] % modulo == k: prefix += 1

            # nums[i]를 오른쪽 끝으로 하는 subarray 중, interesting subarray의 개수를 answer에 더해준다.
            # 누적합이
            #   prefix - k인 것의 개수 +
            #   prefix - k - modulo인 것의 개수 +
            #   prefix - k - 2 * modulo인 것의 개수 +
            #   prefix - k - 3 * modulo인 것의 개수 + ..
            #
            # 즉, 누적합이 (prefix - k) % modulo인 숫자들의 개수 == nums[i]를 오른쪽 끝으로 갖는 interesting subarray의 개수이다.
            target_mod_prefix = (prefix - k) % modulo
            answer += mod_count[target_mod_prefix]

            # 마지막으로 prefix % modulo의 개수를 1 증가
            mod_count[prefix % modulo] += 1
        return answer
