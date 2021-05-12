from typing import List


class NumData:
    def __init__(self):
        self.num_list = []

    def nums(self) -> List[int]:
        return self.num_list

    def add_num(self, num: int) -> None:
        self.num_list.append(num)


num_data = NumData()
