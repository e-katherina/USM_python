from typing import *
import numpy as np


class Calcule:
    def consecutive(l: List[int]) -> int:
        n_arr = []
        i, n = 0, 0
        for i in range(len(l) - 1):
            if l[i] == l[i + 1]:
                n += 1
            else:
                n_arr.append(n)
                n = 0
        return max(n_arr) + 1

    def suma(n: int) -> int:
        """
        Calculate sum of sequence: 1,2,3,3,3,4,5,5,5,5,5,6,7,7,7,7,7,7,7,8,9,9...
        :param n:
        :return: sum of first n elements
        """
        a = (np.sqrt(1 + 4 * n) - 1) / 2
        even, odd = int(a), int(a)
        s = even * (even + 1)
        s += odd * (4 * odd ** 2 - 1) / 3
        if not a.is_integer():
            s += (n - even - odd ** 2) * (2 * even + 1)
        return s
