"""
Init for 'tests' python package
"""
import codecs

import colorama

codecs.register(
    lambda name: codecs.lookup("utf-8") if name == "cp65001" else None)

colorama.init()
