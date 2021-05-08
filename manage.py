#! /usr/bin/env python3

import os

from langkit.libmanage import ManageScript


class Manage(ManageScript):
    def create_context(self, args):
        from langkit.compile_context import CompileCtx

        from language.lexer import p5_lexer
        from language.parser import p5_grammar

        return CompileCtx(lang_name='Peg5',
                          short_name='P5',
                          lexer=p5_lexer,
                          grammar=p5_grammar)

    def do_generate(self, args):
        args.generate_unparser = False
        args.report_unused_doc_entries = True
        super(Manage, self).do_generate(args)
    do_generate.__doc__ = ManageScript.do_generate.__doc__

if __name__ == '__main__':
    Manage().run()
