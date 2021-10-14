from helpers.grammar import do_parse_and_dump

SRC = u"""
# some comment
aa <- bb

"""
unit = do_parse_and_dump(SRC)
