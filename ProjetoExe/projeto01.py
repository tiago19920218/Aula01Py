
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def ler_excel(caminho_arquivo):
    
    try:
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        return df
    except Exception as e:
        messagebox.showerror("Erro ao ler o arquivo Excel", str(e))
    return None

def gerar_graficos(df, pasta_salvar):

    colunas_numericas = df.select_dtypes(include='number').colums.tolist()
    if not colunas_numericas:
        messagebox.showerror("Erro", "Nenhuma coluna numérica encontrada para gerar gráficos.")
        return
    
    col = colunas_numericas[0]

    #GRÁFICO DE BARRAS
    plt .figure(figsize=(8,5))
    df[col].value_counts().plot(kind='bar',color='skyblue')
    plt.title('Gráfico de Barras')
    plt.xlabel(col)
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_salvar,'grafico_barras.png'))
    plt.show()

    #GRÁFICO DE LINHAS
    plt.figure(figsize=(8,5))
    df[col].plot(kind='line', color='green')
    plt.title('Gráfico de Linhas')
    plt.xlabel('Indice')
    plt.ylabel(col)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_salvar, 'grafico_linhas.png'))
    plt.show()

    #GRÁFICO DE PIZZA
    plt.figure(figsize=(6,6))
    df[col].value_counts().head(5).plot(kind='pie', autopct='1%.1%%', startangle=90)
    plt.title("Gráfico de Pizza (Top 5)")
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(os.phat.join(pasta_salvar, 'grafico_pizza.png'))
    plt.show()

    #GRÁFICO DE HISTOGRAMA
    plt.figure(figsize=(8,5))
    df[col].plot(kind='hist', bins=20, color='orange')
    plt.title('Histograma')
    plt.xlabel(col)
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_salvar, 'histograma.png'))
    plt.show()

def selecionar_arquivo():
    """
    Bloco 3: Interface gráfica (Slide 6)
    Abre diálogo para o usuário escolher arquivo Excel (.xlsx).
    Atualiza campo de texto com o caminho escolhido.
    """
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
    if caminho:
        entry_arquivo.delete(0, tk.END)  # Limpa campo de texto
        entry_arquivo.insert(0, caminho)  # Insere caminho selecionado

def processar_arquivo():
    """
    Função que é chamada ao clicar "Ler Arquivo" (Slide 6)
    - Lê o arquivo Excel usando a função ler_excel()
    - Mostra estatísticas básicas no campo de texto
    - Habilita botão "Gerar Gráficos" se a leitura for bem-sucedida
    """
    caminho = entry_arquivo.get()
    if not caminho:
        messagebox.showwarning("Aviso", "Por favor, selecione um arquivo Excel antes.")
        return
    
    df = ler_excel(caminho)
    if df is not None:
        text_output.delete('1.0', tk.END)  # Limpa área de texto
        text_output.insert(tk.END, df.describe().to_string())  # Exibe estatísticas (média, desvio, quartis...)
        global df_global
        df_global = df  # Armazena DataFrame global para usar na geração dos gráficos
        gerar_button.config(state=tk.NORMAL)  # Habilita botão gerar gráficos

def gerar():
    """
    Função acionada ao clicar "Gerar Gráficos" (Slide 6)
    Abre diálogo para escolher pasta onde salvar os gráficos e chama geração.
    """
    pasta = filedialog.askdirectory(title="Selecione a pasta para salvar os gráficos")
    if not pasta:
        return
    gerar_graficos(df_global, pasta)


def main():
    """
    Bloco 4: Interface principal (Slide 6 e 7)
    Configura janela, widgets, layout e inicia o loop da interface Tkinter.
    """
    global entry_arquivo, text_output, gerar_button
 
    root = tk.Tk()
    root.title("Visualizador de Dados Excel")
    root.geometry("700x550")
 
    frame = tk.Frame(root)
    frame.pack(pady=10)
 
    # Label e campo para exibir o caminho do arquivo Excel
    tk.Label(frame, text="Selecione o arquivo Excel (.xlsx):").grid(row=0, column=0, sticky="w")
 
    entry_arquivo = tk.Entry(frame, width=55)
    entry_arquivo.grid(row=1, column=0, padx=5)
 
    # Botão para abrir diálogo de seleção de arquivo
    tk.Button(frame, text="Procurar", command=selecionar_arquivo).grid(row=1, column=1)
 
    # Botão para ler o arquivo selecionado
    tk.Button(frame, text="Ler Arquivo", command=processar_arquivo).grid(row=2, column=0, pady=10)
 
    1# Botão para gerar gráficos, inicialmente desativado (ativo após leitura válida)
    gerar_button = tk.Button(frame, text="Gerar Gráficos", command=gerar, state=tk.DISABLED)
    gerar_button.grid(row=2, column=1, pady=10)
 
    #2 Área de texto para exibir estatísticas dos dados
    text_output = tk.Text(root, height=18, width=80)
    text_output.pack(padx=10, pady=10)
 
    root.mainloop()
 
if __name__ == '__name__':
    """
    Bloco 5: Execução principal (Slide 7)
    Roda a interface gráfica principal ao executar o script.
    """
    main()
    