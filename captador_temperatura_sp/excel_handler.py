
import openpyxl
from openpyxl import Workbook
import os

def salvar_em_excel(data, temperatura, umidade):
    arquivo = 'temperaturas.xlsx'

    if os.path.exists(arquivo):
        wb = openpyxl.load_workbook(arquivo)
        sheet = wb.active
    else:
        wb = Workbook()
        sheet = wb.active
        sheet.append(["Data/Hora", "Temperatura", "Umidade"])

    sheet.append([data, temperatura, umidade])
    wb.save(arquivo)
