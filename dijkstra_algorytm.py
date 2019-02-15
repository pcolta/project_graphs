##!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


def dijkstra(graf, start, stop):
    krotszy_dystans = {}
    poprzednik = {}
    niewidocznywezel = graf
    nieskonczonosc = 9999999
    sciezka = []

    for wezel in niewidocznywezel:
        krotszy_dystans[wezel] = nieskonczonosc
    krotszy_dystans[start] = 0

    while niewidocznywezel:
        minwezel = None
        for wezel in niewidocznywezel:
            if minwezel is None:
                minwezel = wezel
            elif krotszy_dystans[wezel] < krotszy_dystans[minwezel]:
                minwezel = wezel

        for childwezel, waga in graf[minwezel].items():
            if waga['weight'] + krotszy_dystans[minwezel] < krotszy_dystans[childwezel]:
                krotszy_dystans[childwezel] = waga['weight'] + krotszy_dystans[minwezel]
                poprzednik[childwezel] = minwezel
        niewidocznywezel.remove_node(minwezel)

    aktualnywezel = stop
    while aktualnywezel != start:
        try:
            sciezka.insert(0, aktualnywezel)
            aktualnywezel = poprzednik[aktualnywezel]
        except KeyError:
            dial1 = wx.MessageDialog(None, u"Ścieżka nie osiągalna w tym grafie", u"Błąd", wx.OK | wx.ICON_ERROR)
            dial1.ShowModal()
            break
    sciezka.insert(0, start)
    if krotszy_dystans[stop] != nieskonczonosc:
        return sciezka, str(krotszy_dystans[stop])
