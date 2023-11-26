import os
from SQLconnector import sqlconnector_patient
from threading import Thread, Lock
from time import sleep
from SQLconnector import sqlconnector_schedule, dbLock

## T1 - T2
# Cranio            1
# Breast            2
# Breast Special    3
# Lung              8
## V1 - V2
# Crane             7
# Pelvis            6
# Abdomen           5
# H&N               4
## U
# Lung Special      9
# Whole Brain       10

machines_dict = {
    "T": {
        "Allowed_treatments": [1, 2, 3, 8],
        "T1": {
            "timesum": 11,
            "Sessions": {

            }
        },
        "T2": {
            "timesum": 11,
            "Sessions": {

            }
        }
    },
    "V": {
        "Allowed_treatments": [4, 5, 6, 7],
        "V1": {
            "timesum": 11,
            "Sessions": {

            }
        },
        "V2": {
            "timesum": 11,
            "Sessions": {

            }
        }
    },
    "U": {
        "Allowed_treatments": [9, 10],
        "timesum": 11,
        "Sessions": {

        }
    }
}

def process_new_machines():
    sqlcon = sqlconnector_schedule('root','', '127.0.0.1')
    user_result = sqlcon.get_schedule_item()
    if user_result:
        print(user_result)

def calc_BMI(weight: int, height: int):
    if int(weight / height * height) >= 25:
        return False
    return True

process_new_machines()