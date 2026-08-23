class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, res, maxF = 0, 0, 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0) # 0 by default
            maxF = max(maxF, count[s[right]])

            while ((right - left + 1) - maxF) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        