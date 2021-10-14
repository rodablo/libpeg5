from helpers.grammar import do_parse_and_dump

SRC = u"""TemplType <- PrimType (LANGLE TemplType RANGLE)?

ShiftExpr <- PrimExpr (ShiftOper PrimExpr)*

ShiftOper <- LSHIFT / RSHIFT

LANGLE <- '<' Spacing

RANGLE <- '>' Spacing

LSHIFT <- '<<' Spacing

RSHIFT <- '>>' Spacing

"""

unit = do_parse_and_dump(SRC)
