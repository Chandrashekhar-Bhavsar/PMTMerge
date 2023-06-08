from flask import Flask, jsonify, request
import jwt
from functools import wraps

import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
import datetime
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

file = open("myfile.txt","w")





##############################################################################################################
                                        # login
###############################################################################################################

def pm_loginn():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call for login api")
        logging.debug(dt_string + " Inside the Login api ")
        data = request.get_json()
        Email_ID = data['email_id']
        Password = data['password']
        cursor = mydb.cursor()
        logging.debug(dt_string + " Checking for valid email")
        query1 = "SELECT * FROM Users WHERE Email_ID=%s"
        values1 = (Email_ID,)
        cursor.execute(query1, values1)
        users1 = cursor.fetchone()
        logging.debug(dt_string + " Email Checking Query executed successfully")
        logging.debug(dt_string + " Query result is ", users1)
        if not users1:
            logging.debug(dt_string + " Email id is not valid")
            return jsonify({'error': "Email is invalid"}), 400
        else:
            flag = True
            logging.debug(dt_string + " Checking for valid password")
            query2 = "SELECT * FROM Users WHERE Password=%s"
            values2 = (Password,)
            cursor.execute(query2, values2)
            users2 = cursor.fetchone()
            logging.debug(dt_string + " Password Checking Query executed successfully")
            logging.debug(dt_string + " Query result is ", users2)
            if not users2:
                logging.debug(dt_string + " Password is not valid")
                return jsonify({'error': 'Password is invalid'}), 400
            else:
                flag2 = True
        if flag and flag2:
            query3 = "SELECT * FROM Users WHERE Password=%s and Email_ID=%s"
            values3 = (Password,Email_ID)
            cursor.execute(query3, values3)
            users3 = cursor.fetchall()
            logging.debug(dt_string + " Email id and password are valid")
            logging.debug(dt_string + " Login api execution completed without errors")
            token = jwt.encode({'username': "Email_ID"}, 'your_secret_key', algorithm='HS256')
            return jsonify({'msg': "login successful"},{"user_detail":users3},{'token': token}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# def pm_loginn():g
#     try:
#         now = datetime.now()
#         dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
#         logging.debug(dt_string+" User has made a call for login api")
#         logging.debug(dt_string+"Inside the Login api ")
#         data = request.get_json()
#         Email_ID = data['email_id']
#         Password = data['password']
#         cursor = mydb.cursor()
#         logging.debug(dt_string+"Checking for valid email")
#         query = "SELECT * FROM Users WHERE Email_ID=%s"
#         values = (Email_ID,)
#         cursor.execute(query, values)
#         users = cursor.fetchone()
#         logging.debug(dt_string+"Email Checking Query executed sucessfully")
#         logging.debug(dt_string+"Query result is ",users)
#         if not users:
#             logging.debug(dt_string+"Email id is not valid")
#             return jsonify({'error': "Email is invalid"}), 400
#         else:
#             flag=True
#         logging.debug(dt_string+"Checking for valid password")
#         query = "SELECT * FROM Users WHERE Password=%s"
#         values = (Password,)
#         cursor.execute(query, values)
#         users = cursor.fetchone()
#         logging.debug(dt_string+"Password Checking Query executed sucessfully")
#         logging.debug(dt_string+"Query result is ",users)
#         # token = jwt.encode({"username": "Email_ID"}, "secret", algorithm="HS256")
#         if not users:
#             logging.debug(dt_string+"Password is not valid")
#             return jsonify({'error': 'Password is invalid'}), 400
#         else:
#             flag2=True
#         if flag==flag2==True:
#             logging.debug(dt_string+"Email id and ppassword is valid")
#             logging.debug(dt_string+"Login api execution completed no error occur")
#             # token = jwt.encode({"username": "Email_ID"}, "secret", algorithm="HS256")
#             # # token = jwt.encode({'username': "Email_ID"}, 'your_secret_key', algorithm='HS256').decode('utf-8')
#             # return jsonify({"Return": "login successful",'token': token}), 200

#             token = jwt.encode({'username': Email_ID}, app.secret_key, algorithm='HS256').decode('utf-8')


#             return jsonify({'token': token})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400



##############################################################################################################
                                        # CREATE PROJECT
###############################################################################################################


def create_projects():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for create roject api")
        logging.debug(dt_string+"Inside the create project api ")
        data = request.get_json()
        logging.debug(dt_string+"payload comming from frontend ")
        print(data)
        project_name = data['project_name']
        project_description = data['project_description']
        planned_sd = data['planned_sd']
        planned_ed = data['planned_ed']
        actual_sd = '2023-07-06'#data['actual_sd']
        actual_ed = '2023-07-06'#data['actual_ed']
        planned_hours = "30 hour" #data['planned_hours']
        actual_hours = "30 hour"#data['actual_hours']""
        status = "To_Do"#data['status']
        project_lead = data['project_lead']
        client_name = data['client_name']
        risk = data['risk']
        mitigation = data['mitigation']
        workflowTask=data['workflowTask']
        workflowDefects2=data['workflowDefects']
        logging.debug(dt_string+"Calling create project query function ")
        return create_project_query(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                                    planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation)

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500

def get_cardprojectdetails():
    try:
        data = request.get_json()
        project_name = data['user_id']
        print("inside the function")
        cursor = mydb.cursor()
        query = "SELECT * FROM Project_Details p join project_member m on m.Project_ID=p.Project_ID  where user_id=%s;"
        cursor.execute(query)
        columns = cursor.column_names
        projects = cursor.fetchall()
        project_list = []
        for project in projects:
            project_dict = {
                    'Project_id': project[0],
                    'Project_name': project[1],
                    'description': project[2],
                    'planned_sd':project[3],
                    'planned_ed':project[4],
                    'Actual_sd' : project[5],
                    'Actual_ed' : project[6],
                    'planned_hours':project[7],
                    "actual_hours":project[8],
                    "Status":project[9],
                    "project_lead":project[10],
                    "client_name":project[11],
                    "risk":project[12],
                    "mitigation":project[13]
                }
            project_list.append(project_dict)
        return jsonify(project_list)
    except Exception as e:
        print("An error occurred:", str(e))
        return jsonify({'error': 'An error occurred while fetching project details'})


################################################################################################################    
                                   # UPDATE PROJECT DETAILS
############################################################################################################### 


def update_projects():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for Update project api")
        logging.debug(dt_string,"Inside the update project api ")
        data = request.get_json()
        logging.debug(dt_string,"payload received from frontend is ", data)
        comment=data["comments"]
        project_id = data['project_id']
        project_name = data['project_name']
        project_description = data['project_description']
        planned_sd = data['planned_sd']
        planned_ed = data['planned_ed']
        actual_sd = data['actual_sd']
        actual_ed = data['actual_ed']
        planned_hours ="30 minute" #data['planned_hours']
        actual_hours = "40 minute" #data['actual_hours']
        status = data['status']
        project_lead = data['project_lead']
        client_name = data['client_name']
        risk = "xyz" #data['risk']
        mitigation = "xyz" #data['mitigation']
        logging.debug(dt_string,"Calling update project query function ")
        
        if not isinstance(project_id, int):
            return jsonify({'error': 'Invalid data type for project_id'}), 400
        if not isinstance(planned_hours, str):
            return jsonify({'error': 'Invalid data type for planned_hours'}), 400
        if not isinstance(actual_hours, str):
            return jsonify({'error': 'Invalid data type for actual_hours'}), 400
        
        
        return update_project_details(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                                      planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, project_id)

    except KeyError:
        # Handle missing key error
        return jsonify({'error': 'Missing key in the request'}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500



def ProjectDetails():
    try:
        data = request.get_json()
        pm_id = data['project_id']
        cursor = mydb.cursor()
        query = "SELECT * FROM Project_Details where project_id=%s; "
        values=(pm_id,)
        cursor.execute(query,values)
        projects = cursor.fetchall()
        project_list = []
        for project in projects:
            project_dict = {
                    'Project_id': project[0],
                    'Project_name': project[1],
                    'description': project[2],
                    'planned_sd':project[3],
                    'planned_ed':project[4],
                    'Actual_sd' : project[5],
                    'Actual_ed' : project[6],
                    'planned_hours':project[7],
                    "actual_hours":project[8],
                    "Status":project[9],
                    "project_lead":project[10],
                    "client_name":project[11],
                    "risk":project[12],
                    "mitigation":project[13]
                }
            project_list.append(project_dict)
        return jsonify(project_dict)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400



###################################### GET ALL PROJECT DETAILS ###################################



def create_task():
    try:
        data = request.get_json()
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        priority = data['priority']
       

       

        
        return createtask(issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500



def update_task():
    try:
        data = request.get_json()
        task_id = data['task_id']
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        priority = str(data['priority'])
        
        

        return updatetask(description, status, task_sd, task_ed, planned_hours, actual_hours,priority,task_id, issue_id)
    

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    


############################ DELETE TASK #################################

def delete_task():
    try:
        data = request.get_json()
        task_id = data['task_id']
        cursor = mydb.cursor()


      

        return deletetask(task_id)
        

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    






    

