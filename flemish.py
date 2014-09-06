#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
fishy = inquisition.SPANISH.replace('surprise', 'haddock')
find_spanish = fishy.index("Spanish")
len_of_spanish = len("Spanish")
after_spanish = fishy[(find_spanish+len_of_spanish):-1]
flemish = fishy[0:find_spanish] + "Flemish" + after_spanish