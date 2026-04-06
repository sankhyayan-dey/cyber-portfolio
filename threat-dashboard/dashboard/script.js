async function fetchData() {
    const now = new Date();
    const past = new Date();

    // last 7 days
    past.setDate(now.getDate() - 7);

    function formatDate(date) {
        return date.toISOString().split(".")[0] + ".000Z";
    }

    const startDate = formatDate(past);
    const endDate = formatDate(now);

    const url = `https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=10&pubStartDate=${startDate}&pubEndDate=${endDate}`;

    const response = await fetch(url);
    const data = await response.json();

    const vulnerabilities = data.vulnerabilities;

    let filtered = [];

    vulnerabilities.forEach(vuln => {
        const cve = vuln.cve;

        const id = cve.id;
        const description = cve.descriptions[0].value;

        let severity = "UNKNOWN";
        let score = "N/A";

        if (cve.metrics.cvssMetricV31) {
            const cvss = cve.metrics.cvssMetricV31[0].cvssData;
            severity = cvss.baseSeverity;
            score = cvss.baseScore;
        }

        if (severity === "HIGH" || severity === "CRITICAL") {
            filtered.push({ id, description, severity, score });
        }
    });

    renderData(filtered);
}

function renderData(data) {
    const container = document.getElementById("vulnerabilities");

    let critical = 0;
    let high = 0;

    container.innerHTML = "";

    data.forEach((v, index) => {
        if (v.severity === "CRITICAL") critical++;
        if (v.severity === "HIGH") high++;

        const div = document.createElement("div");
        div.className = "card";

        div.innerHTML = `
            <div class="card-header">
                <span class="cve-id">${v.id}</span>
                <span class="severity ${v.severity.toLowerCase()}">${v.severity}</span>
            </div>
            <p class="cvss">CVSS: ${v.score}</p>
            <p class="desc">${v.description}</p>
        `;

        container.appendChild(div);
    });

    document.getElementById("total").innerText = data.length;
    document.getElementById("critical").innerText = critical;
    document.getElementById("high").innerText = high;
}

fetchData();