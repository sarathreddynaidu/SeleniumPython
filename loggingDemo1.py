import logging

# This prints the messages to a log file, without these 2 lines it prints on the console
# level=logging.DEBUG gives us debug and info messages as well
# using format we can add time, levelname, message
filePath = "C://SeleniumPython//LoginLogs//test.log"
logging.basicConfig(filename=filePath,
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
