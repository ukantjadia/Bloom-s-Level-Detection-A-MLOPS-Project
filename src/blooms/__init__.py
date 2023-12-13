import os
import sys
import logging
import colorlog

# Define a color formatter
formatter = colorlog.ColoredFormatter(
    "[%(asctime)s: %(log_color)s%(levelname)s%(reset)s: %(module)s: %(message)s]",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

# Set up the logger with color formatter
logging_str = "%(asctime)s: %(levelname)s: %(module)s: %(message)s"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
    ]
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

logger = logging.getLogger("bloomsleveldetection")
logger.addHandler(console_handler)