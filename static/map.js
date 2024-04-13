bus_markers = []

async function updatePositions() {
    const response = await fetch("/data/vehicles", {
        method: "POST",
    });
    const data = await response.json();

    for (const marker of bus_markers) {
        marker.remove()
    }
    
    for (const bus of data) {
        bus_markers.push(L.marker([bus.lat, bus.lon], {icon: bus1}).addTo(map))
    }

    setBusPosition(1, data[0].lat, data[0].lon);
}

updatePositions()
setInterval(() => {
    updatePositions();
}, 5000)
