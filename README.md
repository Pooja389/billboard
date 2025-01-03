# billboard
A code that makes a playlist in spotify of desired date  by scraping from billboard
# Billboard Top 20 Playlist Creator

This Python project scrapes the **Top 20 Billboard songs** for a user-specified date and creates a private playlist on Spotify with those songs.
## clone the repository
```bash
git clone https://github.com/Pooja389/billboard.git
```
## Requirements

To run this project, you need the following Python packages:

- `selenium` (for web scraping Billboard chart data)
- `spotipy` (for interacting with the Spotify API)

You can install these packages using pip:

```bash
pip install spotipy
```
```bash
pip install selenium
```
##  Spotify API Setup:

You'll need to create an app on Spotify Developer Dashboard to obtain the following credentials:
1. client_id
2. client_secret
3. redirect_uri (usually http://localhost:7000/callback)
Set these credentials in the script in the following variables:
1. client_id
2. client_secret
## Create a Spotify Playlist:

This script will create a private playlist on your Spotify account using the Top 20 Billboard songs for a specific date.
Billboard Chart Date:

Input the date (in yyyy-mm-dd format) for which you want to scrape the Billboard Top 100 chart.

## WebDriver:
This script uses Selenium to scrape the Billboard website. You need to have the Chrome WebDriver installed. You can download it from here.

## How to run
Clone the repository or create a new Python script.
Install the required packages.
Input your Spotify credentials (client_id, client_secret, redirect_uri).
## Run the script.
```bash
python spotify.py
