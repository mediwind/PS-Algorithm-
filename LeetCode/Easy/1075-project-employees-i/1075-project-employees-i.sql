# Write your MySQL query statement below
SELECT project_id, ROUND(SUM(experience_years) / COUNT(project_id), 2) AS average_years
FROM Project p
JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY project_id