from langkit.parsers import (
    Grammar, Or, List, Pick, Opt, NoBacktrack,
    #_, Skip,  # , NoBacktrack as cut, Null
)

from langkit.dsl import (
    T, ASTNode, Annotations, Field,
    abstract, has_abstract_list, synthetic
)

from langkit.expressions import (
    langkit_property, Self  # , Property
)

from langkit.envs import (
    EnvSpec, add_to_env_kv
)

from peg5.language.lexer import Token, p5_lexer as L

#
GROUP_AS_EXPRESSION = True


#
@abstract
class Peg5Node(ASTNode):
    """
    Root class for Peg5 nodes.
    """
    #dummy = Property(Self.match(lambda j=T.Peg5: 2323))
    pass


#class Peg5Grammar(Peg5Node):
#    """
#    Root Peg5 Grammar Node.
#    """
#    definitions = Field(type=T.Definition.list)
#
#    @langkit_property(return_type=T.Int, public=True)
#    def n_def():
#        """
#        Return the number of definitions in this grammar
#        """
#        return Self.definitions.length
#
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


@has_abstract_list
class Definition(Peg5Node):
    """
    Definition
    """
    id = Field(type=T.Identifier)
    #expression = Field(type=T.ExpressionAsList)
    expression = Field(type=T.Expression)
    #expression = Field(type=T.Sequence.list)

    #doc = Field(type=T.CommentNode)
    env_spec = EnvSpec(
        add_to_env_kv(Self.id.sym, Self)
    )
    pass


class Definitions(Definition.list):

    annotations = Annotations(repr_name="Grammar")

    @langkit_property(return_type=T.Int, public=True)
    def n_dummy():
        """
        Return the number of definitions in this grammar
        """
        return Self.length


class Identifier(Peg5Node):
    """
    Identifier.
    """
    annotations = Annotations(repr_name="IdDef")

    token_node = True

    @langkit_property(return_type=T.Symbol, public=True)
    def sym():
        """
        Return the symbol for this identifier.
        """
        return Self.symbol


@abstract
@has_abstract_list
class AbstractPrimary(Peg5Node):
    """
    AbstractPrimary: Base for...
    TODO: suffix as boolean (remember to desugar the expression)
    """
    pass


# this way i suspect is how implement the specialized list
# this class replace sequence
@has_abstract_list
class PrimaryList(AbstractPrimary.list):
    annotations = Annotations(repr_name="Primaries")
    pass

#class ExpressionAsList(PrimaryList.list):
#    annotations = Annotations(repr_name="Expression")

#
#class ExpressionAsList(AbstractPrimary.list):
#    annotations = Annotations(repr_name="ExpressionAsList")
#    pass
#

# TODO: making Expression subclass abstractPrimary make it composite
# and make Group redundant
class Expression(AbstractPrimary):
    """
    Expression
    """
    choices = Field(type=T.Choices)


@has_abstract_list
class Sequence(Peg5Node):
    """
    Sequence (also Alternative)
    """
    primaries = Field(type=T.PrimaryList)
    pass


class Choices(Sequence.list):
    annotations = Annotations(repr_name="Choices")


@abstract
class AbstractOperator(Peg5Node):
    """
    AbstractOperator Node.
    """
    pass


class PrefixOperator(AbstractOperator):
    """
    """
    enum_node = True
    alternatives = ['and', 'not']


class PrefixedPrimary(AbstractPrimary):
    """
    PrefixedPrimary Node.
    """
    prefix = Field(type=T.PrefixOperator)
    primary = Field(type=T.AbstractPrimary)


class SuffixOperator(AbstractOperator):
    """
    """
    enum_node = True
    alternatives = ['optional', 'zero_or_more', 'one_or_more']


class SuffixedPrimary(AbstractPrimary):
    """
    SuffixedPrimary Node.
    """
    primary = Field(type=T.AbstractPrimary)
    suffix = Field(type=T.SuffixOperator)


class IdentifierReference(AbstractPrimary):
    """
    """
    annotations = Annotations(repr_name="IdRef")

    token_node = True


#class Group(AbstractPrimary):
#    """
#    Grouped Expression
#    """
#    expression = Field(type=(T.Expression if GROUP_AS_EXPRESSION else T.Sequence.list))


@abstract
class AbstractClass(AbstractPrimary):
    """
    Char Class Base.
    """
    token_node = True


class UnaryClass(AbstractClass):
    """
    UnaryClass
    """
    #a = Field(type=T.AbstractChar)
    pass


class BinaryClass(AbstractClass):
    """
    BinaryClass
    """
    #a = Field(type=T.AbstractChar)
    #b = Field(type=T.AbstractChar)
    pass

#@synthetic
#class Range(BaseTypeDecl):
#    pass
#class CharClassNode(AbstractPrimary):
#    """
#    CharClassNode
#    """
#    range = Field(type=T.RangeNode)
#    pass


class Dot(AbstractPrimary):
    pass
    #token_node = True


#
##@has_abstract_list
#@abstract
#class AbstractLiteral(AbstractPrimary):
#    pass
#


class Literal(AbstractPrimary):
    """
    Literal
    """
    token_node = True


#class Literal(AbstractLiteral):
#    pass
#    literals = Field(type=T.AbstractChar.list)


#class NonEscapedLiteral(AbstractLiteral):
#    token_node = True
#
#
#class EscapedCharLiteral(AbstractLiteral):
#    escaped_char = Field(type=CharNode)


# class CommentNode(P5Node):
#    """
#    TODO: transform this in a document node
#    """
#    pass
#    #text = Field()

@abstract
class AbstractChar(Peg5Node):
    token_node = True
    pass


@synthetic
class CharNode(AbstractChar):
    """
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
    pass


p5_grammar = Grammar(main_rule_name='definitions')
G = p5_grammar

p5_grammar.add_rules(

    # main_rule=List(Identifier(L.Identifier(match_text="first")),
    #               empty_valid=True),

    #definitions=Peg5Grammar(
    #    List(
    #        G.definition,
    #        list_cls=T.Definition.list,
    #        empty_valid=True
    #    ),
    #    L.Termination
    #),
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
        list_cls=T.Choices,
        sep="/",
        empty_valid=False
    ),

    sequence=Sequence(
        List(
            G.prefixed,
            list_cls=T.PrimaryList,
            empty_valid=False
        )
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
        #G.group,
        Pick(
            "(",
            NoBacktrack(),
            G.expression if GROUP_AS_EXPRESSION else G.choices,
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

    #range=Or(
    #    BinaryRangeNode(G.char, "-", G.char),
    #    UnaryRangeNode(G.char)
    #),

    #nl=NLNode(L.NL),

    literal=Literal(Token.Literal),

    #char=CharNode(Token.Char),

    #comment = Pick(CommentNode(Token.Comment),Opt(L.NL)),
)
