import speech_recognition as sr
import pygame as pg
import sqlite3
from gtts import gTTS
r = sr.Recognizer()
m = sr.Microphone()
c = 0
pg.mixer.init()
def play_music(music_file, volume=1.0):
    pg.mixer.music.set_volume(volume)
    pg.mixer.music.load(music_file)
    
    clock = pg.time.Clock()
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)
    #try:
    #except pg.error:
    #print("File {} not found! ({})".format(music_file, pg.get_error()))
    return
try:
    print("A moment of silence, please...")
    
    while 1==1:
        c = c + 1
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            value1 = r.recognize_google(audio)
            if str is bytes:
                print(u"You said {}".format(value1).encode("utf-8"))
            else:
                print("You said {}".format(value1))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        conn = sqlite3.connect('test.db')
        data = conn.execute("select * from Bot where Query = '"+value1+"'" )
        
        text  =''
        file=''
        if value1=='quit':
            text = "Bye"
            print(text)
            speech = gTTS(text,'en')
            file = "a" + str(c) + "gir.mp3"
            speech.save(file)
            music_file = file
            volume = 0.8
            play_music(music_file, volume)
            break
        if data == None:
            conn.execute("create table if not exists Train(Query text)")
            conn.execute("insert into Bot(Query,Answer) values(?,?)",(value1))
            text = "Sorry could not process your Data"
            print(text)
            speech = gTTS(text,'en')
            file = "a" + str(c) + "gir.mp3"
            speech.save(file)
            conn.commit
            music_file = file
            volume = 0.8
        for row in data:
            text = "Bot:" + row[1]
            text1=row[1]
            print(text)
            speech = gTTS(text1,'en')
            file = "a" + str(c) + "gir.mp3"
            speech.save(file)
            music_file = file
            volume = 0.8
            play_music(music_file, volume)
except KeyboardInterrupt:
    pass
