
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os
from client_config import get_client

def verificar_atualizacoes():
    client = get_client()
    client.refresh()
    app_update = client.update_check('YoutubeMP3App', '1.0.0')
    if app_update:
        if messagebox.askyesno("Atualização", "Nova versão disponível! Atualizar agora?"):
            app_update.download()
            if app_update.is_downloaded():
                app_update.extract_restart()

def baixar_mp3():
    link = entrada.get()
    if not link:
        messagebox.showerror("Erro", "Por favor, insira o link do YouTube.")
        return

    salvar_como = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                filetypes=[("MP3 files", "*.mp3")],
                                                title="Salvar como")

    if not salvar_como:
        return

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': salvar_como,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'noplaylist': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        messagebox.showinfo("Sucesso", "Download e conversão concluídos com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

root = tk.Tk()
root.title("YouTube para MP3")
root.geometry("400x150")
verificar_atualizacoes()

tk.Label(root, text="Cole o link do YouTube:").pack(pady=10)
entrada = tk.Entry(root, width=50)
entrada.pack()

btn = tk.Button(root, text="Converter para MP3", command=baixar_mp3)
btn.pack(pady=20)

root.mainloop()
