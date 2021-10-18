SELECT 
	Sellers.LastName || " " || Sellers.firstname as SellerFullName,
    SUM(SalesItems.QuantitySold * Products.SellingPrice) AS TotalRevenue,
    COUNT(DISTINCT Sales.ID) as CountOfSales 
FROM SalesItems
	JOIN Products on SalesItems.ProductID = Products.ID
    JOIN Sales on SalesItems.SaleID = Sales.ID
    JOIN Sellers ON Sales.SellerID = Sellers.ID
GROUP BY SellerFullName
ORDER by TotalRevenue DESC
LIMIT 10
