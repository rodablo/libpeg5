from helpers.grammar import do_parse_and_dump
import libpeg5lang as lp5l

SRC = u"""///"""
unit = do_parse_and_dump(SRC, lp5l.GrammarRule.expression_rule)
