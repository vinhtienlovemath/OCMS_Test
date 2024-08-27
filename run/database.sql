CREATE DATABASE online_courses CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE online_courses;

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    duration VARCHAR(100),
    seats_available INT,
    price DECIMAL(10, 2),
    image_url VARCHAR(255),
    instructor_name VARCHAR(255),
    instructor_details TEXT
);


INSERT INTO courses (title, description, start_date, duration, seats_available, price, image_url, instructor_name, instructor_details)
VALUES ('Professional Ceramic Moulding', 'Learn ceramic moulding from scratch.', '2023-10-10', '7 days', 30, 150.00, 'path/to/image.jpg', 'John Doe', 'Experienced ceramic artist with 10 years of teaching.');
