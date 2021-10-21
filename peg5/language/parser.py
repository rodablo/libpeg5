from langkit.parsers import Grammar, Or, List, Pick, Opt, _  # , NoBacktrack as cut, Null

from langkit.dsl import T, ASTNode, abstract, Field  # , synthetic

from langkit.expressions import (
    langkit_property, Self  # , Property
)

from language.lexer import Token, p5_lexer as L


def ZeroOrMoreNewlinesHelper():
    return _(List(G.nl, empty_valid=True))


def ZeroOrOneNewlinesHelper():
    return _(Opt(G.nl))


def ZeroOrOneNewlinesOrTerminationHelper():
    return _(Opt(Or(G.nl, L.Termination)))


@abstract
class Peg5Node(ASTNode):
    """
    Root class for Peg5 AST nodes.
    """
    #toto = Property(Self.match(
    #    lambda j=T.Peg5Node: 2323
    #                           )
    #                )
    pass


class GrammarNode(Peg5Node):
    """
    Root grammar node.
    """
    definitions = Field(type=T.DefinitionNode.list)
#
#    #@langkit_property(return_type=T.Int, public=True)
#    #def n_def():
#    #    """
#    #    Return the number of definitions in a grammar
#    #    """
#    #    return Self.definitions.length
#    #
#    #@langkit_property(return_type=ParameterDecl, public=True)
#    #def find_parameter(name=T.String):
#    #    """
#    #    Return the parameter associated with the given name, if any.
#    #    """
#    #    return Self.parameters.find(lambda p: p.param_identifier.text == name)
#
#    #@langkit_property(return_type=SelectorExpr.list, public=True)
#    #def nth_expressions(n=(T.Int, 0)):
#    #    """
#    #    Return the selector expressions associated with the nth selector arm.
#    #    """
#    #    return Self.arms.at(n - 1).exprs_list


class DefinitionNode(Peg5Node):
    """
    Definition
    """
    id = Field(type=T.IdentifierNode)
    expression = Field(type=T.ExpressionNode)
    #doc = Field(type=T.CommentNode)
    pass


class IdentifierNode(Peg5Node):
    """
    Identifier.
    """
    token_node = True

    @langkit_property(return_type=T.Symbol, public=True)
    def sym():
        """
        Return the symbol for this identifier.
        """
        return Self.symbol


class ExpressionNode(Peg5Node):
    """
    Expression (also Pattern)
    """
    choices = Field(type=T.SequenceNode.list)


class SequenceNode(Peg5Node):
    """
    Sequence (also Alternative)
    """
    primaries = Field(type=T.PrimaryNode.list)
    pass


@abstract
class PrimaryNode(Peg5Node):
    """
    PrimaryNode: Base for...

    todo: suffix as boolean (remember desugaring the expression)
    """
    pass


@abstract
class OpNode(Peg5Node):
    """
    Base Op
    """
    pass


class PrefixOpNode(OpNode):
    """
    """
    enum_node = True
    alternatives = ['and', 'not']


class PrefixNode(PrimaryNode):
    """
    PrefixNode.
    """
    op = Field(type=T.PrefixOpNode)
    prefixed = Field(type=T.PrimaryNode)


class SuffixOpNode(OpNode):
    """
    .
    """
    enum_node = True
    alternatives = ['optional', 'zero_or_more', 'one_or_more']


class SuffixNode(PrimaryNode):
    """
    Base class for operators.
    """
    suffixed = Field(type=T.PrimaryNode)
    op = Field(type=T.SuffixOpNode)


class RefIdentifierNode(PrimaryNode):
    """
    .
    """
    token_node = True


class GroupNode(PrimaryNode):
    """
    GroupNode
    """
    expression = Field(type=T.ExpressionNode)


class LiteralNode(PrimaryNode):
    """
    .
    """
    token_node = True
    #text=Field()


class CharClassNode(PrimaryNode):
    """
    CharClassNode
    """
    range = Field()
    pass


class RangeNode(Peg5Node):
    """
    RangeNode
    """
    #token_node=True
    pass

#
#class Char(P5Node):
#    """
#    char node
#    """
#    token_node=True
#


class DotNode(PrimaryNode):
    """
    .
    """
    token_node = True


class NLNode(PrimaryNode):
    """
    .
    """
    pass


# class CommentNode(P5Node):
#    """
#    TODO: transform this in a document node
#    """
#    pass
#    #text = Field()


p5_grammar = Grammar('main_rule')
G = p5_grammar

p5_grammar.add_rules(

    # main_rule=List(IdentifierNode(L.Identifier(match_text="first")),
    #               empty_valid=True),

    #main_rule=Or(
    #    #Pick(List(G.comment,empty_valid=False), L.Termination),
    #    Pick(G.definition, L.Termination),
    #    Pick(
    #        List(
    #            G.definition,
    #            list_cls=T.Definition.list, empty_valid=True
    #        ),
    #        L.Termination
    #    ),
    #    #Pick(G.comment, L.Termination)
    #),

    main_rule=GrammarNode(
        List(
            ZeroOrMoreNewlinesHelper(),
            G.definition,
            ZeroOrMoreNewlinesHelper(),
            list_cls=T.DefinitionNode.list,
            empty_valid=True
        ),
        L.Termination
    ),

    definition=DefinitionNode(
        G.identifier,  # (Token.DefIdentifier),
        "<-",
        G.expression,
        #ZeroOrOneNewlinesOrTerminationHelper(),
        L.NL  # TODO: this extra NL is cheating...
    ),

    identifier=IdentifierNode(Token.Identifier),

    expression=ExpressionNode(
        List(
            G.sequence,
            list_cls=SequenceNode.list, sep=L.Slash  # "/"
        )
    ),

    sequence=SequenceNode(
        List(
            G.prefix,
            list_cls=PrimaryNode.list, empty_valid=True
        )
    ),

    prefix=Or(
        PrefixNode(
            Or(
                PrefixOpNode.alt_and(L.And),  # "&"),
                PrefixOpNode.alt_not("!")
            ),
            G.suffix
        ),
        G.suffix
    ),

    suffix=Or(
        SuffixNode(
            G.primary,
            Or(
                SuffixOpNode.alt_optional("?"),
                SuffixOpNode.alt_zero_or_more("*"),
                SuffixOpNode.alt_one_or_more("+")
            )
        ),
        G.primary
    ),

    primary=Pick(
        #ZeroOrMoreNewlinesHelper(),
        Or(
            RefIdentifierNode(Token.Identifier),
            #Group(Pick("(",G.expression,")")),
            G.group,
            LiteralNode(Token.Literal),
            CharClassNode(Pick("[", G.range, "]")),
            DotNode(".")
        ),
        ZeroOrOneNewlinesHelper(),
    ),

    # TODO: ZeroOrMoreNewlinesHelper here breaks the unparser generator
    group=GroupNode(
        Pick("(",
             ZeroOrMoreNewlinesHelper(),
             G.expression,
             ZeroOrMoreNewlinesHelper(),
             ")"
             )
    ),

    #char = CharNode(Token.Char),

    range=Or(
        RangeNode(Pick(Token.Char, "-", Token.Char)),
        RangeNode(Token.Char)
    ),

    #comment = Pick(CommentNode(Token.Comment),Opt(L.NL)),

    nl=NLNode(L.NL)

)
