#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
FIND_SPANISH = FISHY.index("Spanish")
LEN_OF_SPANISH = len("Spanish")
FLEMISH = (FISHY[0:FIND_SPANISH] + "Flemish" + 
	FISHY[(FIND_SPANISH+LEN_OF_SPANISH)::])