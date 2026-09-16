import customtkinter as ctk

# Apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class VentanaYarvis(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ANNA - Asistente Personal")
        self.geometry("900x600")
        self.resizable(False, False)

        # Título
        self.titulo = ctk.CTkLabel(
            self,
            text="ANNA - Asistente Personal",
            font=("Segoe UI", 30, "bold")
        )
        self.titulo.pack(pady=20)

        # Estado
        self.estado = ctk.CTkLabel(
            self,
            text="● Esperando activación...",
            font=("Segoe UI", 18)
        )
        self.estado.pack(pady=10)

        # Historial
        self.historial = ctk.CTkTextbox(
            self,
            width=800,
            height=350
        )
        self.historial.pack(pady=20)

        # Botón
        self.boton = ctk.CTkButton(
            self,
            text="Iniciar",
            width=200
        )
        self.boton.pack(pady=20)


if __name__ == "__main__":
    app = VentanaYarvis()
    app.mainloop()