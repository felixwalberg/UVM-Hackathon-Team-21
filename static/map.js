async function updatePositions() {
    const response = await fetch("/data/vehicles", {
        method: "POST",
    });
    const data = await response.json();
    setBusPosition(1, data[0].lat, data[0].lon);
}

setInterval(() => {
    updatePositions()
}, 5000)
