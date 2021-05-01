example = {
    'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15 / 2, False],
    'fire': ['hot', 46, ['cha', 'ching'], 81.13],
    'earth': ['solid', 100, (13, 31, 1), 90.01, {'b': 'c'}]
}

elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']


def func(dct, lst):
    for i in lst:
        try:
            summ = 0
            for j in dct[i]:
                try:
                    summ += j
                except TypeError:
                    continue
            print(f"{i}----{summ}")
        except KeyError:
            print(f"ключа {i} не существует")


func(example,elements)
