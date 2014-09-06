#!/usr/bin/env python
# -*- coding: utf-8 -*-

import decimal
from fractions import Fraction

floatvar = 1.0/10.0

decimalvar = decimal.Decimal('0.1')

fractionvar = Fraction(1, 10)

df_equality = decimalvar == fractionvar

are_inequal = floatvar != decimalvar != fractionvar