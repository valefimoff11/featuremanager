import cmd, sys
from turtle import *

from src.io_interfaces.io_interfaces import query_key_from_db


class MarketResearchShell(cmd.Cmd):
    intro = 'Welcome to the Markets Research Platform shell.   Type help or ? to list commands.\n'
    prompt = 'markets_research> '
    file = None

    # ----- basic commands -----
    def do_get_feature_std(self, arg):
        'Get the standard deviation of a feature:  get_feature_std feature_0'
        print(query_key_from_db(arg))

    def do_bye(self, arg):
        'Close the CLI Shell and Exit:  BYE'
        print('Thank you for using the Market Research Platform')
        self.close()
        bye()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    MarketResearchShell().cmdloop()