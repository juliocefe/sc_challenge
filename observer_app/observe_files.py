from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from processor import process_file_service


def on_create(event):
    print("a file was created 0.0!")
    print("calling flask service...")
    process_file_service(event.src_path)


if __name__ == "__main__":

    path = './stori/stori/media/transactions_files'
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_create
    observer = Observer()
    observer.schedule(event_handler, path)
    observer.start()
    try:
        print("watching for directory changes...")
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()