#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlramen import SQLRamen as sql
from sys import argv

DIGRAPH = """digraph structs {
    graph [
       rankdir= "LR"
       bgcolor=white
    ]

    node [
        fontsize=12
        fontname="Courier New"
        shape=record
    ]

    %s
}
"""

def main():

    db = sql(argv[1])

    print("introspecting %s" % argv[1])
    to_scan = list(db.base.classes)
    vertices = []
    nodes = dict()
    interesting = set([])
    fk_count = 0
    field_count = 0

    while to_scan:
        node_str = ''
        try:
            table = to_scan.pop()

            table_name = table.__table__.name

            node_str += """
        %s [
            label="Table: %s\\l""" % (table_name, table_name,)
            has_fk = False
            for c in table.__table__.c:
                node_str += "|<%s>- %s\\l" % (c.name, c.name)
                field_count += 1
                if c.foreign_keys:
                    for fk in c.foreign_keys:
                        interesting |= {table_name, fk.column.table.name, }
                        fk_count += 1
                        vertices += [(
                            ":".join([table_name, c.name]),
                            ":".join([fk.column.table.name, fk.column.name]),
                            fk.name or '""'),
                        ]

            nodes[table_name] = """%s"
            color=%%s
            bgcolor=%%s
        ]""" % node_str

        except Exception as e:
            print("problem with %r" % table_name)
            print(repr(e))


    to_print = ""
    for node in nodes:
        to_print += nodes[node] % (("grey", "grey"), ("black", "white"))[
            node in interesting]

    for v in vertices:
        to_print += """
        %s -> %s [ label=%s ]
    """ % v
    to_print = DIGRAPH % to_print
    print("nb col = %r" % field_count)
    print("nb fk = %r" % fk_count)

    with open("out.dot", "w") as f:
        f.write(to_print)
    print("output available in out.dot")
