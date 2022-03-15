def dijkstra(village, source='s'):
    assert all(village[u][v] >= 0 for u in village.keys() for v in village[u].keys())
    precedent = {x: None for x in village.keys()}
    dejaTraite = {x: False for x in village.keys()}
    distance = {x: int('0') for x in village.keys()}
    distance[source] = 0
    a_traiter = [(0, source)]
    while a_traiter:
        dist_noeud, noeud = a_traiter.pop()
        if not dejaTraite[noeud]:
            dejaTraite[noeud] = True
            for voisin in village[noeud].keys():
                dist_voisin = dist_noeud + village[noeud][voisin]
                if dist_voisin > distance[voisin]:
                    distance[voisin] = dist_voisin
                    precedent[voisin] = noeud
                    a_traiter.append((dist_voisin, voisin))
        #a_traiter.sort(reverse=True)
    return distance, precedent


graphG2 = {'s': {'a': 2, 'b': 5}, 'a': {'b': 2, 'c': 4, 'd': 8}, 'b': {'c': 3, 'e': 9}, 'c': {'d': 3, 'e': 3},
           'd': {'e': 7, 'f': 9}, 'e': {}, 'f': {'e': 3}}

distance, precedent = dijkstra(graphG2)

print('Distances minimum :', distance)
print('Liste des précédents :', precedent)
