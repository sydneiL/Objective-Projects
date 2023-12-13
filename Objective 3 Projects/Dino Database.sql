CREATE DATABASE dinosaur_database;
USE dinosaur_database;
CREATE TABLE dinosaurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    era VARCHAR(255),
    group_type VARCHAR(255),
    species VARCHAR(255),
    family VARCHAR(255),
    length VARCHAR(255),
    fossils INT
);
INSERT INTO dinosaurs (era, group_type, species, family, length, fossils)
VALUES
('Triassic', 'Theropod', 'Herrerasaurus', 'Herrerasauridae', '3 meters', 12),
('Triassic', 'Sauropod', 'Plateosaurus', 'Plateosauridae', '8 meters', 24),
-- Add more data as needed
('Cretaceous', 'Theropod', 'Tyrannosaurus Rex', 'Tyrannosauridae', '12 meters', 62),
('Cretaceous', 'Sauropod', 'Argentinosaurus', 'Titanosauridae', '30 meters', 48);
