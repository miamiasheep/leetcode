"""
Time Complexity: O(N) : Because I have to scan the array one time

Space Complexity: O(N): Because I have to maintain the hashtable to checkout the last index

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
		# mapping is used to save the previous character (last index)
        mapping = {}
        ans = 0
		
		# start point
        i = 0
        
		for j in xrange(len(s)):
			"""
            if I can find previous charcter which is exctly the same 
			as current one: the start point should be the maxima
			of the last index of same charater or the last start point
			"""
			if s[j] in mapping:
                i = max(i, mapping[s[j]])
			# find the maxma
            ans = max(ans, j - i + 1)
			
            # save the mapping
			mapping[s[j]] = j + 1
        return ans