function webSocketConnection() {
    const url = `ws://${window.location.host}/ws/socket-server/`;
    const socket = new WebSocket(url);

    document.addEventListener('mousemove', updateCoordinates);
    document.addEventListener('click', trackCoordinates);

    socket.onmessage = function (event) {
        event.preventDefault();

        const data = JSON.parse(event.data);
        console.log('Data:', data.message);
    };

    function updateCoordinates(event) {
        event.preventDefault();

        const coord_x = event.clientX;
        const coord_y = event.clientY;

        document.getElementById('coordinates')
            .innerText = `Live Coordinates - X: ${coord_x}, Y: ${coord_y}`;
    }

    function trackCoordinates(event) {
        event.preventDefault();

        const clicked_x = event.clientX;
        const clicked_y = event.clientY;

        document.getElementById('saved-coordinates')
            .innerText = `Saved Coordinates - X: ${clicked_x} Y: ${clicked_y}`;

        socket.send(JSON.stringify({
            clicked_x: clicked_x,
            clicked_y: clicked_y,
        }));
    }
}

