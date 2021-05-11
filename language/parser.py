from langkit.parsers import Grammar, Or, List, Pick, Opt, NoBacktrack as cut, Null, _

from langkit.dsl import T, ASTNode, abstract, Field, synthetic

from language.lexer import Token, p5_lexer as L

from langkit.expressions import (
    langkit_property, Self, Property
)


@abstract
class P5Node(ASTNode):
    """
    Root node class for Peg5 AST nodes.
    """
    toto = Property(Self.match(
        lambda j=T.P5Node: 2323
                               )
                    )
    pass

#class GrammarNode(P5Node):
#    """
#    Root grammar node.
#    """
#    definitions = Field()#type=T.DefinitionNode.list)
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


class Definition(P5Node):
    """
    Definition
    """
    id = Field(type=T.Identifier)
    expression = Field(type=T.Expression)
    #doc = Field(type=T.CommentNode)
    pass


class Identifier(P5Node):
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


class Expression(P5Node):
    """
    expression
    """
    #choices = Field(type=T.P5Node.list)
    choices = Field(type=T.Sequence.list)


class Sequence(P5Node):
    """
    sequence
    """
    primaries = Field(type=T.Primary.list)
    pass


@abstract
class Primary(P5Node):
    """
    Primary: Base for... 
    """
    pass


@abstract
class Op(P5Node):
    """
    Base Op
    """
    pass

class PrefixOp(Op):
    """
    .
    """
    enum_node = True
    alternatives = [ 'and', 'not' ]


class Prefix(Primary):
    """
    Prefix.
    """
    op=Field(type=T.PrefixOp)
    prefixed=Field(type=T.Primary)


class SuffixOp(Op):
    """
    .
    """
    enum_node = True
    alternatives = [ 'optional', 'zero_or_more', 'one_or_more' ]


class Suffix(Primary):
    """
    Base class for operators.
    """
    suffixed=Field(type=T.Primary)
    op=Field(type=T.SuffixOp)


#class PrimaryNode(Primary):
#    """
#    primary
#    """
#    toto=Field()

class RefIdentifier(Primary):
    """
    IdentifierReference
    """
    token_node = True

class Group(Primary):
    """
    Group
    """
    expression=Field(type=T.Expression)
    pass


class Literal(Primary):
    """
    literal node
    """
    token_node = True
    #text=Field()
    pass

class Class(Primary):
    """
    Class: char class
    """
    range=Field()
    pass

class Range(P5Node):
    """
    range
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

class Dot(Primary):
    """
    dummy
    """
    token_node = True

class NL(Primary):
    """
    dummy
    """
    pass



class CommentNode(P5Node):
    """
    TODO: transform this in a document node
    """
    pass
    #text = Field()


#------------------------------------------------------------
# this is imported in manage.py
p5_grammar = Grammar('main_rule')
G = p5_grammar

p5_grammar.add_rules(

    
    # main_rule=List(IdentifierNode(L.Identifier(match_text="first")),
    #               empty_valid=True),

    # main_rule=GrammarNode(G.definition),

    main_rule=Or(
        #Pick(List(G.comment,empty_valid=False), L.Termination),
        Pick(G.definition, L.Termination),
        Pick(
            List(
                G.definition, 
                list_cls=T.Definition.list, empty_valid=True
            ), 
            L.Termination
        ),
        #Pick(G.comment, L.Termination)
    ),

    definition=Definition(
        G.identifier, #(Token.DefIdentifier),
        "<-",
        G.expression,
        L.NL,
        L.NL
    ),

    identifier=Identifier(Token.Identifier),

    expression=Expression(
        List(
            G.sequence, 
            list_cls=Sequence.list, sep="/"
        )
    ),

    sequence=Sequence(
        List(
            G.prefix,
            list_cls=Primary.list, empty_valid=True
        )
    ),

    prefix=Or(
        Prefix(
            Or(
                PrefixOp.alt_and("&"),
                PrefixOp.alt_not("!")
            ),
            G.suffix
        ), 
        G.suffix
    ),
    
    suffix=Or(
        Suffix(
            G.primary,
            Or(
                SuffixOp.alt_optional("?"),
                SuffixOp.alt_zero_or_more("*"),
                SuffixOp.alt_one_or_more("+")
            )
        ),
        G.primary
    ),

    primary=Pick(Or(
        RefIdentifier(Token.Identifier),
        Group(Pick("(",G.expression,")")),
        Literal(Token.Literal),
        Class(Pick("[",G.range,"]")),
        Dot(".")
        
    ),Opt(L.NL)),


    #char = CharNode(Token.Char),

    range = Or(
        Range(Pick(Token.Char,"-",Token.Char)),
        Range(Token.Char)
    ),

    comment = Pick(CommentNode(Token.Comment),Opt(L.NL)),

    nl = Pick(NL(L.NL))

)

