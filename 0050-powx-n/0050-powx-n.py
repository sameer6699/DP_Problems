class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        half_pow = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half_pow * half_pow
        else:
            return half_pow * half_pow * x

if __name__ == "__main__":
    solution = Solution()
    x1 = 2.00000
    n1 = 10
    print(f"pow({x1}, {n1}) = {solution.myPow(x1, n1):.5f}")
    x2 = 2.10000
    n2 = 3
    print(f"pow({x2}, {n2}) = {solution.myPow(x2, n2):.5f}")
    x3 = 2.00000
    n3 = -2
    print(f"pow({x3}, {n3}) = {solution.myPow(x3, n3):.5f}")  