import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)#exist_ok=True-->even if there is folder  then append the file in this


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#we have to set thi Basics Config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

# Checking if Working fine or not
# if __name__=="__main__":
#     logging.info("Logging Has Started")
