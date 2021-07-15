class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        
        temp = x
        y = 0
        ten = 10 ** int(math.log10(x))
        while temp:
            y += (temp % 10) * ten
            temp = temp // 10
            ten /= 10
        return x == y