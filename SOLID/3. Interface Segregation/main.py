from abc import abstractmethod

class AbstractPrinter:
    @abstractmethod
    def print(self, document):
        raise NotImplementedError("Not implemented")

class AbstractScanner:
    @abstractmethod
    def scan(self, document):
        raise NotImplementedError("Not implemented")

class AbstractFax:
    @abstractmethod
    def fax(self, document):
        raise NotImplementedError("Not implemented")

class Printer(AbstractPrinter):
    def print(self, document):
        print("Printing document: {}".format(document))

class Scanner(AbstractScanner):
    def scan(self, document):
        print("Scanning document: {}".format(document))

class Fax(AbstractFax):
    def fax(self, document):
        print("Faxing document: {}".format(document))

class AbstractMultiMachineDevice(AbstractPrinter, AbstractScanner):
    @abstractmethod
    def print(self, document):
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def scan(self, document):
        raise NotImplementedError("Not implemented")

class MultiMachineDevice(AbstractMultiMachineDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)

if __name__ == "__main__":
    p = Printer()
    p.print("Document1")

    s = Scanner()
    s.scan("Document2")

    m = MultiMachineDevice(printer=p, scanner=s)
    m.print("Document3")
    m.scan("Document4")
    try:
        d = AbstractMultiMachineDevice()
        d.print("Document5")
        d.scan("Document6")
    except Exception as exp:
        print("Exception {}".format(exp))
