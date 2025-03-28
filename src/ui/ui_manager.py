import cmd, sys

from src.io_interfaces.io_interfaces import IOInterfaces
from src.models.feature_model_1 import FeatureStatsModel

class MarketResearchShell(cmd.Cmd):

    intro = 'Welcome to the Markets Research Platform shell.   Type help or ? to list commands.\n'
    prompt = 'markets_research> '
    file = None
    io_interfaces = None

    def do_enter_io_paths(self, arg):
        'Enter the paths for IO Interfaces:  get_io_paths'

        #PRICES_PATH = "E:\\tst-data\\prices.parquet"
        #FEATURES_PATH = "E:\\tst-data\\features.parquet"
        #DB_LOCATION = "E:\\tst-data\\feature_stats_db"

        PRICES_PATH = input("Enter Prices file path: ")
        FEATURES_PATH = input("Enter Features file path: ")
        DB_LOCATION = input("Enter Object DB file path: ")

        MarketResearchShell.io_interfaces = IOInterfaces(PRICES_PATH, FEATURES_PATH, DB_LOCATION)

    def do_get_feature_std(self, arg):
        'Query the Object DB to get the standard deviation of a feature:  get_feature_std feature_0'
        print(MarketResearchShell.io_interfaces.query_key_from_db(arg))

    def do_run_model(self, arg):
        'Run the Feature Stats Model and persist its results in key/value object DB:  run_model'
        FeatureStatsModel(MarketResearchShell.io_interfaces).run_model()

    def do_quit(self, arg):
        'Close the CLI Shell and Exit:  quit'
        print('Thank you for using the Market Research Platform')
        self.quit()
        return True

    def quit(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    MarketResearchShell().cmdloop()