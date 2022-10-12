import base64, requests, datetime, pprint, json, logging, sys, smtplib
from pathlib import Path
from pprint import pformat
import __main__

pp = pprint.PrettyPrinter(indent=2)

today_yyyy_mm_dd = datetime.datetime.today().strftime('%Y-%m-%d')

sys.path.append("..")

logging.basicConfig(
    level=logging.INFO,
    format="\n[%(levelname)s] %(asctime)s -- %(filename)s on line %(lineno)s\n\tFunction name: %(funcName)s\n\tMessage: %(message)s\n",
    datefmt='%B-%d-%Y %H:%M:%S',
    filename=f"../logs/{Path(__main__.__file__).stem}.log",
    filemode='w'
)