import logging

# This prints the messages to a log file, without these 2 lines it prints on the console
# level=logging.DEBUG gives us debug and info messages as well
# using format we can add time, levelname, message
filePath = "/LoginLogs/test.log"
logging.basicConfig(filename=filePath,
                    format="%(asctime)s: %(levelname)s: %(message)s")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
