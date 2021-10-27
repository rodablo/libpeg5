from langkit.parsers import Grammar, Or, List, Pick, Opt, NoBacktrack, _  # , NoBacktrack as cut, Null

from langkit.dsl import T, ASTNode, Annotations, abstract, has_abstract_list, Field  # , synthetic

from langkit.expressions import (
    langkit_property, Self  # , Property
)

from peg5.language.lexer import Token, p5_lexer as L


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
    Expression
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

    todo: suffix as boolean (remember to desugar the expression)
    """
    pass


@abstract
class OperandNode(Peg5Node):
    """
    Abstract Base Operator Node.
    """
    pass


class PrefixOperandNode(OperandNode):
    """
    """
    enum_node = True
    alternatives = ['and', 'not']


class PrefixedNode(PrimaryNode):
    """
    Prefixed Primary Node.
    """
    prefix = Field(type=T.PrefixOperandNode)
    primary = Field(type=T.PrimaryNode)


class SuffixOperandNode(OperandNode):
    """
    .
    """
    enum_node = True
    alternatives = ['optional', 'zero_or_more', 'one_or_more']


class SuffixedNode(PrimaryNode):
    """
    Suffixed Primary Node.
    """
    primary = Field(type=T.PrimaryNode)
    suffix = Field(type=T.SuffixOperandNode)


class RefIdentifierNode(PrimaryNode):
    """
    .
    """
    token_node = True


class GroupNode(PrimaryNode):
    """
    Grouped Expression
    """
    expression = Field(type=T.ExpressionNode)


class LiteralNode(PrimaryNode):
    """
    LiteralNode
    TODO: define this as a choice of CharNodes to allow escapes.
    """
    token_node = True
    #text=Field()


class CharNode(Peg5Node):
    """
    CharNode
    """
    # needs extension implementation
    @langkit_property(return_type=T.Character, external=True, public=True,
                      uses_entity_info=False, uses_envs=False)
    def denoted_value():
        """
        Return the value that this literal denotes.
        """
        pass
    #char = Field()
    #token_node = True
    pass


@abstract
class RangeNode(Peg5Node):
    """
    RangeNode.
    """
    pass


class UnaryRangeNode(RangeNode):
    """
    UnaryRangeNode
    """
    #token_node=True
    a = Field(type=T.CharNode)


class BinaryRangeNode(RangeNode):
    """
    BinaryRangeNode
    """
    #token_node=True
    a = Field(type=T.CharNode)
    b = Field(type=T.CharNode)
    pass


class CharClassNode(PrimaryNode):
    """
    CharClassNode
    """
    range = Field(type=T.RangeNode)
    pass


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


#@has_abstract_list
@abstract
class AbstractLiteral(PrimaryNode):
    pass


class QuotedLiteral(AbstractLiteral):
    """
    """
    #annotations = Annotations(repr_name="SQuote")
    token_node = True


class EscapedCharLiteral(AbstractLiteral):
    token_node = True



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
            list_cls=SequenceNode.list, 
            sep="/", 
            empty_valid=False
        )
    ),

    sequence=SequenceNode(
        List(
            G.prefixed,
            list_cls=PrimaryNode.list, 
            empty_valid=False
        )
    ),

    prefixed=Or(
        PrefixedNode(
            Or(
                PrefixOperandNode.alt_and("&"),
                PrefixOperandNode.alt_not("!")
            ),
            G.suffixed
        ),
        G.suffixed
    ),

    suffixed=Or(
        SuffixedNode(
            G.primary,
            Or(
                SuffixOperandNode.alt_optional("?"),
                SuffixOperandNode.alt_zero_or_more("*"),
                SuffixOperandNode.alt_one_or_more("+")
            ), #cut(),
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
            G.char_class,
            DotNode(".")#,
            #G.literal
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

    char_class=CharClassNode(
        Pick("[",  # cut
             G.range,
             "]"
             )
    ),

    char=CharNode(Or(Token.Char, L.Dot)),

    range=Or(
        BinaryRangeNode(G.char, "-", G.char),
        UnaryRangeNode(G.char)
    ),

    #comment = Pick(CommentNode(Token.Comment),Opt(L.NL)),

    nl=NLNode(L.NL),

    #literal=SingleQuoteLiteral(Token.Toto),
    

    literal=Pick(
        "'",
        Opt(
            List(
                Or(
                    QuotedLiteral(Token.NonEscapedChars),
                    EscapedCharLiteral(Token.Char)
                ),
                list_cls=PrimaryNode.list, 
                empty_valid=True
            )
        ),
        NoBacktrack(),
        "'"
    )
)
