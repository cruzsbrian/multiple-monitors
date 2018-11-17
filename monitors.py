#!/usr/bin/env python

import subprocess
import re

operatorToArg = {
        "=": "--same-as",
        ">": "--right-of",
        "<": "--left-of",
        "^": "--above",
        "V": "--below",
        }

oppositeOperator = {
        "=": "--same-as",
        ">": "--left-of",
        "<": "--right-of",
        "^": "--below",
        "V": "--above",
        }

# get xrandr output as list of lines
xrandrList = subprocess.check_output(["xrandr"]).decode("utf-8").split('\n')

# filter into a list of monitor names (every line that contains ' connected')
monitors = [
        line.split(' ')[0]
        for line in xrandrList
        if " connected" in line
        ]

# for quick testing
#monitors = ['M0', 'M1', 'M2', 'M3']

# print a numbered list of monitors
for i in range(len(monitors)):
    print(i, monitors[i])

config = input()

cmd = ["xrandr"]

enabled = []

# find all pairs of monitor-operator-monitor (number, operator, number)
pairs = re.findall(r'(?=(\d+[=<>^V]\d+))', config)

for p in pairs:
    # get the two relevant monitors and the operator
    m1, m2 = [monitors[int(m)] for m in re.split('[=<>^V]', p)]
    op = re.search('[=<>^V]', p).group()

    if m1 not in enabled:
        cmd += ["--output", m1, "--auto"]
        enabled.append(m1)

        if m2 in enabled:
            cmd += [oppositeOperator.get(op), m2]

    if m2 not in enabled:
        cmd += ["--output", m2, "--auto"]
        cmd += [operatorToArg.get(op), m1]
        enabled.append(m2)

for m in monitors:
    if m not in enabled:
        cmd += ["--output", m, "--off"]

#print(' '.join(cmd))
subprocess.run(cmd)
