"""
Histogramer main module.
"""
import asyncio

from histogramer.src.helpers.args_helper import parse_arguments
from histogramer.src.helpers.log_helper import init_logger
from histogramer.src.histogram import process_text_files, show_histogram


async def main():
    """
    Run Histogrammer.
    :return: None.
    """
    arguments = await parse_arguments()
    logger = await init_logger(folder_name=".logs", root_path=arguments.log)
    words_count = await process_text_files("*.txt", logger, arguments.path)
    await show_histogram(logger, words_count)


{"__main__": lambda: asyncio.run(main())}.get(__name__, lambda: None)()
