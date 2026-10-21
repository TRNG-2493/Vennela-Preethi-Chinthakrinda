import logging

file_handler = logging.FileHandler("app.log")
console_handler = logging.StreamHandler()
logging.basicConfig(
    level =logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers= [file_handler,console_handler], #console_handler to get on console
    
)

logging.debug("This is debug") 
logging.info("Application Started")
logging.warning("This is a warning")
logging.error("This is error")
logging.critical("This is Critical")

try:
    result = 10/0
except ZeroDivisionError:
    logging.exception("Division by Zero")