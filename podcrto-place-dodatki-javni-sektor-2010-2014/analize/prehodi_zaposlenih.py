# -*- coding: utf-8 -*-

from lib import parser, structure

def pretok_zaposlenih(parser_output):
    header_cells, entries = parser_output

    zaposleni_dict = {}
    for entry in entries:
        if structure.zaposleni(entry) not in zaposleni_dict:
            zaposleni_dict[structure.zaposleni(entry)] = []
        zaposleni_dict[structure.zaposleni(entry)].append(entry)

    def stevilo_delovnih_mest(entries):
        return len(set(map(lambda x: structure.sifra_dm(x), entries)))
    zaposleni_prehodi = filter(lambda x: stevilo_delovnih_mest(x[1]) > 1, zaposleni_dict.items())

    def total_income_key(tuple_entry):
        return sum(map(lambda x: structure.total_income(x), tuple_entry[1]))
    zaposleni_prehodi = sorted(zaposleni_prehodi, key=total_income_key, reverse=True)

    for prehod in zaposleni_prehodi:
        print "Zaposleni #{} - {} delovnih mest".format(prehod[0], stevilo_delovnih_mest(prehod[1]))

        prehodi = sorted(prehod[1], key=structure.leto)
        for entry in prehodi:
            print "    {}: {} - {} -- {} EUR + {} EUR dodatki, {} mesecev". \
                format(structure.leto(entry), entry[0], entry[1], entry[4], \
                    structure.dodatki_sum(entry), entry[3])

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

    pretok_zaposlenih((podatki_parsed[0][0], sum(map(lambda x: x[1], podatki_parsed), [])))
