import os, sys

def print_done() -> None:
    print('Done.')

def run_make(additional_make_args=[]):
    """
    """
    from langkit.libmanage import ManageScript, DiagnosticError

    class Manage(ManageScript):
        def __init__(self, ctx) -> None:
            self._cached_context = ctx
            super().__init__()

        def create_context(self, args) -> 'CompileCtx':
            return self._cached_context

        def do_generate(self, args) -> None:
            args.generate_unparser = False
            args.generate_ada_api = False
            # TODO check if the next one make sense
            args.report_unused_doc_entries = True
            super(Manage, self).do_generate(args)

        do_generate.__doc__ = ManageScript.do_generate.__doc__

    argv = ['make'] #+ sys.argv[1:] 
    argv.append('--build-mode=dev')
    argv.append('--disable-all-mains')
    argv.append('--verbosity=none')
    argv.append('--no-ada-api')
    argv.extend(additional_make_args)
    #
    from language import prepare_peg5_context
    m = Manage(prepare_peg5_context())

    return_code = m.run_no_exit(argv)
    # Flush stdout and stderr, so that diagnostics appear deterministically
    # before the script/program output.
    sys.stdout.flush()
    sys.stderr.flush()
    if return_code != 0:
        raise DiagnosticError()   
    #
    def update_os_environ(env_var: str, directory: str) -> None:
        path = os.environ.get(env_var)
        path = ('{}{}{}'.format(directory, os.path.pathsep, path) if path else env_var)
        os.environ[env_var] = path
        #print(env_var,'===========', path)

    m.setup_environment(update_os_environ)

