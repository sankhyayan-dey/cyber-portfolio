from datetime import datetime, timedelta, timezone
import requests


API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def fetch_latest_vulnerabilities(results_per_page=5):
    """
    Fetch recent CVE data from NVD API
    """

    # Get last 2 days data
    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=7)

    params = {
        "resultsPerPage": results_per_page,
        "pubStartDate": start_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "pubEndDate": end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch data: {e}")
        return None