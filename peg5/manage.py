#! /usr/bin/env python3

#import sys
#from langkit.libmanage import ManageScript

from language import Manage

#class Manage(ManageScript):
#    def create_context(self, args):
#        from language import prepare_peg5_context
#        return prepare_peg5_context()
#
#    def do_generate(self, args):
#        # TODO: args.generate_unparser = False
#        args.report_unused_doc_entries = True
#        super(Manage, self).do_generate(args)
#
#    do_generate.__doc__ = ManageScript.do_generate.__doc__


if __name__ == '__main__':
    Manage().run()
