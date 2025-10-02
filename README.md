# SQLSoup

SQLSoup is no longer supported and does not work with modern versions of SQLAlchemy. For modern support of ad-hoc models based on database reflection, please refer to the automap feature at: https://docs.sqlalchemy.org/en/stable/orm/extensions/automap.html

# SQLRamen


SQLRamen provides a convenient way to map Python objects to relational database tables, with no declarative code of any kind. It's built on top of the SQLAlchemy ORM and provides a super-minimalistic interface to an existing database.

Usage is as simple as:

```python

from sqlramen import *
db = SQLRamen("sqlite:///../pdca/aide")
user = db.query(db.table.user).filter_by(email="j@j.com").one()
[ l.message for l in u.comment_collection ]
# ['SCAM Manual\r\n\r\nA complete guide to create a guide with scam',
# ...
#  'future plan',
#  'further down']
db.query(db.table.comment.message).join(db.table.comment.user
    ).filter(db.table.user.email=="j@j.com").all()
# same
print([l for l in db.table.user.__table__.c])
# [Column('id', INTEGER(), table=<user>, primary_key=True, nullable=False),
# Column('pic_file', TEXT(), table=<user>),
# Column('name', TEXT(), table=<user>, nullable=False),
# Column('email', TEXT(), table=<user>, nullable=False),
# Column('secret_token', TEXT(), table=<user>),
# Column('secret_password', TEXT(), table=<user>, nullable=False)]
db.raw("select * from comment limit 5").all()
#[('2025-01-12 12:52:09', 1, 1, None, 'SCAM Manual\r\n\r\nA complete guide to create a guide with scam', None, 'story'),
# ('2025-01-12 13:28:14', 2, 1, 1, 'Synopsis\r\n\r\nA frontend to a pandoc toolchain to build a book in a supposedly new way.', None, 'story_item'),
# ('2025-01-12 13:28:47', 3, 1, 1, 'How to install and start it\r\n', None, 'story_item'),
# ('2025-01-12 13:29:48', 4, 1, 1, 'walkthrough to create this manual with the tool\r\n\r\nFirst post//landing page', None, 'story_item'),
# ('2025-01-12 13:30:23', 5, 1, 3, 'Quickstart', None, 'comment')]
```

## db\_introspect

Usage:
```bash

db_introspect sqlite:///../pdca/aide && xdot out.dot
# introspecting sqlite:///../pdca/aide
# nb col = 23
# nb fk = 7
# output available in out.dot
```

output:

![entity relation diagram](https://github.com/jul/sqlramen/blob/main/out.png?raw=true)

