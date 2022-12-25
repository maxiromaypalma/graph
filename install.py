#!/usr/bin/env python3
import subprocess
from venv import create

create(".venv", with_pip=True)
subprocess.run(".venv/bin/python3 -m pip install -r requirements.txt".split(" "))