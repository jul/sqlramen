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
#  'Synopsis\r\n\r\nA frontend to a pandoc toolchain to build a book in a supposedly new way.',
#  'How to install and start it\r\n',
#  'walkthrough to create this manual with the tool\r\n\r\nFirst post//landing page',
#  'Quickstart',
#  'rendering of first post ',
#  'time to attach a content',
#  'Time to edit the FIRST text which is special\r\n\r\nSetting a title for the document',
#  'time to check on your book rendering !',
#  'Rinse and repeat',
#  'Editing your first text',
#  'Sub case PDF rendering',
#  'Dev notes',
#  'model',
#  'serendipity',
#  'psycodélic',
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
```



