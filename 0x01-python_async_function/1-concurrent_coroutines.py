#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n: takes in 2 int arguments
    (in this order): n and max_delay.
    """
    tasks = (wait_random(max_delay) for i in range(n))
    lst = await asyncio.gather(*tasks)
    return sorted(lst)
