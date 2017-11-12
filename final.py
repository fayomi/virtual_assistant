import wx   #to import wx
import wolframalpha #to import wolframalpha API
import wikipedia    #to import wikipedia API
from espeak import espeak #to install espeak to speak audio


espeak.synth('Welcome, how can I help?')


class MyFrame(wx.Frame): #to design the GUI
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title='Pyda')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label='Hello I am PyDa, your Digital Assistant. How can I help?')
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def onEnter(self, event):#what happens when enter is pressed
        input = self.txt.GetValue()
        input = input.lower()



        try:#search wolframaplha first
            app_id = 'W37GXV-5LKPQ23Q2Y'
            client = wolframalpha.Client(app_id) #connects the app_id to the client

            res = client.query(input)
            answer = next(res.results).text #prints out the next result in text form

            print answer
            espeak.synth('the answer is '+answer)

        except: #if nothing from wolframalpha, then search wikipedia
            espeak.synth('Searched for '+input)
            print wikipedia.summary(input, sentences=3) #prints the first 3 sentences from result



if __name__ == '__main__': # to open GUI
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
