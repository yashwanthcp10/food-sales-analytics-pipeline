import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileHandler(FileSystemEventHandler):

    def on_created(self, event):

        if not event.is_directory:

            print(
                f"New file detected: {event.src_path}"
            )


def start_watching(folder_path):

    event_handler = FileHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        folder_path,
        recursive=False
    )

    observer.start()

    print(f"Watching folder: {folder_path}")

    try:
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()