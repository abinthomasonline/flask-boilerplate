from sqlalchemy.orm import Query
from sqlalchemy.exc import OperationalError
from time import sleep


class RetryingQuery(Query):
    __retry_count__ = 3
    __retry_delay__ = 0.5  # 500ms

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        attempts = 0
        while True:
            attempts += 1
            try:
                return super().__iter__()
            except OperationalError as ex:
                if attempts <= self.__retry_count__:
                    sleep(self.__retry_delay__)
                else:
                    raise