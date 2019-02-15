#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import dijkstra_algorytm
from window2 import Window2
import json
import networkx as nx
import re
import os


class Window1(wx.Frame):
    def __init__(self, parent, **kw):
        super(Window1, self).__init__(parent=None, **kw)

        self.SetTitle('Algorithm Dijkstra')
        self.Maximize(True)
        self.Centre()
        self.InitUI()
        self.Show(True)

    with open("moje_dane1.json") as plik:
        moje_dane = json.load(plik)

    def InitUI(self):

        self.menu()
        self.rightpanel, panel = self.panel()
        sizer = wx.GridBagSizer(1, 2)

        text1 = wx.StaticText(panel, label="DANE:")
        sizer.Add(text1, pos=(1, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.combodane = wx.StaticText(panel)
        sizer.Add(self.combodane, pos=(1, 2), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        sizer1 = wx.GridBagSizer(2, 2)

        button1 = wx.Button(panel, label='Algorytm Dijkstry')
        button1.Bind(wx.EVT_BUTTON, self.OnAlgorytmDijkstry)
        sizer1.Add(button1, pos=(1, 2), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        text2 = wx.StaticText(panel, label="Punkt początkowy:")
        sizer1.Add(text2, pos=(2, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.klucze1 = []
        self.combo = wx.ComboBox(panel, choices=self.klucze1, style=wx.CB_READONLY)
        sizer1.Add(self.combo, pos=(2, 2), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        textk1 = wx.StaticText(panel, label="Punkt końcowy:")
        sizer1.Add(textk1, pos=(3, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        self.combok1 = wx.ComboBox(panel, choices=self.klucze1, style=wx.CB_READONLY)
        sizer1.Add(self.combok1, pos=(3, 2), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        sizer2 = wx.GridBagSizer(1, 2)

        button2 = wx.Button(panel, label='Podgląd grafu')
        button2.Bind(wx.EVT_BUTTON, self.OnPodgladGrafu)
        sizer2.Add(button2, pos=(1, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        button3 = wx.Button(panel, label='Edycja grafu')
        button3.Bind(wx.EVT_BUTTON, self.OnEdycjagrafu)
        sizer2.Add(button3, pos=(2, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

        sizer.AddGrowableCol(1)
        sizer1.AddGrowableCol(1)
        sizer2.AddGrowableCol(1)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 5
        box = wx.StaticBox(panel, -1, 'Algorytm:')
        nmSizer1 = wx.StaticBoxSizer(box, wx.VERTICAL)
        nmSizer1.Add(sizer1, 0, wx.ALL | wx.CENTER, b)

        box = wx.StaticBox(panel, -1, 'Graf:')
        nmSizer2 = wx.StaticBoxSizer(box, wx.VERTICAL)
        nmSizer2.Add(sizer2, 0, wx.ALL | wx.CENTER, b)

        vsizer1.Add(sizer, 1, wx.ALL | wx.CENTER, b)
        vsizer1.Add(nmSizer1, 1, wx.ALL | wx.CENTER, b)
        vsizer1.Add(nmSizer2, 1, wx.ALL | wx.CENTER, b)

        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        vsizer2.Add(self.rightpanel, 1, wx.EXPAND, b)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(vsizer1, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)
        hsizer.Add(vsizer2, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)

        panel.SetSizerAndFit(hsizer)

    def menu(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        fileMenu.Append(wx.ID_NEW, '&Nowy')
        fileMenu.Append(wx.ID_OPEN, '&Otwórz')
        fileMenu.Append(wx.ID_FILE, '&Otwórz z innego pliku')
        fileMenu.Append(wx.ID_EXIT, '&Zamknij')

        self.Bind(wx.EVT_MENU, self.OnWidgetNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.openGrafzJSON, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.onOpen, id=wx.ID_FILE)
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, id=wx.ID_EXIT)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        menubar.Append(fileMenu, '&Plik (edycja)')

        self.SetMenuBar(menubar)

    def OnWidgetHelp(self, e):
        os.startfile(file)

    class Dialog(wx.Dialog):
        def __init__(self, parent, id):
            wx.Dialog.__init__(self, None, -1, "Otwórz graf")

            self.InitUI()
            self.Centre()
            self.Show()

        def InitUI(self):
            with open("moje_dane1.json") as plik:
                self.moje_dane = json.load(plik)

            self.lista = []
            panel = wx.Panel(self, -1)
            sizer = wx.GridBagSizer(2, 1)

            self.lst = wx.ListBox(panel, choices=self.moje_dane.keys(), style=wx.CB_READONLY)
            self.lst.SetSelection(1)
            sizer.Add(self.lst, pos=(1, 1), span=(1, 1), flag=wx.ALL | wx.EXPAND, border=10)

            button = wx.Button(panel, wx.ID_OK)
            sizer.Add(button, pos=(2, 1), span=(1, 1), flag=wx.ALL | wx.CENTER, border=10)

            sizer.AddGrowableCol(1)
            panel.SetSizer(sizer)

    def pobierzDane(self, parametrp):
        dane = self.moje_dane[parametrp]
        self.G = nx.DiGraph(dane)
        return self.G

    def openGrafzJSON(self, event):
        dlg = self.Dialog(parent=None, id=-1)
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            nazwagrafu = dlg.lst.GetString(dlg.lst.GetSelection())
            self.combodane.SetLabel(str(nazwagrafu))
            self.OnMenu()
        dlg.Destroy()

    def OnMenu(self):
        self.parametrp = self.combodane.GetLabel()
        self.G = self.pobierzDane(self.parametrp)
        self.listacombo = self.G.nodes()
        self.combo.Clear()
        self.combok1.Clear()
        for a in self.listacombo:
            self.combo.Append(a)
            self.combok1.Append(a)

    def onOpen(self, event):
        openFileDialog = wx.FileDialog(self, "Open", "", "",
                                       "Pliki tekstowe (*.txt)|*.txt",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        self.path = openFileDialog.GetPath()
        self.combodane.SetLabel(str(self.path))
        self.openselectfile(self.path)
        openFileDialog.Destroy()

    def openselectfile(self, path):
        with open(path, "r") as file:
            data = file.read()
        surowedane = re.compile(r'\w+,\w+,\w+')
        findalldata = surowedane.findall(data)
        k = re.compile(r'\w+')
        self.G = nx.DiGraph()
        for z in range(len(findalldata)):
            danedografu = k.findall(findalldata[z])
            if len(danedografu) == 3:
                self.G.add_edge(danedografu[0], danedografu[1], weight=int(danedografu[2]))
                for e in danedografu:
                    if e < 0:
                        continue

            else:
                continue
        self.listacombo = self.G.nodes()
        if len(self.listacombo) > 50:
            err1 = wx.MessageBox(u"Graf zbyt duży", 'Info', wx.OK | wx.ICON_EXCLAMATION)
            err1.ShowModal()
        else:
            self.combo.Clear()
            self.combok1.Clear()
            for a in self.listacombo:
                self.combo.Append(a)
                self.combok1.Append(a)
            return self.G

    def OnWidgetNew(self, event):
        self.frame = Window2(parent=None)
        self.frame.Bind(wx.EVT_CLOSE, self.OnWidgetNewclose)

    def OnWidgetNewclose(self, event):
        try:
            dt = self.frame.data
            kl = self.frame.nazwaklucza
            self.moje_dane[kl] = dt
            event.Skip()
        except:
            self.frame.Destroy()

    def OnAlgorytmDijkstry(self, event):
        node_z = str(self.combo.GetValue())
        node_do = str(self.combok1.GetValue())
        try:
            ddd = str(self.combodane.GetLabel())
            if os.path.isfile(ddd):
                self.G = self.openselectfile(ddd)
                if not self.G:
                    self.komunikat()
                else:
                    self.sciezka, self.koszt = dijkstra_algorytm.dijkstra(self.G, node_z, node_do)
                    self.G = self.openselectfile(ddd)
                    lista = []
                    for i in self.sciezka:
                        elem = str(i)
                        lista.append(elem)
                    self.sciezka = lista

                    self.podsumujAlgorytmDijkstry(self.G, self.sciezka, self.koszt)
            else:
                self.parametrp = self.combodane.GetLabel()
                self.G = self.pobierzDane(self.parametrp)
                if not self.G:
                    self.komunikat()
                else:
                    self.sciezka, self.koszt = dijkstra_algorytm.dijkstra(self.G, node_z, node_do)
                    self.G = self.pobierzDane(self.parametrp)
                    lista = []
                    for i in self.sciezka:
                        elem = str(i)
                        lista.append(elem)
                    self.sciezka = lista
                    self.podsumujAlgorytmDijkstry(self.G, self.sciezka, self.koszt)
        except TypeError:
            print " "

    def podsumujAlgorytmDijkstry(self, g, sciezka, koszt):
        self.rightpanel.print_line_in_graph(g, sciezka)
        dlg_reset = wx.MessageDialog(self,
                                     "Najkrótsza droga przechodzi przez ściekę: " + str(sciezka) + "    "
                                     + "Koszt najkrótszej ścieżki wynosi: " + koszt, "Algorytm Dijkstry",
                                     wx.CANCEL)
        dlg_reset.ShowModal()

    def OnPodgladGrafu(self, event):
        ddd = str(self.combodane.GetLabel())
        if os.path.isfile(ddd):
            self.openselectfile(ddd)
        else:
            self.G = self.pobierzDane(self.parametrp)
        self.rightpanel.print_graph(self.G)

    def OnEdycjagrafu(self, event):
        ddd = str(self.combodane.GetLabel())
        if os.path.isfile(ddd):
            self.G = self.openselectfile(ddd)
            self.frame1 = Window2(parent=None)
            self.frame1.G = self.G
            self.frame1.rightpanel.print_graph(self.G)
            self.frame1.Bind(wx.EVT_CLOSE, self.OnWidgeteditclose)
        else:
            self.G = self.pobierzDane(self.parametrp)
            self.frame1 = Window2(parent=None)
            self.frame1.G = self.G
            self.frame1.rightpanel.print_graph(self.G)
            self.frame1.Bind(wx.EVT_CLOSE, self.OnWidgeteditclose)

    def OnWidgeteditclose(self, event):
        try:
            dt = self.frame1.data
            kl = self.frame1.nazwaklucza
            self.moje_dane[kl] = dt
            event.Skip()
        except:
            self.frame1.Destroy()

    def OnCloseWindow(self, e):
        dial = wx.MessageDialog(None, 'Czy chcesz zamknąć?', 'Pytanie',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        else:
            e.Veto()

    def panel(self):
        panel = wx.Panel(self, -1)
        rightpanel = Window2.Grafy(panel, -1)
        return rightpanel, panel

    def komunikat(self):
        dial1 = wx.MessageDialog(None, u"Niepełne dane", u"Błąd", wx.OK | wx.ICON_ERROR)
        dial1.ShowModal()


def main():
    ex = wx.App()
    Window1(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
