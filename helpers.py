import random

first_names = ['Mikhail', 'Viktor', 'Svetlana', 'Elena', 'Yaroslav', 'Anastasia', 'Konstantin',
               'Valentina', 'Roman', 'Irina', 'Denis', 'Galina', 'Timur', 'Zoya', 'Nina']
last_names = ['Bogdanov', 'Gusev', 'Zaitsev', 'Korolev', 'Matveev', 'Nikiforov', 'Orlov',
              'Panov', 'Rogov', 'Sorokin', 'Trifonov', 'Ulyanov', 'Filatov', 'Chekhov', 'Shirokov']


def login_generator(domain):
    name = random.choice(first_names)
    last_name = random.choice(last_names)
    number = random.randint(0, 999)
    email = f'{name}_{last_name}{number}@{domain}'
    return email, name
