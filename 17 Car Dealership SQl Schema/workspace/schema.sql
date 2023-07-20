CREATE TABLE Cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    year_of_construction INT,
    color VARCHAR(20),
    mileage INT,
    condition VARCHAR(20)
);

CREATE TABLE Owners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    phone_number VARCHAR(15),
    address VARCHAR(100),
    email VARCHAR(50)
);

CREATE TABLE Employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Purchases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_id INT,
    owner_id INT,
    employee_id INT,
    price DECIMAL(10, 2),
    date_of_purchase DATE,
    FOREIGN KEY (car_id) REFERENCES Cars(id),
    FOREIGN KEY (owner_id) REFERENCES Owners(id),
    FOREIGN KEY (employee_id) REFERENCES Employees(id)
);
