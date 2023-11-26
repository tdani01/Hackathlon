import os
import mysql.connector
from datetime import datetime, date
from threading import Lock
dbLock = Lock()
class sqlconnector_account:
    def __init__(self, user: str, pw: str, ip: str):
        self.con = mysql.connector.connect(user=user, password=pw, host=ip, database='Accounts')

    def create_account(self, a_user: str, a_pw: str, a_perm: int, a_email: str):
        command = ("INSERT INTO users "
                   "(account_id, account_pass, perm, reg_date, email) "
                   "VALUES (%s, %s, %s, %s, %s)")
        data = (a_user, a_pw, a_perm, date(int(datetime.now().strftime('%y')), int(datetime.now().strftime('%m')),
                                           int(datetime.now().strftime('%d'))), a_email)
        cursor = self.con.cursor()
        try:
            cursor.execute(command, data)
            self.con.commit()
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            cursor.close()

    def remove_account(self, a_id):
        command = ("DELETE FROM users WHERE id = %s")
        data = (a_id,)
        cursor = self.con.cursor()
        try:
            cursor.execute(command, data)
            self.con.commit()
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            cursor.close()

    def update_password(self, a_us, a_pass):
        command = "UPDATE users SET account_pass = %s WHERE users.account_id = %s"
        data = (a_pass, a_us)
        cursor = self.con.cursor()
        try:
            cursor.execute(command,data)
            self.con.commit()
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            cursor.close()

    def querry_account_by_us(self, a_id: str):
        result = []
        command = ("SELECT account_id, account_pass, perm, reg_date, email, id FROM users WHERE account_id = %s")
        data = (a_id,)
        cursor = self.con.cursor()
        try:
            cursor.execute(command, data)
            user_data = cursor.fetchone()
            if user_data:
                return [user_data[0].decode('utf-8'),
                        user_data[1].decode('utf-8'),
                        user_data[2],
                        user_data[3],
                        user_data[4].decode('utf-8'),
                        user_data[5]]
            else:
                return None
        except Exception as ex:
            print(ex)
            return None
        finally:
            cursor.close()



    def querry_account_by_id(self, a_id: int):
        result = []
        command = ("SELECT account_id, account_pass, perm, reg_date, email FROM users WHERE id = %s")
        data = (a_id,)
        cursor = self.con.cursor()
        try:
            cursor.execute(command, data)
            user_data = cursor.fetchone()
            if user_data:
                return [user_data[0].decode('utf-8'),
                        user_data[1].decode('utf-8'),
                        user_data[2],
                        user_data[3],
                        user_data[4].decode('utf-8')]
            else:
                return False
        except Exception as ex:
            print(ex)
            return None
        finally:
            cursor.close()
    def check_login(self, a_id: str, a_pw: str):
        try:
            user_data = self.querry_account_by_us(a_id)
            if user_data and a_pw == user_data[1]:  # PASSWORD ENCRYPT !!
                print("Login Successful")
                return [True, None, 0, user_data[2], user_data[4]]
            elif not user_data:
                print("Username is incorrect!")
                return [False, "Username is incorrect!", 1, None, None]
            else:
                print("Password is incorrect")
                return [False, "Password is incorrect", 2, None, None]
        except Exception as ex:
            print(ex)
            return None

    def register(self, a_id: str, a_pw: str, a_email: str):
        if not self.querry_account_by_us(a_id):
            try:
                if self.create_account(a_id, a_pw, 0, a_email):
                    print("Registration successful")
                    return [True, "Registration successful, please verify your email and continue to the site!"]
                else:
                    print("Registration failed")
                    return [False, "Registration failed! Username has been taken."]
            except Exception as ex:
                print(ex)
                return [None, ex]

class sqlconnector_patient:
    def __init__(self, user: str, pw: str, ip: str):
        self.con = mysql.connector.connect(user=user, password=pw, host=ip, database='patient_data')

    def add_patient_to_queue(self, patient_id: int, height: int, weight: int, age: int, sex: str, region_id: int,
                             name: str, taj: str, allergy: str, others: str):
        command = ("INSERT INTO Patients "
                   "(Height, Weight, Age, TAJ, Name, Allergy, Sex, region_type_id, patient_id, others, priority, machine_id, remaining_fractions) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (height, weight, age, taj, name, allergy, "Male" if sex == 1 else "Female", region_id, patient_id, others, None, None, None)
        cursor = self.con.cursor()
        try:
            cursor.execute(command, data)
            self.con.commit()
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            cursor.close()

    def query_queue_item(self):
        command = "SELECT * FROM Patients WHERE 1"
        data = (id, )
        cursor = self.con.cursor()
        try:
            cursor.execute()
            user_data = cursor.fetchone()
            if user_data:
                return [
                    user_data[0],                   # ID
                    user_data[1],                   # Height
                    user_data[2],                   # Weight
                    user_data[3],                   # Age
                    user_data[4].decode('utf-8'),   # TAJ
                    user_data[5].decode('utf-8'),   # Name
                    user_data[6].decode('utf-8'),   # Allergy
                    user_data[7].decode('utf-8'),   # Sex
                    user_data[8],                   # region_type_id
                    user_data[9],                   # patient_id
                    user_data[10].decode('utf-8'),  # others
                    user_data[11],                  # machine_id
                    user_data[12],                  # remaining_fractions
                    user_data[13]]                  # priority
        except Exception as ex:
            print(ex)
            return None
        finally:
            cursor.close()

    def remove_queue_item(self, id: int):
        command = "DELETE FROM Patients WHERE ID = %s"
        data = (id, )
        cursor = self.con.cursor()
        try:
            cursor.execute(command, data)
            self.con.commit()
            return True
        except Exception as ex:
            print(ex)
            return None
        finally:
            cursor.close()


class sqlconnector_schedule:
    def __init__(self, user: str, pw: str, ip: str):
        self.con = mysql.connector.connect(user=user, password=pw, host=ip, database='patient_data')

    def add_schedule_item(self, patient_id: int, height: int, weight: int, age: int, sex: str, region_id: int,
                          name: str, taj: str, allergy: str, others: str, priority: int, remaining_fractions: int):
        command = ("INSERT INTO ready_to_schedule "
                   "(Height, Weight, Age, TAJ, Name, Allergy, Sex, region_type_id, "
                   "patient_id, others, priority, remaining_fractions) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (height, weight, age, taj, name, allergy, sex, region_id, patient_id, others,
                priority, remaining_fractions)
        cursor = self.con.cursor()
        with dbLock:
            try:
                cursor.execute(command, data)
                self.con.commit()
                return True
            except Exception as ex:
                print(ex)
                return False
            finally:
                cursor.close()

    def get_schedule_item(self):
        with dbLock:
            command = "SELECT * FROM ready_to_schedule WHERE 1"
            cursor = self.con.cursor(buffered=True)
            try:
                cursor.execute(command)
                user_data = cursor.fetchone()
                if user_data:
                    return [
                        user_data[0],                   # ID
                        user_data[1],                   # Height
                        user_data[2],                   # Weight
                        user_data[3],                   # Age
                        user_data[4].decode('utf-8'),   # TAJ
                        user_data[5].decode('utf-8'),   # Name
                        user_data[6].decode('utf-8'),   # Sex
                        user_data[7],                   # region_type_id
                        user_data[8],                   # patient_id
                        user_data[9].decode('utf-8'),  # others
                        user_data[10],                  # remaining_fractions
                        user_data[11]]                  # priority
            except Exception as ex:
                print(ex)
                return None
            finally:
                cursor.close()

    def remove_schedule_item(self, id: int):
        command = "DELETE FROM ready_to_schedule WHERE ID = %s"
        data = (id, )
        cursor = self.con.cursor()
        with dbLock:
            try:
                cursor.execute()
                self.con.commit()
                return True
            except Exception as ex:
                print(ex)
                return None
            finally:
                cursor.close()