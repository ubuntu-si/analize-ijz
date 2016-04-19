
def dodatki(entry):
    assert type(entry) is list
    return map(lambda x: float(x), entry[5:68])

def dodatki_sum(entry):
    assert type(entry) is list
    return sum(dodatki(entry))

def dodatki_relative(entry):
    assert type(entry) is list
    if float(entry[4]) == 0:
        return 0
    return dodatki_sum(entry) / float(entry[4])

def placa(entry):
    assert type(entry) is list
    return float(entry[4])

def total_income(entry):
    assert type(entry) is list
    return dodatki_sum(entry) + float(entry[4])

def zaposleni(entry):
    assert type(entry) is list
    return entry[2]

def sifra_dm(entry):
    assert type(entry) is list
    return entry[70]

def leto(entry):
    assert type(entry) is list
    return int(entry[71])

def organ(entry):
    assert type(entry) is list
    return entry[68]

def ime_organa(entry):
    assert type(entry) is list
    return entry[0]
