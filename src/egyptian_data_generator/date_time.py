import datetime
import time

from egyptian_data_generator.helpers import Helpers

class DateTime:
    def between(self, _from = None, _to = None):
        if _from is None:
            _from = datetime.datetime(year = 1979, month = 1, day = 1)
        if _to is None:
            _to = datetime.datetime.now()
        return _from + datetime.timedelta(seconds = Helpers.intBetween(0, int((_to - _from).total_seconds())))
    
    def recent(self, _seconds = None):
        if _seconds is None:
            # 172800 = 2 days
            _seconds = Helpers.intBetween(0, 172800)
        result = datetime.datetime.now() - datetime.timedelta(seconds = _seconds)
        return result
    
    def recentUnixTime(self, _seconds = None):
        if _seconds is None:
            # 172800 = 2 days
            _seconds = Helpers.intBetween(0, 172800)
        date = self.recent(_seconds)
        return int(time.mktime(date.timetuple()))
               
