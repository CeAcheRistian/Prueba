### [mismo enlace, clase 3](https://tech.io/playgrounds/123318/sql-facilito)

## Common Table Expressions
Es un conjunto de resultados con nombre temporal al que puede hacer referencia dentro de una instrucción SELECT, INSERT, UPDATE o DELETE. El CTE también se la puede usar en una vista. 

El resultado del query es usado como una tabla para otros querys, pero usas su nombre temporal, como si se almacenara en una variable.

Sintaxis:

_WITH_ + alias + _AS_ + (QUERY CTE) Query que hace referencia al CTE

    WITH UK_Customers AS (
        SELECT customerNumber 
        FROM customers
        WHERE country = 'UK'
    )
    SELECT *
    FROM orders O
    INNER JOIN UK_Customers C ON C.customerNumber = O.customerNumber;

    WITH CTE AS (
        SELECT CustomerNumber
        FROM customers
        WHERE customerNumber BETWEEN 121 AND 471
        AND (customerName LIKE 'A%'
            OR customerName LIKE '_A%')
        AND addressLine1 IS NOT NULL
        AND addressLine2 IS NULL
        AND creditLimit > 0
        AND postalCode IN ('4110', '51247')
    )
    UPDATE customers
    INNER JOIN CTE C 
    ON C.CustomerNumber = customers.CustomerNumber
    SET customers.creditLimit = 17.19;

## Window Functions
Una window function nos da visibilidad de información sobre un set de datos, desde cada fila podemos acceder a ese set de datos. A diferencia de las funciones de agregación que nos obliga a hacer agrupaciones, las window function no. Es posible usar las funciones de agregación con las window functions a fin de obtener calculos para cada fila sin realizar agrupaciones.

Sintaxis general:

( [ ALL ] expression ) OVER ( [ PARTITION BY partition_list ] [ ORDER BY order_list] )

Algunas funciones comunes:

    FIRST_VALUE: Para obtener el primer valor de un grupo.
    LAST_VALUE: Para obtener el ultimo valor de un grupo.
    LAG: Para obtener un valor de la fila anterior.
    LEAD: ara obtener un valor de la fila siguiente.
    RANK: Asigna un valor o un rank a cada fila segun la particion.
    ROW_NUMBER: Obtiene el numero de fila, puede ser una numeracion general o reiniciar la numeracion por grupos o particiones.
[Mas info window functions MySQL](https://dev.mysql.com/doc/refman/8.0/en/window-functions-usage.html)

[Mas info de windows functions](https://www.sqlservertutorial.net/sql-server-window-functions/)

Query con una funcion de agregacion la cual devuelve el total de ordenes para cada cliente, pero no es posible listar los datos de esa orden.

SELECT C.customerNumber, C.customerName, COUNT(O.orderNumber) total_orders  
FROM customers C  
INNER JOIN orders O ON C.customerNumber = O.customerNumber  
GROUP BY C.customerNumber, C.customerName;

Query con una window function la cual devuelve el total de ordenes para cada cliente, pero si es posible listar los datos de esa orden.

SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate,  
COUNT(O.orderNumber) OVER(PARTITION BY C.customerNumber) AS total_orders  
FROM customers C  
INNER JOIN orders O ON C.customerNumber = O.customerNumber;

Query con una window function para acceder a valores en otras filas. Adicional a los datos de la fila actual muestra la fecha de la primera orden que realizo el cliente.

SELECT C.customerNumber, C.customerName, O.orderNumber, O.orderDate,  
FIRST_VALUE(O.orderDate) OVER(PARTITION BY C.customerNumber) AS firstOrderDate  
FROM customers C  
INNER JOIN orders O ON C.customerNumber = O.customerNumber

