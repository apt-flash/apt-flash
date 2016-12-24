#!/usr/bin/env python3

import os
if os.geteuid() != 0:
    exit('This script requires root privileges.\nPlease try again with sudo.')

