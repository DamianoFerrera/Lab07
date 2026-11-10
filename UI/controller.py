import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        self._view.dd_biblioteca.options.clear()
        self._view.dd_genere.options.clear()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))

        biblioteche = self._model.get_biblioteche()
        generi = self._model.get_generi()
        if biblioteche is None or generi is None:
            self._view.show_alert("Errore di connessione al database")
            return

        for biblioteca in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome))
        for genere in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(genere))
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def on_biblioteca_selezionata(self, e):
        valore = self._view.dd_biblioteca.value
        self.biblioteca_selezionata = None if valore == "Nessun filtro" else valore

    def on_genere_selezionato(self, e):
        valore = self._view.dd_genere.value
        self.genere_selezionato = None if valore == "Nessun filtro" else valore

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        self._view.lista_libri.controls.clear()

        if libri is None:
            self._view.show_alert("Errore di connessione al database")
        elif len(libri) == 0:
            self._view.show_alert("Nessun libro soddisfa i criteri di filtraggio")
        else:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(str(libro), size=16))
        self._view.update()
