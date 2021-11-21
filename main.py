from cv2 import CalibrateCRF
import capture as cap
import ocr as ocr
import tkinter

win = tkinter.Tk()
win.geometry("300x200")

btn = tkinter.Button(win, 
    text = "btn",
    background = "white")

btn.config(width = 300, height = 200)
btn.config(text = "Capture")

def CAPandOCR():
    cap.cap()
    ocr.ocr()
btn.config(command = CAPandOCR)

btn.pack()

win.mainloop()