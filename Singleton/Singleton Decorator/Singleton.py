from threading import Lock

class Singleton:
    def __init__(self, cls):
        self._cls = cls  # Store the class to be decorated
        self._instance = None  # Initialize the instance as None
        self._lock = Lock()  # Lock to ensure thread safety

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            with self._lock:  # Only one thread can create the instance at a time
                if self._instance is None:  # Double-check to ensure thread-safety
                    self._instance = self._cls(*args, **kwargs)
        return self._instance  # Return the instance (whether new or existing)
