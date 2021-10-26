#! /usr/bin/env sh
python3 manage.py make --library-types relocatable --debug --build-mode dev --verbosity debug --pretty-print $1 $2 $3 $4

#                            --pass-on "emit railroad diagrams"
#                            --library-types=static,static-pic,relocatable \

