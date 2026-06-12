class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        HashLen = 256 

        hash = [-1] * HashLen
        for i in range(HashLen):
            hash[i] = -1

        l, r, maxLen = 0, 0, 0
        while r < n:
            """ If current character s[r] 
                is already in the substring """
            if hash[ord(s[r])] != -1:
                """ Move left pointer to the right
                    of the last occurrence of s[r] """
                l = max(hash[ord(s[r])] + 1, l)
            
            # Calculate the current substring length
            current_len = r - l + 1
            
            # Update maximum length found so far
            maxLen = max(current_len, maxLen)
            
            """ Store the index of the current
                character in the hash table """
            hash[ord(s[r])] = r
            
            # Move right pointer to next position
            r += 1
        
        # Return the maximum length found
        return maxLen


        