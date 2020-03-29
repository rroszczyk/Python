# Ćwiczenie 3:
# Znajdowanie parametrów funkcji liniowej przechodzącej przez dwa punkty.

import plotly.graph_objs as go
import numpy as np

# Współrzędne punktów
pt1 = [-2, 3]
pt2 = [2, -4]

# Parametry funkcji liniowej
A = np.array([[pt1[0], 1],
              [pt2[0], 1]])
B = np.array([pt1[1], pt2[1]])
[a, b] = np.linalg.solve(A, B)

# funkcja jako wyrażenia lambda
f = lambda x_in: a*x_in+b

# Współrzędne do wykresu
x = np.linspace(-3, 3, 2)
y = f(x)

# Rysowanie wykresu
wyk_lin = go.Scatter(x=x, y=y, name='funkcja liniowa', mode='lines')
# Wykres punktu przecięcia
wyk_pt1 = go.Scatter(x=np.array(pt1[0]), y=np.array(pt1[1]), name='punkt 1')
wyk_pt1.marker = dict(
    color='rgba(0,250,150,0.5)',
    size=15,
    line=dict(
        color='rgba(0,0,0,1)',
        width=2
    )
)
wyk_pt2 = go.Scatter(x=np.array(pt2[0]), y=np.array(pt2[1]), name='punkt 2')
wyk_pt2.marker = dict(
    color='rgba(150,250,0,0.5)',
    size=15,
    line=dict(
        color='rgba(0,0,0,1)',
        width=2
    )
)


fig = go.Figure()
fig.add_trace(wyk_lin)
fig.add_trace(wyk_pt1)
fig.add_trace(wyk_pt2)

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
    range=[-3, 3])

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    dtick=1,
    range=[-5, 5])


fig.show()