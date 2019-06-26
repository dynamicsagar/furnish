import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ViewRoom(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

