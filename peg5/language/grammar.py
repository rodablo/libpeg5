from peg5.language.ast import *

from langkit.dsl import (
    T
)

from peg5.language.lexer import (  # noqa: E402
    Token, peg5_lexer as L
)

# From libadalang/ada/grammar.py
# This import is after the language.ast import, because we want to be sure
# no class from langkit.expressions are shadowing the parser combinators.
from langkit.parsers import (  # noqa: E402
    Grammar, Or, List, Pick, Opt, NoBacktrack,
    #_, Skip,  # , NoBacktrack as cut, Null
)

peg5_grammar = Grammar(main_rule_name='definitions')
G = peg5_grammar

peg5_grammar.add_rules(

    # main_rule=List(Identifier(L.Identifier(match_text="first")),
    #               empty_valid=True),
    definitions=Pick(
        List(
            G.definition,
            list_cls=T.Definitions,
            empty_valid=True
        ),
        L.Termination
    ),

    definition=Definition(
        G.defining_id,
        G.expression,
        Opt(";")
    ),

    defining_id=Pick(
        G.identifier,
        NoBacktrack(),
        "<-"
    ),

    identifier=Identifier(
        Token.Identifier
    ),

    expression=Expression(
        G.choices
    ),

    choices=List(
        G.sequence,
        list_cls=T.ExpressionList,
        sep="/",
        empty_valid=False
    ),

    sequence=List(
        G.prefixed,
        list_cls=T.SequenceList,
        empty_valid=False
    ),

    prefixed=Or(
        PrefixedPrimary(
            Or(
                PrefixOperator.alt_and("&"),
                PrefixOperator.alt_not("!")
            ),
            G.suffixed
        ),
        G.suffixed
    ),

    suffixed=Or(
        SuffixedPrimary(
            G.primary,
            Or(
                SuffixOperator.alt_optional("?"),
                SuffixOperator.alt_zero_or_more("*"),
                SuffixOperator.alt_one_or_more("+")
            ),
        ),
        G.primary
    ),

    primary=Or(
        IdentifierReference(Token.Identifier),
        Pick(
            "(",
            NoBacktrack(),
            G.expression,
            ")"
        ),
        G.literal,
        G.char_class,
        Dot("."),
    ),

    char_class=Or(
        UnaryClass(L.UnaryRangeClass),
        BinaryClass(L.BinaryRangeClass),
    ),

    literal=Literal(Token.Literal),

    #char=CharNode(Token.Char),
)
