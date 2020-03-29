# Ćwiczenie 1:
# Rysowanie pojedynczej funkcji liniowej

import plotly.graph_objs as go
import numpy as np


# parametry funkcji
a = 0.5
b = -1
# funkcja jako wyrażenia lambda
f = lambda x_in: a*x_in+b

# Współrzędne do wykresu
x = np.linspace(-2, 2, 2)
y = f(x)

# Rysowanie wykresu
wyk_lin = go.Scatter(x=x, y=y, name='funkcja liniowa', mode='lines')

fig = go.Figure()
fig.add_trace(wyk_lin)

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
    tick0=-2,
    dtick=0.5,
    range=[-2, 2])

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightGray',
    zeroline=True,
    zerolinewidth=1,
    zerolinecolor='lightGray',
    tick0=-2,
    dtick=0.5,
    range=[-2, 2])


fig.show()
