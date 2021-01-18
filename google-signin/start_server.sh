#!/usr/bin/env bash

# Create a page in the current dir

# Start server
python3 -m http.server 5500 &> /dev/null &
pid=$!

# Give server time to start up
sleep 1

# request page and print to stdout
wget -O - http://0.0.0.0:5500/index.html 2> /dev/null

# Stop server
#kill "${pid}"

# Output on running script:
