# Импорт используемых библиотек
import pandas as pd
import matplotlib.pyplot as plt
from log import log


# Получение данных из csv
df = pd.read_csv('steam_players.csv')

# Создание класса
class Stat:

    # Логгирование ф-ции
    @log
    def statistic():
        # Группировка данных по странам и подсчет количества playerid
        country_stats = df.groupby('country')['playerid'].nunique().reset_index()

        country_stats.columns = ['Страна', 'Количество игроков']

        country_stats['Игроки (сотни тысяч)'] = country_stats['Количество игроков'] / 100000

        # Создание гистограммы
        plt.figure(figsize=(16, 9))
        plt.bar(country_stats['Страна'], country_stats['Игроки (сотни тысяч)'], color='skyblue')
        plt.title('Количество игроков Steam')
        plt.ylabel('В сотнях тысяч)')
        plt.xticks(rotation=90)
        plt.grid(axis='y')

        # Убираем пустые места по бокам
        plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.25)

        # Показ гистограммы
        plt.tight_layout()
        plt.show()