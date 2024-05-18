# Fetch Citations from API

This Python script fetches data from a paginated API endpoint, identifies whether the response for each response-sources pair came from any of the sources, and lists down the sources from which the response was formed. The shortlisted sources are called citations.

## Requirements

- Python 3.x
- requests library

## Installation

1. **Clone the repository or download the script.**
2. **Install the required library using pip:**
   ```
   pip install requests
   ```

3. **Running the Script**:
   - Save the updated script as `fetch_citations.py`.
   - Run the script by navigating to the directory where the script is saved and using:
     ```sh
     python fetch_citations.py
     ```

This script includes proper error handling and checks for unexpected data formats. It should fetch and process data from the API, identifying citations and printing them.


