CREATE TABLE Employees (
  empl_id INT PRIMARY KEY,
  first_name VARCHAR(160),
  last_name VARCHAR(160),
  date_hired DATE,
  job_id VARCHAR(160),
  phone_number INT,
  email VARCHAR(160),
  manager_id INT,
  department_id INT
  );

 INSERT INTO Employees(empl_id, first_name, last_name, date_hired, job_id, phone_number, email, manager_id, department_id)
 SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, HIRE_DATE, JOB_ID, PHONE_NUMBER, EMAIL, MANAGER_ID, DEPARTMENT_ID 
 FROM 'employees.csv';
 
 