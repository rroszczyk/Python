# Ćwiczenie 1:
# Rysowanie pojedynczej funkcji liniowej z zastosowaniem własnoręcznie zdefiniowanych funkcji

import plotly.graph_objs as go
import numpy as np
import funkcje_liniowe


# parametry funkcji
a = 0.5
b = -1

# Rysowanie wykresu
wyk_lin = funkcje_liniowe.wygeneruj_wykres(a, b, [-2, 2])
wyk_lin.name = 'funkcja liniowa'

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
