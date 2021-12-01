import rumps

class CryptoVisualizerApp(rumps.App):
    def __init__(self):
        super(CryptoVisualizerApp, self).__init__("CryptoVisualizer App", title='Crypto')
        self.menu = ["Preferences", "Silly button", "Say hi"]

    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state
    
    @rumps.clicked("On")
    def button(self, sender):
        print(sender)
        self.title = sender.title
        sender.title = 'Off' if sender.title == 'On' else 'On'
        Window("I can't think of a good example app...").run()

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

if __name__ == "__main__":
    CryptoVisualizerApp().run()