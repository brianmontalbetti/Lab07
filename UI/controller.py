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
    def popola_dropdowns(self):
        biblioteche = self._model.get_biblioteche()
        generi = self._model.get_generi()

        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))
        self._view.dd_genere.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))

        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

        self._view.update()

    def callback_biblioteca(self, e):
        valore = e.control.value
        if valore == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.genere_selezionato = valore

    def callback_genere(self, e):
        valore = e.control.value
        if valore == "Nessun filtro" or valore is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    def mostra_libri(self,e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        self._view.lista_libri.controls.clear()

        if len(libri) == 0:
            self._view.show_alert("Nessun libro trovato con i criteri selezionati.")
        else:
            for libro in libri:
                testo = f"Titolo: {libro.titolo},  |  Autore: {libro.autore}  |  Genere: {libro.genere}"
                self._view.lista_libri.controls.append(ft.Text(testo))

        self._view.update()