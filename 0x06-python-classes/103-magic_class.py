#!/usr/bin/python3
class MagicClass:
    def __init__(self):
        self._MagicClass__radius = 0

import dis
dis.dis(MagicClass.__init__)
