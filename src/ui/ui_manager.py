import cmd, sys

from src.io_interfaces.io_interfaces import query_key_from_db
from src.models.feature_model_1 import FeatureStatsModel


class MarketResearchShell(cmd.Cmd):

    intro = 'Welcome to the Markets Research Platform shell.   Type help or ? to list commands.\n'
    prompt = 'markets_research> '
    file = None

    def do_get_feature_std(self, arg):
        'Get the standard deviation of a feature:  get_feature_std feature_0'
        print(query_key_from_db(arg))

    def do_run_model(self, arg):
        'Run the Feature Stats Model and persist its results in key/value object DB:  run_model'
        FeatureStatsModel().run_model()

    def do_close(self, arg):
        'Close the CLI Shell and Exit:  BYE'
        print('Thank you for using the Market Research Platform')
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    MarketResearchShell().cmdloop()