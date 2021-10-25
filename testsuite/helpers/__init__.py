import os
import sys


def print_done() -> None:
    print('Done.')


def run_make(additional_make_args=[]):
    """
    """
    from langkit.libmanage import DiagnosticError
    argv = ['make']
    argv.append('--build-mode=dev')
    #argv.append('--disable-all-mains')
    argv.append('--verbosity=none')
    #argv.append('--no-ada-api')
    #argv.append('--generate-unparser')
    argv.extend(additional_make_args)
    #
    from language import Manage
    m = Manage()

    return_code = m.run_no_exit(argv)
    # Flush stdout and stderr, so that diagnostics appear deterministically
    # before the script/program output.
    sys.stdout.flush()
    sys.stderr.flush()
    if return_code != 0:
        raise DiagnosticError()

    def update_os_environ(env_var: str, directory: str) -> None:
        path = os.environ.get(env_var)
        path = ('{}{}{}'.format(directory, os.path.pathsep, path) if path else env_var)
        os.environ[env_var] = path
        # print(env_var,' = ', path)

    m.setup_environment(update_os_environ)
