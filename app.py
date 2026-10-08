#!/usr/bin/env python3
import time
import logging
import sys
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout
)
logging.info("InfraGuardian Python application starting")
counter = 0
while True:
    counter += 1
    logging.info(
        "Application is healthy - check number %d",
        counter
    )
    time.sleep(10)
