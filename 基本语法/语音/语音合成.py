# 系统客户端
import win32com.client

# 系统识别字符串并说话
speaker = win32com.client.Dispatch("SAPI.SPVOICE")

speaker.Speak("hanyb is a good boy!")
