import requests
import datetime
import pathlib
import apimoex
import pandas as pd
import concurrent.futures

board_list = ['TQBR', 'TQTF'] # список досок(акции, рублевые фонды)
num_threads = 10 

with open("TICK.txt", "r") as TICKs: # загружаем список тикеров из файла
    TICKs = [line.rstrip() for line in TICKs]

for board in board_list:
    pathlib.Path(".../Database/{}".format(board)).mkdir(parents=True, exist_ok=True) # создаем каталог для сохранения файлов Excel с данными
    
    def process_ticker(session, TICK): 
        data = apimoex.get_board_history(session, TICK, board=board) # функция API для загрузки данных с MOEX, метод get_board_history - получаем данные по каждому тикеру
        if data == []:
            return
        df = pd.DataFrame(data)
        df = df[['TRADEDATE','CLOSE']]
        df['TICKER'] = TICK
        df.to_excel(".../Database/{}/{}.xlsx".format(board,TICK), index=False)
        return df

    with requests.Session() as session: # сеанс устанавливает соединение с сервером MOEX
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor: 
            futures = []
            dfs = []
            for TICK in TICKs:
                futures.append(executor.submit(process_ticker, session, TICK))
            for future in concurrent.futures.as_completed(futures):
                try:
                    df = future.result()
                    if df is not None:
                        dfs.append(df)
                except Exception as e:
                    print(e)
            # Объединяем данные из всех датафреймов в один датафрейм и записываем в файл Excel
            if len(dfs) > 0:
                combined_df = pd.concat(dfs)
                combined_df.to_excel(".../Database/{}.xlsx".format(board), index=False)


