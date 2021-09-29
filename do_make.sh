#! /usr/bin/env sh
python3 langkit/manage.py make --library-types static --debug --build-mode dev --verbosity debug --pretty-print --library-types=static,static-pic,relocatable --pass-on "emit railroad diagrams"

