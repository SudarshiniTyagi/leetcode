class FrogJump:
    def __init__(self, input_):
        self.input = input_
        self.input_size = len(input_)
        self.output = False
        self.last_position = input_[-1]
        print("Input is: " + str(input_))

    def can_jump(self):
        queue = []
        jumps = 0
        if 1 not in self.input:
            return False
        else:
            queue = [(1, 1)]
        while queue:
            ele = queue.pop()
            print("Checking for: " + str(ele))
            position = ele[0]
            steps_taken = ele[1]
            if steps_taken > 1:
                # Case 1: Steps 1 less than previous number of steps
                next_pos = position + steps_taken - 1
                if next_pos == self.last_position:
                    return True
                if next_pos in self.input:
                    queue.append((next_pos, steps_taken - 1))
            # Case 2: Steps same as previous number of steps
            next_pos = position + steps_taken
            if next_pos == self.last_position:
                return True
            if next_pos in self.input:
                queue.append((next_pos, steps_taken))
            # Case 3: Steps 1 more than previous number of steps
            next_pos = position + steps_taken + 1
            if next_pos == self.last_position:
                return True
            if next_pos in self.input:
                queue.append((next_pos, steps_taken + 1))
        return False


example_input_1 = FrogJump([0, 1, 3, 5, 6, 8, 12, 17])
print(example_input_1.can_jump())
print()
example_input_2 = FrogJump([0, 1, 2, 3, 4, 8, 9, 11])
print(example_input_2.can_jump())

