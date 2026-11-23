DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS categories;


CREATE TABLE categories (
    id  SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    category_id INTEGER NOT NULL REFERENCES categories(id),
    note TEXT,
    expense_date DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
