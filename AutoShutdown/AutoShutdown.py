import tkinter as tk
from tkinter import ttk, messagebox
import os

def executar_comando():
    try:
        # 1. Obter o tempo digitado
        tempo_str = entrada_tempo.get().replace(',', '.') # Garante que virgulas funcionem como pontos
        if not tempo_str:
            messagebox.showwarning("Aviso", "Por favor, digite um tempo.")
            return
        
        tempo = float(tempo_str)
        
        # 2. Converter para segundos
        unidade = var_unidade.get()
        if unidade == "Horas":
            segundos = int(tempo * 3600)
            msg_tempo = f"{tempo} horas"
        elif unidade == "Minutos":
            segundos = int(tempo * 60)
            msg_tempo = f"{tempo} minutos"
        else: # Segundos (opcional, mas bom ter)
            segundos = int(tempo)
            msg_tempo = f"{tempo} segundos"

        # 3. Definir a ação (Desligar ou Reiniciar)
        acao = var_acao.get()
        parametro = "/s" if acao == "Desligar" else "/r"
        acao_verbo = "desligado" if acao == "Desligar" else "reiniciado"

        # 4. Executar o comando no Windows
        # /t = tempo em segundos, /f = força o fechamento de apps
        comando = f"shutdown {parametro} /t {segundos} /f"
        os.system(comando)
        
        lbl_status.config(text=f"Agendado: {acao} em {msg_tempo}.", fg="green")
        messagebox.showinfo("Sucesso", f"O PC será {acao_verbo} em {msg_tempo}.")
        
    except ValueError:
        messagebox.showerror("Erro", "O tempo deve ser um número válido.")

def cancelar_agendamento():
    # O comando /a aborta qualquer desligamento agendado
    os.system("shutdown /a")
    lbl_status.config(text="Agendamento cancelado!", fg="red")
    messagebox.showinfo("Cancelado", "O desligamento automático foi cancelado.")

# --- Configuração da Interface (GUI) ---
janela = tk.Tk()
janela.title("Timer Desligamento")
janela.geometry("350x300")
janela.resizable(False, False)

# Estilos e Layout
pad_y = 10

# Título
tk.Label(janela, text="Configurar Timer", font=("Arial", 14, "bold")).pack(pady=pad_y)

# Entrada de Tempo
frame_tempo = tk.Frame(janela)
frame_tempo.pack(pady=5)
tk.Label(frame_tempo, text="Tempo:").pack(side=tk.LEFT, padx=5)
entrada_tempo = tk.Entry(frame_tempo, width=10)
entrada_tempo.pack(side=tk.LEFT)

# Seleção de Unidade (Radio Buttons)
frame_unidade = tk.Frame(janela)
frame_unidade.pack(pady=5)
var_unidade = tk.StringVar(value="Minutos")
tk.Radiobutton(frame_unidade, text="Minutos", variable=var_unidade, value="Minutos").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(frame_unidade, text="Horas", variable=var_unidade, value="Horas").pack(side=tk.LEFT, padx=5)

# Seleção de Ação (Radio Buttons)
frame_acao = tk.Frame(janela)
frame_acao.pack(pady=5)
tk.Label(frame_acao, text="Ação:").pack(side=tk.LEFT)
var_acao = tk.StringVar(value="Desligar")
tk.Radiobutton(frame_acao, text="Desligar", variable=var_acao, value="Desligar").pack(side=tk.LEFT)
tk.Radiobutton(frame_acao, text="Reiniciar", variable=var_acao, value="Reiniciar").pack(side=tk.LEFT)

# Botão Agendar
btn_agendar = tk.Button(janela, text="AGENDAR", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=executar_comando)
btn_agendar.pack(pady=10, ipadx=20)

# Botão Cancelar (Importante ter!)
btn_cancelar = tk.Button(janela, text="Cancelar Agendamento", command=cancelar_agendamento)
btn_cancelar.pack(pady=5)

# Status
lbl_status = tk.Label(janela, text="", font=("Arial", 9))
lbl_status.pack(pady=10)

janela.mainloop()