# -*- coding: utf-8 -*-

from lib import parser, structure

def dodatki_relativno_organi(parser_output):
    header_cells, entries = parser_output

    organi_dict = {}
    for entry in entries:
        key = structure.organ(entry)
        if key not in organi_dict:
            organi_dict[key] = []
        organi_dict[key].append(entry)

    def organi_relativno_key(tuple_pair):
        sum_placa = sum(map(lambda x: structure.placa(x), tuple_pair[1]))
        sum_dodatki = sum(map(lambda x: structure.dodatki_sum(x), tuple_pair[1]))
        if sum_placa == 0:
            return 0
        if (sum_placa + sum_dodatki) == 0:
            return 0
        return sum_dodatki / (sum_placa + sum_dodatki)
    organi_entries = sorted(organi_dict.items(), key=organi_relativno_key, reverse=True)

    for organ in organi_entries[:100]:
        entries = organ[1]
        imena_organa = list(set(map(lambda x: structure.ime_organa(x), entries)))

        total_placa = sum(map(lambda x: float(x[4]), entries))
        total_dodatki = sum(map(lambda x: structure.dodatki_sum(x), entries))

        print "{} - {} EUR izplačanih dodatkov, {:.2f}% celotnega zneska". \
            format(imena_organa[0], total_dodatki, total_dodatki * 100 / (total_placa + total_dodatki))
        if len(imena_organa) > 1:
            print "    Ostala imena:"
            for ime in imena_organa[1:]:
                print "      ", ime

        place_dodatki_letno = dict.fromkeys(set(map(lambda x: structure.leto(x), entries)), [0, 0])
        for entry in entries:
            leto = structure.leto(entry)
            assert leto in place_dodatki_letno
            cur_pd = place_dodatki_letno[leto]
            place_dodatki_letno[leto] = [cur_pd[0] + structure.placa(entry), cur_pd[1] + structure.dodatki_sum(entry)]
        place_dodatki_letno_entries = sorted(place_dodatki_letno.items(), key=lambda x: x[0])

        for entry in place_dodatki_letno_entries:
            leto, izplacila = entry
            izplacila_sum = sum(izplacila)
            print "    {} - {} EUR ({:.2f}%) plače bruto, {} EUR ({:.2f}%) dodatki, skupaj {} EUR". \
                format(leto, izplacila[0], izplacila[0] * 100.0 / izplacila_sum, \
                    izplacila[1], izplacila[1] * 100.0 / izplacila_sum, izplacila[0] + izplacila[1])

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

    print "Top 100 lestvica po izplačilu dodatkov relativno plači bruto, po organu"
    print
    dodatki_relativno_organi((podatki_parsed[0][0], sum(map(lambda x: x[1], podatki_parsed), [])))
