#!/bin/bash

# Generate the site
python /Users/sarahlampkin/documents/MyWebProject/src/main.py

# Start a simple web server
python /Users/sarahlampkin/documents/MyWebProject/server.py --dir /Users/sarahlampkin/documents/MyWebProject/public

# Exit the script
exit
