import requests

def fetch_data_from_api(url, page):
    """
    Fetch data from the API for a given page.
    :param url: Base API URL.
    :param page: Page number to fetch.
    :return: JSON data from the API response.
    """
    try:
        response = requests.get(url, params={'page': page})
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def identify_citations(data):
    """
    Identify citations from the given data.
    :param data: List of dictionaries containing response text and sources.
    :return: List of citations.
    """
    citations = []
    for item in data:
        response_text = item.get("response", "")
        sources = item.get("sources", [])
        item_citations = []
        for source in sources:
            source_context = source.get("context", "")
            if source_context.lower() in response_text.lower():
                item_citations.append({"id": source["id"], "link": source.get("link", "")})
        citations.append(item_citations)
    return citations

def main():
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    all_citations = []

    # Fetch data from API and process paginated responses
    page = 1
    while True:
        data = fetch_data_from_api(api_url, page)
        if not data:
            break
        if isinstance(data, dict) and "results" in data:  # Check if 'results' key exists
            data = data["results"]
        if not isinstance(data, list):
            print(f"Unexpected data format on page {page}: {data}")
            break
        citations = identify_citations(data)
        all_citations.extend(citations)
        page += 1

    print("Citations:")
    for citation in all_citations:
        print(citation)

if __name__ == "__main__":
    main()
