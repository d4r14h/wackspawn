from faker import Faker
from faker.providers import internet
import PySimpleGUI as sg

sg.theme('DarkTeal')

def newFake():
    global faker
    global name
    global address
    global ipPriv
    global ipPub
    global cc
    faker = Faker()
    name = faker.name()
    address = faker.address()
    faker.add_provider(internet)
    ipPriv = faker.ipv4_private()
    ipPub = faker.ipv4_public()
    cc = faker.credit_card_full()
    

newFake()


layout = [
        [sg.Text('WackSpawn')],
        [sg.Text(size=(70,2), key='-name-')],
        [sg.Text(size=(70,2), key='-address-')],
        [sg.Text(size=(70,2), key='-ipPriv-')],
        [sg.Text(size=(70,2), key='-ipPub-')],
        [sg.Text(size=(70,4), key='-cc-')],
        [sg.Button('Spawn')]
        ]

window = sg.Window('WackSpawn Identity Generator', layout, size=(400, 400), element_justification='c')

while True:
    event, values = window.read()
    if event == 'Spawn':
        newFake()
    if event == sg.WINDOW_CLOSED:
        break
    window['-name-'].update(f'Name: {name}')
    window['-address-'].update(f'Address: {address}')
    window['-ipPriv-'].update(f'Private IP: {ipPriv}')
    window['-ipPub-'].update(f'Public IP: {ipPub}')
    window['-cc-'].update(f'Credit Card Info: {cc}')
    #window = sg.Window('WackSpawn Identity Generator', layout, size=(400, 400), element_justification='c')
    

        




