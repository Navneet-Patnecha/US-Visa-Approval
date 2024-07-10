from US_Visa_Approval.logger import logging
from US_Visa_Approval.exception import USvisaException
import sys

logging.info("logging started")

try:
    a = 2/0

except Exception as e :
    raise USvisaException(e,sys)


