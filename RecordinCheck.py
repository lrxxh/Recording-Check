import psutil
from termcolor import colored

recording_softwares = {'bdcam.exe': 'Bandicam',
                       'action.exe': 'Action',
                       'obs64.exe': 'OBS',
                       'dxtory.exe': 'Dxtory',
                       'nvsphelper64.exe': 'Geforce Experience',
                       'camtasia.exe': 'Camtasia',
                       'fraps.exe': 'Fraps',
                       'screencast.exe': 'Screencast',
                       'xsplit.exe': 'XSplit',
                       'playclaw.exe': 'PlayClaw',
                       'mirillis.exe': 'Mirillis Action',
                       'wmcap.exe': 'Bandicam',
                       'lightstream.exe': 'Lightstream',
                       'streamlabs.exe': 'Streamlabs OBS',
                       'webrtcvad.exe': 'Audacity (recording)',
                       'openbroadcastsoftware.exe': 'Open Broadcaster Software',
                       'movavi.screen.recorder.exe': 'Movavi Screen Recorder',
                       'icecreamscreenrecorder.exe': 'Icecream Screen Recorder',
                       'smartpixel.exe': 'Smartpixel',
                       'd3dgear.exe': 'D3DGear',
                       'gadwinprintscreen.exe': 'Gadwin PrintScreen',
                       'apowersoftfreescreenrecorder.exe': 'Apowersoft Free Screen Recorder',
                       'bandicamlauncher.exe': 'Bandicam (launcher)',
                       'hypercam.exe': 'HyperCam',
                       'loiloilgamerecorder.exe': 'LoiLo Game Recorder',
                       'nchexpressions.exe': 'Express Animate (recording)',
                       'captura.exe': 'Captura',
                       'vokoscreenNG': 'VokoscreenNG',
                       'simple.screen.recorder': 'SimpleScreenRecorder',
                       'recordmydesktop': 'RecordMyDesktop',
                       'kazam': 'Kazam',
                       'gtk-recordmydesktop': 'Gtk-RecordMyDesktop',
                       'screenstudio': 'ScreenStudio',
                       'screenkey': 'Screenkey',
                       'pycharm64.exe': 'PyCharm (recording)',
                       'jupyter-notebook.exe': 'Jupyter Notebook (recording)'}


# Loop through the running processes
found = False
for proc in psutil.process_iter(['pid', 'name']):
    # Check if the process name matches any of the recording software names
    if proc.info['name'] in recording_softwares:
        print(colored(f"{recording_softwares[proc.info['name']]} is running (PID: {proc.info['pid']})", "yellow"))
        found = True

if not found:
    print(colored("No Recording Softwares are currently running", "red"))

input("Press Enter to continue...")
# made by lrxh#0001
