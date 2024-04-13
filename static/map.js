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
    
    for (const bus of data['cat']) {
        bus_markers.push(L.marker([bus.lat, bus.lon], {icon: bus1}).addTo(map))
    }
    for (const bus of data['gmt']) {
        bus_markers.push(L.marker([bus.lat, bus.lon], {icon: bus1}).addTo(map))
    }

    setBusPosition(1, data['gmt'][0].lat, data['gmt'][0].lon);
}
async function setRoutes() {
    const response = await fetch("/data/routes", {
        method: "POST",
    });
    const data = await response.json();
    
    setBusRoutes(data)
}
setRoutes()
updatePositions()
setInterval(() => {
    updatePositions();
}, 5000)
