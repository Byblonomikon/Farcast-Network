# Script per a afegir el fitxer (encriptat previament amb CCript) a l’IPFS i obtenir el HASH IPFS resultant



import tkinter as tk
from tkinter import filedialog
from ipfshttpclient import connect

def add_file_to_ipfs(file_path):
    # Connecta amb el node (Nodium)  IPFS local
    ipfs = connect('/ip4/127.0.0.1/tcp/5001/http')

    # Llegeix el contingut del fitxer
    with open(file_path, "rb") as file:
        file_contents = file.read()

    # Emmagatzema el contingut del fitxer a IPFS
    res = ipfs.add_bytes(file_contents)
    
    return res['Hash']

def handle_drop(event):
    file_path = event.data
    file_hash = add_file_to_ipfs(file_path)
    status_label.config(text=f"Fitxer emmagatzemat a IPFS amb hash: {file_hash}")

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_hash = add_file_to_ipfs(file_path)
        status_label.config(text=f"Fitxer emmagatzemat a IPFS amb hash: {file_hash}")

# Crear finestra
root = tk.Tk()
root.title("IPFS File Uploader")

# Etiqueta d'estat
status_label = tk.Label(root, text="", padx=10, pady=10)
status_label.pack()

# Configurar zona de drag and drop
drop_zone = tk.Label(root, text="Arrossega i deixa anar aquí els fitxers", borderwidth=2, relief="groove", height=10)
drop_zone.pack(fill="both", expand=True)
drop_zone.bind("<Drop>", handle_drop)

# Configurar botó de navegació
browse_button = tk.Button(root, text="Navegar...", command=browse_file)
browse_button.pack()

root.mainloop()


