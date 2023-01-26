from Stack import Stack
from typing import List


class Bot:
    def __init__(self) -> None:
        self._data_items = Stack()

    def A(self) -> None:
        # Getting the top two integers from stack
        int1 = self._data_items.pop()
        int2 = self._data_items.top()

        # Putting the top integer back on to maintain correct positioning
        self._data_items.push(int1)

        # Sum of top two integers in stack
        sum = int1 + int2

        # Adding sum of top integers to stack
        self._data_items.push(sum)

    def T(self) -> None:
        # The top item in the stack
        prev = self._data_items.top()

        # Finding the triple the value of the top integer
        res = prev * 3

        # Adding result to top of stack
        self._data_items.push(res)

    def D(self) -> None:
        # Deleting previous integer value from stack
        self._data_items.pop()

    def I(self, num: int) -> None:
        # Adds num to top of stack
        self._data_items.push(num)

    def read_input(self, inpt_str: List[str]) -> List[int]:
        # Performing operation for each input in input string
        for inpt in inpt_str:
            if inpt == 'A':
                self.A()
            elif inpt == 'T':
                self.T()
            elif inpt == 'D':
                self.D()
            else:
                num = int(inpt)
                self.I(num)

        return self._data_items


string = ["10", "3", "D", "T", "A"]
bot = Bot()
print(bot.read_input(string))
