import logging
import unittest
import sys
import time

from motionDetector import MotionDetector

logger = logging.getLogger("TestSwipe")
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

class TestSwipe(unittest.TestCase):

    def test_right_swipe(self):
        logger.info("Testing Right Swipe")
        md = MotionDetector("ZoeticRightSwipe")
        md.update([20, 20, 20, 2000, 20, 20])
        md.update([2000, 2000, 20, 20, 20, 20])
        md.update([20, 20, 20, 20, 2000, 20])
        del md

    def test_left_swipe(self):
        logger.info("Testing Left Swipe")
        md = MotionDetector("ZoeticLeftSwipe")
        md.update([20, 20, 20, 20, 2000, 20])
        md.update([2000, 2000, 20, 20, 20, 20])
        md.update([20, 20, 20, 2000, 20, 20])
        del md

    def test_delayed_swipe(self):
        logger.info("Testing Delayed Swipe")
        md = MotionDetector("ZoeticDelayedSwipe")
        md.update([20, 20, 20, 2000, 20, 20])
        time.sleep(0.5)
        md.update([2000, 2000, 20, 20, 20, 20])
        time.sleep(0.5)
        md.update([20, 20, 20, 20, 2000, 20])
        del md
        logger.info("\n\n")

    def test_right_swipe2(self):
        logger.info("Testing Right Swipe2")
        md = MotionDetector("ZoeticRightSwipe2")
        md.update([20, 20, 20, 2000, 20, 20])
        md.update([20, 20, 20, 2000, 20, 20])
        md.update([20, 20, 20, 2000, 20, 20])
        md.update([2000, 2000, 20, 20, 20, 20])
        md.update([2000, 2000, 20, 20, 20, 20])
        md.update([20, 20, 20, 20, 2000, 20])
        del md
