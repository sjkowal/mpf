""" Contains the base classes for standup targets and standup target banks."""
# standup.py
# Mission Pinball Framework
# Written by Brian Madden & Gabe Knuth
# Released under the MIT License. (See license info at the end of this file.)

# Documentation and more info at http://missionpinball.com/framework

import logging

from mpf.devices.target import Target, TargetGroup


class Standup(Target):
    """Represents a single drop target in a pinball machine."""

    config_section = 'Standups'
    collection = 'standups'

    def __init__(self, machine, name, config, collection=None):
        self.log = logging.getLogger('Standup.' + name)
        super(Standup, self).__init__(machine, name, config, collection)

        self.device_str = 'standup'


class StandupGroup(TargetGroup):
    """Represents a group of standup targets in a pinball machine by grouping
    together multiple Standup class devices.
    """

    config_section = 'StandupGroups'
    collection = 'standup_groups'

    def __init__(self, machine, name, config, collection=None):
        self.log = logging.getLogger('StandupGroup.' + name)
        self.devices_str = 'standups'
        self.member_collection = machine.standups
        super(StandupGroup, self).__init__(machine, name, config, collection)

# The MIT License (MIT)

# Copyright (c) 2013-2014 Brian Madden and Gabe Knuth

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
