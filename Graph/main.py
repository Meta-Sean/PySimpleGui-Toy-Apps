from cgitb import enable
from turtle import update
import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def updateFigure(data):
    axes = fig.axes
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    axes[0].plot(x, y, "r-")
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()


sg.theme("DarkTeal6")
table_content = []
layout = [
    [
        sg.Table(
            headings=["Observation", "Result"],
            values=table_content,
            expand_x=True,
            hide_vertical_scroll=True,
            key="-TABLE-",
        )
    ],
    [sg.Input(key="-INPUT-", expand_x=True), sg.Button("Submit")],
    [sg.Canvas(key="-CANVAS-")],
]

window = sg.Window("Graph", layout, finalize=True)

# matplotlib
fig = matplotlib.figure.Figure(figsize=(5, 4))
fig.add_subplot(111).plot([], [])
figure_canvas_agg = FigureCanvasTkAgg(fig, window["-CANVAS-"].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Submit":
        new_value = values["-INPUT-"]
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1, float(new_value)])
            window["-TABLE-"].update(table_content)
            window["-INPUT-"].update("")
            updateFigure(table_content)


window.close()