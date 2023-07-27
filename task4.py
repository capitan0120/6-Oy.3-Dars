class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 1
        for i in range(2, math.floor(num**0.5)+1):
            if(num % i == 0):
                s += i
                s += num//i

        if s == num and num != 1:
            return True
        return False