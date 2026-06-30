# 🌦️ Weather Web Scraper

A Python project that fetches real-time weather information for Indian cities by scraping data from AQI.in.

The application first determines the state of the entered city using the OpenStreetMap Nominatim API and then scrapes the weather details from the corresponding AQI.in weather page using BeautifulSoup.

## Features

- 🌍 Find the state of an Indian city automatically.
- 🌡️ Fetch current temperature.
- 💧 Fetch humidity.
- 🌬️ Fetch wind speed.
- 📈 Fetch atmospheric pressure.
- ⚠️ Handles invalid city names gracefully.
- 🕸️ Built using web scraping and HTTP requests.

## Tech Stack

- Python
- Requests
- BeautifulSoup4
- OpenStreetMap Nominatim API

## Project Structure

```
weather-web-scraper/
│
├── src/
│   ├── main.py
│   ├── state_finder.py
│
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

## Installation

Clone the repository

```bash
git clone https://github.com/Smokein96/Web-scraping-weather-app.git
```

Move into the project directory

```bash
cd Web-scraping-weather-app
```

Install the dependencies

```bash
pip install requests beautifulsoup4
```

or, if you're using **uv**

```bash
uv sync
```

## Usage

Run the application

```bash
python src/main.py
```

Example

```
Enter city name: Pune

Temperature : 29°C - Warm
Humidity    : 64%
Wind         : 14 km/h
Pressure     : 1008 mb
```

## How It Works

1. The user enters an Indian city.
2. The application uses the OpenStreetMap Nominatim API to determine the city's state.
3. It constructs the AQI.in weather URL.
4. The webpage is downloaded using the Requests library.
5. BeautifulSoup parses the HTML.
6. Weather information is extracted and displayed in the terminal.

## Dependencies

- requests
- beautifulsoup4

## Learning Objectives

This project helped me learn:

- HTTP requests
- Web scraping with BeautifulSoup
- HTML parsing
- Working with REST APIs
- Exception handling
- Project organization in Python
