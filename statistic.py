# Импорт используемых библиотек
import pandas as pd
import matplotlib.pyplot as plt
from log import log
import geopandas as gpd


# Получение данных из csv
df = pd.read_csv('steam_players.csv')

# Создание класса
class Stat:

    # Логгирование ф-ции
    @log
    # Функция создания гистограммы
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

        # Показ гистограммы
        plt.tight_layout()
        plt.show()

    # Логгирование ф-ции
    @log
    # Функция создания тепловой карты
    def map():
        # Группируем данные по странам
        country_counts = df['country'].value_counts().reset_index()
        country_counts.columns = ['country', 'count']

        # Загружаем карту мира 
        world = gpd.read_file("data/ne_110m_admin_0_countries.shp")  

        # Объединяем данные с картой 
        world = world.merge(country_counts, how='left', left_on='ADMIN', right_on='country')
        world['count'] = world['count'].fillna(0) 

        # Строим тепловую карту
        fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        world.plot(column='count', cmap='Reds', linewidth=0.8, edgecolor='black', legend=True, ax=ax)
        
        # Показ тепловой карты
        ax.set_title("Количество игроков Steam", fontsize=15)
        plt.show()