# watcher.py
# example usage: python3 watcher.py quicksort.py
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.run_script()

    def run_script(self):
        # Kill previous process if running
        if self.process:
            self.process.kill()
        print(f"\n--- Running {self.script} ---\n")
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            self.run_script()

if __name__ == "__main__":
    script = sys.argv[1]  # pass your script as argument

    handler = ReloadHandler(script)
    observer = Observer()
    observer.schedule(handler, path=".", recursive=False)
    observer.start()

    print(f"Watching for changes... (Ctrl+C to stop)")
    try:
        while observer.is_alive():
            observer.join(timeout=1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()