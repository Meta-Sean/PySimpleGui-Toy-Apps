from cgitb import enable
import PySimpleGUI as sg

layout = [
    [
        sg.Text("Choose units to convert", enable_events=True, key="-TEXT-"),
        sg.Spin(["km to miles", "kg to pounds"], key="-UNITS-"),
    ],
    [sg.Input(key="-INPUT-")],
    [sg.Button("Convert", key="-BUTTON-")],
    [sg.Text("Result:", key="-TEXT2-")],
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "-BUTTON-":
        if values["-INPUT-"].isnumeric():
            if values["-UNITS-"] == "km to miles":
                res = round(0.6214 * float(values["-INPUT-"]), 2)
            else:
                res = round(2.20461 * float(values["-INPUT-"]), 2)
            window["-TEXT2-"].update(res)
        else:
            window["-TEXT2-"].update("Please enter a number")

window.close()