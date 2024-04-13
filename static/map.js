const GMT_VEHICLES_URL = "https://maps.trilliumtransit.com/gtfsmap-realtime/feed/ccta-vt-us/vehicles";
const GMT_ROUTES_URL = "https://gtfs-api.trilliumtransit.com/gtfs-api/routes/by-feed/ccta-vt-us"
const GMT_STOPS_URL = "https://gtfs-api.trilliumtransit.com/gtfs-api/stops/by-feed/ccta-vt-us/route-id/19137,19139,13496,13497,13498,3190,3191,7458,11182,7455,74419,74409,74410,74411,19141,74418,74413,3175,74412,3153,3176,3167,3177,3181,3168,3183,3197,3194,19140,3195,3196,3186,7335,74414,74415,3171,3172,3174,3188,74416,74417,3163,3164,3165,19138,32941,32942,11183,19143,19142,19144,19145,"

async function getVehicles() {
    const response = await fetch(GMT_VEHICLES_URL, {
        method: "GET",
    })

    console.log(response)
}

getVehicles();
