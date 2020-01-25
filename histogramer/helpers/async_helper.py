"""
helps to work with async code
"""
import asyncio


def background(function):
    """
    run function in background
    :param function: function for running in background
    :return: wrapped function
    """

    def wrapped(*args, **kwargs):
        """
        run function using asyncio package
        :param args: args for "run_in_executor" interface implementation
        :param kwargs: kwargs for "run_in_executor" interface implementation
        :return: function (added to event loop) which will run in executor
        """
        return asyncio.get_event_loop().run_in_executor(None,
                                                        function,
                                                        *args,
                                                        *kwargs)

    return wrapped
