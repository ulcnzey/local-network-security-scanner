const scanButton = document.getElementById("scanButton");
const targetInput = document.getElementById("targetInput");
const radarLabel = document.querySelector(".radar-label");
const radar = document.querySelector(".radar");


scanButton.addEventListener("click", async () => {

    const target = targetInput.value.trim();

    // Hedef kontrolü
    if (!target) {
        radarLabel.textContent = "ENTER TARGET";
        targetInput.focus();
        return;
    }

    // Tarama durumunu başlat
    scanButton.disabled = true;
    scanButton.querySelector("span:first-child").textContent = "SCANNING...";
    radarLabel.textContent = "SCANNING TARGET...";
    radar.classList.add("scanning");

    try {

        // Flask API'ye istek gönder
        const response = await fetch("/scan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                target: target
            })
        });

        const data = await response.json();

        // Hata kontrolü
        if (!data.success) {
            throw new Error(data.error || "Scan failed.");
        }

        // Sonuçları ekrana göster
        displayResults(data);

        radarLabel.textContent = "SCAN COMPLETED";

    } catch (error) {

        console.error(error);

        radarLabel.textContent = "SCAN FAILED";

        alert(error.message);

    } finally {

        scanButton.disabled = false;
        scanButton.querySelector("span:first-child").textContent = "SCAN TARGET";
        radar.classList.remove("scanning");
    }
});


function displayResults(data) {

    // Daha önce oluşturulmuş sonuç alanı varsa kaldır
    const oldResults = document.querySelector(".results-section");

    if (oldResults) {
        oldResults.remove();
    }

    // Sonuç bölümü
    const resultsSection = document.createElement("section");

    resultsSection.className = "results-section";

    // Açık portlar
    let portsHTML = "";

    if (data.open_ports.length === 0) {

        portsHTML = `
            <div class="no-ports">
                No open TCP ports detected.
            </div>
        `;

    } else {

        data.open_ports.forEach(port => {

            portsHTML += `
                <div class="result-row">

                    <div>
                        <span class="result-label">PORT</span>
                        <strong>${port.port}</strong>
                    </div>

                    <div>
                        <span class="result-label">PROTOCOL</span>
                        <strong>${port.protocol}</strong>
                    </div>

                    <div>
                        <span class="result-label">STATE</span>
                        <strong class="status-open">${port.state}</strong>
                    </div>

                    <div>
                        <span class="result-label">SERVICE</span>
                        <strong>${port.service}</strong>
                    </div>

                </div>
            `;
        });
    }


    resultsSection.innerHTML = `

        <div class="results-header">

            <div>
                <span class="small-label">SCAN RESULT</span>

                <h2>Network analysis</h2>
            </div>

            <div class="target-result">
                ${data.target}
            </div>

        </div>


        <div class="host-status">

            <span class="status-dot"></span>

            <div>
                <span class="result-label">HOST STATUS</span>
                <strong>${data.status}</strong>
            </div>

        </div>


        <div class="ports-container">

            <div class="ports-header">
                <span>OPEN PORTS</span>
                <span>${data.open_ports.length} detected</span>
            </div>

            ${portsHTML}

        </div>

    `;


    // Sonuçları sayfaya ekle
    const mainContainer = document.querySelector(".main-container");

    mainContainer.appendChild(resultsSection);

    // Sonuçlara yumuşak şekilde kaydır
    resultsSection.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}

