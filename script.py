import pandas as pd
import gspread

# Изменяем таблицу из Эвотора, удаляя ненужные столбцы
# Сохраняем в новый файл, с которого пойдет обновление в гугл таблицу
sheet = pd.read_excel("goods.xlsx", index_col=None, header=None)
unwanted_columns = [0, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
sheetNew = sheet.drop(unwanted_columns, axis = 1)
sheetNew.to_excel("goodsNew.xlsx", header=False, index=False)

# Креды сервисного аккаунта
gc = gspread.service_account(filename='goodsevo-New.json')

# ID существующего документа
wks = gc.open_by_key('1AjQbrkUbEXUnQK76QwwHDPTnKe6cRdVeVpMNZ4HlNJE').sheet1

# Очищаем табличку
wks.spreadsheet.values_clear(
    'Прайс-лист'
)

# Обновляем отформатированную данные
wks.spreadsheet.values_update(
    'Прайс-лист',
    params= {
        'valueInputOption': 'USER_ENTERED'
    },
    body= {
        'values': sheetNew.values.tolist()
    }
)
