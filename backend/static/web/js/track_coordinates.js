function webSocketConnection() {
    const url = `ws://${window.location.host}/ws/socket-server/`;
    const socket = new WebSocket(url);

    document.addEventListener('mousemove', updateCoordinates);
    document.addEventListener('click', trackCoordinates);

    socket.onmessage = function (event) {
        event.preventDefault();

        const eventData = JSON.parse(event.data);

        if (eventData['image_url']) {
            displayImage(eventData['image_url']);
        }
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

    function displayImage(imageUrl) {
        const imageContainer = document.getElementById('image-container');
        const imgElement = document.createElement('img');

        imageContainer.innerHTML = '';
        imgElement.src = imageUrl;
        imgElement.alt = 'Captured Image';
        imageContainer.appendChild(imgElement);
    }
}

