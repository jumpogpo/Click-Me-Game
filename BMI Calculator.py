from tkinter import *
from tkinter import ttk

root = Tk()
root.title('BMI Calculator')
root.geometry('300x300')

def CalculateBMI():
    if Weight.get() != '' and Height.get() != '':
        Criterion = None
        WeightUnitChose = WeightUnit.get()
        HeightUnitChose = HeightUnit.get()

        if WeightUnitChose == "Kg":
            WeightValue = float(Weight.get())
        elif WeightUnitChose == "g":
            WeightValue = float(Weight.get()) / 1000

        if HeightUnitChose == 'cm':
            HeightValue = float(Height.get()) / 100
        elif HeightUnitChose == 'm':
            HeightValue = float(Height.get())

        BMI = float("{:.2f}".format(WeightValue / (HeightValue ** 2)))

        if BMI < 18.50:
            Criterion = 'น้ำหนักน้อย / ผอม'
        elif BMI >= 18.50 and BMI <= 22.99:
            Criterion = 'ปกติ (สุขภาพดี)'
        elif BMI >= 23 and BMI <= 24.99:
            Criterion = 'ท้วม / โรคอ้วนระดับ 1'
        elif BMI >= 25 and BMI <= 29.99:
            Criterion = 'อ้วน / โรคอ้วนระดับ 2'
        elif BMI > 30:
            Criterion = 'อ้วนมาก / โรคอ้วนระดับ 3'

        BMIResult.configure(text='BMI ของคุณคือ: ' + str(BMI))
        Result.configure(text=Criterion)

Weight = StringVar()
Height = StringVar()
WeightUnit = StringVar(value='Kg')
HeightUnit = StringVar(value='cm')

WeightLabel = Label(root, text="นํ้าหนัก", fg='Black', font=10, justify=LEFT)
HeightLabel = Label(root, text="ส่วนสูง", fg='Black', font=10, justify=LEFT)

WeightUnitChoice = ttk.Combobox(width=4, font=30, textvariable=WeightUnit)
HeightUnitChoice = ttk.Combobox(width=4, font=30, textvariable=HeightUnit)
WeightUnitChoice['values']=('Kg', 'g')
HeightUnitChoice['values']=('cm', 'm')
WeightUnitChoice['state'] = 'readonly'
HeightUnitChoice['state'] = 'readonly'

WeightBox = Entry(root, textvariable=Weight, justify=CENTER, font=20, width=10)
HeightBox = Entry(root, textvariable=Height, justify=CENTER, font=20, width=10)

Button1 = Button(root, text='คำนวณ', fg='Black', bg='White', command=CalculateBMI, font=50)
BMIResult = Label(root, fg='Black', font=10)
Result = Label(root, fg='Black', font=10)

WeightLabel.place(x=105,y=10)
HeightLabel.place(x=105,y=80)
WeightBox.place(x=70, y=45)
HeightBox.place(x=70, y=110)
WeightUnitChoice.place(x=180, y=45)
HeightUnitChoice.place(x=180, y=110)
Button1.place(x=118, y=145)
BMIResult.place(x=70, y=200)
Result.place(x=88, y=230)

root.resizable(False, False)
root.wm_attributes("-transparentcolor", 'grey')
root.mainloop()