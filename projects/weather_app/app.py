import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        # adding widgets in main method
        self.city_label = QLabel("City: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI() # calling new function for auxilary actions
        
    def initUI(self):
       self.setWindowTitle("Weather App")

       # making the widgets pan out vertically
       vbox = QVBoxLayout()

       vbox.addWidget(self.city_label)
       vbox.addWidget(self.city_input)
       vbox.addWidget(self.get_weather_button)
       vbox.addWidget(self.temperature_label)
       vbox.addWidget(self.emoji_label)
       vbox.addWidget(self.description_label)

       self.setLayout(vbox)

       # making widgets aligned to center
       self.city_label.setAlignment(Qt.AlignCenter)
       self.city_input.setAlignment(Qt.AlignCenter)
       self.temperature_label.setAlignment(Qt.AlignCenter)
       self.emoji_label.setAlignment(Qt.AlignCenter)
       self.description_label.setAlignment(Qt.AlignCenter)

       # stylling 1) labelling objects 2) css
       self.city_label.setObjectName("city_label")
       self.city_input.setObjectName("city_input")
       self.get_weather_button.setObjectName("get_weather_button")
       self.temperature_label.setObjectName("temperature_label")
       self.emoji_label.setObjectName("emoji_label")
       self.description_label.setObjectName("description_label")

       self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;          
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;          
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px; 
            }
            QLabel#emoji_label{
                font-size: 100px; 
                font-family: Segoe UI Emoji; 
            } 
            QLabel#description_label{
                font-size: 50px;
            } 
       """) # Segoe UI Emoji for windows - & Linux cant render colored emojis
       
       self.get_weather_button.clicked.connect(self.get_weather)   

    def get_weather(self):
        print('get_weather')
        api_key = "8c215fad03ab9599ab3320a7c012661b"
        city = self.city_input.text().lower()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status() # need for except requests.exceptions.HTTPError: later
            # print(response)

            if response.status_code == 200:
                weather_data = response.json() 
                # print("data retrieved.")
                print(url)
                self.display_weather(weather_data)
                return weather_data

        # IMPORTANT
        except requests.exceptions.HTTPError as http_error: # ⬆️ response.raise_for_status() is needed in try block
            # print(f"HTTPError. Status code {response.status_code}") # if city is not available
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nCheck your input.")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCity not found.")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later.")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid resoponse from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down.")
                case 504:
                    self.display_error("Gateway timeout:\nNo response from the server.")
                case _:
                    self.display_error(f"HTTPError:{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection.")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out.")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck your URL.")

        except requests.exceptions.RequestException as req_error: # network prob , invalid urls
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)

    def display_weather(self, data):
        print('display_weather')
        # if data:
            # print(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())        