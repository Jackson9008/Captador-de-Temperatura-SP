import requests
import tkinter as tk
from tkinter import messagebox
from excel_handler import salvar_em_excel    # type: ignore
from datetime import datetime

API_KEY = "54b219313269a13f41f7dc54cb3fb2c6"
CIDADE = "Sao Paulo"
UNIDADE = "metric"

def captar_dados():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units={UNIDADE}&lang=pt_br"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        temperatura = f"{data['main']['temp']}°C"
        umidade = f"{data['main']['humidity']}%"
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        return agora, temperatura, umidade
    except Exception:
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "Erro", "Erro"