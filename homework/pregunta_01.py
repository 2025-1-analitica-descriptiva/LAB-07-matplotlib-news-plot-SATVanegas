"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    df = pd.read_csv("files/input/news.csv")
    print(df)

    # Estilo de la gráfica
    plt.figure(figsize=(10, 7))
    plt.plot(df["Unnamed: 0"], df["Television"], label="Television", color="gray", linewidth=2.5)
    plt.plot(df["Unnamed: 0"], df["Newspaper"], label="Newspaper", color="dimgray", linewidth=2.5)
    plt.plot(df["Unnamed: 0"], df["Internet"], label="Internet", color="dodgerblue", linewidth=3, marker='o')
    plt.plot(df["Unnamed: 0"], df["Radio"], label="Radio", color="lightgray", linewidth=2.5)

    # Etiquetas de puntos iniciales y finales
    plt.text(2001, 74, "Television 74%", va='center', ha='right', color='gray')
    plt.text(2010, 66, "66%", va='center', ha='left', color='gray')

    plt.text(2001, 45, "Newspaper 45%", va='center', ha='right', color='gray')
    plt.text(2010, 31, "31%", va='center', ha='left', color='gray')

    plt.text(2001, 13, "Internet 13%", va='center', ha='right', color='dodgerblue')
    plt.text(2010, 41, "41%", va='center', ha='left', color='dodgerblue')

    plt.text(2001, 18, "Radio 18%", va='center', ha='right', color='lightgray')
    plt.text(2010, 16, "16%", va='center', ha='left', color='lightgray')

    # Título y subtítulo
    plt.title("How people get their news", fontsize=16, weight='bold')
    plt.suptitle("An increasing proportion cite the internet as their primary news source", fontsize=10, y=0.91)

    # Ejes
    plt.xticks(df["Unnamed: 0"])
    plt.yticks([])
    plt.grid(False)
    plt.tick_params(left=False, bottom=False)

    # Eliminar marco
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    # Guardar gráfico
    os.makedirs("files/plots", exist_ok=True)
    output_path = "files/plots/news.png"
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    plt.show()