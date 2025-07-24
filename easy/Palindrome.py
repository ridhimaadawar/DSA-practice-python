class Solution:
    @staticmethod
    def isPalindrome(x):
        if x < 0:
            return False

        original = x
        reverse = 0

        while x != 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10

        return reverse == original

for n in [121, -121, 10]:
    print("{} → {}".format(n, Solution.isPalindrome(n)))
