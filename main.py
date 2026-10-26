import requests
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout

class WeatherApp(MDApp):
    def build(self):
        screen = MDScreen()
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.title_label = MDLabel(text='Weather App', halign='center', font_style='Headline')
        layout.add_widget(self.title_label)
        self.city_input = MDTextField(hint_text='Enter city name (e.g. Tokyo)', mode='filled')
        layout.add_widget(self.city_input)
        search_button = MDButton(MDButtonText(text='Check Weather'), pos_hint={'center_x': 0.5}, on_release=self.get_weather)
        layout.add_widget(search_button)
        self.result_label = MDLabel(text='', halign='center', font_style='Title')
        layout.add_widget(self.result_label)
        screen.add_widget(layout)
        return screen

    def get_weather(self, instance):
        city = self.city_input.text
        if not city:
            self.result_label.text = 'Please enter a city name'
            return
        api_key = '7ee01e540038e7e4a2bc861ec121e319'
        url = f"http://openweathermap.org{city}&appid={api_key}&lang=en&units=metric"
        try:
            response = requests.get(url).json()
            if response.get('cod') == 200:
                weather = response['weather'][0]['description']
                temp = response['main']['temp']
                self.result_label.text = f'Weather in {city}: {weather}\nTemp: {temp}C'
            else:
                self.result_label.text = 'City not found'
        except Exception as e:
            self.result_label.text = 'Error occurred'

if __name__ == '__main__':
    WeatherApp().run()
