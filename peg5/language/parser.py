from peg5.language.ast import (
    Definition, Definitions,
    Label, LabelReference,
    Expression, ExpressionList, SequenceList,
    PrefixedPrimary, Prefix, SuffixedPrimary, Suffix,
    UnaryClass, BinaryClass, Dot, Literal
)

from peg5.language.lexer import peg5_lexer as L

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
            list_cls=Definitions,
            empty_valid=True
        ),
        L.Termination
    ),

    definition=Definition(
        G.header,
        G.expression,
        Opt(";")
    ),

    header=Pick(
        G.label,
        NoBacktrack(),
        "<-"
    ),

    label=Label(
        L.Identifier
    ),

    expression=Expression(
        G.choices
    ),

    choices=List(
        G.sequence,
        list_cls=ExpressionList,
        sep="/",
        empty_valid=False
    ),

    sequence=List(
        G.prefixed,
        list_cls=SequenceList,
        empty_valid=False
    ),

    prefixed=Or(
        PrefixedPrimary(
            Or(
                Prefix.alt_and("&"),
                Prefix.alt_not("!")
            ),
            G.suffixed
        ),
        G.suffixed
    ),

    suffixed=Or(
        SuffixedPrimary(
            G.primary,
            Or(
                Suffix.alt_optional("?"),
                Suffix.alt_zero_or_more("*"),
                Suffix.alt_one_or_more("+")
            ),
        ),
        G.primary
    ),

    primary=Or(
        G.reference,
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

    reference=LabelReference(
        Label(L.Identifier)
    ),

    char_class=Or(
        UnaryClass(L.UnaryRangeClass),
        BinaryClass(L.BinaryRangeClass),
    ),

    literal=Literal(L.Literal),

    #char=CharNode(L.Char),
)
