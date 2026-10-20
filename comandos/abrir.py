import subprocess


def abrir_chrome():
    subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

def abrir_bloc_notas():
    subprocess.Popen("notepad.exe")


def abrir_calculadora():
    subprocess.Popen(["calc"])

def abrir_vscode():
    subprocess.Popen(r"C:\Users\diego\AppData\Local\Programs\Microsoft VS Code")

def abrir_netbeans():
    subprocess.Popen(r"C:\Program Files\NetBeans-25\netbeans\bin")


def abrir_mysql():
    subprocess.Popen(r"C:\Program Files\MySQL\MySQL Workbench 8.0")