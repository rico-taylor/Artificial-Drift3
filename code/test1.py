import pyglet
from pyglet.window import mouse

# Window setup
window = pyglet.window.Window(600, 400)
batch = pyglet.graphics.Batch()

# Data (example entries)
data = [
    ('User1', '01:23', '2024-10-01'),
    ('User2', '01:25', '2024-10-02'),
    ('User3', '01:20', '2024-10-03'),
    ('User4', '01:28', '2024-10-04'),
    ('User5', '01:22', '2024-10-05'),
    ('User6', '01:26', '2024-10-06'),
    ('User7', '01:24', '2024-10-07'),
    ('User8', '01:21', '2024-10-08'),
    ('User9', '01:23', '2024-10-09'),
    ('User10', '01:27', '2024-10-10'),
    ('User11', '01:22', '2024-10-11'),
    ('User12', '01:30', '2024-10-12'),
]

# Constants
row_height = 30
visible_rows = 10
table_start_y = 350  # Starting Y position for the first row
scroll_offset = 0
me = 0
# Create a label for each row in the data
labels = []

def update_labels():
    global labels
    labels = []
    start_idx = scroll_offset
    end_idx = min(scroll_offset + visible_rows, len(data))
    
    for i, row in enumerate(data[start_idx:end_idx]):
        username, lap_time, date_completed = row
        y_pos = table_start_y - (i * row_height)
        labels.append(pyglet.text.Label(username, x=50, y=y_pos, batch=batch))
        labels.append(pyglet.text.Label(lap_time, x=200, y=y_pos, batch=batch))
        labels.append(pyglet.text.Label(date_completed, x=400, y=y_pos, batch=batch))

update_labels()

# Scrolling functionality
@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    global scroll_offset
    if scroll_y > 0 and scroll_offset > 0:
        scroll_offset -= 1  # Scroll up
    elif scroll_y < 0 and scroll_offset < len(data) - visible_rows:
        scroll_offset += 1  # Scroll down
    update_labels()

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()