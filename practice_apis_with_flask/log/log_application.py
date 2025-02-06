import logging
class LogApplication :
    def __init__(self, fileName):
        # set log format when inital class
        # create logger
        self.log = logging.getLogger(fileName)
        # self.log.setLevel(logging.DEBUG)
        self.log.setLevel(logging.DEBUG)

        __consoleHandler = logging.StreamHandler()
        # __consoleHandler.setLevel(logging.DEBUG)

        # create formatter
        __formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

        # add formatter to ch
        __consoleHandler.setFormatter(__formatter)

        # add ch to logger
        self.log.addHandler(__consoleHandler)


# logApplication = LogApplication(__file__)
# logApplication.log.debug("Test")