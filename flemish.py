#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
find_spanish = FISHY.index("Spanish")
len_of_spanish = len("Spanish")
FLEMISH = FISHY[0:find_spanish] + "Flemish" + FISHY[(find_spanish+len_of_spanish):-1]