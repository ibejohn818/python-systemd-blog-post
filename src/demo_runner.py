from argparse import ArgumentParser
import os
import time
import sys

_SELF=sys.modules[__name__]

def cmd1(**kw):
    """ command number 1
    """
    pid = os.getpid()
    print("({})Here is my argument: {}".format(
        pid,
        kw.get('arg')))
    print("({})I will sleep for {} seconds.".format(
        pid,
        kw.get('sleep')))
    time.sleep(kw.get('sleep'))
    print("({}) Done.".format(pid))


def init():
    """ initialize cli app and return it
    """

    parser = ArgumentParser(description="Demo daemon cli")

    sub = parser.add_subparsers()

    cmd1 = sub.add_parser('cmd1', description="Command numero 1")
    cmd1.add_argument('--arg',
                      '-a',
                      type=str,
                      default='default value',
                      help="I am an argument")
    cmd1.add_argument('--sleep',
                      '-s',
                      type=int,
                      default=5,
                      help="Time to sleep")
    cmd1.set_defaults(cmd=getattr(_SELF, "cmd1"))


    return parser

if __name__ == '__main__':

    try:
        args = init().parse_args()
        if hasattr(args, 'cmd'):
            cmd = getattr(args, 'cmd')
            kw = vars(args)
            cmd(**kw)
        else:
            args.print_help()
    except Exception as e:
          print("ERROR: ", str(e))


