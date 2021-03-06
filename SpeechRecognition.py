import speech_recognition as sr
import os
import shutil
import subprocess



##Variables declare
audio_result = ""


def converFile():
    testdir = os.path.dirname(os.path.realpath(__file__)) + '/music'
    testfile = os.path.join(testdir,"s.wav")
    outputpath = os.path.dirname(os.path.realpath(__file__)) + '/music'
    outputFile = os.path.join(outputpath,"sM4a.wav")
    print( outputFile, "\n", testfile )
    cmd = [ "ffmpeg", "-i", testfile, outputFile ]
    #subprocess.call(cmd, shell = True)
    subprocess.run( cmd )


    #process = Popen(command, shell=True)
    #subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=process.pid))
    print("Convert m4a to wav Success")


def Speech_Recognition():   
    audio_dirpath = os.path.dirname(os.path.realpath(__file__)) + '/music'
    AUDIO_FILE_EN = os.path.join(audio_dirpath, "sM4a.wav")
    r = sr.Recognizer()
    # use the audio file as the audio source
    with sr.AudioFile(AUDIO_FILE_EN) as source:
        audio_en = r.record(source)  # read the entire audio file
    
    # grammar example using Sphinx
    try:
        print("My own voice file")
        audio_result = str( r.recognize_google(audio_en) )
        return audio_result
    except sr.UnknownValueError:
        audio_result = "Sphinx could not understand audio"
        return audio_result 
    except sr.RequestError as e:
        audio_result = str( "Sphinx error; {0}".format(e) )
        return audio_result 

def CleanData():
    audio_dirpath = os.path.dirname(os.path.realpath(__file__)) + '/music'
    shutil.rmtree( audio_dirpath )
    os.makedirs(audio_dirpath)



#if __name__ == '__main__':
#    uploadMusic.app.run()
#    audio_result = Speech_Recognition()
#    WriteResult()
#    CleanData()
    