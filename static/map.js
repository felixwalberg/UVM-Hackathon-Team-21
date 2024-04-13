async function updatePositions() {
    const response = await fetch("/data/vehicles", {
        method: "POST",
    });
    console.log(await response.json())
}

updatePositions()
