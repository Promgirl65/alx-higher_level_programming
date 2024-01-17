-- creates the unique table unique_id on my MySQL Server.

CREATE table IF NOT EXISTS unique_id(id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));
