SELECT
	Employees.fullname as EmployeeFullNames,
    sum(Positions.Salary * Salaries.SalaryPercentage) as SumSalary
from Employees
	left JOIN Salaries on Salaries.EmployeeID = Employees.ID
    left JOIN Positions on Salaries.PositionID = Positions.ID
WHERE Positions.Salary > 0 
AND Salaries.SalaryPercentage BETWEEN 0 AND 1
GROUP BY Employees.fullname
HAVING SumSalary <(
	SELECT avg(avg_sum)
	FROM (
    	SELECT 
    		sum(Salaries.SalaryPercentage * Positions.Salary) as avg_sum
		from Salaries
			LEFT JOIN Employees on Salaries.EmployeeID = Employees.ID
    		LEFT JOIN Positions on Salaries.PositionID = Positions.ID
		GROUP BY Employees.FullName
    ) 
)
