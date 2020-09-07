import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("GreenCartApp.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s",
                                     datefmt="%d/%m/%Y  %I:%M:%S %p")
        logger.addHandler(fileHandler)
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        return logger



