#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The cat must have slept on the keyboard!!!

Strip this terribly formatted string of its excess characters.
"""


nervous_as = """




 //////////A long-tailed cat in a room full of rockin' chairs.,,,,,,,,,, 





"""
nervous_as = nervous_as.strip().lstrip('/').rstrip(',')