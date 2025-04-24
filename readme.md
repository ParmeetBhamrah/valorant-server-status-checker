
# Valorant Server Status Checker

A simple Python tool that checks if the **VALORANT** servers are down or working fine, by scraping data from a web service. This tool is designed to provide real-time updates on the server status, alerting users if there are any known issues with the game servers.

### Features:
- Fetches server status from [IsTheServiceDown.in](https://istheservicedown.in) using web scraping.
- Displays messages based on server status:
  - **VALORANT servers are working fine!**
  - **There might be issues with VALORANT servers at the moment.**
- Handles common errors like:
  - No internet connection
  - Invalid URL or HTTP errors
  - Failed HTML parsing
  
### Requirements:
- Python 3.x
- `requests` library
- `beautifulsoup4` library

### Setup:
1. Clone this repository:
   ```bash
   git clone https://github.com/ParmeetBhamrah/valorant-server-status-checker.git
   cd valorant-server-status-checker
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python script.py
   ```

### Example Output:
- When servers are working fine:
   ```text
   VALORANT servers are working fine!
   ```

- When there are issues with the servers:
   ```text
   There might be issues with VALORANT servers at the moment.
   Try again later.
   ```

- When there's no internet:
   ```text
   No internet connection detected.
   Please check your connection and try again.
   ```

- When there's an HTTP error or failed HTML parsing:
   ```text
   HTTP error occurred.
   ```

### How It Works:
1. The script makes an HTTP request to [IsTheServiceDown.in](https://istheservicedown.in/problems/valorant), which provides real-time information about server status.
2. It scrapes the page using `BeautifulSoup` to extract the server status.
3. Based on the extracted status, it prints a message indicating whether the servers are working fine or there are potential issues.

### Contributions:
Feel free to fork this project, open issues, or contribute enhancements. Here's what you could work on next:
- Support additional games (user-input driven)
- Save server status to a log file
- Send notifications (email or Telegram) when there's an issue

### License:
This project is open-source and available under the [MIT License](LICENSE).
