#!/usr/bin/env python
#Exercise 1

import sys

for line in sys.stdin:

    data = line.strip().split("\t")

    date, time, item, category, sales, payment = data
#changed from payment to category
    sys.stdout.write("{0}\t{1}\n".format(category, sales))
