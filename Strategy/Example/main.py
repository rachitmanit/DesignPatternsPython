from TextProcessor import TextProcessor
from OutputFormat import OutputFormat

if __name__ == '__main__':

    items = ["A", "B", "C"]

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.HTML)
    tp.append_list(items)
    print(tp)

    tp.clear()
    print("---------------")
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)