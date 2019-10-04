import config
import logging
import sys
import time

from enum import Enum

class Buttons(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"

class Motions(Enum):
   Untouched = "Untouched"
   LightTouch = "LightTouch"
   FirmPress = "FirmPress"

#Right Swipes
RIGHT_SWIPES = [
    [[Buttons.D], [Buttons.A], [Buttons.E]],
    [[Buttons.D], [Buttons.B], [Buttons.E]],
    [[Buttons.D], [Buttons.C], [Buttons.E]],
    [[Buttons.D], [Buttons.A, Buttons.B], [Buttons.E]],
    [[Buttons.D], [Buttons.B, Buttons.C], [Buttons.E]],
    [[Buttons.D], [Buttons.A, Buttons.B, Buttons.C], [Buttons.E]],
]
#Left Swipes
LEFT_SWIPES = [
    [[Buttons.E], [Buttons.A], [Buttons.D]],
    [[Buttons.E], [Buttons.B], [Buttons.D]],
    [[Buttons.E], [Buttons.C], [Buttons.D]],
    [[Buttons.E], [Buttons.A, Buttons.B], [Buttons.D]],
    [[Buttons.E], [Buttons.B, Buttons.C], [Buttons.D]],
    [[Buttons.E], [Buttons.A, Buttons.B, Buttons.C], [Buttons.D]],
]

class MotionDetector(object):
    name = None
    prev_states = {}

    def __init__(self, name):
        self.prev_states = {}
        self.name = name
        self.logger = logging.getLogger('MotionDetector.' + name)

    @staticmethod
    def get_motions(touch_inputs):
        motions = []
        for t in touch_inputs:
            if t >= config.MIN_FIRM_TOUCH:
                motions.append(Motions.FirmPress)
            elif t >= config.MIN_LIGHT_TOUCH:
                motions.append(Motions.LightTouch)
            else:
                motions.append(Motions.Untouched)
        return motions

    @staticmethod
    def get_button(motions):
        buttons = []
        pressed_motions = [Motions.FirmPress, Motions.LightTouch]
        if motions[0] in pressed_motions:
            buttons.append(Buttons.A)
        if motions[1] in pressed_motions:
            buttons.append(Buttons.B)
        if motions[2] in pressed_motions:
            buttons.append(Buttons.C)
        if motions[3] in pressed_motions:
            buttons.append(Buttons.D)
        if motions[4] in pressed_motions:
            buttons.append(Buttons.E)
        if motions[5] in pressed_motions:
            buttons.append(Buttons.F)
        return buttons

    def update(self, touch_inputs):
        #Add current input to prev_states
        cur_time = time.time()
        cur_motions = MotionDetector.get_motions(touch_inputs)
        cur_buttons = MotionDetector.get_button(cur_motions)
        self.logger.info("Time: " + str(cur_time) + \
                         " Input:" + str(cur_buttons))
        self.prev_states[cur_time] = cur_buttons

        #Remove 1 sec old prev_states
        states_to_remove = []
        for t in self.prev_states:
            if t < (cur_time - 1):
                states_to_remove.append(t)
        for t in states_to_remove:
            del self.prev_states[t]

        self.logger.info("Prev States: " + str(self.prev_states))

        buttons = []
        for t in self.prev_states:
            if len(buttons):
                if buttons[-1] == self.prev_states[t]:
                    continue #Skip same consequetive states
            buttons.append(self.prev_states[t])
        self.logger.info("Buttons: " + str(buttons))
        self.check_swipe(buttons)

    def check_swipe(self, buttons):
        if buttons in RIGHT_SWIPES:
            self.logger.info("RIGHT SWIPE...\n\n")
            #Todo: raise Right Swipe Event.
        elif buttons in LEFT_SWIPES:
            self.logger.info("LEFT SWIPE...\n\n")
            #Todo: raise Left Swipe Event.
