from UI.view import View
from model.model import Model
import flet as ft
import datetime

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def set_dates(self):
        first, last = self._model.get_date_range()

        self._view.dp1.first_date = datetime.date(first.year, first.month, first.day)
        self._view.dp1.last_date = datetime.date(last.year, last.month, last.day)
        self._view.dp1.current_date = datetime.date(first.year, first.month, first.day)

        self._view.dp2.first_date = datetime.date(first.year, first.month, first.day)
        self._view.dp2.last_date = datetime.date(last.year, last.month, last.day)
        self._view.dp2.current_date = datetime.date(last.year, last.month, last.day)

    def setcategory(self):
        lista = self._model.get_category()
        for i in lista:
            self._view.dd_category.options.append(ft.dropdown.Option(i.name))
        self._view.update()

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """
        categoria = self._view.dd_category.value
        data_inizio = self._view.dp1.value
        data_fine = self._view.dp2.value
        self._model.crea_grafo(categoria,data_inizio,data_fine)
        self._view.txt_risultato.controls.append(ft.Text(f"Grafo correttamente creato"))
        self._view.txt_risultato.controls.append(ft.Text(f"numero nodi: {self._model.G.number_of_nodes()}"))
        self._view.txt_risultato.controls.append(ft.Text(f"numero archi: {self._model.G.number_of_edges()}"))
        self._view.update()

    def handle_best_prodotti(self, e):
        """ Handler per gestire la ricerca dei prodotti migliori """
        lista_prodotti = self._model.ricerca_prodotti()
        self._view.txt_risultato.controls.append(ft.Text(f"best_prodotti:"))
        for i in range(5):
            nodo = lista_prodotti[i][0]
            somma = lista_prodotti[i][1]
            self._view.txt_risultato.controls.append(ft.Text(f"{nodo} : {somma}"))
        self._view.update()


    def handle_cerca_cammino(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO
