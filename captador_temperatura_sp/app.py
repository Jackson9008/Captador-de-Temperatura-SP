
import tkinter as tk
from tkinter import messagebox
from scraper import captar_dados # type: ignore
from excel_handler import salvar_em_excel # type: ignore

def buscar_e_salvar():
    try:
        data, temperatura, umidade = captar_dados()
        salvar_em_excel(data, temperatura, umidade)
        mensagem = f"Dados capturados:\n\n📅 {data}\n🌡️ {temperatura}\n💧 {umidade}"
        messagebox.showinfo("Sucesso", mensagem)
    except Exception as e:
        messagebox.showerror("Erro na Automação", f"Não foi possível buscar os dados.\n\nErro: {str(e)}")

janela = tk.Tk()
janela.title("Captador de Temperatura de São Paulo - UniFecaf - 2025")
janela.geometry("800x500")
janela.configure(bg="#f8f8f8")

titulo = tk.Label(janela, text="Previsão do tempo de São Paulo", font=("Helvetica", 30, "bold"), bg="#f8f8f8")
titulo.pack(pady=20)

descricao = tk.Label(janela, text="Clique no botão para atualizar a previsão na planilha:", font=("Helvetica", 12), bg="#f8f8f8")
descricao.pack(pady=5)

btn = tk.Button(janela, text="Buscar Previsão", font=("Helvetica", 14, "bold"), bg="#2EC233", fg="white",border=5, width=20, height=2, command=buscar_e_salvar)
btn.pack(pady=40)

descricao = tk.Label(janela, text="Portfólio - Development Python - UniFecaf - 2025", font=("Helvetica", 12), bg="#f8f8f8")
descricao.pack(pady=50)


descricao = tk.Label(janela, text="Todos os direitos reservados por Jackson@ - UniFecaf - 2025", font=("Helvetica", 12), bg="#f8f8f8")
descricao.pack(pady=40)

janela.mainloop()
