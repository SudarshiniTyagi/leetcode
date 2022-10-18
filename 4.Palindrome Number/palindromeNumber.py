class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        xString = str(x)
        xLength = len(xString)
        i = 0
        j = xLength-1
        while (i<= j):
            if xString[i] == xString[j]:
                i = i+1
                j = j-1
            else:
                return False
        return True


def main():
    good_number = 121
    print(str(good_number) + ": " + str(Solution.isPalindrome(good_number)))
    bad_number = -121
    print(str(bad_number) + ": " + str(Solution.isPalindrome(bad_number)))



if __name__ == "__main__":
    main()
