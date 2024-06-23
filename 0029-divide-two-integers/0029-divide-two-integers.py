class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if divisor == 0:
            raise ValueError("Divisor cannot be zero")
        if dividend == 0:
            return 0
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        quotient = -quotient if negative else quotient
        return max(MIN_INT, min(MAX_INT, quotient))
if __name__ == "__main__":
    solution = Solution()
    dividend = 10
    divisor = 3
    print(solution.divide(dividend, divisor))
    dividend = 7
    divisor = -3
    print(solution.divide(dividend, divisor))