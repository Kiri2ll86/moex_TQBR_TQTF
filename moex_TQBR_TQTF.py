import requests
import datetime
import pathlib
import apimoex
import pandas as pd
import concurrent.futures

board_list = ['TQBR', 'TQTF'] #список досок(акции, рублевые фонды)
num_threads = 10 
with open("E:/project_moex/TICK.txt", "r") as TICKs: #загружаем список тикеров из файла
    TICKs = [line.rstrip() for line in TICKs]

for board in board_list:
    pathlib.Path("E:/project_moex/Database/{}".format(board)).mkdir(parents=True, exist_ok=True) #создаем каталог для сохранения файлов Excel с данными
    
    def process_ticker(session, TICK): 
        data = apimoex.get_board_history(session, TICK, board=board) #функция API для загрузки данных с MOEX, метод get_board_history - получаем данные по каждому тикеру
        if data == []:
            return
        df = pd.DataFrame(data)
        df = df[['TRADEDATE','CLOSE']]
        df.to_excel("E:/project_moex/Database/{}/{}.xlsx".format(board,TICK), index=False)

    with requests.Session() as session: #сеанс устанавливает соединение с сервером MOEX
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor: 
            futures = []
            for TICK in TICKs:
                futures.append(executor.submit(process_ticker, session, TICK))
            
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(e)

