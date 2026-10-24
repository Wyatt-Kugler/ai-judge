import time

# Simulate a 16x2 LCD display buffer
# Each row holds 16 characters
class SimulatedLCD:
    def __init__(self, cols=16, rows=2):
        self.cols = cols
        self.rows = rows
        # Initialize display with spaces
        self.buffer = [" " * cols for _ in range(rows)]
        self.display_offset = 0

    def begin(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.buffer = [" " * cols for _ in range(rows)]

    def print(self, text):
        # Place text on the first row, padded to fit the display width if needed
        row0 = text.ljust(self.cols)
        self.buffer[0] = row0[:self.cols]

    def scroll_display_left(self):
        # Shift the view window to the left (simulated by rotating the string buffer)
        self.buffer[0] = self.buffer[0][1:] + self.buffer[0][0]
        self.buffer[1] = self.buffer[1][1:] + self.buffer[1][0]
        self._render()

    def scroll_display_right(self):
        # Shift the view window to the right
        self.buffer[0] = self.buffer[0][-1] + self.buffer[0][:-1]
        self.buffer[1] = self.buffer[1][-1] + self.buffer[1][:-1]
        self._render()

    def _render(self):
        # Print the current state of the LCD to the terminal
        print(f"\r[{self.buffer[0]}]", end="", flush=True)


# --- Main Program Loop ---

lcd = SimulatedLCD()

def setup():
    lcd.begin(16, 2)
    lcd.print("Hello World!")
    print("\nInitial Display:")
    print(f"[{lcd.buffer[0]}]")
    time.sleep(1)

def loop():
    print("\n--- Scrolling Left ---")
    for position_counter in range(13):
        lcd.scroll_display_left()
        time.sleep(1)

    print("\n--- Scrolling Right ---")
    for position_counter in range(29):
        lcd.scroll_display_right()
        time.sleep(1)

    print("\n--- Scrolling Back to Center ---")
    for position_counter in range(16):
        lcd.scroll_display_left()
        time.sleep(1)

    time.sleep(1)

if __name__ == "__main__":
    setup()
    while True:
        loop()
