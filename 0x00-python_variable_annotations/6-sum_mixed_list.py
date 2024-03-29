#!/usr/bin/env python3
'''module.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Compute the sum of a list of integers and float numbers.
    '''
    return float(sum(mxd_lst))
