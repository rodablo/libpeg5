from langkit.dsl import (
    T, ASTNode, Annotations, Field,  # Symbol,
    abstract, has_abstract_list, synthetic
)

from langkit.envs import (
    EnvSpec, add_to_env_kv,  # add_env
)

from langkit.expressions import (
    langkit_property, Self,  # ArrayLiteral, String, No, If, Property
)


@abstract
class Peg5Node(ASTNode):
    """
    Root class for Peg5 nodes.
    """
    #dummy = Property(Self.match(lambda j=T.Peg5: 2323))
    pass


@has_abstract_list
class Definition(Peg5Node):
    """
    Definition
    """
    id = Field(type=T.Identifier)
    expression = Field(type=T.Expression)
    #  doc = Field(type=T.CommentNode)
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


@has_abstract_list
class SequenceList(AbstractPrimary.list):
    annotations = Annotations(repr_name="Primaries")


class ExpressionList(SequenceList.list):
    annotations = Annotations(repr_name="Choices")


class Expression(AbstractPrimary):
    """
    Expression
    """
    choices = Field(type=T.SequenceList.list)
    #choices = Field(type=T.ExpressionList)


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
    annotations = Annotations(repr_name="Prefixed")
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
    annotations = Annotations(repr_name="Suffixed")
    primary = Field(type=T.AbstractPrimary)
    suffix = Field(type=T.SuffixOperator)


class IdentifierReference(AbstractPrimary):
    """
    """
    annotations = Annotations(repr_name="IdRef")

    token_node = True


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


class Dot(AbstractPrimary):
    pass


class Literal(AbstractPrimary):
    """
    Literal
    """
    token_node = True


@synthetic
class CharNode(Peg5Node):
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