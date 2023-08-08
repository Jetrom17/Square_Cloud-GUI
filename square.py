import PySimpleGUI as sg
import requests
import json

theme_name = "Tan"

def get_api_data():
    url = "https://api.squarecloud.app/v2/service/statistics"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

layout = [
    [sg.Text("Status da Square Cloud")],
    [sg.Button("Get")],
    [sg.Multiline("", size=(30, 14), key="-OUTPUT-", disabled=True)]
]

sg.theme(theme_name)

window = sg.Window("Square Cloud", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Get":
        api_data = get_api_data()
        if api_data:
            formatted_data = json.dumps(api_data, indent=4)  # Formatação JSON com indent
            window["-OUTPUT-"].update(formatted_data)
        else:
            window["-OUTPUT-"].update("Erro ao obter dados da API.")

window.close()
