document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const predictionDiv = document.getElementById('prediction');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        displayPrediction(data);
    });

    function displayPrediction(data) {
        predictionDiv.innerHTML = `<h2>Prediction Result</h2>`;
        for (const [medicine, prediction] of Object.entries(data)) {
            predictionDiv.innerHTML += `<p><strong>${medicine}:</strong> ${prediction}</p>`;
        }
    }
});
