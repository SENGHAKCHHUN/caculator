import tkinter as tk
window = tk.Tk()
window.title("MY calculator")
window.geometry("240x430")
window.resizable(False,False)
text_result = tk.Text(window,font = ('bold', 40), width=36, height=1,bg='orange')
text_result.grid(columnspan=5)
result = ''
def add_to_calculator(symbol):
    global result
    print(result)
    result+= str(symbol)
    # print(result)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, result)
def evaluate_calculation():
    global result
    # print(result)
    try:
        result = str(eval(result))
        # print(result)
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
def clear_field():
    global result
    result = ''
    text_result.delete(1.0, 'end')
btn_7 = tk.Button(window, bg='white', text='7',font = ('bold', 30),width=2,command=lambda: add_to_calculator(7))
btn_7.place(x=10, y=65)
btn_8 = tk.Button(window, bg='white', text='8',font = ('bold', 30),width=2,command=lambda: add_to_calculator(8))
btn_8.place(x=65, y=65)
btn_9 = tk.Button(window, bg='white', text='9',font = ('bold', 30),width=2,command=lambda: add_to_calculator(9))
btn_9.place(x=120, y=65)
btn_Divider = tk.Button(window, bg='white', text='/',font = ('bold', 30), width=2,command=lambda: add_to_calculator("/"))
btn_Divider.place(x=175, y=65)



btn_4 = tk.Button(window, bg='white', text='4',font = ('bold', 30),width=2,command=lambda: add_to_calculator(4))
btn_4.place(x=10, y=140)
btn_5 = tk.Button(window, bg='white', text='5',font = ('bold', 30),width=2,command=lambda: add_to_calculator(5))
btn_5.place(x=65, y=140)
btn_6 = tk.Button(window, bg='white', text='6',font = ('bold', 30),width=2,command=lambda: add_to_calculator(6))
btn_6.place(x=120, y=140)
btn_X = tk.Button(window, bg='white', text='*',font = ('bold', 30),width=2, command=lambda: add_to_calculator("*"))
btn_X.place(x=175, y=140)



btn_1 = tk.Button(window, bg='white', text='1',font = ('bold', 30),width=2,command=lambda: add_to_calculator(1))
btn_1.place(x=10, y=215)
btn_2 = tk.Button(window, bg='white', text='2',font = ('bold', 30),width=2,command=lambda: add_to_calculator(2))
btn_2.place(x=65, y=215)
btn_3 = tk.Button(window, bg='white', text='3',font = ('bold', 30),width=2,command=lambda: add_to_calculator(3))
btn_3.place(x=120, y=215)
btn_Min = tk.Button(window, bg='white', text='-',font = ('bold', 30), width=2, command=lambda: add_to_calculator("-"))
btn_Min.place(x=175, y=215)
btn_0 = tk.Button(window, bg='white', text='0',font = ('bold', 30), width=2,command=lambda: add_to_calculator(0))
btn_0.place(x=10, y=280)


btn_digt = tk.Button(window, bg='white', text='.',font = ('bold', 30), width=2, command=lambda: add_to_calculator('.'))
btn_digt.place(x=65, y=280)
btn_clear = tk.Button(window, bg='white', text='C',font = ('bold', 30), width=2, command=clear_field)
btn_clear.place(x=120, y=280)
btn_plus = tk.Button(window, bg='white', text='+',font = ('bold', 30), width=2, command=lambda: add_to_calculator("+"))
btn_plus.place(x=175, y=280)



btn_equal = tk.Button(window, bg='white', text='(',font = ('bold', 30), width=2,command=lambda: add_to_calculator('('))
btn_equal.place(x=10, y=360)
btn_equal = tk.Button(window, bg='white', text=')',font = ('bold', 30), width=2,command=lambda: add_to_calculator(')'))
btn_equal.place(x=65, y=360)
btn_equal = tk.Button(window, bg='white', text='=',font = ('bold', 30), width=5,command=evaluate_calculation)
btn_equal.place(x=120, y=360)

window.mainloop()
