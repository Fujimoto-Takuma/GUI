#!/usr/bin/env python
# coding: utf-8

# In[36]:


import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import pandas as pd
from tkinter import font
import tkinter.font as font
import random
import os
from tkinter import messagebox

def ret(frame):
    global cole
    cole = 0
    first(frame,var.get(),val.get())

def maxprob(A,sum):
    A.sort(reverse=True, key=lambda x :x[2])
    return A[0:sum]

def randomprob(A,sum): #単語帳からランダムに取り出したリストを返す関数
    random.shuffle(A)
    return A[0:sum]


def last(l_frame,list,tf):
    global cnt
    global s
    global A
    global B
    global frame1
    global frame2
    global sframe
    global cole
    cole += max(0,tf*-1)
    per = round(cole/list*100)
    l_frame.destroy()
    fram = ttk.Frame(root)
    fram.pack(fill = tk.BOTH,pady = 20)
    B[cnt-1][2] = max(B[cnt-1][2]+tf,0)
    ddf = pd.DataFrame(A,columns=["1","2","3"])
    ddf.to_csv(path + "/word.csv",encoding="cp932",index=False,header=False)
    cnt = 0
    B.clear()
    label_per =ttk.Label(fram,text="正解率:"+str(per)+"%",font=cnt_font)
    label_per.pack()
    button_back = ttk.Button(fram,text="スタート画面に戻る",style="color.TButton",width=40,padding=25,command=lambda :dest(0,fram))
    button_re = ttk.Button(fram,text="もう一度やる",style="color.TButton",width=40,padding=25,command=lambda :ret(fram))
    button_back.pack(pady=50)
    button_re.pack()
    

def ans(frame,answer,button_ans): #答えを出力する関数
    global B
    ans_word = font.Font(root,size=20)
    label_ans = ttk.Label(frame,text=answer,font=ans_word)
    label_ans.pack(pady=20,padx=30,side=tk.BOTTOM)
    button_ans.destroy()


def make(list,tf): #1つ目の画面
    #フレーム、変数の作成
    global frame1
    global cnt
    global s
    global B
    global cole
    cole += max(0,tf*-1)
    B[cnt-1][2] = max(B[cnt-1][2]+tf,0)

    frame2.destroy()
    frame1 = ttk.Frame(root)
    frame1.pack(fill = tk.BOTH,pady = 20)

    #部品の作成
    label1_frame =ttk.Label(frame1,text="第"+str(cnt+1)+"問",font=cnt_font)
    label2_frame =ttk.Label(frame1,text=list[0],font=word_font)
    button1_change = ttk.Button(frame1,text="次の問題",image=img_c,command=lambda :change(B[cnt],-1) if cnt < len(B) else last(frame1,cnt,-1))
    button2_change = ttk.Button(frame1,text="次の問題",image=img_w,command=lambda :change(B[cnt],1) if cnt < len(B) else last(frame1,cnt,1))
    button_ans = ttk.Button(frame1,text="答えを見る",width=20,padding=30,style="color.TButton",command=lambda :ans(frame1,list[1],button_ans))
    cnt += 1

    #部品のパック
    label1_frame.pack()
    label2_frame.pack()
    button1_change.pack(pady=10,padx=10,side=tk.LEFT)
    button2_change.pack(pady=10,padx=10,side=tk.RIGHT)
    button_ans.pack()


def change(list,tf): #2つめの画面
    #変数、フレームの作成
    global frame2
    global cnt
    global s
    global B
    global cole
    cole += max(0,tf*-1)
    B[cnt-1][2] = max(B[cnt-1][2]+tf,0)
    frame1.destroy()
    frame2 = ttk.Frame(root)
    frame2.pack(fill = tk.BOTH,pady = 20)


    #部品の作成
    label1_frame =ttk.Label(frame2,text="第"+str(cnt+1)+"問",font=cnt_font)
    label2_frame =ttk.Label(frame2,text=list[0],font=word_font)
    button1_change = ttk.Button(frame2,text="次の問題",image=img_c,command=lambda :make(B[cnt],-1) if cnt < len(B) else last(frame2,cnt,-1))
    button2_change = ttk.Button(frame2,text="次の問題",image=img_w,command=lambda :make(B[cnt],1) if cnt < len(B) else last(frame2,cnt,1))
    button_ans = ttk.Button(frame2,text="答えを見る",width=20,padding=30,style="color.TButton",command=lambda :ans(frame2,list[1],button_ans))
    cnt += 1

    #部品をパック
    label1_frame.pack()
    label2_frame.pack()
    button1_change.pack(pady=10,padx=10,side=tk.LEFT)
    button2_change.pack(pady=10,padx=10,side=tk.RIGHT)
    button_ans.pack()

def first(frame,sum,vari):
    global cnt
    global B
    global frame1
    global A
    global sframe
    if vari == 1:
        B = maxprob(A,sum)
    else:
        B = randomprob(A,sum)
    frame.destroy()
    frame1 = ttk.Frame(root)
    label1_frame =ttk.Label(frame1,text="第"+str(cnt+1)+"問",font=cnt_font)
    label2_frame =ttk.Label(frame1,text=B[cnt][0],font=word_font)
    button1_change = ttk.Button(frame1,text="次の問題",image=img_c,command=lambda :change(B[cnt],-1) if cnt < len(B) else last(frame1,cnt,-1))
    button2_change = ttk.Button(frame1,text="次の問題",image=img_w,command=lambda :change(B[cnt],1) if cnt < len(B) else last(frame1,cnt,1))
    button_ans = ttk.Button(frame1,text="答えを見る",width=20,padding=30,style="color.TButton",command=lambda :ans(frame1,B[0][1],button_ans))
    cnt+=1

#部品のパック
    frame1.pack(fill = tk.BOTH,pady=10)
    label1_frame.pack()
    label2_frame.pack()
    button1_change.pack(pady=10,padx=10,side=tk.LEFT)
    button2_change.pack(pady=10,padx=10,side=tk.RIGHT)
    button_ans.pack()

def title():
    global t
    tframe = ttk.Frame(root)
    titlelabel = ttk.Label(tframe,font=word_font,text="単語勉強アプリ")
    homebutton = ttk.Button(tframe,width=35,padding=25,text="勉強を始める",style="my.TButton",command=lambda :che(tframe))
    addbutton = ttk.Button(tframe,width=35,padding=25,text="単語を追加する",style="my.TButton",command=lambda :dest(1,tframe))
    setbutton = ttk.Button(tframe,width=35,padding=25,text="単語の管理",style="my.TButton",command=lambda :setting(tframe))
    titlelabel.pack()
    homebutton.pack()    
    addbutton.pack(pady=25,padx=40)
    setbutton.pack()
    tframe.pack(fill = tk.BOTH,pady = 10)

def che(frame):
    print(len(A))
    if len(A) == 1 and A[0][0]=="エラー回避用":
        tk.messagebox.showerror('エラー', '単語が登録されていません。')
    else:
        home(frame)


def dest(num,frame):
    global cole
    cole = 0
    frame.destroy()
    if num == 0:
        title()
    if num == 1:
        add()


def wo_add(ja,en):
    if ja == "" or en == "":
        tk.messagebox.showerror(title="エラー",message="入力ミスがあります")
    else:
        A.append([en,ja,0])
        ddf = pd.DataFrame(A,columns=["1","2","3"])
        ddf.to_csv(path + "/word.csv",encoding="cp932",index=False,header=False)
        tk.messagebox.showinfo(title="確認",message="単語:"+en+"を追加しました。")

def home(frame):
    global sframe
    global colors
    frame.destroy()
    sframe = ttk.Frame(root)
    sframe.pack(fill = tk.BOTH,pady = 10)
    slabel_1 = ttk.Label(sframe,font=word_font,text="単語帳アプリ")
    slabel_2 = ttk.Label(sframe,font=wo_font,text="出題数:")
    slabel_3 = ttk.Label(sframe,font=cnt_font,text="出題パターン")
    o = ttk.Style()
    colo = random.choice(colors)
    o.configure("color.TButton",background=colo,font=50)
    var.set(0)

    s = tk.Spinbox(sframe,textvariable=var,from_ = 1,to = len(A),increment=1)
    s.place(height=50,width=80,x=420,y=98)
    
    # value=0のラジオボタンにチェックを入れる
    val.set(0)

    # ラジオボタン作成
    rdo1 = tk.Radiobutton(sframe, value=0, variable=val, text='ランダム')
    rdo1.place(x=390, y=255)

    rdo2 = tk.Radiobutton(sframe, value=1, variable=val, text='苦手な問題')
    rdo2.place(x=190, y=255)
    button_start = ttk.Button(sframe,text="スタート",width=20,padding=25,command=lambda :first(sframe,var.get(),val.get()))
    slabel_1.pack()
    slabel_2.pack(pady=20)
    slabel_3.pack(pady=15,padx=40)
    button_start.pack(pady=70)

def add():
    add_frame = ttk.Frame(root)
    add_frame.pack(fill = tk.BOTH,pady = 10)
    t_en = ttk.Entry(add_frame)
    t_en.place(y=-40,relx=0.37,rely=0.5,anchor=tk.CENTER,height=60)
    t_ja = ttk.Entry(add_frame)
    t_ja.place(y=-40,relx=0.63,rely=0.5,anchor=tk.CENTER,height=60)
    en_label = ttk.Label(add_frame,text="英語",font=cnt_font)
    ja_label = ttk.Label(add_frame,text="日本語",font=cnt_font)
    en_label.place(y=-40,relx=0.18,rely=0.5,anchor=tk.CENTER,)
    ja_label.place(y=-40,relx=0.82,rely=0.5,anchor=tk.CENTER,)
    add_button = ttk.Button(add_frame,text="単語を追加する",width=20,padding=25,command=lambda :wo_add(t_ja.get(),t_en.get()))
    titlebutton = ttk.Button(add_frame,text="タイトルに戻る",width=20,padding=25,command=lambda :dest(0,add_frame))
    titlebutton.pack(pady=120,side=tk.BOTTOM)
    add_button.pack(pady=20,side=tk.BOTTOM)

def de(frame,lis):
    global A
    if len(lis) == 0:
        tk.messagebox.showerror('エラー', '単語が選択されていません。')
    else:
        if len(A) <= 1:
            tk.messagebox.showerror('エラー', 'これ以上単語を削除できません。最低でも1つ以上の単語を登録した状態にしてください。')
        else:
            A.pop(lis[0])
            odf = pd.DataFrame(A,columns=["1","2","3"])
            odf.to_csv(path + "/word.csv",encoding="cp932",index=False,header=False)
            setting(frame)

def setting(frame):
    global A
    frame.destroy()
    seframe = ttk.Frame(root,style="my.TFrame")
    seframe.pack(fill = tk.BOTH,pady = 10)
    words = [str(A[i][0])+ "   " + str(A[i][1]) for i in range(len(A))]
    words_v = tk.StringVar(seframe,value=words)
    t = ttk.Style()
    t.theme_use("classic")
    t.configure('my.TFrame',background="#87ceeb")
    listbox = tk.Listbox(seframe,listvariable=words_v,width=30,height=12)
    scrollbar = tk.Scrollbar(seframe, orient=tk.VERTICAL, command=listbox.yview)
    listbox["yscrollcommand"] = scrollbar.set
    listbox.grid(row=1,column=1,padx=60,columnspan=3)
    scrollbar.grid(row=1, column=3,sticky=(tk.N, tk.S))
    
    tex = ttk.Label(seframe,text="削除したい単語を選択してから\n[削除ボタン]を押してください。",font=set_font)
    tex.grid(row=0,column=0,rowspan=2,padx=20)
    n = ttk.Button(seframe,width=15,padding=15,text="単語を削除する",command=lambda : de(seframe,listbox.curselection()))
    n.grid(pady=20,row=2,column=0,columnspan=4)
    titlebutton = ttk.Button(seframe,text="タイトルに戻る",width=40,padding=20,command=lambda :dest(0,seframe))
    titlebutton.grid(pady=20,row=3,column=0,columnspan=8)

path = os.getcwd()

cnt = 0
B = []
cole = 0
color = "#000000 #333333 #666666 #999999 #cccccc #ffffff #ff3300 #cc3300 #ff6633 #993300 #cc6633 #ff9966 #ff6600 #663300 #996633 #cc9966 #cc6600 #ffcc99 #ff9933 #ff9900 #996600 #cc9933 #ffcc66 #cc9900 #ffcc33 #ffcc00 #333300 #666633 #666600 #999966 #999933 #999900 #cccc99 #cccc66 #cccc33 #cccc00 #ffffcc #ffff99 #ffff66 #ffff33 #ffff00 #ccff00 #99cc00 #ccff33 #669900 #99cc33 #ccff66 #99ff00 #336600 #669933 #99cc66 #66cc00 #ccff99 #99ff33 #66ff00 #339900 #66cc33 #99ff66 #33cc00 #66ff33 #33ff00 #003300 #336633 #006600 #669966 #339933 #009900 #99cc99 #66cc66 #33cc33 #00cc00 #ccffcc #99ff99 #66ff66 #33ff33 #00ff00 #00ff33 #00cc33 #33ff66 #009933 #33cc66 #66ff99 #00ff66 #006633 #339966 #66cc99 #00cc66 #99ffcc #33ff99 #00ff99 #009966 #33cc99 #66ffcc #00cc99 #33ffcc #00ffcc #003333 #336666 #006666 #669999 #339999 #009999 #99cccc #66cccc #33cccc #00cccc #ccffff #99ffff #66ffff #33ffff #00ffff #00ccff #0099cc #33ccff #006699 #3399cc #66ccff #0099ff #003366 #336699 #6699cc #0066cc #99ccff #3399ff #0066ff #003399 #3366cc #6699ff #0033cc #3366ff #0033ff #000033 #333366 #000066 #666699 #333399 #000099 #9999cc #6666cc #3333cc #0000cc #ccccff #9999ff #6666ff #3333ff #0000ff #3300ff #3300cc #6633ff #330099 #6633cc #9966ff #6600ff #330066 #663399 #9966cc #6600cc #cc99ff #9933ff #9900ff #660099 #9933cc #cc66ff #9900cc #cc33ff #cc00ff #330033 #663366 #660066 #996699 #993399 #990099 #cc99cc #cc66cc #cc33cc #cc00cc #ffccff #ff99ff #ff66ff #ff33ff #ff00ff #ff00cc #cc0099 #ff33cc #990066 #cc3399 #ff66cc #ff0099 #660033 #993366 #cc6699 #cc0066 #ff99cc #ff3399 #ff0066 #990033 #cc3366 #ff6699 #cc0033 #ff3366 #ff0033 #330000 #663333 #660000 #996666 #993333 #990000 #cc9999 #cc6666 #cc3333 #cc0000 #ffcccc #ff9999 #ff6666 #ff3333 #ff0000"
colors = color.split(" ")
# ウィンドウの作成

root = tk.Tk()
root.title('単語帳アプリ')
root.iconbitmap(path + '/testicon.ico')
root.geometry('650x450')


try:
    df = pd.read_csv(path + "/word.csv",encoding="cp932",header=None)
    A = df.values.tolist()
except pd.errors.EmptyDataError:
    df = pd.DataFrame(
    data={'0': ["エラー回避用"], 
          '1': ["消して大丈夫です"],
          '2': [0]}
    )
    A = df.values.tolist()
    tk.messagebox.showwarning('警告', '単語が登録されていません。登録をしてください。')
    #df.to_csv("word.csv",encoding="cp932",index=False,header=False)


#画像とフォントの作成
img_c = Image.open(path + "/correct.png")
img_w = Image.open(path + "/wrong.png")
img_c = img_c.resize((130,100))
img_w = img_w.resize((130,100))
img_c = ImageTk.PhotoImage(img_c)
img_w = ImageTk.PhotoImage(img_w)
bu_font = font.Font(root,size=10)
set_font = font.Font(root,size=15)
cnt_font = font.Font(root,size=20)
wo_font = font.Font(root,size=40)
word_font = font.Font(root,size=50)
s = ttk.Style()
s.configure("my.TButton",background="#e9967a",font=50)
val = tk.IntVar()
var = tk.IntVar(root)
title()
#first()
#フレームやウィジェットの作成


    #おまじない
root.mainloop()


# In[ ]:




