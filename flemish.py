#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
FIND_SPAN = FISHY.index("Spanish")
LEN_OF_SPAN = len("Spanish")
FLEMISH = (FISHY[0:FIND_SPAN] + "Flemish" + FISHY[(FIND_SPAN+LEN_OF_SPAN)::])