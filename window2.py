#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import networkx as nx
import matplotlib.pyplot as plt
import json

from matplotlib.backends.backend_wxagg import \
    FigureCanvasWxAgg as FigCanvas, \
    NavigationToolbar2WxAgg as NavigationToolbar


class Window2(wx.Frame):
    def __init__(self, parent, **kw):
        super(Window2, self).__init__(parent=parent, **kw)
        self.G = nx.DiGraph()
        self.Maximize(True)
        self.SetTitle('Edycja grafu')
        self.InitUI()
        self.Centre()
        self.Show()

    with open("moje_dane1.json") as plik:
        moje_dane = json.load(plik)

    def InitUI(self):
        self.rightpanel, panel = self.panel()

        self.sizer1 = wx.GridBagSizer(1, 1)

        self.window3 = wx.TextCtrl(panel)
        self.sizer1.Add(self.window3, pos=(1, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.button2 = wx.Button(panel, label='Dodaj wierzchołek')
        self.button2.Bind(wx.EVT_BUTTON, self.OnDodajWierzcholek)
        self.sizer1.Add(self.button2, pos=(2, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.sizer2 = wx.GridBagSizer(2, 3)

        self.window5 = wx.TextCtrl(panel)
        self.sizer2.Add(self.window5, pos=(1, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.text5 = wx.StaticText(panel, label="i")
        self.sizer2.Add(self.text5, pos=(1, 2), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.window6 = wx.TextCtrl(panel)
        self.sizer2.Add(self.window6, pos=(1, 3), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.text5 = wx.StaticText(panel, label="O wadze:")
        self.sizer2.Add(self.text5, pos=(2, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.window4 = wx.TextCtrl(panel)
        self.sizer2.Add(self.window4, pos=(2, 3), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.button3 = wx.Button(panel, label='Dodaj krawędź')
        self.button3.Bind(wx.EVT_BUTTON, self.OnDodajWage)
        self.sizer2.Add(self.button3, pos=(3, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.sizer4 = wx.GridBagSizer(2, 3)

        self.windowk1 = wx.TextCtrl(panel)
        self.sizer4.Add(self.windowk1, pos=(1, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.textk = wx.StaticText(panel, label="i")
        self.sizer4.Add(self.textk, pos=(1, 2), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.windowk2 = wx.TextCtrl(panel)
        self.sizer4.Add(self.windowk2, pos=(1, 3), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.buttonk = wx.Button(panel, label='Usuń krawędź')
        self.buttonk.Bind(wx.EVT_BUTTON, self.OnUsunKrawedz)
        self.sizer4.Add(self.buttonk, pos=(3, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.sizer5 = wx.GridBagSizer(1, 1)

        self.windowu = wx.TextCtrl(panel)
        self.sizer5.Add(self.windowu, pos=(1, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.buttonu = wx.Button(panel, label='Usuń wierzchołek')
        self.buttonu.Bind(wx.EVT_BUTTON, self.OnUsunWierzcholek)
        self.sizer5.Add(self.buttonu, pos=(2, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.sizer3 = wx.GridBagSizer(1, 1)

        self.button4 = wx.Button(panel, label='Zapisz graf')
        self.button4.Bind(wx.EVT_BUTTON, self.OnSaveGraphName)
        self.sizer3.Add(self.button4, pos=(1, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.sizer1.AddGrowableCol(1)
        self.sizer2.AddGrowableCol(1)
        self.sizer4.AddGrowableCol(1)
        self.sizer5.AddGrowableCol(1)
        self.sizer3.AddGrowableCol(1)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 5
        box = wx.StaticBox(panel, 1, 'Dodaj wierzchołek:')
        nmSizer1 = wx.StaticBoxSizer(box, wx.VERTICAL)
        nmSizer1.Add(self.sizer1, 0, wx.ALL | wx.CENTER, b)

        box = wx.StaticBox(panel, 1, 'Dodaj krawędź pomiędzy wierzchołkami:')
        nmSizer2 = wx.StaticBoxSizer(box, wx.VERTICAL)
        nmSizer2.Add(self.sizer2, 0, wx.ALL | wx.CENTER, b)

        box = wx.StaticBox(panel, 1, 'Usuń krawędź pomiędzy wierzchołkami:')
        nmSizer4 = wx.StaticBoxSizer(box, wx.VERTICAL)
        nmSizer4.Add(self.sizer4, 0, wx.ALL | wx.CENTER, b)

        box = wx.StaticBox(panel, 1, 'Usuń wierzchołek:')
        nmSizer5 = wx.StaticBoxSizer(box, wx.VERTICAL)
        nmSizer5.Add(self.sizer5, 0, wx.ALL | wx.CENTER, b)

        box = wx.StaticBox(panel, 1, '')
        nmSizer3 = wx.StaticBoxSizer(box, wx.VERTICAL)
        nmSizer3.Add(self.sizer3, 0, wx.ALL | wx.CENTER, b)

        hsizer15 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer15.Add(nmSizer1, 1, wx.EXPAND | wx.CENTER, b)
        hsizer15.Add(nmSizer5, 1, wx.EXPAND | wx.CENTER, b)

        hsizer24 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer24.Add(nmSizer2, 1, wx.EXPAND | wx.CENTER, b)
        hsizer24.Add(nmSizer4, 1, wx.EXPAND | wx.CENTER, b)

        vsizer1.Add(hsizer15, 1, wx.EXPAND | wx.CENTER, b)
        vsizer1.Add(hsizer24, 1, wx.EXPAND | wx.CENTER, b)
        vsizer1.Add(nmSizer3, 1, wx.EXPAND | wx.CENTER, b)

        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        vsizer2.Add(self.rightpanel, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(vsizer1, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)
        hsizer.Add(vsizer2, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)

        panel.SetSizerAndFit(hsizer)

    class Grafy(wx.Window):
        def __init__(self, parent, id):
            wx.Window.__init__(self, parent, id, size=(200, 200), style=wx.BORDER_RAISED)
            self.Centre()

        def print_graph(self, g):
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self.fig = plt.figure(figsize=(9, 9), dpi=75)
            self.canvas = FigCanvas(self, -1, self.fig)
            pos = nx.circular_layout(g)
            nx.draw(g, pos)
            labels = nx.get_edge_attributes(g, 'weight')
            nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
            nx.draw(g, pos, with_labels=True, node_color='#A0CBE3', node_size=350)
            plt.axis('off')
            self.sizer.Add(self.canvas, 1, wx.EXPAND)
            self.SetSizerAndFit(self.sizer)

        def print_line_in_graph(self, g, list):
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self.fig = plt.figure(figsize=(9, 9), dpi=75)
            self.canvas = FigCanvas(self, -1, self.fig)

            krawedzie = []
            for i in range(len(list) - 1):
                a = (list[i], list[i + 1])
                krawedzie.append(a)

            edge_labels = dict([((u, v,), d['weight'])
                                for u, v, d in g.edges(data=True)])
            red_edges = krawedzie
            edge_colors = ['black' if not edge in red_edges else 'red' for edge in g.edges()]

            pos = nx.shell_layout(g)
            nx.draw_networkx_edge_labels(g, pos, with_labels=True, edge_labels=edge_labels)
            nx.draw(g, pos, with_labels=True, node_color='#A0CBE3', node_size=300, edge_color=edge_colors)
            plt.axis('off')
            self.sizer.Add(self.canvas, 1, wx.EXPAND)
            self.SetSizerAndFit(self.sizer)

    def OnDodajWierzcholek(self, event):
        wierzcholek = str(self.window3.GetValue())
        self.G.add_node(wierzcholek)
        self.rightpanel.print_graph(self.G)
        self.window3.Clear()

    def OnDodajWage(self, event):
        try:
            waga = int(self.window4.GetValue())
            krawedz_z = str(self.window5.GetValue())
            krawedz_do = str(self.window6.GetValue())
            if waga < 0:
                dial4 = wx.MessageDialog(None, u"Zły typ parametru wagi. Musi być liczbą całkowitą, nieujemną", u"Błąd",
                                         wx.OK | wx.ICON_ERROR)
                dial4.ShowModal()
            else:
                self.G.add_edge(krawedz_z, krawedz_do, weight=waga)
                self.rightpanel.print_graph(self.G)
                for i in [self.window4, self.window5, self.window6]:
                    i.Clear()
        except:
            dial4 = wx.MessageDialog(None, u"Zły typ parametru wagi. Musi być liczbą całkowitą, nieujemną", u"Błąd",
                                     wx.OK | wx.ICON_ERROR)
            dial4.ShowModal()

    def OnUsunWierzcholek(self, event):
        wierzcholeku = str(self.windowu.GetValue())
        if wierzcholeku in self.G:
            self.G.remove_node(wierzcholeku)
            self.rightpanel.print_graph(self.G)
            self.windowu.Clear()
        else:
            dial = wx.MessageBox(u"Nie ma takiego wierzchołka", 'Info', wx.OK | wx.ICON_EXCLAMATION)
            dial.ShowModal()

    def OnUsunKrawedz(self, event):
        krawedz_z1 = str(self.windowk1.GetValue())
        krawedz_z2 = str(self.windowk2.GetValue())
        if krawedz_z1 in self.G and krawedz_z2 in self.G:
            self.G.remove_edge(krawedz_z1, krawedz_z2)
            self.rightpanel.print_graph(self.G)
            self.windowk1.Clear()
            self.windowk2.Clear()
        else:
            dial2 = wx.MessageBox(u"Nie ma takiej krawędzi", 'Info', wx.OK | wx.ICON_EXCLAMATION)
            dial2.ShowModal()

    def OnSaveGraphName(self, event):
        if len(self.G.nodes()) > 50:
            err = wx.MessageBox(u"Graf zbyt duży", 'Info', wx.OK | wx.ICON_EXCLAMATION)
            err.ShowModal()
        else:
            dlg = wx.TextEntryDialog(self, 'Podaj nazwe grafu do zapisu', 'Zapis')
            if dlg.ShowModal() == wx.ID_OK:
                self.nazwaklucza = dlg.GetValue()
                self.nazwaklucza = "_".join(self.nazwaklucza.split(" "))
                self.data = self.G._pred
                self.moje_dane[self.nazwaklucza] = self.data
                with open("moje_dane1.json", "w+") as plik:
                    json.dump(self.moje_dane, plik, indent=4, sort_keys=True)
                    if True:
                        wx.CallLater(500, self.ShowMessage)
                    else:
                        dial3 = wx.MessageDialog(None, u"Nie można zapisać", u"Błąd", wx.OK | wx.ICON_ERROR)
                        dial3.ShowModal()
            dlg.Destroy()

    def ShowMessage(self):
        wx.MessageBox(u"Zapisywanie zakończone", 'Informacja',
                      wx.OK | wx.ICON_INFORMATION)

    def panel(self):
        panel = wx.Panel(self, -1)
        rightpanel = self.Grafy(panel, -1)
        return rightpanel, panel


def main():
    ex = wx.App()
    Window2(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
