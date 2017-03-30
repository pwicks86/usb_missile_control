#!/usr/bin/python

# Copyright 2017, Paul Wicks
# Copyright 2012, Nathan Milford

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import time
import usb.core


class MissileLauncher():
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x2123, idProduct=0x1010)
        if self.dev is None:
            raise ValueError('Launcher not found.')
        if self.dev.is_kernel_driver_active(0) is True:
            self.dev.detach_kernel_driver(0)
        self.dev.set_configuration()

    def turret_up(self):
        self.dev.ctrl_transfer(
            0x21, 0x09, 0, 0, [0x02, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    def turret_down(self):
        self.dev.ctrl_transfer(
            0x21, 0x09, 0, 0, [0x02, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    def turret_left(self):
        self.dev.ctrl_transfer(
          0x21, 0x09, 0, 0, [0x02, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    def turret_right(self):
        self.dev.ctrl_transfer(
            0x21, 0x09, 0, 0, [0x02, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    def turret_stop(self):
        self.dev.ctrl_transfer(
            0x21, 0x09, 0, 0, [0x02, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    def turret_fire(self):
        self.dev.ctrl_transfer(
            0x21, 0x09, 0, 0, [0x02, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])


def basic_missile_test():
    from pynput import keyboard
    launcher = MissileLauncher()

    last_movement_dir = None

    def on_press(key):
        nonlocal last_movement_dir
        if key == keyboard.Key.up:
            last_movement_dir = key
            launcher.turret_up()
        if key == keyboard.Key.down:
            last_movement_dir = key
            launcher.turret_down()
        if key == keyboard.Key.left:
            last_movement_dir = key
            launcher.turret_left()
        if key == keyboard.Key.right:
            last_movement_dir = key
            launcher.turret_right()
        if key == keyboard.Key.space:
            launcher.turret_fire()

    def on_release(key):
        if key == last_movement_dir:
            launcher.turret_stop()
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    basic_missile_test()
