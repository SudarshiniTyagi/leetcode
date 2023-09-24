class TwoSum:
    input = []
    target = 0
    size_input = 0

    def __init__(self, input_data, target_number):
        self.input = input_data
        self.target = target_number
        self.size_input = len(input_data)
        print("Input Data is: " + str(self.input))
        print("Target is: " + str(self.target))
        print("Size Input is: " + str(self.size_input))

    def get_two_sum(self):
        # implement solution here
        i,j = 0,0
        while (i<self.size_input):
            j = i + 1
            while (j<self.size_input):
                if (self.input[i]+self.input[j]==self.target):
                    return [i,j]
                else:
                    j = j+1
            i=i+1



example = TwoSum([2, 7, 11, 15], 9)
output = example.get_two_sum()
print("Output is: "+str(output)+"\n\n")

example2 = TwoSum([3,2,4], 6)
output2 = example2.get_two_sum()
print("Output is: "+str(output2)+"\n\n")

example3 = TwoSum([3,3], 6)
output3 = example3.get_two_sum()
print("Output is: "+str(output3)+"\n\n")
