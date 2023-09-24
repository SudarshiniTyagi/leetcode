class AddTwoNumbers:
    def __init__(self, input_1, input_2):
        self.input_1 = input_1
        self.input_2 = input_2
        self.size_input_1 = len(self.input_1)
        self.size_input_2 = len(self.input_2)
        self.output = []
        print("Input Number One is: " + str(self.input_1))
        print("Input Number Two is: " + str(self.input_2))

    def add_two_numbers(self):
        carry, i, j = 0, 0, 0
        while i < self.size_input_1 or j < self.size_input_2:
            input_1 = 0 if i >= self.size_input_1 else self.input_1[i]
            input_2 = 0 if j >= self.size_input_2 else self.input_2[j]
            sum_of_digits = input_1 + input_2 + carry
            output_digit = sum_of_digits % 10
            carry = sum_of_digits // 10
            self.output.append(output_digit)
            i = i + 1
            j = j + 1
        if carry > 0:
            self.output.append(carry)
        print("Output Number is: " + str(self.output) + "\n")
        return self.output


example_input_1 = AddTwoNumbers([2, 4, 3], [5, 6, 4])
example_input_1.add_two_numbers()

example_input_2 = AddTwoNumbers([0], [5, 6, 4])
example_input_2.add_two_numbers()

example_input_3 = AddTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
example_input_3.add_two_numbers()

example_input_4 = AddTwoNumbers([0], [0])
example_input_4.add_two_numbers()
