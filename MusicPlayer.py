def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)
    
def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='Playing.....')
def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100
        
def volumedown():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100
def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stoped.....')

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Paused....')
def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    root.mutebutton.grid()
    ProgressbarLabel.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value']=40
    ProgressbarVolumeLabel['text']='40%'
    mixer.music.play()
    AudioStatusLabel.configure(text='Playing.....')

    Song=MP3(ad)
    totalsonglength=int(Song.info.length)
    ProgressbarMusic['maximum']=totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progressbarmusictick():
        CurrentSongLength=mixer.music.get_pos()//1000
        ProgressbarMusic['value']=CurrentSongLength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()    
        

    

def musicurl():
    try:
        dd=filedialog.askopenfilename(initialdir='F:songs/Audio songs/Ram',
                                      title='Select Audio File',
                                      filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
        dd=filedialod.askopenfilename(title='Select Audio File',
                                      filetype=(('MP3','*.mp3'),('WAV','*.wav')))

    audiotrack.set(dd)     
    

def createwidthes():
    '''
    global implay,impause,imstop,imbrowse,imvolumeup,imvolumedown
    ###=====Images Register===========
    implay= PhotoImage(file='Play.png')
    impause= PhotoImage(file='Pause.png')
    imbrowse= PhotoImage(file='Browsing.png')
    imvolumeup= PhotoImage(file='VolumeUp.png')
    imvolumedown= PhotoImage(file='VolumeDown.png')
    imstop= PhotoImage(file='Stop.png')
    ###=====Change Images size========
    implay=implay.subsample(2,2)
    impause=impause.subsample(2,2)
    imbrowse=imbrowse.subsample(2,2)
    imvolumeup=imvolumeup.subsample(2,2)
    imvolumedown=imvolumedown.subsample(2,2)
    imstop=imstop.subsample(2,2)'''
    global AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicStartTimeLabel,ProgressbarMusicEndTimeLabel
    ####========Lables========
    TrackLabel=Label(root,text="Select Audio Track :",background='lightskyblue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel=Label(root,text="",background='lightskyblue',font=('arial',15,'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1,padx=20,pady=20)
    ####========Entry Box========
    TrackLabelEntry=Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    ###======Buttons===========
    BrowseButton = Button(root,text='Search',background='deeppink',font=('arial',13,'italic bold'),
                          width=20,bd=5,activebackground='purple4',command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root,text='Play',background='green2',font=('arial',13,'italic bold'),
                        width=20,bd=5,activebackground='purple4',command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    root.PauseButton = Button(root,text='Pause',background='yellow',font=('arial',13,'italic bold'),
                         width=20,bd=5,activebackground='purple4',command=pausemusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume',background='yellow',font=('arial',13,'italic bold'),
                         width=20,bd=5,activebackground='purple4',command=resumemusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    root.mutebutton=Button(root,text='Mute',width=10,bg='yellow',font=('arial',13,'italic bold'),
                           activebackground='purple4',bd=5,command=mutemusic)
    root.mutebutton.grid(row=3,column=3)
    root.mutebutton.grid_remove()

    root.unmutebutton=Button(root,text='UnMute',width=10,bg='yellow',font=('arial',13,'italic bold'),
                             activebackground='purple4',bd=5,command=unmutemusic)
    root.unmutebutton.grid(row=3,column=3)
    root.unmutebutton.grid_remove()

    VolumeUpButton = Button(root,text='Volume Up',background='blue',font=('arial',13,'italic bold'),
                            width=20,bd=5,activebackground='purple4',command=volumeup)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

    StopButton = Button(root,text='Stop',background='red',font=('arial',13,'italic bold'),
                        width=20,bd=5,activebackground='purple4',command=stopmusic)
    StopButton.grid(row=2,column=0,padx=20,pady=20)

    VolumeDownButton = Button(root,text='Volume Down',background='blue',font=('arial',13,'italic bold'),
                              width=20,bd=5,activebackground='purple4',command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

    ####Progressbar Volume=====
    ProgressbarLabel=Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()

    ProgressbarVolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                  value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)
    

    ProgressbarVolumeLabel=Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)
    
    ###======Progress bar music========
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)
    

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)

    
    
    


from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root= Tk()
root.geometry("1100x500+200+50")
root.title('Simple Music Player')
root.iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')
####global vaiables====
audiotrack=StringVar()
currentvol=0
totalsonglength=0
###Create Slider
ss='Developed By Nitin Garg'
count=0
text=''
SliderLabel=Label(root,text=ss,bg='lightskyblue',font=('arial',40,'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
    global count,text
    if(count>=len(ss)):
        count=-1
        text=''
        SliderLabel.configure(text=text)
    else:
        text=text+ss[count]
        SliderLabel.configure(text=text)
    count+=1
    SliderLabel.after(200,IntroLabelTrick)
IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()
