violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

Alltime = 0
n = int(input('Сколько песен выбрать?\n'))
for i in range(n):
    name = input(f'Название {str(1+i)} песни:\n')
    time = violator_songs[name]
    Alltime = time + Alltime
print(f'Общее время звучания песен: {Alltime}')

