# Ćwiczenie 7:
# Narysuj okrąg wpisany w trójkąt

import plotly.graph_objs as go
import numpy as np
import funkcje_liniowe

zakres = [-3, 4]

# Współrzędne trójkąta
punkty_trojkat = np.array([[-2, -1],
                           [ 1,  4],
                           [ 2, -2],
                           [-2, -1]])

# Wykres dla trójkąta
wyk_trojkat = go.Scatter(x=punkty_trojkat[:, 0], y=punkty_trojkat[:, 1], name='trojkat', fill='toself')

# ----------------------------------------------------------------------------------------------------------------------

# Wyznaczanie prostych zawierające boki trójkąta
[a1, b1] = funkcje_liniowe.znajdz_parametry_funkcji_przechodzacej_przez_dwa_punkty(
    punkty_trojkat[0, :], punkty_trojkat[1, :])
[a2, b2] = funkcje_liniowe.znajdz_parametry_funkcji_przechodzacej_przez_dwa_punkty(
    punkty_trojkat[1, :], punkty_trojkat[2, :])
[a3, b3] = funkcje_liniowe.znajdz_parametry_funkcji_przechodzacej_przez_dwa_punkty(
    punkty_trojkat[2, :], punkty_trojkat[3, :])

# Wykresy dla prostych zawierające boki trójkąta
wyk_bok1 = funkcje_liniowe.wygeneruj_wykres(a1, b1, zakres)
wyk_bok1.name = 'bok 1'

wyk_bok2 = funkcje_liniowe.wygeneruj_wykres(a2, b2, zakres)
wyk_bok2.name = 'bok 2'

wyk_bok3 = funkcje_liniowe.wygeneruj_wykres(a3, b3, zakres)
wyk_bok3.name = 'bok 3'

# ----------------------------------------------------------------------------------------------------------------------

# Wyznaczanie punktów leżących na bokach trójkąta oddalonych o r od wierzchołka
r = 0.5
w1_b1 = funkcje_liniowe.znajdz_punkt_oddalonu_o_r_od_pocz_polprostej(punkty_trojkat[0, :], a1, b1, r, '+')
w1_b3 = funkcje_liniowe.znajdz_punkt_oddalonu_o_r_od_pocz_polprostej(punkty_trojkat[0, :], a3, b3, r, '+')

w2_b1 = funkcje_liniowe.znajdz_punkt_oddalonu_o_r_od_pocz_polprostej(punkty_trojkat[1, :], a1, b1, r, '-')
w2_b2 = funkcje_liniowe.znajdz_punkt_oddalonu_o_r_od_pocz_polprostej(punkty_trojkat[1, :], a2, b2, r, '+')

w3_b2 = funkcje_liniowe.znajdz_punkt_oddalonu_o_r_od_pocz_polprostej(punkty_trojkat[2, :], a2, b2, r, '-')
w3_b3 = funkcje_liniowe.znajdz_punkt_oddalonu_o_r_od_pocz_polprostej(punkty_trojkat[2, :], a3, b3, r, '-')

# Wykres dla punktów odległych o r
pt_r = np.vstack((w1_b1,
                  w1_b3,
                  w2_b1,
                  w2_b2,
                  w3_b2,
                  w3_b3))
wyk_pt_r = go.Scatter(x=pt_r[:, 0], y=pt_r[:, 1], mode='markers', name='punkty oddalone o r')

# ----------------------------------------------------------------------------------------------------------------------

# Wyznaczanie dwusiecznych kątów trójkąta
[a_d1, b_d1] = funkcje_liniowe.znajdz_parametry_funkcji_przechodzacej_przez_dwa_punkty(punkty_trojkat[0, :], (w1_b1+w1_b3)/2)
[a_d2, b_d2] = funkcje_liniowe.znajdz_parametry_funkcji_przechodzacej_przez_dwa_punkty(punkty_trojkat[1, :], (w2_b1+w2_b2)/2)
[a_d3, b_d3] = funkcje_liniowe.znajdz_parametry_funkcji_przechodzacej_przez_dwa_punkty(punkty_trojkat[2, :], (w3_b2+w3_b3)/2)

# Wykresy dla dwusiecznych
wyk_d1 = funkcje_liniowe.wygeneruj_wykres(a_d1, b_d1, zakres)
wyk_d1.name = 'dwusieczna 1'
wyk_d2 = funkcje_liniowe.wygeneruj_wykres(a_d2, b_d2, zakres)
wyk_d2.name = 'dwusieczna 2'
wyk_d3 = funkcje_liniowe.wygeneruj_wykres(a_d3, b_d3, zakres)
wyk_d3.name = 'dwusieczna 3'

# ----------------------------------------------------------------------------------------------------------------------

# wyznaczanie punktu przecięcia dwusiecznych
pt_ok = funkcje_liniowe.znajdz_punkt_przeciecia(a_d1, b_d1, a_d2, b_d2)

# Wykres dla środka okręgu wpisanego
wyk_pt_ok = go.Scatter(x=np.array(pt_ok[0]), y=np.array(pt_ok[1]), mode='markers', name='środek okręgu')

# ----------------------------------------------------------------------------------------------------------------------

# parametry funkcji prostopadłej
a_pr = -1/a1
b_pr = pt_ok[1]-a_pr*pt_ok[0]

# punkt promienia
pt_prom = funkcje_liniowe.znajdz_punkt_przeciecia(a_pr, b_pr, a1, b1)

# Wykres punktu promieia
wyk_pt_prom = go.Scatter(x=np.array(pt_prom[0]),
                         y=np.array(pt_prom[1]),
                         mode='markers', name='punkt promienia')

# Wykres odcinak zawierającego promień
wyk_prom = go.Scatter(x=np.array([pt_ok[0], pt_prom[0]]),
                      y=np.array([pt_ok[1], pt_prom[1]]),
                      mode='lines', name='promień')

# ----------------------------------------------------------------------------------------------------------------------

# Wyznaczanie współrzędnych dla wykresu okręgu wpisanego
r = np.sqrt(np.sum(np.power(pt_ok-pt_prom, 2)))

t = np.linspace(0, 2*np.pi, 60)
pts_ok_wp = np.zeros([len(t), 2])
pts_ok_wp[:, 0] = pt_ok[0] + r*np.sin(t)
pts_ok_wp[:, 1] = pt_ok[1] + r*np.cos(t)

# Wykres dla okręgu wpisanego
wyk_ok_wp = go.Scatter(x=pts_ok_wp[:, 0],
                       y=pts_ok_wp[:, 1],
                       name='okrąg wpisany')

# ----------------------------------------------------------------------------------------------------------------------

# Rysowanie wykresów
fig = go.Figure()
fig.add_trace(wyk_trojkat)

fig.add_trace(wyk_bok1)
fig.add_trace(wyk_bok2)
fig.add_trace(wyk_bok3)

fig.add_trace(wyk_pt_r)

fig.add_trace(wyk_d1)
fig.add_trace(wyk_d2)
fig.add_trace(wyk_d3)

fig.add_trace(wyk_pt_ok)
fig.add_trace(wyk_pt_prom)
fig.add_trace(wyk_prom)

fig.add_trace(wyk_ok_wp)

# ----------------------------------------------------------------------------------------------------------------------

# Konfiguracja wyglądu
fig.update_layout(
    width=750,
    height=750,
    yaxis=dict(
        scaleanchor="x",
        scaleratio=1,
    ),
    plot_bgcolor='rgba(255,255,255,255)'
)

fig.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    dtick=1,
    range=zakres)

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    dtick=1,
    range=[-2, 3])

fig.show()