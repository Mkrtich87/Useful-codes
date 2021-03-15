SELECT * FROM [dbo].[tblTransaction] AS T
INNER JOIN [dbo].[tblEmployee] AS E
ON T.EmployeeNumber=E.EmployeeNumber
WHERE  [EmployeeLastName] LIKE 'Y%'
ORDER BY T.EmployeeNumber



SELECT * FROM [dbo].[tblTransaction] AS T
WHERE [EmployeeNumber] in ( SELECT [EmployeeNumber] FROM  [dbo].[tblEmployee] WHERE [EmployeeLastName] LIKE 'Y%')
ORDER BY [EmployeeNumber]