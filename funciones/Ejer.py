import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Salud de Residentes")

        self.create_widgets()

    def create_widgets(self):
        self.tabControl = ttk.Notebook(self.root)

        self.tab_residentes = ttk.Frame(self.tabControl)
        self.tab_incidencias = ttk.Frame(self.tabControl)
        self.tab_reportes = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab_residentes, text='Residentes')
        self.tabControl.add(self.tab_incidencias, text='Incidencias')
        self.tabControl.add(self.tab_reportes, text='Reportes')

        self.tabControl.pack(expand=1, fill="both")

        self.create_residentes_tab()
        self.create_incidencias_tab()
        self.create_reportes_tab()

    def create_residentes_tab(self):
        ttk.Label(self.tab_residentes, text="Gestión de Residentes").grid(column=0, row=0, padx=10, pady=10)

        self.residente_tree = ttk.Treeview(self.tab_residentes,
                                           columns=("ID", "Nombre", "Edad", "Género", "Habitación"), show='headings')
        self.residente_tree.heading("ID", text="ID")
        self.residente_tree.heading("Nombre", text="Nombre")
        self.residente_tree.heading("Edad", text="Edad")
        self.residente_tree.heading("Género", text="Género")
        self.residente_tree.heading("Habitación", text="Habitación")

        self.residente_tree.grid(column=0, row=1, padx=10, pady=10, columnspan=4)

        ttk.Button(self.tab_residentes, text="Agregar Residente", command=self.agregar_residente).grid(column=0, row=2,
                                                                                                       padx=10, pady=10)
        ttk.Button(self.tab_residentes, text="Editar Residente", command=self.editar_residente).grid(column=1, row=2,
                                                                                                     padx=10, pady=10)
        ttk.Button(self.tab_residentes, text="Eliminar Residente", command=self.eliminar_residente).grid(column=2,
                                                                                                         row=2, padx=10,
                                                                                                         pady=10)

    def agregar_residente(self):
        pass

    def editar_residente(self):
        pass

    def eliminar_residente(self):
        pass

    def create_incidencias_tab(self):
        ttk.Label(self.tab_incidencias, text="Gestión de Incidencias").grid(column=0, row=0, padx=10, pady=10)

        self.incidencia_tree = ttk.Treeview(self.tab_incidencias, columns=(
        "ID Incidencia", "ID Residente", "Fecha", "Síntomas", "Diagnóstico", "Tratamiento", "Estado Actual"),
                                            show='headings')
        self.incidencia_tree.heading("ID Incidencia", text="ID Incidencia")
        self.incidencia_tree.heading("ID Residente", text="ID Residente")
        self.incidencia_tree.heading("Fecha", text="Fecha")
        self.incidencia_tree.heading("Síntomas", text="Síntomas")
        self.incidencia_tree.heading("Diagnóstico", text="Diagnóstico")
        self.incidencia_tree.heading("Tratamiento", text="Tratamiento")
        self.incidencia_tree.heading("Estado Actual", text="Estado Actual")

        self.incidencia_tree.grid(column=0, row=1, padx=10, pady=10, columnspan=4)

        ttk.Button(self.tab_incidencias, text="Agregar Incidencia", command=self.agregar_incidencia).grid(column=0,
                                                                                                          row=2,
                                                                                                          padx=10,
                                                                                                          pady=10)
        ttk.Button(self.tab_incidencias, text="Editar Incidencia", command=self.editar_incidencia).grid(column=1, row=2,
                                                                                                        padx=10,
                                                                                                        pady=10)
        ttk.Button(self.tab_incidencias, text="Eliminar Incidencia", command=self.eliminar_incidencia).grid(column=2,
                                                                                                            row=2,
                                                                                                            padx=10,
                                                                                                            pady=10)

    def agregar_incidencia(self):
        pass

    def editar_incidencia(self):
        pass

    def eliminar_incidencia(self):
        pass

    def create_reportes_tab(self):
        ttk.Label(self.tab_reportes, text="Generación de Reportes").grid(column=0, row=0, padx=10, pady=10)

        ttk.Button(self.tab_reportes, text="Generar Reporte", command=self.generar_reporte).grid(column=0, row=1,
                                                                                                 padx=10, pady=10)

    def generar_reporte(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
