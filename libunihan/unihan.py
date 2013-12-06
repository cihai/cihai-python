# -*- coding: utf8 - *-
"""For accessing vcspull as a package.

libunihan.unihan
~~~~~~~~~~~~~~~~

:copyright: Copyright 2013 Tony Narlock.
:license: BSD, see LICENSE for details

"""

from __future__ import absolute_import, division, print_function, with_statement

from pkg_resources \
    import resource_filename  # @UnresolvedImport #pylint: disable=E0611
import zipfile
import csv


def get_datafile(file_):
    return resource_filename(__name__, 'data/' + file_)


def unichr3( *args ):
    return [unichr( int( i[2:7], 16 ) ) for i in args if i[2:7]][0]


def main():
    print('%s' % get_datafile('Unihan.zip'))
    z = zipfile.ZipFile(get_datafile('Unihan.zip'))
    print([f.filename for f in z.filelist])

    with open(get_datafile('Unihan_Readings.txt'), 'rb') as csvfile:
        csvfile = filter(lambda row: row[0]!='#', csvfile)
        #r = csv.reader(csvfile)
        r = UnihanReader(
            csvfile,
            fieldnames=['char', 'field', 'value'],
            delimiter='\t'
        )
        for row in r:
            #print(', '.join(row))
            #print(unichr3(row['char']))
            print(row)


class UnihanReader(csv.DictReader):
    def __init__(self, *args, **kwargs):
        csv.DictReader.__init__(self, *args, **kwargs)