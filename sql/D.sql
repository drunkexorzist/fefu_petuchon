SELECT
	Employees.FullName as EmployeeFullNames ,
    round(sum(Salaries.SalaryPercentage * Positions.Salary),0) as SumSalary
FROM Salaries
	JOIN Employees on Salaries.EmployeeID = Employees.ID
    JOIN Positions on Salaries.PositionID = Positions.ID
GROUP by Employees.FullName
HAVING SumSalary < (
	SELECT 
		avg(rab_sum)
	from(
		SELECT
			Employees.FullName,
    		sum(Salaries.SalaryPercentage * Positions.Salary) as rab_sum
		FROM Salaries
			JOIN Employees on Salaries.EmployeeID = Employees.ID
    		JOIN Positions on Salaries.PositionID = Positions.ID
		GROUP by Employees.FullName
)
  )
ORDER by SumSalary