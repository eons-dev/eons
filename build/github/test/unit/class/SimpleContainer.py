import sys, os, logging
import eons as e

class SimpleContainer(e.DataContainer):
    def __init__(this, name=e.INVALID_NAME()):
        logging.debug(f"init SimpleContainer")
        super().__init__(name)
