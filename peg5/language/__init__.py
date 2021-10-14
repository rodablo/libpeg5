from langkit.compile_context import CompileCtx


def prepare_peg5_context() -> CompileCtx:
    from .lexer import p5_lexer
    from .parser import p5_grammar
    ctx = CompileCtx(lang_name='Peg5',
                     short_name='Peg5',
                     lexer=p5_lexer,
                     grammar=p5_grammar)
    return ctx
