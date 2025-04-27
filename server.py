import socketio
import serial
import eventlet
import eventlet.wsgi

# Set this to the port your ESP32 is using
# On Windows it might be 'COM3', 'COM4' etc. — check in Device Manager
# On Mac/Linux it might be '/dev/ttyUSB0' or similar
ser = serial.Serial('COM3', 115200)

# Create a Socket.IO server
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

# Handle data received from the p5.js sketch
@sio.on('video-grid')
def handle_grid(sid, grid):
    flat = bytearray()
    for row in grid:
        for r, g, b in row:
            flat.extend([r, g, b])
    try:
        ser.write(flat)
    except Exception as e:
        print("Serial error:", e)

# Run the server
if __name__ == '__main__':
    print("Server started on http://0.0.0.0:3000")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 3000)), app)
