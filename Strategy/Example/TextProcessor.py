from ListStrategy import HTMLListStrategy, MarkdownListStrategy
from OutputFormat import OutputFormat

class TextProcessor:
    def __init__(self, list_strategy=HTMLListStrategy()):
        self.buffer = []
        self.list_strategy = list_strategy

    def append_list(self, item_list):
        ls = self.list_strategy
        ls.start(self.buffer)
        ls.add_item_to_list(self.buffer, item_list)
        ls.end(self.buffer)

    def set_output_format(self, output_format: OutputFormat = OutputFormat.HTML):
        if output_format == OutputFormat.HTML:
            self.list_strategy = HTMLListStrategy()
        else:
            self.list_strategy = MarkdownListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "\n".join(self.buffer)