class Solution:
    def __init__(self, input_string):
        self.inputString = input_string
        self.compressedString = ""
        self.inputStringLength = len(self.inputString)

    def get_compressed_string(self):
        i = 0
        while i < self.inputStringLength:
            anchor = self.inputString[i]
            i = i + 1
            count = 1
            while i < self.inputStringLength and self.inputString[i] == anchor :
                count += 1
                i += 1
            if count > 2:
                self.compressedString = self.compressedString + anchor + str(count)
            else:
                self.compressedString = self.compressedString + anchor * count
        return self.compressedString


def get_compressed_string(string):
    print("String: {}".format(string))
    solution = Solution(string)
    print("Compressed String: {}".format(solution.get_compressed_string()))


def main():
    get_compressed_string("aabcccccqu")
    get_compressed_string("aAaaaaabbd")

if __name__ == "__main__":
    main()
