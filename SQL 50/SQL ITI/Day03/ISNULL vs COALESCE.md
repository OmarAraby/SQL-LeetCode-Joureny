
> `ISNULL` and `COALESCE` are used to handle `NULL` values in SQL, but they have some differences in terms of functionality and use cases
> 
### `ISNULL`

- **Purpose**: Replaces `NULL` with a specified replacement value.
    
- **Syntax**: `ISNULL(expression, replacement_value)`
- `ISNULL` accepts exactly **two argumentsrguments**.
	- `expression`: The value or column to check for `NULL`.
	- `replacement_value`: The value to return if `expression` is `NULL`.
```sql
SELECT ISNULL(column_name, 'default_value') AS result
FROM table_name;

```

```sql
SELECT ISNULL(salary, 0) AS salary
FROM employees;

```

### `COALESCE`

- **Purpose**: Returns the first non-`NULL` expression in a list of expressions.
    
- **Syntax**: `COALESCE(expression1, expression2, ..., expressionN)`
- `COALESCE` accepts multiple arguments (two or more).

```sql
SELECT COALESCE(column_name1, column_name2, 'default_value') AS result
FROM table_name;
```

```sql 
SELECT COALESCE(phone_number, alternate_phone, 'No Phone') AS contact_number
FROM contacts;
```