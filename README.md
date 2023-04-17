# moex_TQBR_TQTF
## Основные возможности
+ Программа по заданным тикерам рублевых акций(TQBR) и фондов(TQTF), торгующихся на московской бирже отслеживает их цену на конец торговой сессии. 
+ Программа формирует .xlsx файлы отдельно для каждого тикера, где можно просмотреть как менялась стоимость акций за всю историю торгов в данном режиме, удобно для формирования своего инвестиционного портфеля и отслеживания кореляции между активами.
+ Отдельно добавлена функция, которая создает один .xlsx файл, куда в столбец помещаются все заданные тикеры, удобно для построения портфеля по Марковицу.
## Начало работы
- Установите необходимые библиотеки
```
pip install xlsxwriter
```
```
pip install openpyxl
```
```
pip install apimoex
```
- Внесите в текстовый документ `TICK.txt` необходимые тикеры, например `SBER, GAZP`
- После запуска программы в папке `Database` сформируются необходимые .xlsx файлы 
## Результат
![Image alt](https://github.com/Kiri2ll86/moex_TQBR_TQTF/blob/main/1.jpg)
_________________________________________________________________________
![Image alt](https://github.com/Kiri2ll86/moex_TQBR_TQTF/blob/main/2.jpg)
