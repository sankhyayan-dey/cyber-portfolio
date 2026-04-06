def parse_vulnerabilities(data, allowed_severity=None):
    """
    Extract and filter relevant fields from raw CVE data

    Parameters:
        data (dict): Raw JSON data from NVD API
        allowed_severity (list): List of severity levels to include

    Returns:
        list: List of parsed vulnerability dictionaries
    """

    if not data:
        return []

    if allowed_severity is None:
        allowed_severity = ["HIGH", "CRITICAL"]

    parsed_list = []

    vulnerabilities = data.get("vulnerabilities", [])

    for vuln in vulnerabilities:
        cve = vuln.get("cve", {})

        # CVE ID
        cve_id = cve.get("id", "N/A")

        # Description
        descriptions = cve.get("descriptions", [])
        description = (
            descriptions[0].get("value", "No description")
            if descriptions else "No description"
        )

        # Severity + CVSS Score
        metrics = cve.get("metrics", {})
        severity = "UNKNOWN"
        cvss_score = "N/A"

        if "cvssMetricV31" in metrics:
            cvss_data = metrics["cvssMetricV31"][0]["cvssData"]
            severity = cvss_data.get("baseSeverity", "UNKNOWN")
            cvss_score = cvss_data.get("baseScore", "N/A")

        # Filtering based on severity
        if severity not in allowed_severity:
            continue

        parsed_list.append({
            "cve_id": cve_id,
            "description": description,
            "severity": severity,
            "cvss_score": cvss_score
        })

    return parsed_list