import matplotlib.pyplot as plt

# Dados
dados = [
    (53906, 5.00, 0.00),
    (54308, 4.88, 0.12),
    (54711, 4.69, 0.31),
    (55113, 4.51, 0.49),
    (55516, 4.33, 0.67),
    (55918, 4.16, 0.84),
    (56321, 3.99, 1.01),
    (56723, 3.84, 1.16),
    (57124, 3.69, 1.31)
]

# Separando os dados
x = [item[0] for item in dados]
y1 = [item[1] for item in dados]  # azul
y2 = [item[2] for item in dados]  # laranja

# --- Gráfico 1: azul e laranja ---
plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='blue', label='Y1 (Azul)')
plt.plot(x, y2, color='orange', label='Y2 (Laranja)')
plt.xlabel('X')
plt.ylabel('Valores')
plt.title('Gráfico com as duas linhas')
plt.legend()
plt.grid(True)
plt.savefig("grafico_geral.png", dpi=300, bbox_inches="tight")
plt.close()

# --- Gráfico 2: apenas linha laranja ---
plt.figure(figsize=(10, 6))
plt.plot(x, y2, color='orange', label='Y2 (Laranja)')
plt.xlabel('X')
plt.ylabel('Valores')
plt.title('Gráfico apenas da linha laranja')
plt.legend()
plt.grid(True)
plt.savefig("grafico_laranja.png", dpi=300, bbox_inches="tight")
plt.close()

# --- Gráfico 3: apenas linha azul ---
plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='blue', label='Y1 (Azul)')
plt.xlabel('X')
plt.ylabel('Valores')
plt.title('Gráfico apenas da linha azul')
plt.legend()
plt.grid(True)
plt.savefig("grafico_azul.png", dpi=300, bbox_inches="tight")
plt.close()

print("✅ Gráficos salvos na pasta 'assets'!")
