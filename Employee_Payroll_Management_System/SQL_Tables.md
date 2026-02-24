# Employee Payroll Management System – 2CSE_23_31083_G1

> This project is a Payroll Management System implemented in MariaDB.  
> It includes tables for Company, Department, Designation, Employee, Attendance, Users, Payroll, and Company Contact (for multivalued attributes).

---

## 1. Use Database

```sql
USE 2CSE_23_31083_G1;
````

**Output:**

```
Database changed
```

---

## 2. Company Table

```sql
CREATE TABLE COMPANY(
    company_id INT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    street VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    pincode INT
);
```

**Insert Record:**

```sql
INSERT INTO Company
(company_id, company_name, email, street, city, state, pincode)
VALUES
(1, 'Quantum Enterprises Pvt. Ltd.', 'quantumenterprises.in@gmail.com', 'MG Road', 'Delhi', 'Delhi', 110001);
```

**Select Table:**

```sql
SELECT * FROM Company;
```

```
+------------+-------------------------------+---------------------------------+---------+-------+-------+---------+
| company_id | company_name                  | email                           | street  | city  | state | pincode |
+------------+-------------------------------+---------------------------------+---------+-------+-------+---------+
|          1 | Quantum Enterprises Pvt. Ltd. | quantumenterprises.in@gmail.com | MG Road | Delhi | Delhi |  110001 |
+------------+-------------------------------+---------------------------------+---------+-------+-------+---------+
```

---

## 3. Company Contact Table (Multivalued Contact Attribute)

```sql
CREATE TABLE Company_Contact(
    company_id INT NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    PRIMARY KEY (company_id, contact_number),
    FOREIGN KEY (company_id) REFERENCES COMPANY(company_id)
);
```

**Insert Sample Records:**

```sql
INSERT INTO Company_Contact (company_id, contact_number)
VALUES
(1, '9876543210'),
(1, '9123456780'),
(1, '9812345678');
```

**Select Table:**

```sql
SELECT * FROM Company_Contact;
```

```
+------------+----------------+
| company_id | contact_number |
+------------+----------------+
|          1 | 9876543210     |
|          1 | 9123456780     |
|          1 | 9812345678     |
+------------+----------------+
```

---

## 4. Department Table

```sql
CREATE TABLE Department(
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL,
    contact_number VARCHAR(15),
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES COMPANY(company_id)
);
```

**Insert Records:**

```sql
INSERT INTO DEPARTMENT
(department_id, department_name, contact_number, company_id)
VALUES
(1000, 'IT Department', '9876543210', 1),
(1001, 'Human Resources', '9123456780', 1),
(1002, 'Finance Department', '9812345678', 1),
(1003, 'Operations Department', '9098765432', 1);
```

**Select Table:**

```sql
SELECT * FROM Department;
```

```
+---------------+-----------------------+----------------+------------+
| department_id | department_name       | contact_number | company_id |
+---------------+-----------------------+----------------+------------+
|          1000 | IT Department         | 9876543210     |          1 |
|          1001 | Human Resources       | 9123456780     |          1 |
|          1002 | Finance Department    | 9812345678     |          1 |
|          1003 | Operations Department | 9098765432     |          1 |
+---------------+-----------------------+----------------+------------+
```

---

## 5. Designation Table

```sql
CREATE TABLE Designation(
    Designation_ID INT PRIMARY KEY,
    Designation_Name VARCHAR(100) NOT NULL,
    Base_Salary DECIMAL(10,2) NOT NULL,
    Hra_Percentage DECIMAL(5,2),
    Da_Percentage DECIMAL(5,2)
);
```

**Insert Records:**

```sql
INSERT INTO DESIGNATION
(designation_id, designation_name, base_salary, hra_percentage, da_percentage)
VALUES
(101, 'Software Engineer', 40000.00, 20.00, 10.00),
(102, 'HR Manager', 50000.00, 25.00, 12.00),
(103, 'Accountant', 35000.00, 18.00, 8.00),
(104, 'Project Manager', 70000.00, 30.00, 15.00);
```

**Select Table:**

```sql
SELECT * FROM Designation;
```

```
+----------------+-------------------+-------------+----------------+---------------+
| Designation_ID | Designation_Name  | Base_Salary | Hra_Percentage | Da_Percentage |
+----------------+-------------------+-------------+----------------+---------------+
|            101 | Software Engineer |    40000.00 |          20.00 |         10.00 |
|            102 | HR Manager        |    50000.00 |          25.00 |         12.00 |
|            103 | Accountant        |    35000.00 |          18.00 |          8.00 |
|            104 | Project Manager   |    70000.00 |          30.00 |         15.00 |
+----------------+-------------------+-------------+----------------+---------------+
```

---

## 6. Employee Table

```sql
CREATE TABLE EMPLOYEE(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male','Female','Other'),
    contact_number VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(100),
    designation_id INT NOT NULL,
    department_id INT NOT NULL,
    bank_account_no VARCHAR(20),
    ifsc_code VARCHAR(11),
    join_date DATE NOT NULL,
    FOREIGN KEY (designation_id) REFERENCES Designation(Designation_ID),
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);
```

**Insert Records:**

```sql
INSERT INTO EMPLOYEE(employee_id, first_name, last_name, date_of_birth, gender, contact_number, email, address, designation_id, department_id, bank_account_no, ifsc_code, join_date)
VALUES
(11, 'RUPESH', 'CHAUDHARY', '2004-02-02', 'Male', '9838292838', 'rupesh.chaudhary.cs28@iilm.edu', 'Delhi', 101, 1000, '123456789012', 'SBIN0000123', '2022-06-01'),
(22, 'AHSAN', 'KHAN', '2004-09-09', 'Male', '98373627362', 'ahsan.khan.cs28@iilm.edu', 'Noida', 102, 1001, '234567890123', 'HDFC0000456', '2023-01-15'),
(33, 'ABHAY', 'SHAKYA', '2004-08-08', 'Male', '9828372727', 'abhay.shakya.cs28@iilm.edu', 'Delhi', 103, 1002, '345678901234', 'ICIC0000789', '2021-09-10'),
(44, 'PRINCE', 'KUMAR', '2004-05-06', 'Male', '9837262522', 'prince.kumar.cs28@iilm.edu', 'Noida', 104, 1003, '456789012345', 'AXIS0000345', '2024-02-01');
```

**Select Table:**

```sql
SELECT * FROM EMPLOYEE;
```

```
+-------------+------------+-----------+---------------+--------+----------------+--------------------------------+---------+----------------+---------------+-----------------+-------------+------------+
| employee_id | first_name | last_name | date_of_birth | gender | contact_number | email                          | address | designation_id | department_id | bank_account_no | ifsc_code   | join_date  |
+-------------+------------+-----------+---------------+--------+----------------+--------------------------------+---------+----------------+---------------+-----------------+-------------+------------+
|          11 | RUPESH     | CHAUDHARY | 2004-02-02    | Male   | 9838292838     | rupesh.chaudhary.cs28@iilm.edu | Delhi   |            101 |          1000 | 123456789012    | SBIN0000123 | 2022-06-01 |
|          22 | AHSAN      | KHAN      | 2004-09-09    | Male   | 98373627362    | ahsan.khan.cs28@iilm.edu       | Noida   |            102 |          1001 | 234567890123    | HDFC0000456 | 2023-01-15 |
|          33 | ABHAY      | SHAKYA    | 2004-08-08    | Male   | 9828372727     | abhay.shakya.cs28@iilm.edu     | Delhi   |            103 |          1002 | 345678901234    | ICIC0000789 | 2021-09-10 |
|          44 | PRINCE     | KUMAR     | 2004-05-06    | Male   | 9837262522     | prince.kumar.cs28@iilm.edu     | Noida   |            104 |          1003 | 456789012345    | AXIS0000345 | 2024-02-01 |
+-------------+------------+-----------+---------------+--------+----------------+--------------------------------+---------+----------------+---------------+-----------------+-------------+------------+
```

---

## 7. Attendance Table

```sql
CREATE TABLE Attendance (
    Employee_ID INT NOT NULL,
    Date DATE NOT NULL,
    Status VARCHAR(20),
    PRIMARY KEY (Employee_ID, Date),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
```

**Insert Records:**

```sql
INSERT INTO Attendance (Employee_ID, Date, Status)
VALUES
(11, '2024-02-20', 'Present'),
(11, '2024-02-21', 'Absent'),
(22, '2024-02-20', 'Present'),
(22, '2024-02-21', 'Present'),
(33, '2024-02-20', 'Leave'),
(33, '2024-02-21', 'Present'),
(44, '2024-02-20', 'Present'),
(44, '2024-02-21', 'Absent');
```

**Select Table:**

```sql
SELECT * FROM Attendance;
```

```
+-------------+------------+---------+
| Employee_ID | Date       | Status  |
+-------------+------------+---------+
|          11 | 2024-02-20 | Present |
|          11 | 2024-02-21 | Absent  |
|          22 | 2024-02-20 | Present |
|          22 | 2024-02-21 | Present |
|          33 | 2024-02-20 | Leave   |
|          33 | 2024-02-21 | Present |
|          44 | 2024-02-20 | Present |
|          44 | 2024-02-21 | Absent  |
+-------------+------------+---------+
```

---

## 8. Users Table

```sql
CREATE TABLE USERS(
    user_id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    employee_id INT UNIQUE,
    FOREIGN KEY (employee_id) REFERENCES EMPLOYEE(employee_id)
);
```

**Insert Records:**

```sql
INSERT INTO USERS (user_id, username, password, role, email, employee_id)
VALUES
(501, 'hr_admin01', 'hr@334', 'HR', 'hr@quantument.com', 11),
(502, 'admin12', 'admin@334', 'ADMIN', 'admin12@quantum.com', 22),
(503, 'payroll1', 'payroll@334', 'HR', 'pay1@quantum.com', 33),
(504, 'payroll2', 'payroll@894', 'HR', 'pay2@quantum.com', 44);
```

**Select Table:**

```sql
SELECT * FROM USERS;
```

```
+---------+------------+-------------+-------+---------------------+-------------+
| user_id | username   | password    | role  | email               | employee_id |
+---------+------------+-------------+-------+---------------------+-------------+
|     501 | hr_admin01 | hr@334      | HR    | hr@quantument.com   |          11 |
|     502 | admin12    | admin@334   | ADMIN | admin12@quantum.com |          22 |
|     503 | payroll1   | payroll@334 | HR    | pay1@quantum.com    |          33 |
|     504 | payroll2   | payroll@894 | HR    | pay2@quantum.com    |          44 |
+---------+------------+-------------+-------+---------------------+-------------+
```

---

## 9. Payroll Table

```sql
CREATE TABLE Payroll(
    employee_id INT,
    pay_period VARCHAR(20),
    gross_salary DECIMAL(10,2),
    deductions DECIMAL(10,2),
    net_pay DECIMAL(10,2),
    payment_date DATE,
    user_id INT,
    PRIMARY KEY (employee_id, pay_period),
    FOREIGN KEY (employee_id) REFERENCES EMPLOYEE(employee_id),
    FOREIGN KEY (user_id) REFERENCES USERS(user_id)
);
```

**Insert Records:**

```sql
INSERT INTO Payroll (employee_id, pay_period, gross_salary, deductions, net_pay, payment_date, user_id)
VALUES
(11, 'Feb-2026', 70000.00, 7000.00, 63000.00, '2026-02-28', 501),
(22, 'Feb-2026', 65000.00, 6500.00, 58500.00, '2026-02-28', 502),
(33, 'Feb-2026', 60000.00, 6000.00, 54000.00, '2026-02-28', 503),
(44, 'Feb-2026', 55000.00, 5500.00, 49500.00, '2026-02-28', 504);
```

**Select Table:**

```sql
SELECT * FROM Payroll;
```

```
+-------------+------------+--------------+------------+----------+--------------+---------+
| employee_id | pay_period | gross_salary | deductions | net_pay  | payment_date | user_id |
+-------------+------------+--------------+------------+----------+--------------+---------+
|          11 | Feb-2026   |     70000.00 |    7000.00 | 63000.00 | 2026-02-28   |     501 |
|          22 | Feb-2026   |     65000.00 |    6500.00 | 58500.00 | 2026-02-28   |     502 |
|          33 | Feb-2026   |     60000.00 |    6000.00 | 54000.00 | 2026-02-28   |     503 |
|          44 | Feb-2026   |     55000.00 |    5500.00 | 49500.00 | 2026-02-28   |     504 |
+-------------+------------+--------------+------------+----------+--------------+---------+
```

---

### ✅ End of Payroll Management Database Setup

```
All tables created, sample data inserted, and foreign key relationships established.
```