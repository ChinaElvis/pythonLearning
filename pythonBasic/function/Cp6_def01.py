def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, " ")
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


def storeMulti(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, "")
        labels = 'first', 'middle', 'last'
        for label,name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


if __name__ == "__main__":
    MyNames = {}
    init(MyNames)
    store(MyNames, "Magnus Lie Hetland")
    print(lookup(MyNames, 'middle', 'Lie'))
    store(MyNames, 'Robin Hood')
    store(MyNames, 'Robin Locksley')
    print(lookup(MyNames, 'first', 'Robin'))
    store(MyNames, 'Mr.Gumby')
    print(lookup(MyNames, 'middle', ' '))
    #### new ####
    d = {}
    init(d)
    storeMulti(d, 'Luke Skywalker', 'Anakin Skywalker')
    print(lookup(d, 'last', 'Skywalker'))
