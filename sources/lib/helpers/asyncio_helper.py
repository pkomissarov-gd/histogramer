"""
Helps to work with asyncio library.
"""
import asyncio


def sleep(seconds):
    """
    Wait N seconds. This way is more efficient than time.sleep(N).
    :param seconds: Seconds to sleep.
    :return: None.
    """
    asyncio.run(asyncio.sleep(seconds))
