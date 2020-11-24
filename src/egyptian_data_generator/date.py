import datetime

from egyptian_data_generator.helpers import Helpers

class Date:
    @staticmethod
    def between(_from = None, _to = None):
        if _from is None:
            _from = datetime.date(year = 1979, month = 1, day = 1)
        if _to is None:
            _to = datetime.date.today()

        date =  _from + datetime.timedelta(seconds = Helpers.intBetween(0, int((_to - _from).total_seconds())))
        return date.strftime("%Y-%m-%d")
    
    def recent(self, _seconds = None):
        if _seconds is None:
            # 172800 = 2 days
            _seconds = Helpers.intBetween(0, 172800)
        result = datetime.datetime.now() - datetime.timedelta(seconds = _seconds)
        return result.strftime("%Y-%m-%d")

