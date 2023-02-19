from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

produtos = [
    {'codigo': '100', 'nome':'Macarrão', 'preco':'20.0', 'qtde':'10'},
    {'codigo': '101', 'nome':'Arroz', 'preco':'21.0', 'qtde':'1'},
    {'codigo': '102', 'nome':'Feijão 2kg', 'preco':'12.0', 'qtde':'1'},
    {'codigo': '103', 'nome':'Açucar', 'preco':'16.0', 'qtde':'1'},
]

#Classes RecycleViews
class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    touch_deselect_last = BooleanProperty(True)


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = []
#Fim classes RecycleViews

class VendasWindow(BoxLayout):
    #Janela do App
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def admin(self):
        pass

    def sair(self):
        pass

    def deletar(self):
        pass

    def atualizar(self):
        pass

    def pesquisar_nome_produto(self, nome_produto):
        pass

    def pesquisar_codigo_produto(self, codigo_produto):
        for produto in produtos:
            if codigo_produto == produto['codigo']:
                #print("Foi localizado ", produto)
                artigo = {}
                artigo['codigo'] = produto['codigo']
                artigo['nome'] = produto['nome']
                artigo['preco'] = float(produto['preco']) / float(produto['qtde'])
                artigo['qtdade_carro'] = 1
                artigo['qtdade_produtos'] = produto['qtde']
                artigo['preco_total'] = produto['preco']

                self.ids.rvs.data.append(artigo)
                break

    def pagar(self):
        pass 

    def nova_compra(self):
        pass

class VendasApp(App):
    #Monta a aplicação
    def build(self):
        return VendasWindow()
    
if __name__ == '__main__':
    VendasApp().run()