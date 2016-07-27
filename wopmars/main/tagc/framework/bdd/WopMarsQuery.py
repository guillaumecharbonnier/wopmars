from sqlalchemy.orm.query import Query

import wopmars.main.tagc.framework.bdd.SQLManager


class WopMarsQuery(Query):
    """
    This class extend the Query class from sqlalchemy.orm in purpose to use the lock provided by the SQLManager in order
    to query the database.

    It overide all methods relatives to finish a query:
      - all
      - one
      - first
      - count
      - one_or_none
      - scalar
    """
    def all(self):
        return wopmars.main.tagc.framework.bdd.SQLManager.SQLManager.instance().result_factory(self, "all")

    def one(self):
        return wopmars.main.tagc.framework.bdd.SQLManager.SQLManager.instance().result_factory(self, "one")

    def first(self):
        return wopmars.main.tagc.framework.bdd.SQLManager.SQLManager.instance().result_factory(self, "first")

    def count(self):
        return wopmars.main.tagc.framework.bdd.SQLManager.SQLManager.instance().result_factory(self, "count")

    def one_or_none(self):
        return wopmars.main.tagc.framework.bdd.SQLManager.SQLManager.instance().result_factory(self, "one_or_none")

    def scalar(self):
        return wopmars.main.tagc.framework.bdd.SQLManager.SQLManager.instance().result_factory(self, "scalar")