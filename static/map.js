bus_markers = []
bus_routes = []

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
async function setRoutes() {
    const response = await fetch("/data/stops", {
        method: "POST",
    });
    const data = await response.json();
    
    for (const route of data) {
        setBusRoutes(route);
    }
}
setRoutes()
updatePositions()
setInterval(() => {
    updatePositions();
}, 5000)
