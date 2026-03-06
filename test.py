from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):

	def __init__(self):
		super().__init__()
		self.title = "Test App"

	def build(self):
		label = Label(text="Hello World")
		return label

def main():
	app = TestApp()
	app.run()

if __name__ == '__main__':
	main()