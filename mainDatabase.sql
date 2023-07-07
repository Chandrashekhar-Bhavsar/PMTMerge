
create database pmt;
use pmt;

CREATE TABLE Project_Details (
  Project_ID INT PRIMARY KEY auto_increment,
  Project_Name TEXT NOT NULL,
  Project_Description TEXT NOT NULL,
  Planned_SD date NOT NULL,
  Planned_ED date NOT NULL,
  Actual_SD DATE NOT NULL,
  Actual_ED DATE NOT NULL,
  Planned_Hours varchar(30) not null,
  Actual_Hours varchar(30) not null,
  Status ENUM('To_do','In_Progress', 'In_Review', 'Done') DEFAULT "To_do",
  Project_Lead VARCHAR(50),
  Client_Name Text,
  Risk TEXT,
  Mitigation TEXT,
  ownby_id INT NOT NULL,
  ownby_name VARCHAR(100) NOT NULL
);

ALTER TABLE Project_Details AUTO_INCREMENT=100;
----------------------------------------------------------

CREATE TABLE Users (
  user_ID INT PRIMARY KEY auto_increment,
  roles varchar(50) Not Null,
  Name TEXT NOT NULL,
  Email_ID VARCHAR(50) UNIQUE NOT NULL,
  Password VARCHAR(100) NOT NULL,
  Contact decimal(10) NOT NULL
);

ALTER TABLE Users AUTO_INCREMENT=2000;
-------------------------------------------------------

create table project_member (member_id int primary key auto_increment, user_ID int not null, Project_ID int not null);
ALTER TABLE project_member AUTO_INCREMENT=1;
select * FROM project_member;

--------------------------------------------------------

CREATE TABLE Issue_Details (
  issue_id INT PRIMARY KEY auto_increment,
  issue_name varchar(30),
  description TEXT NOT NULL,
  type ENUM('task','defect'),
  status VARCHAR(30)
);

ALTER TABLE Issue_Details AUTO_INCREMENT=3000;

--------------------------------------------------------

CREATE TABLE Task (
  task_id INT PRIMARY KEY auto_increment ,
  issue_id INT NOT NULL,
  title VARCHAR(30) NOT NULL,
  task_sd DATE NOT NULL,
  task_ed DATE NOT NULL,
  estimated_time varchar(30) not null,
  priority ENUM('High', 'Medium', 'Low'),
  file_attachment TEXT DEFAULT NULL,
  FOREIGN KEY (issue_id) REFERENCES Issue_Details(issue_id)
  );
 
  Alter table Task auto_increment=5000;
-------------------------------------------------------

CREATE TABLE Defect(
  defect_id INT PRIMARY KEY auto_increment,
  issue_id INT NOT NULL,
  title VARCHAR(30) NOT NULL,
  product VARCHAR(50) NOT NULL,
  component TEXT NOT NULL,
  component_description TEXT default null,
  version VARCHAR(20),
  severity ENUM('Critical','Major','Minor'),
  os ENUM('Windows','Mac','Linux'),
  summary TEXT NOT NULL,
  defect_sd DATE NOT NULL,
  defect_ed DATE NOT NULL,
  priority ENUM('High', 'Medium', 'Low'),
  estimated_time varchar(30) not null,
  file_attachment TEXT DEFAULT NULL,
  FOREIGN KEY (issue_id) REFERENCES Issue_Details(issue_id)
  );
  
alter table Defect auto_increment=7000;

--------------------------------------------------------
  
create table project_issue(projectissue_id int primary key auto_increment,
issue_id int not null,
Project_ID int not null);
ALTER TABLE project_issue AUTO_INCREMENT=1;

create table Issue_Member(issueMember_id int primary key auto_increment,
issue_id int not null,
user_ID int not null,
Project_ID int not null);
ALTER TABLE Issue_Member AUTO_INCREMENT=1;

--------------------------------------------------------
CREATE TABLE comments (comment_ID INT auto_increment PRIMARY KEY,ID INT NOT NULL,description TEXT NOT NULL,user_ID int not null,author_name varchar(50) not null,date date NOT NULL,foreign key(user_ID) references Users(user_ID));
create table workflow (workflow_name varchar(30),workflow text);
create table workflowconnection (Project_ID int,workflow_name varchar(30),issue_type varchar(30));
CREATE TABLE project_status (ID INT primary key,status text NOT NULL);
create table attachment(sno int auto_increment primary key, issue_id int , Name varchar(50) , link text );





