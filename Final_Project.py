import tkinter as tk
import threading
import sys
from io import StringIO
import queue

class DebuggerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Step-by-Step Debugger")

        # Label to show the debugging status
        self.label = tk.Label(master, text="Debugging Status: Waiting for user input")
        self.label.pack()

        # Code input area for user to write their code
        self.code_input_label = tk.Label(master, text="Enter Python code:")
        self.code_input_label.pack()
        
        self.code_input = tk.Text(master, height=10, width=50)
        self.code_input.pack()

        # Start Button to execute the entered code
        self.start_button = tk.Button(master, text="Start Debugging", command=self.start_debugging)
        self.start_button.pack()

        # Step Button to execute one step at a time
        self.step_button = tk.Button(master, text="Step", state=tk.DISABLED, command=self.step)
        self.step_button.pack()

        # Output area to show the results and variable states
        self.output = tk.Text(master, height=10, width=50)
        self.output.pack()

        # Placeholder for tracking current state
        self.user_code = ""
        self.local_vars = {}
        self.output_queue = queue.Queue()

    def update_output(self, message):
        """Update the output window with messages."""
        self.output.insert(tk.END, f"{message}\n")
        self.output.yview(tk.END)

    def start_debugging(self):
        """Start the debugging process."""
        self.user_code = self.code_input.get("1.0", tk.END)
        self.local_vars = {}  # Reset local variables
        self.update_output("Starting debugging...\n")

        # Start the background thread to run the user's code
        self.step_button.config(state=tk.NORMAL)
        self.run_code_in_thread()

    def run_code_in_thread(self):
        """Run the user's code in a separate thread to avoid freezing the GUI."""
        self.update_output("Running your code in a separate thread...\n")
        threading.Thread(target=self.run_code_with_debugger).start()

    def run_code_with_debugger(self):
        """Execute the user's code with the debugger enabled."""
        try:
            # Redirect stdout to capture any print statements
            sys.stdout = StringIO()

            # Start executing the user's code
            exec(self.user_code, {}, self.local_vars)

            # Fetch the output from stdout and send it to the queue to be updated in the GUI
            output = sys.stdout.getvalue()
            sys.stdout = sys.__stdout__  # Restore stdout

            # Put the result in the queue for the main thread to process
            self.output_queue.put(output)

        except Exception as e:
            self.output_queue.put(f"Error: {str(e)}")

        # Process the queue and update the GUI with the results
        self.process_queue()

    def process_queue(self):
        """Process the queue in the main thread to update the output."""
        try:
            while True:  # Keep processing messages in the queue
                message = self.output_queue.get_nowait()
                self.update_output(message)
        except queue.Empty:
            pass

    def step(self):
        """Step through the code line by line."""
        # Currently, this is a placeholder for actual stepwise debugging implementation
        self.update_output("Stepping through the code...\n")
        
        # You could later expand this to use advanced features like pdb or custom logic
        self.update_output(f"Current Variables: {self.local_vars}")


# Main app loop
def run_debugger():
    root = tk.Tk()
    app = DebuggerApp(root)
    root.mainloop()

# Start the app
run_debugger()
