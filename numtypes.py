#!/usr/bin/env python
# -*- coding: utf-8 -*-

import decimal
from fractions import Fraction

FLOATVAR = 1.0/10.0

DECIMALVAR = decimal.Decimal('0.1')

FRACTIONVAR = Fraction(1, 10)

DF_EQUALITY = DECIMALVAR == FRACTIONVAR

ARE_INEQUAL = FLOATVAR != DECIMALVAR != FRACTIONVAR