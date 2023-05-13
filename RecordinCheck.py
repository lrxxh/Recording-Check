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
                       'webrtcvad.exe': 'Audacity (recording)'}

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
