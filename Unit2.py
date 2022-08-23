import os
from delphifmx import *

class Form2(Form):

    def __init__(self, owner):
        self.Button1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Unit2.pyfmx"))

    def Button1Click(self, Sender):
        pass

def main():
    Application.Initialize()
    Application.Title = 'Form2'
    Application.MainForm = Form2(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
