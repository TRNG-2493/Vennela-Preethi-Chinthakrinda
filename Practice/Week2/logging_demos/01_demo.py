import logging

# we start with configuring logging

# levels - debug, info, warning, error, critical (app is down)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)
logging.debug("This is debug") # this is not printed because the logging starts at info.
logging.info("Application Started")
logging.warning("This is a warning")
logging.error("This is error")
logging.critical("This is Critical")

# logs are usually written in log file.
# we have a logging handller is object sends the log to a destination, the most 
# common handler is steam handle, file handler - sends logs to file, rotating file handler - 
# rotating file handler - writes logs to file and it is moce to another file if memory is running out creates a new file
# time rotating file handler - logs everyday
# PROJECT _ MUST HAVE LOG FILE