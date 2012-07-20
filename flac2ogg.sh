#!/bin/bash

find "$1" -type f -iname *.flac -print0 | xargs -n1 -0 -P 4 oggenc -b 320

find "$1" -type f -iname *.ogg -print0 | xargs -0 picard
