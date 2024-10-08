import pyglet
import time
import threading

# Function to be executed in the terminal
def terminal_function():
    # This function can perform any logic or interact with the terminal
    print("Running terminal function")
    # Example logic
    for i in range(5):
        print(f"Terminal output: {i}")
        # Simulate some work
        time.sleep(1)
    print("Terminal function completed")

# Create a Pyglet window
window = pyglet.window.Window(800, 600, "Pyglet App")

@window.event
def on_draw():
    window.clear()

# Run the terminal function in a separate thread
thread = threading.Thread(target=terminal_function)
thread.start()

# Start the Pyglet event loop
pyglet.app.run()