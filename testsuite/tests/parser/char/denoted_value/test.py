"""
Test that CharNode.p_denoted_value properly decodes all valid escape character
literals.
"""
import libpeg5lang as lp5l

ctx = lp5l.AnalysisContext('utf-8')
unit = ctx.get_from_file(filename='input',
                         rule=lp5l.GrammarRule.range_rule)

for node in unit.root.findall(lp5l.CharNode):
    #name = decl.f_ids.text
    #expr = decl.f_default_expr
    assert isinstance(node, lp5l.CharNode)
    try:
        value = u'{} {}:{}-{}:{} {}'.format(
            node.kind_name,
            node.token_start._sloc_range.start.line,
            node.token_start._sloc_range.start.column,
            node.token_start._sloc_range.end.line,
            node.token_start._sloc_range.end.column,
            node.p_denoted_value
        )
    except lp5l.PropertyError as err:
        value = u'<PropertyError>' + err
    #print('{} ({}) -> {}'.format(name, ascii(expr.text), ascii(value)))
    print(value)
