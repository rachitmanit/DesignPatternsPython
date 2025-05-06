from Event import Event

class PropertyObservable:
    def __init__(self):
        self.__on_status_changed = Event()

    def call_on_status_changed(self, *args, **kwargs):
        self.__on_status_changed(*args, **kwargs)

    def add_observer(self, observer):
        self.__on_status_changed.append(observer)

    def remove_observer(self, observer):
        if observer in self.__on_status_changed:
            print("Removing observer: {}".format(observer.__name__))
            self.__on_status_changed.remove(observer)