from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text


class SQLRamen:
    def __init__(self, dsn):
        self.Base = automap_base()
        self.engine = create_engine(dsn)
        self.Base.prepare(autoload_with=self.engine)
        self.session = Session(self.engine)

    def __getattr__(self, attr):
        if attr == "table":
            return self.Base.classes
        if attr == "base":
            return self.Base
        if attr == "engine":
            return self.engine
        if attr == 'raw':
            return lambda *s, **kw: self.session.execute(text(*s, **kw))
        return getattr(self.session, attr)
