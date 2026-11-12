USE bank_loan;

SELECT loan_status, COUNT(*) AS total
FROM loan_data
GROUP BY loan_status;

SELECT AVG(loan_amnt) AS avg_loan
FROM loan_data;

SELECT grade, loan_status, COUNT(*) AS total
FROM loan_data
GROUP BY grade, loan_status
ORDER BY grade;

SELECT loan_status, AVG(annual_inc) AS avg_income
FROM loan_data
GROUP BY loan_status;

SELECT home_ownership, loan_status, COUNT(*) AS total
FROM loan_data
GROUP BY home_ownership, loan_status;

SELECT * FROM loan_data;