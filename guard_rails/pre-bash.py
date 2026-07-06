#!/usr/bin/env python3

import json
import sys

payload = json.load(sys.stdin)

command = payload["tool_input"]["command"]

if "push" in command:
    sys.exit(2)
    
