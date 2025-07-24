from tkinter import *
window = Tk()
window.geometry('550x300')
window.title('Color picker')
frame_RGB = LabelFrame(window, text='выберите цвета', height=250, width=250)
frame_RGB.place(relx=0.03,y=0)
frame_color = LabelFrame(window, text='Получаемый цвет', height=250, width=250)
frame_color.place(relx=0.52,y=0)
label_color = Label(frame_color, text='#000000', font=('Arial', 15, 'bold'), height=6, width=16, bg='#000000', fg='white')
label_color.place(relx=0.1,y=10)
def color_generator(value):
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    color = f'#{red:02x}{green:02x}{blue:02x}'
    label_color['bg'] = color
    label_color['text'] = color
    invetr_color = f'#{255-red:02x}{255-green:02x}{255-blue:02x}'
    label_color['fg'] = invetr_color
    copy.delete(0, END)
    copy.insert(0, color)

red_scale = Scale(frame_RGB, from_=0, to=255, resolution=1, orient=HORIZONTAL, label='красный', width=20, length=200, fg='red', activebackground='red', command=color_generator)
red_scale.place(relx=0.1, y=1)
green_scale = Scale(frame_RGB, from_=0, to=255, resolution=1, orient=HORIZONTAL, label='зеленый', width=20, length=200, fg='green', activebackground='green', command=color_generator)
green_scale.place(relx=0.1, y=70)
blue_scale = Scale(frame_RGB, from_=0, to=255, resolution=1, orient=HORIZONTAL, label='синий', width=20, length=200, fg='blue', activebackground='blue', command=color_generator)
blue_scale.place(relx=0.1, y=150)
copy = Entry(frame_color)
copy.place(relx=0.2, y=200)
window.mainloop()