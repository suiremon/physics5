import matplotlib.pyplot as plt
import numpy as np

from shiny.express import input, render, ui

with ui.sidebar():
    ui.input_slider("n", "N", min=0, max=100, value=20)


@render.plot(alt="A histogram")
def plot() -> object:
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)

    fig, ax = plt.subplots()
    ax.hist(x, input.n(), density=True)
    return fig
