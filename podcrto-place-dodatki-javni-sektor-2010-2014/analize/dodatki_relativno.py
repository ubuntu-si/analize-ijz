# -*- coding: utf-8 -*-

import sys

from lib import parser, structure

def dodatki_relativno(parser_output):
    header_cells, entries = parser_output

    entries = sorted(entries, key=structure.dodatki_relative, reverse=True)

    for entry in entries[:100]:
        dodatki_sum = structure.dodatki_sum(entry)
        dodatki_relative = structure.dodatki_relative(entry)

        print "{} - {} - {}: {} EUR".format(entry[0], entry[1], structure.leto(entry), dodatki_sum)
        print "    plača bruto {} EUR, za obdobje {} mesca/mescev, skupaj {} EUR". \
            format(entry[4], entry[3], float(entry[4]) + dodatki_sum)
        print "    dodatki znesejo {:.2f}% plače bruto, {:.2f}% celotnega zneska". \
            format(dodatki_sum * 100.0 / float(entry[4]), dodatki_sum * 100.0 / (float(entry[4]) + dodatki_sum))

        print "    dodatki:"
        dodatki = structure.dodatki(entry)
        dodatek_index = 0
        for dodatek in dodatki:
            if dodatek > 0:
                print "        {}: {} EUR".format(header_cells[dodatek_index + 5], dodatek)
            dodatek_index = dodatek_index + 1

        print

if __name__ == "__main__":
    podatki = [
        "../podatki/csv/dodatki_agregat_2010.csv",
        "../podatki/csv/dodatki_agregat_2011.csv",
        "../podatki/csv/dodatki_agregat_2012.csv",
        "../podatki/csv/dodatki_agregat_2013.csv",
        "../podatki/csv/dodatki_agregat_2014.csv"
    ]
    podatki_parsed = map(lambda x: parser.parse(x), podatki)
    assert all(map(lambda x: x[0] == podatki_parsed[0][0], podatki_parsed))

    print "Top 100 lestvica po izplačilu dodatkov relativno glede na bruto plačo"
    print
    dodatki_relativno((podatki_parsed[0][0], sum(map(lambda x: x[1], podatki_parsed), [])))
