import libpeg5lang as lp5l

ctx = lp5l.AnalysisContext()

def process(text):
    u = ctx.get_from_buffer('main.txt', text)
    if u.diagnostics:
        print('Found errors:')
        for d in u.diagnostics:
            print(' {}'.format(d))
    else:
        u.root.dump()

process(b"""
# toto
aa <-  ( bb  cc 'dd' 
  [\200-\222])
""".strip())