class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()

        r= ''.join(list(filter(lambda x: x.isalnum() == True, s)))
        R=r[::-1]

        return r == R
    s=input()
    print(isPalindrome(s,s))
