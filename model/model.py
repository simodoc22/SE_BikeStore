from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.Dao = DAO()
        self.elenco_categorie= self.Dao.get_category()
        self.dizionario_categoria = {}
        for i in self.elenco_categorie:
            self.dizionario_categoria[i.name]=i.id
        self.G = nx.DiGraph()
        self.lista_calcolo_prodotti= []

    def get_date_range(self):
        return self.Dao.get_date_range()

    def get_category(self):
        return self.elenco_categorie

    def crea_grafo(self,categoria,data_inizio,data_fine):
        dizionario_ordini_per_prodotto = self.Dao.get_order(data_inizio,data_fine)
        id_categoria = self.dizionario_categoria[categoria]
        elenco_prodotti = self.Dao.get_prodotti(id_categoria)
        for i in elenco_prodotti:
            self.G.add_node(i)
        for node in self.G.nodes():
            for node2 in self.G.nodes():
                somma = 0
                if node!=node2:
                    try:
                        lunghezza_node = len(dizionario_ordini_per_prodotto[node.id])
                        lunghezza_node2= len(dizionario_ordini_per_prodotto[node2.id])
                    except KeyError:
                        continue
                    if lunghezza_node>0 and lunghezza_node2>0:
                        somma = lunghezza_node + lunghezza_node2
                        if lunghezza_node>lunghezza_node2:
                            self.G.add_edge(node,node2,weight=somma)
                        if lunghezza_node<lunghezza_node2:
                            self.G.add_edge(node2,node,weight=somma)
                        if lunghezza_node==lunghezza_node2:
                            self.G.add_edge(node2,node,weight=somma)
                            self.G.add_edge(node,node2,weight=somma)

    def ricerca_prodotti(self):
        for node in self.G.nodes():
            self.calcola_best(node)
        ordinata = sorted(self.lista_calcolo_prodotti,key=lambda x: x[1],reverse=True)
        return ordinata

    def calcola_best(self,node):
        somma_uscenti = 0
        somma_entranti = 0
        for node2 in self.G.nodes():
            if self.G.has_edge(node,node2):
                peso = self.G[node][node2]['weight']
                somma_uscenti += peso

        for node2 in self.G.nodes():
            if self.G.has_edge(node2,node):
                peso = self.G[node2][node]['weight']
                somma_entranti += peso
        somma = somma_uscenti-somma_entranti
        self.lista_calcolo_prodotti.append((node,somma))












