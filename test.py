from solution import Solution

def testcase01():
    # Input: 123
    return 123

def testcase02():
    # Input: -123
    return -123

def testcase03():
    # Input: 120
    return 120

def testcase04():
    # Input: 1534236469
    return 1534236469


if __name__ == '__main__':
    
    in_int = testcase03()
    sol = Solution()
    print(sol.reverse(in_int))

