import requests
import webbrowser


def edgar(full_name: str, email: str, ticker: str, form: str, year: str):
    """
    EDGAR Filing Search and Viewer

    This function searches the SEC EDGAR database for a company's filings
    based on the provided year and form type, and opens the first matching
    filing in a web browser.

    Parameters:
    ----------
    full_name : str
        Your full name. Required by SEC to identify automated requests.
        Example: "John Doe"
        
    email : str
        Your email address. Required by SEC to identify automated requests.
        Example: "johndoe@gmail.com"

    ticker : str
        The company's stock ticker symbol. This will be converted to the
        corresponding SEC CIK (Central Index Key) automatically.
        Example: "AAPL"

    form : str
        The type of SEC filing to search for. Matches the 'form' field in EDGAR.
        Example: "10-K", "10-Q", "8-K"

    year : str
        The year of filings to search for. Only filings where the filing date
        starts with this year will be included.
        Example: "2022"

    Returns:
    -------
    Opens the first matching SEC filing in a new browser tab.
    Prints the filing metadata and the direct SEC URL.

    Example usage:
    --------------
    edgar(
        full_name="John Doe",
        email="johndoe@gmail.com",
        ticker="AAPL",
        form="10-K",
        year="2022"
    )
    """

    # --- Convert ticker to CIK ---
    ticker = ticker.upper()
    url_ticker = "https://www.sec.gov/files/company_tickers.json"
    headers = {"User-Agent": f"{full_name} ({email})"}
    response = requests.get(url_ticker, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error fetching ticker list: {response.status_code}")

    data = response.json()
    CIK = None
    for item in data.values():
        if item['ticker'] == ticker:
            CIK = str(item['cik_str']).zfill(10)
            break

    if not CIK:
        raise Exception(f"Ticker {ticker} not found")

    # --- Fetch EDGAR JSON --- #
    url_edgar = f"https://data.sec.gov/submissions/CIK{CIK}.json"
    response = requests.get(url_edgar, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    data = response.json()
    recent_filings = data['filings']['recent']
    forms = recent_filings['form']
    dates = recent_filings['filingDate']
    filing_docs = recent_filings['primaryDocument']
    accession_numbers = recent_filings['accessionNumber']

    # --- Filter filings by year and form --- #
    filtered_filings = [
        {"form": f, "date": d, "document": u, "accession": a}
        for f, d, u, a in zip(forms, dates, filing_docs, accession_numbers)
        if d.startswith(year) and f.startswith(form)
    ]

    if not filtered_filings:
        print(f"No filings found for {form} in {year}")
        return

    first_filing = filtered_filings[0]
    print("First filing:", first_filing)

    # --- Build correct URL ---
    accession_clean = first_filing["accession"].replace("-", "")
    doc_url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{accession_clean}/{first_filing['document']}"
    print("Document URL:", doc_url)

    # --- Open in browser ---
    webbrowser.open_new_tab(doc_url)