# Microsoft-Hackthon
Sure! Here are the instructions for running the given code:

1. Install the required packages:
   - `geopy`: You can install it using `pip install geopy`.
   - `timezonefinder`: You can install it using `pip install timezonefinder`.
   - `requests`: You can install it using `pip install requests`.
   - `pytz`: You can install it using `pip install pytz`.
   - `Pillow`: You can install it using `pip install Pillow`.

2. Make sure you have the required image files:
   - `download.png`: This should be the icon image for the application.
   - `logos/box-hori.png`: This should be an image for the round box in the UI.
   - `logos/search-bar.png`: This should be an image for the search bar in the UI.
   - `logos/search-icon.png`: This should be an image for the search icon in the UI.
   - `logos/bottom-box-hori.png`: This should be an image for the bottom box in the UI.
   - `logos/bottom-box-ver.png`: This should be an image for the bottom box in the UI.
   - `icon/`: This folder should contain weather icons in the format `{icon_code}@2x.png`. Make sure you have the appropriate weather icons in this folder.

3. Import the necessary packages in your Python environment:
   ```python
   from tkinter import *
   import tkinter as tk
   from geopy.geocoders import Nominatim
   from tkinter import ttk, messagebox
   from timezonefinder import TimezoneFinder
   from datetime import *
   import requests
   import pytz
   from PIL import Image, ImageTk
   ```

4. Copy and paste the provided code into your Python environment.

5. Run the code and the weather application window will appear.

6. Enter the desired city name in the search bar and click the search icon.

7. The application will display the current weather information for the specified city, including temperature, humidity, pressure, wind speed, and a weather description. It will also show the current time, timezone, and latitude/longitude coordinates of the location.

8. The application will also display the weather forecast for the next day, including the day of the week, an icon representing the weather condition, and the maximum and minimum temperatures for that day.

Note: Make sure you have a stable internet connection to fetch weather data from the OpenWeatherMap API.

That's it! You should now be able to use the weather application created with Tkinter.
