# -*- coding: utf-8 -*-

import sqlite3


class Instruction(object):
    def __init__(self, name, params, desc=''):
        self.name = name
        self.params = params
        self.desc = desc

    def to_rst(self):
        return """
.. mips:instructions:: {name} {params}

   {desc}

{params_list}
""".format(name=self.name, params=", ".join(self.params), desc=self.desc, params_list=self._rst_paramslist())

    def _rst_paramslist(self):
        result = []

        for idx, param in enumerate(self.params):
            result.append("   :param {name}: Parameter {index}".format(name=param, index=idx))
        return "\n".join(result)

    def _get_permalink(self):
        parts = ["mips"]
        parts.append(self.name)
        parts.extend(self.params)
        return ".".join(parts)

    def insert_dash(self, conn):
        params = (self.name, 'Directive', 'directives.html#' + self._get_permalink())
        conn.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?, ?, ?)", params)


def main():
    fp = open('raw_data/directives.txt')

    conn = sqlite3.connect('docSet.dsidx')

    cur = conn.cursor()

    # try: cur.execute('DROP TABLE searchIndex;')
    # except: pass
    # cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
    # cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

    for line in fp:
        if not line:
            continue

        sig = line[:12].strip()
        desc = line[12:].strip()

        try:
            name, params = sig.split(' ', 1)
            name = name.strip()
            params = params.split(',')
        except ValueError:
            name = sig.strip()
            params = []

        inst = Instruction(name, params, desc)

        inst.insert_dash(cur)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    exit(main())
