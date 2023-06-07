
from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
from workflow import *
from Filter import *
from connection import *
from Comments_Module import *
from issue import *
from pmt import *
from UserManagement_module import *
import datetime
from datetime import datetime
import logging
import jwt
from functools import wraps
from functools import wraps

import datetime
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

file = open("myfile.txt","w")

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')




@app.route('/')
def home():
    return '<h1>Welcome Team :To the POC YJB</h1>'


############################################################
#                       workflow module                    #
############################################################

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            # Verify and decode the token
            data = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            # Add the decoded token data to the request context if needed
            
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/GetWorkFlow', methods=['POST'])
#@token_required
def GetWorkFlow():
    return getwf()

@app.route('/StatusUpdate', methods=['POST'])
def StatusUpdate():
    return statusupdate()


@app.route('/GetWorkflowIssue', methods=['POST'])
def GetWorkflowIssue():
    return getworkflowussue()

############################################################
#                       Issue module                       #
############################################################


@app.route('/IssueByMonth', methods=['POST'])
def IssueByMonth():
    return IssueFilterationMonth()

@app.route('/IssueByWeek', methods=['POST'])
def IssueByWeek():
    return IssueFilterationWeek()

@app.route('/IssueByQuarter', methods=['POST'])
def IssueByQuarterly():
    return IssueFilterationQuarterly()

@app.route('/DetailedIssue', methods=['GET'])
def DetailedIssue():
    return DetailedIssueFilteration()
    
    
############################################################
#                       authentication module              #
############################################################
from flask_bcrypt import Bcrypt
import bcrypt
bcrypt = Bcrypt(app)


@app.route('/login', methods=['POST'])
def pm_login():
        
    return pm_loginn()


@app.route('/create_project', methods=['POST'])
#@token_required
def create_project():
    return create_projects()

@app.route('/ProjectList', methods=['GET'])
#@token_required
def ProjectList():
    return get_cardprojectdetails()


@app.route('/updateProject', methods=['PUT'])
def update_project():
    return update_projects() 


@app.route('/create_tasks', methods=['POST'])
def create_tasks():
    return create_task() 

@app.route('/update_tasks', methods=['POST'])
def update_tasks():
    return update_task() 

@app.route('/add_user', methods=['POST'])
def add_user():
    return adduser()
    

@app.route('/assign_user', methods=['POST'])
def assign_user():
   return assignuser()
   

@app.route('/add_project_comment', methods=['POST'])
def add_project_comment():
    return add_projectcomment()
   

@app.route('/add_issue_comment', methods=['POST'])
def add_issue_comment():
    return add_issuecomment()
    

@app.route('/display_projectwise_comments', methods=['POST'])
def display_projectwise_comments():
    
      return  display_projectwisecomments()
    

@app.route('/display_issuewise_comments', methods=['POST'])
def display_issuewise_comments():
        return display_issuewisecomments()
        

@app.route('/update_projectwise_comments', methods=['POST'])
def update_projectwise_comments():
    return update_projectwisecomments()
   

@app.route('/update_issuewise_comments', methods=['POST'])
def update_issuewise_comments():
    return update_issuewisecomments()
    
@app.route('/show_user', methods=['POST'])
def show_user():
    return showuser()


@app.route('/deletecomment', methods=['POST'])
def deletecomment():
    return delete_comment()
    

############################ CREATE ISSUE DETAILS #################################

# Defining an API endpoint (/create_issue) for creating a new issue. This endpoint expects a POST request.
@app.route('/create_issue', methods=['POST'])
def create_issue():
    # Call the create_issue function from the queries module with the required arguments
    return createissue()  
    

############################ UPDATE ISSUE DETAILS #################################

# Defining an API endpoint (/update_issue) for updating an existing issue. This endpoint expects a POST request.
@app.route('/update_issue', methods=['POST'])
def update_issue():
    # Call the update_issue function from the queries module with the required arguments
    return updateissue()  # Pass the necessary arguments
    

############################ DELETE ISSUE DETAILS #################################

# Defining an API endpoint (/delete_issue) for deleting an issue. This endpoint expects a POST request.
@app.route('/delete_issue', methods=['POST'])
def delete_issue():
    # Call the delete_issue function from the queries module with the required arguments
    return deleteissue()  # Pass the necessary arguments
    

############################ CREATE TASK #################################

@app.route('/create_task', methods=['POST'])
def create_task():
    # Call the create_task function from the queries module with the required arguments
    return createtask()  # Pass the necessary arguments
    

############################ UPDATE TASK #################################

@app.route('/update_task', methods=['POST'])
def update_task():
    # Call the update_task function from the queries module with the required arguments
    return updatetask()  # Pass the necessary arguments
    

############################ DELETE TASK #################################

@app.route('/delete_task', methods=['POST'])
def delete_task():
    # Call the delete_task function from the queries module with the required arguments
    return deletetask()  # Pass the necessary arguments
 
############################ CREATE DEFECT#################################

@app.route('/create_defect', methods=['POST'])
def create_defect():

    return createdefect()

############################ UPDATE DEFECT#################################

@app.route('/update_defect', methods=['POST'])
def update_defect():

    return updatedefect()

############################ DELETE DEFECT #################################

@app.route('/delete_defect', methods=['POST'])
def delete_defect():
    return deletedefect()

@app.route('/completeProjectdetails', methods=['POST'])
def completeProjectdetails():
    return ProjectDetails()
    
if __name__ == "__main__":
    app.run(debug=True,port=5000)
