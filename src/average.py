from typing import List


def find_average(numbers: List[int]) -> float:
    # raise NotImplementedError
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
