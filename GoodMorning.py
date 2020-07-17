from win32com.client import Dispatch

def speech(str):
    speak=Dispatch(("SAPI.spVoice"))
    speak.speak(str)

if __name__=="__main__":
    # list1=[1,2,3,4,5,6,7]
    # for i in list1:
    #     speech(i)
    file1=open('hello.txt',encoding="utf8")
    content=file1.read()
    speech(content)