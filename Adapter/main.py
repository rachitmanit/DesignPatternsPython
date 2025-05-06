class NewLogger:
    def write(self, message):
        print(f'f[write] {message}')

class LoggingAdapter:
    def __init__(self, logger):
        self.logger = logger

    def info(self, message):
        self.logger.write(message)

if __name__ == '__main__':
    # Suppose after upgrade above is the NewLogger class updates in Library
    # Below code fails as our legacy code expects the

    # logger = NewLogger()
    # logger.info("Test Message")

    # Below wors fine with LoggingAdapter
    logger = LoggingAdapter(NewLogger())
    logger.info("Test Log")