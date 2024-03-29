#!/usr/bin/env python3
'''module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Create a multiplier function.
    '''
    return lambda x: x * multiplier
