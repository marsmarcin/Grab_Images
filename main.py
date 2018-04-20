# Created by Yujiang Fu from NEU
# version 2
from tkinter import *
import random
import urllib.request
import re
import os
import urllib

window = Tk()
window.title('Grab Picture')
window['background'] = 'gray'
window.geometry('520x550+300+300')
Label(window, text='ImgID', relief=RIDGE, width=15).grid(row=0, column=0)
Label(window, text='URL', relief=RIDGE, width=15).grid(row=1, column=0)
Label(window, text='SavePath', relief=RIDGE, width=15).grid(row=2, column=0)

entryVar1 = StringVar()
entry1 = Entry(window, textvariable=entryVar1, width=40)
entry1.grid(row=0, column=1)

entryVar2 = StringVar()
entry2 = Entry(window, textvariable=entryVar2, width=40)
entry2.grid(row=1, column=1)

text_result = Text(window, width=40, height=25)
text_result.grid(row=4, column=1)

entryVar3 = StringVar()
entry3 = Entry(window, textvariable=entryVar3, width=40)
entry3.grid(row=2, column=1)
entryVar3.set('F://get_img//test//')


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('GBK')


def getImg(html):
    reg = r'src="(.+?\.jpg)" width="?"'

    imgre = re.compile(reg)
    imglist = imgre.findall(html)

    x = 0

    m_path = str(entryVar3.get()) + str(entryVar1.get())
    if not os.path.isdir(m_path):
        os.makedirs(m_path)
    m_paths = m_path + '//'

    for imgurl in imglist:
        picName = '{0}' + str(entryVar1.get()) + '_{1}.jpg'
        urllib.request.urlretrieve(imgurl, picName.format(m_paths, x))

        x = x + 1
    # result='Downloading The ' + str(x) + ' of ' + str(entryVar1.get()) + ' Car'
    # print(result)

    return imglist


def hitMe():
    html = getHtml(str(entryVar2.get()))

    (getImg(html))
    # print('The'+str(entryVar1.get())+'Mission is over!')
    m_result = 'The ' + str(entryVar1.get()) + ' Mission is over!'
    text_result.insert(1.0, m_result + '\n')


button1 = Button(window, text='Start', width=14, command=hitMe)
button1.grid(row=3, column=0)


def hitClear():
    # entryVar1.set('')
    entryVar2.set('')


button2 = Button(window, text='Clear', width=14, command=hitClear)
button2.grid(row=3, column=1)


def hitClearText():
    m_result.delete(1.0, Tkinter.END)


button3 = Button(window, text='ClearText', width=14, height=20, command=hitClearText)
button3.grid(row=4, column=0)
mainloop()