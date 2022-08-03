class Solution:
    def __init__(self, input_string_1, input_string_2):
        self.inputString1 = input_string_1
        self.inputString2 = input_string_2
        self.replaces = 0
        self.inserts = 0
        self.size_input1 = len(input_string_1)
        self.size_input2 = len(input_string_2)

    def is_one_away(self):
        if abs(self.size_input1 - self.size_input2) > 1:
            print("No way Jose!")
            return False
        if self.size_input1 == self.size_input2:
            print("oh good, this is easy")
            i = 0
            while i < self.size_input1:
                if self.inputString1[i] == self.inputString2[i]:
                    pass
                elif self.inputString1[i] != self.inputString2 and self.replaces == 0:
                    self.replaces += 1
                else:
                    return False
                i += 1
        else:
            print("Ho ho ho interesting, string lengths don't match")
            i = 0
            j = 0
            smaller_string = self.inputString1 if self.size_input1 < self.size_input2 else self.inputString2
            larger_string = self.inputString1 if self.size_input1 > self.size_input2 else self.inputString2
            while i < min(self.size_input1, self.size_input2):
                if smaller_string[i] == larger_string[j]:
                    pass
                else:
                    j += 1
                    if smaller_string[i] == larger_string[j] and self.inserts == 0:
                        self.inserts += 1
                    else:
                        return False
                i += 1
                j += 1
        return True

def check_is_one_away(string1, string2):
    print("String 1: {} \nString 2: {}".format(string1, string2))
    solution = Solution(string1, string2)
    print("Verdict: {}\n----------".format(str(solution.is_one_away())))

def main():
    check_is_one_away("pale", "ple")
    check_is_one_away("pales", "pale")
    check_is_one_away("pale", "bale")
    check_is_one_away("pale", "bake")
    check_is_one_away("lamp", "plum")
    check_is_one_away("pale", "plle")
    check_is_one_away("p", "b")
    check_is_one_away("p", "pa")
    check_is_one_away("", "b")
    check_is_one_away("", "ba")
    check_is_one_away("", "")
    check_is_one_away("happy", "happy")


if __name__ == "__main__":
    main()
