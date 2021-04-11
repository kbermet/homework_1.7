from datetime import date

band = {
    'members':{
        'Freddy Mercury':{
            'role': 'singer',
            'date': date(1956,12,12)
        },
        'Mirbek Atabekov': {
            'role': 'drummer',
            'date': date(1987, 1, 12)
        },
        'Filip Kirkorov': {
            'role': 'dancer',
            'date': date(1970, 12, 12)
        }
    },

    'concerts': {
        'London': {
            'concert_date': date(2021,1,12),
            'income': 10000,
            'expenses': [1000, 1000, 1000]
        },
        'Bishkek': {
            'concert_date': date(2021, 4, 12),
            'income': 10000,
            'expenses': [500, 500, 500]
        },
        'Osh': {
            'concert_date': date(2021, 5, 12),
            'income': 10000,
            'expenses': [300, 300, 300]
        },
    }
}


def add_new_member(band, **kwargs):
    band['members'].update(kwargs)
    return band

new_member = {'Bob Sincler': {'role': 'DJ', 'date': date(1987,5,5)}}
print(add_new_member(band, **new_member))


def remove_member(band, name):
    return band['members'].pop(name)
remove_member(band, 'Mirbek Atabekov')
print(band['members'])

def calculate_expenses(*args):
    return sum(args)
# print(calculate_expenses('London'))

def func(band, concert_name):
    income = band['concerts'][concert_name]['income']
    print(income)

    return income-calculate_expenses(*band['concerts'][concert_name]['expenses'])
print(func(band, 'London'))

def func(band, concert_name):
    income = band['concerts'][concert_name]['expenses']
    # print(expenses)

total_sum= 0
for concert in band['concerts']:
    a =band['concerts']['expenses']
    total_sum += calculate_expenses(band, a)

print(total_sum)


