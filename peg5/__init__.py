from langkit.libmanage import ManageScript
from langkit.compile_context import (
    CompileCtx,
    # ADA_BODY
)

import os.path as P


class Manage(ManageScript):
    def __init__(self, ctx: CompileCtx = None) -> None:
        if ctx:
            self._cached_context = ctx
        else:
            from peg5.language.lexer import peg5_lexer
            from peg5.language.parser import peg5_grammar
            self._cached_context = CompileCtx(
                lang_name='Peg5',
                # short_name='Peg5',
                lexer=peg5_lexer,
                grammar=peg5_grammar
            )
            #self._cached_context.add_with_clause(
            #    'Implementation',
            #    ADA_BODY, 'LibPeg5lang.Sources',
            #    use_clause=False
            #)
            # check manage_run() in langkit/*/utils.py
            extensions_dir = P.abspath('peg5/extensions')
            if P.isdir(extensions_dir):
                self._cached_context.extensions_dir = extensions_dir

        super().__init__()

    def create_context(self, args) -> CompileCtx:
        return self._cached_context

    def do_generate(self, args):
        # TODO: args.generate_unparser = False
        # args.generate_ada_api = False
        args.report_unused_doc_entries = True
        super(Manage, self).do_generate(args)

    do_generate.__doc__ = ManageScript.do_generate.__doc__
