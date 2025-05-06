from abc import ABC

class ListStrategy(ABC):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_item_to_list(self, buffer, item_list): pass

class MarkdownListStrategy(ListStrategy):
    def add_item_to_list(self, buffer, item_list):
        for item in item_list:
            buffer.append(f'* {item}')

class HTMLListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append("<ul>")

    def end(self, buffer):
        buffer.append("</ul>")

    def add_item_to_list(self, buffer, item_list):
        for item in item_list:
            buffer.append("  <li>{}</li>".format(item))