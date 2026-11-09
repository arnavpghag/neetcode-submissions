class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        max_freq = 0
        left = 0
        longest = 0

        for right in range(len(s)):

            # Update frequency of incoming character
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            # Update maximum frequency
            max_freq = max(max_freq, hash_map[s[right]])

            # Calculate replacements needed
            window_length = right - left + 1
            replacements = window_length - max_freq

            # Shrink window if invalid
            if replacements > k:
                hash_map[s[left]] -= 1
                left += 1

            # Update longest valid window
            longest = max(longest, right - left + 1)

        return longest