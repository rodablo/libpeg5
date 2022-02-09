from langkit.dsl import (
    T, ASTNode, Annotations, Field,  # Symbol,
    # Bool,
    # UserField,
    abstract, has_abstract_list, synthetic
)

from langkit.envs import (
    EnvSpec, add_to_env_kv, add_env,
    # add_to_env
)

from langkit.expressions import (
    langkit_property, Self,
    # And, No, ArrayLiteral,
    If,
    # Property,
    # String,
    # Entity,
    # Var,
    # new_env_assoc
    lazy_field,

)

# import langkit.names as names


@abstract
class Peg5Node(ASTNode):
    """
    Root class for Peg5 nodes.
    """
    #dummy = Property(Self.match(lambda j=T.Peg5: 2323))
    pass
    #current_scope = Property(
    #    Self.parents.find(
    #        lambda p: p.is_a(T.Definition)  # or p.is_a(T.Expression)   # or Expression
    #    ).cast(T.Definition),
    #    doc="Return the env of the enclosing Definition or Expression.",
    #    ignore_warn_on_node=True,
    #    public=True
    #)

    #@langkit_property()
    #def resolve_ref():
    #    return Self.match(
    #        lambda r=T.LabelReference:
    #            r.parent.parent.node_env.get(r.symbol).at(0),
    #        lambda _:
    #            No(T.entity),
    #    )
    @langkit_property(return_type=T.Bool, memoized=True)
    def can_have_dessert():
        """
        Return whether this node can define a named environment.
        """
        return If(
            Self.is_a(T.Expression, T.CharNode),
            # All nodes that can define a named environment are supposed to
            # live in lists, so use Self.parent.parent to get the node that
            # owns that list.
            Self.parent.is_a(T.ExpressionList) & Self.parent.parent.is_a(T.SequenceList) & \
            (Self.parent.parent.is_null | Self.parent.parent.can_have_dessert),
            False,
        )


@has_abstract_list
class Definition(Peg5Node):
    """
    Definition
    """
    label = Field(type=T.Label)
    expression = Field(type=T.Expression)
    #  doc = Field(type=T.CommentNode)
    env_spec = EnvSpec(
        add_to_env_kv(Self.label.symbol, Self),
        #add_env()
    )


class Definitions(Definition.list):

    annotations = Annotations(repr_name="Grammar")

    @langkit_property(return_type=T.Int, public=True)
    def n_dummy():
        """
        Return the number of definitions in this grammar
        """
        return Self.length


class Label(Peg5Node):
    """
    Label.
    """
    annotations = Annotations(repr_name="Label")

    token_node = True

    #@langkit_property(return_type=T.Symbol, public=True)
    #def sym():
    #    """
    #    Return the symbol for this identifier.
    #    """
    #    return Self.symbol

    #@langkit_property()
    #def resolve(base_env=T.LexicalEnv):
    #    return base_env.get_first(Self.symbol).node.cast(T.Definition)


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

    env_spec = EnvSpec(
        add_env(),
        #add_to_env_kv(
        #    key=No(T.Symbol), #String("toto5").to_symbol,
        #    val=Self,
        #)
    )


@abstract
class AbstractOperator(Peg5Node):
    """
    AbstractOperator Node.
    """
    pass


class Prefix(AbstractOperator):
    """
    """
    enum_node = True
    alternatives = ['and', 'not']


class PrefixedPrimary(AbstractPrimary):
    """
    PrefixedPrimary Node.
    """
    annotations = Annotations(repr_name="Prefixed")
    prefix = Field(type=T.Prefix)
    primary = Field(type=T.AbstractPrimary)

    #__scope = Var(Entity.current_scope)
    #print(__scope.current_scope)

    #Entity.current_scope.cast(T.Definition).env_spec(
    #    add_to_env_kv(String("toto2").to_symbol, Self)
    #)
    #Entity.current_scope.env_spec(
    #    add_to_env_kv(String("toto3").to_symbol, Self)
    #)


class Suffix(AbstractOperator):
    """
    """
    #annotations = Annotations(repr_name="Suffix_")
    enum_node = True
    alternatives = ['optional', 'zero_or_more', 'one_or_more']


class SuffixedPrimary(AbstractPrimary):
    """
    SuffixedPrimary Node.
    """
    annotations = Annotations(repr_name="Suffixed")
    primary = Field(type=T.AbstractPrimary)
    suffix = Field(type=T.Suffix)


class LabelReference(AbstractPrimary):
    """
    """
    annotations = Annotations(repr_name="Reference")
    label = Field(type=Label)
    #token_node = True

    env_spec = EnvSpec(
        #        add_to_env(Self.label.filtermap(
        #            lambda e: new_env_assoc(key=e.cast_or_raise(T.Label).sym, val=Self),
        #            lambda e: e.is_a(T.Label),
        #        ))
        #        add_to_env_kv(
        #            key=Self.symbol,
        #            val=Self,
        #            resolver=Peg5Node.resolve_ref
        #        )
        add_to_env_kv(
            key=Self.label.symbol,
            value=Self,
        ),
    )
#
    #@lazy_field(return_type=T.CharNode)
    #def new_node():
    #    return T.CharNode.new()
#
    #@langkit_property(return_type=T.Int, public=True)
    #def prop():
    #    return Self.new_node.lf
#
#    @langkit_property(return_type=Bool,
#                      public=True)
#    def dummy_fun():
#        dummy = Var(Entity)
#        print('--------------------{}'.format(Entity.canonical_type))
#        return And(
#            Self.type.entity == dummy.entity,
#            True
#        )
#
#    @langkit_property(public=True)
#    def resolve():
#        return Self.node_env.get(Self.symbol).at(0)


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
    #toto = Property(
    #    T.CharNode.new(),  # s.name.singleton
    #    public=True
    #)
    #dummy = UserField(public=False, repr=True, type=T.CharNode, default_value=T.CharNode.new())#.as_entity)
#
    #@langkit_property(memoized=True)
    #def toto3():
    #    return T.CharNode.new().as_entity
    #pass
    # la idea es crearel nodo con New pasarle los campos en la inicializacion
    # y retornarloen una prop memoizada p_ y f_ en el api prefixan
    # properties y fields,
    @lazy_field(return_type=T.Int, public=True)
    def lf():
        return 42

    @langkit_property(return_type=T.Int, public=True, memoized=True)
    def prop():
        return Self.lf


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


@abstract
class AbstractChar(Peg5Node):
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
    #@lazy_field(return_type=T.Int, public=True)
    #def lf():
    #    return 42
    #@langkit_property(return_type=T.Int, public=True)
    #def prop():
    #    return Self.lf
