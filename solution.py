class Solution:
    def reverse(self, x: int) -> int:
        # remember the input value is minus or positive first
        minus = False
        if x < 0:
            minus = True
            # and initialize it as a positive number
            x = 0 - x
        # store the digit number of each position
        digits = []
        # store them from the lower place
        while True:
            if 1 > x and x > -1:
                break
            digits.append(int(x % 10))
            x = x / 10
        # the variable to summarize the result
        result = 0
        # list up the digits from the higher place
        for i in range(len(digits)):
            result = result + digits[-1 - i] * 10 ** i
        # add minus if the input number is minus
        if minus:
            result = 0 - result
        # by the problem assumption, "assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]"
        if result >= 2 ** 31 or -2 ** 31 > result:
            result = 0
            
        return result
