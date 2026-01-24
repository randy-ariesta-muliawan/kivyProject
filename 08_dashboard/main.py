import json
from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.config import Config

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder


LabelBase.register(name='Roboto',
					fn_regular='assets/font/Roboto-Thin.ttf',
					fn_bold='assets/font/Roboto-Medium.ttf')

WIDTH = 9*40
HEIGHT = 16*40

Config.set('graphics', 'width', f'{WIDTH}')
Config.set('graphics', 'height', f"{HEIGHT}")
Config.write()

Window.clearcolor = get_color_from_hex("#101216")

class MyApp(MDApp):
	
	def __init__(self):
		super().__init__()
		self.data = None
		self.load_data("users.json")
		print(self.data["budi_geming"]["nama_lengkap"])
		self.pengguna = "budi_geming"

		self.title = "My KIVY MD APP"

		self.screen_manager = ScreenManager()
		# self.screen_manager.add_widget(Builder.load_file("pages/splash.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv"))
		

	def load_data(self, path):
		with open(path, "r") as json_data:
			self.data = json.load(json_data)


	def build(self):
		self.screen_manager.current = "login"
		return self.screen_manager

	# def on_start(self):
	#   	Clock.schedule_once(self.to_login_page, 3)

	def logger(self):
		username_entry = self.screen_manager.screens[0].ids['username_entry'].text
		password_entry = self.screen_manager.screens[0].ids['password_entry'].text
		if username_entry in self.data:
			if password_entry == self.data[username_entry]["password"]:
				self.pengguna = username_entry
				self.screen_manager.add_widget(Builder.load_file("pages/dashboard.kv"))
				self.screen_manager.current = "dashboard"
		else:
			pass

if __name__ == '__main__':
	app = MyApp()
	app.run()