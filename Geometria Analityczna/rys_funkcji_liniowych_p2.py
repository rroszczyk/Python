# Ćwiczenie 2:
# Rysowanie dwóch funkcji liniowych
# Lokalizacja punktu przecięcia

import plotly.graph_objs as go
import numpy as np

# Pierwsza funkcja liniowa
a1 = 0.5
b1 = -1
f1 = lambda x_in: a1*x_in+b1

# Druga funkcja liniowa
a2 = -1.25
b2 = 1
f2 = lambda x_in: a2*x_in+b2

# punkt przecięcia
A = np.array([[-a1, 1],
              [-a2, 1]])
B = np.array([b1, b2])
pt_p = np.linalg.solve(A, B)

# Współrzędne do wykresu
x = np.linspace(-2, 2, 2)
y1 = f1(x)
y2 = f2(x)

# Rysowanie wykresu

wyk_lin1 = go.Scatter(x=x, y=y1, name='f_1', mode='lines')
wyk_lin2 = go.Scatter(x=x, y=y2, name='f_2', mode='lines')
sc_ptp = go.Scatter(x=np.array(pt_p[0]), y=np.array(pt_p[1]), name='przecięcie')
sc_ptp.marker = dict(
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
fig.add_trace(sc_ptp)

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
    dtick=0.5,
    range=[-2, 2])

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    dtick=0.5,
    range=[-2, 2])


fig.show()
