import libpeg5lang as lp5l

_ctx = lp5l.AnalysisContext()


def do_parse_and_dump(source: str,
                      rule: str = lp5l.GrammarRule.main_rule_rule):

    unit = _ctx.get_from_buffer(filename='test.peg',
                                buffer=source,
                                rule=rule)
    print('==BEGIN==DUMP==')

    if unit.diagnostics:
        print('P&D - Found errors:')
        for d in unit.diagnostics:
            print('P&D - {}'.format(d))
    else:
        for t in unit.iter_tokens():
            print('{}'.format(t))
        print('===============')
        unit.root.dump()

    print('====END==DUMP==')
    return unit
