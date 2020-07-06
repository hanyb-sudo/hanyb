from win32com.client import constants
import os
import win32com.client
import pythoncom
import win32con
import win32api
import time


class SpeechRecognition:
    def __init__(self,wordsToAddd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule",constants.SRATopLevel + constants.SRADynamic,0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAddd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule",1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self,phrase):
        self.speaker.Speak(phrase)

class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, Streamposition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("说：",newResult.PhraseInfo.GetText())
        dos =  newResult.PhraseInfo.GetText()
        if dos=='上':
            self.keyWord(38)
            print("上")
        elif dos=='下':
            self.keyWord(40)
            print("下")
        elif dos=='左':
            self.keyWord(37)
            print("左")
        elif dos=='右':
            self.keyWord(39)
            print("右")
    def keyWord(self, num):
        win32api.keybd_event(num, 0, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(num, 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__=='__main__':
    wordsToAdd = ["上","下","左","右"]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()