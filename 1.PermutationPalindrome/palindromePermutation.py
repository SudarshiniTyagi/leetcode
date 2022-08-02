class Solution:
    def __init__(self, input_string):
        self.inputString = input_string
        self.ledger = {}
        self.oddPresent = False

    def is_palindrome_permutation(self):
        for ele in self.inputString:
            ele = ele.lower()
            if ele == " ":
                continue
            if ele in self.ledger:
                self.ledger[ele] += 1
            else:
                self.ledger[ele] = 1
        for ele in self.ledger:
            if self.ledger[ele] % 2 == 0:
                continue
            elif self.ledger[ele] % 2 != 0 and not self.oddPresent:
                self.oddPresent = True
            else:
                return False
        return True


def main():
    good_string = "Taco cat"
    solution = Solution(good_string)
    print(good_string + ": " + str(solution.is_palindrome_permutation()))
    bad_string = "Princess"
    solution = Solution(bad_string)
    print(bad_string + ": " + str(solution.is_palindrome_permutation()))



if __name__ == "__main__":
    main()
