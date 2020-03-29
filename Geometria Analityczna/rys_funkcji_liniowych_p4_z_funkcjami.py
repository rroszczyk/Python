# Ćwiczenie 4:
# Znajdowanie współrzędnych punktów leżących na prostej odległych o r od innego punktu leżącego na prostej z zastosowaniem własnoręcznie zdefiniowanych funkcji


import plotly.graph_objs as go
import numpy as np
import funkcje_liniowe

# parametry funkcji
a = 0.5
b = -1
# funkcja jako wyrażenia lambda
f = lambda x_in: a*x_in+b

# Współrzędne punktu
pt = [1, f(1)]

# Współrzędne punktów oddalone od r
pts = funkcje_liniowe.znajdz_wsp_punktow_oddalone_o_r(pt, a, b, 2)

# Rysowanie wykresu
wyk_lin = funkcje_liniowe.wygeneruj_wykres(a, b, [-3, 4])
wyk_lin.name = 'funkcja liniowa'
wyk_lin.marker = dict(color='rgba(255,0,0,1)')

wyk_pt = go.Scatter(x=np.array(pt[0]), y=np.array(pt[1]), name='punkt')
wyk_pt.marker = dict(
    color='rgba(0,255,0,0.5)',
    size=15,
    line=dict(
        color='rgba(0,0,0,1)',
        width=2
    )
)

wyk_pts = go.Scatter(x=pts[:, 0], y=pts[:, 1], mode='markers', name='punkty oddalone o r')

fig = go.Figure()
fig.add_trace(wyk_lin)
fig.add_trace(wyk_pt)
fig.add_trace(wyk_pts)

# Konfiguracja wyglądu
fig.update_layout(
    width=500,
    height=500,
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
    range=[-2, 4])

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    dtick=1,
    range=[-2, 1])


fig.show()