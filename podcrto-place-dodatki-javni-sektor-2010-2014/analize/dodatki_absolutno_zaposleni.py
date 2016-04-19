# -*- coding: utf-8 -*-

from lib import parser, structure

def dodatki_absolutno_zaposleni(parser_output):
    header_cells, entries = parser_output

    zaposleni_dict = {}
    for entry in entries:
        key = structure.zaposleni(entry)
        if key not in zaposleni_dict:
            zaposleni_dict[key] = []
        zaposleni_dict[key].append(entry)

    def dodatki_sum(tuple_entry):
        return sum(map(lambda x: structure.dodatki_sum(x), tuple_entry[1]))
    zaposleni_entries = sorted(zaposleni_dict.items(), key=dodatki_sum, reverse=True)

    for zaposleni in zaposleni_entries[:100]:
        entries = sorted(zaposleni[1], key=structure.leto)

        print "Zaposleni #{} - {} EUR dodatkov". \
            format(zaposleni[0], dodatki_sum(zaposleni))
        for entry in entries:
            print "    {} ({} mesecev) - {} - {}: plača bruto {} EUR, dodatki {} EUR, skupaj {} EUR". \
                format(structure.leto(entry), entry[3], entry[0], entry[1], \
                    entry[4], structure.dodatki_sum(entry), structure.total_income(entry))

            print "      dodatki:"
            dodatek_index = 0
            for dodatek in structure.dodatki(entry):
                if dodatek > 0:
                    print "        {}: {} EUR".format(header_cells[dodatek_index + 5], dodatek)
                dodatek_index = dodatek_index + 1

        total_placa = sum(map(lambda x: float(x[4]), entries))
        total_dodatki = sum(map(lambda x: structure.dodatki_sum(x), entries))
        print "    Skupaj: Plača bruto {} EUR, dodatki {} EUR, skupaj {} EUR". \
            format(total_placa, total_dodatki, total_placa + total_dodatki)

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

    print "Top 100 lestvica po izplačilu dodatkov absolutno, po zaposlenem"
    print
    dodatki_absolutno_zaposleni((podatki_parsed[0][0], sum(map(lambda x: x[1], podatki_parsed), [])))
