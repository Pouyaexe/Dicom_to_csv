import csv 
import pydicom # pip install pydicom IF NOT INSTALLED, It is used to read the dicom files
import os.path 
import PySimpleGUI as sg # pip install PySimpleGUI IF NOT INSTALLED, It is used to create the GUI
from loading_files import data_processing

# Sample pictures from http://www.rubomedical.com/dicom_files/
column = [
    [
        # Text elements for the GUI
        sg.Text("Input Path"),
        sg.In(size=(37, 1), enable_events=True, key="-INPUT-"),
        sg.FolderBrowse(),
    ],

       [ sg.Text("Output Path:") ,
        sg.In(size=(35, 1), enable_events=True, key="-OUTPUT-"),
        sg.FolderBrowse(),],
        [sg.ReadFormButton("Export to CSV", key="-LOAD-", size=(33, 1))],
    
] 

# Choose a Theme for the Layout
sg.theme("Reddit")
# latout
layout = [ #main layout
    [
        sg.Column(column),
        sg.HSeparator()      
    ]
]

window = sg.Window("Dicom", layout)
# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-LOAD-":
        folder_input = values["-INPUT-"]
        folder_ouput = values["-OUTPUT-"]
        file_list = os.listdir(folder)
        ## Call the function to process the data
        data_processing(folder_input,file_list,folder_ouput)

    # making a list of all the files in the folder
    if event == "-INPUT-":
        folder = values["-INPUT-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f)) # and f.lower().endswith((".dcm",".dicom",".jpg",".jpeg",".png"))
            and f.lower().endswith((".dcm",".dicom",".jpg",".jpeg",".png")) 
        ]
        
            

window.close()
