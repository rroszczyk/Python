# Ćwiczenie 6:
# Znajdowanie parametrów prostej prostopadłej przechodzącej przez punkt

import plotly.graph_objs as go
import numpy as np
import funkcje_liniowe

# parametry funkcji liniowej
a = 0.5
b = -1
# funkcja jako wyrażenia lambda
f = lambda x_in: a*x_in+b

# Współrzędne punktu
pt = [1, f(1)]

# parametry funkcji prostopadłej
a_p = -1/a
b_p = pt[1]-a_p*pt[0]

# Rysowanie wykresu
wyk_lin1 = funkcje_liniowe.wygeneruj_wykres(a, b, [-3, 4])
wyk_lin1.name = 'zadana prosta'

wyk_lin2 = funkcje_liniowe.wygeneruj_wykres(a_p, b_p, [-3, 4])
wyk_lin2.name = 'prosta prostopadła'

wyk_pt = go.Scatter(x=np.array(pt[0]), y=np.array(pt[1]), name='punkt')
wyk_pt.marker = dict(
    color='rgba(0,255,0,0.5)',
    size=15,
    line=dict(
        color='rgba(0,0,0,1)',
        width=2
    )
)

fig = go.Figure()
fig.add_trace(wyk_lin1)
fig.add_trace(wyk_lin2)
fig.add_trace(wyk_pt)

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