
import os
import urllib.request
import subprocess
from pathlib import Path

username = os.getlogin()
download_url = "https://www.torproject.org/dist/torbrowser/12.0.7/torbrowser-install-win64-12.0.7_ALL.exe"
save_path = fr"C:\Users\{username}\Downloads\tor.exe"

urllib.request.urlretrieve(download_url, save_path)


subprocess.call(['cmd','/c',f'{save_path} /S /D=C:\Tor'])
os.remove(save_path)

escritorio = fr"C:\users\{username}\Desktop\Tor.exe"
tor_pref = os.path.join(R"C:\Tor\Browser\TorBrowser\Data\Browser\profile.default\prefs.js")
tor_executable = R"C:\Tor\Browser\firefox.exe"
subprocess.call([tor_executable, "-f"])
subprocess.call(['cmd','/c',f'copy {tor_executable} {escritorio}'])

with open(tor_pref, "a") as prefs:
    prefs.write('user_pref("network.proxy.type", 1);\n')
    prefs.write('user_pref("network.proxy.socks", "127.0.0.1");\n')
    prefs.write('user_pref("network.proxy.socks_port", 9150);\n')
    prefs.write('user_pref("network.proxy.socks_remote_dns", true);\n')


