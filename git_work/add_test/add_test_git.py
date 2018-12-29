import unittest
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handle = logging.FileHandler()
logging.Formatter()
logger.addHandler(file_handle)


file_handle.close()
logger.removeHandler(file_handle)
