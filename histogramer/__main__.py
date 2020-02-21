"""
Run histogramer.
"""
import asyncio

from histogramer.src.helpers.args_helper import get_arguments
from histogramer.src.helpers.log_helper import init_logger
from histogramer.src.histogram import build_histogram, process_data


async def main():
    """
    Run Histogrammer.
    :return: None
    """
    arguments = await get_arguments()
    logger = await init_logger(folder_name=".logs", root_path=arguments.log)
    words_count = await process_data("*.txt", logger, arguments.path)
    await build_histogram(logger, words_count)


{"__main__": lambda: asyncio.run(main())}.get(__name__, lambda: None)()
