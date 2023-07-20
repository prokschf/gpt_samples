SELECT e.name, p.name
FROM employees e
JOIN (
    SELECT name, fk_employee_id
    FROM projects
    WHERE id IN (
        SELECT MAX(id)
        FROM projects
        GROUP BY name
    )
) p ON e.ID = p.fk_employee_id
WHERE e.ID IN (
    SELECT fk_employee_id
    FROM projects
    GROUP BY fk_employee_id
    HAVING COUNT(id) = 1
)
ORDER BY e.name ASC;
