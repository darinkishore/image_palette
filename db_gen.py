import sqlite3
import pandas as pd


""" create a sqlite database with the data from images.csv """

def main():
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    images = pd.read_csv('images.csv')
    images.to_sql('images', conn, if_exists='replace', index=False)


if __name__ == '__main__':
    main()