import PySimpleGUI as sg
import subprocess
import os

from dotenv import load_dotenv
from os import listdir, getcwd
from os.path import isfile, join

# Load env variables
load_dotenv()

def updateWindow(window):
    window['-DATACOUNT-'].update("Avalible history: [" + str(getFileCount(TICKER)) + "]")

def getFileCount(ticker):
    # Get all files
    path = getcwd() + "/workspace/src/" + ticker + "/"
    files = onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return(len(files))

TICKERS = os.getenv('TICKERS').split(",")
TICKER = ""

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [ 
            [sg.Text('Select ticker'), sg.DropDown(TICKERS), sg.Button('Reload')],
            [sg.Text('Avalible history: []', key='-DATACOUNT-'), sg.Button('Re-train')],
            [sg.Button('Predict'), sg.Button('Retrieve last')] ]

# Create the Window
window = sg.Window('FOREX Prediction', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event)
    if event == 'Reload':
        # Reload all files
        TICKER = values[0]
        updateWindow(window)

    if event == 'Re-train':
        child = subprocess.Popen(['python', 'train.py'], stdin=subprocess.PIPE)
        child.communicate(input=TICKER.encode('utf-8'))

    if event == 'Retrieve last':
        child = subprocess.Popen(['python', 'retrieve_last.py'], stdin=subprocess.PIPE)
        child.communicate(input=TICKER.encode('utf-8'))

    if event == 'Predict' or event == 'Retrieve last':
        child = subprocess.Popen(['python', 'predict.py'], stdin=subprocess.PIPE)
        child.communicate(input=TICKER.encode('utf-8'))
        child.communicate(input=b'Y')

    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break

window.close()