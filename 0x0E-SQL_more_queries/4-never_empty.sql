-- creates the table id_not_null on my MySQL Server
-- with default value 1

CREATE table IF NOT EXISTS id_not_null(id INT NOT NULL DEFAULT 1, name VARCHAR(256));
