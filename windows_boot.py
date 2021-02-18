import subprocess

def windows_boot():
	subprocess.run('%HOMEPATH%\AppData\Roaming\Zoom\\bin\Zoom.exe', shell=True)
windows_boot()
