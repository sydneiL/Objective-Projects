create database if not exists trivia_game;

use trivia_game;

DROP DATABASE IF EXISTS ap;

USE ap;

CREATE TABLE TriviaGame (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(120) NOT NULL
);

INSERT INTO TriviaGame (category_id, category_name) VALUES
    (1, 'General Knowledge'),
    (2, 'Science'),
    (3, 'History'),
    (4, 'Geography'),
    (5, 'Movies'),
    (6, 'Music'),
    (7, 'Sports'),
    (8, 'Art'),
    (9, 'Literature'),
    (10, 'Technology');
CREATE TABLE Questions (
    question_id INT PRIMARY KEY NOT NULL,
    question_text VARCHAR(120) NOT NULL,
    category_id INT,
    level INT NULL,
    FOREIGN KEY (category_id) REFERENCES TriviaGame(category_id)
);
INSERT INTO Questions (question_id, question_text, category_id, level) VALUES
    (1, 'What is the capital of France?', 4, 2),
    (2, 'Who wrote "Romeo and Juliet"?', 9, 1),
    (3, 'What is the boiling point of water?', 2, 3),
    (4, 'In which year did World War II end?', 3, 2),
    (5, 'Who painted the Mona Lisa?', 8, 1),
    (6, 'What is the largest planet in our solar system?', 2, 2),
    (7, 'Who won the Nobel Prize in Physics in 1921?', 1, 3),
    (8, 'In which year was the first successful manned mission to the moon?', 2, 2),
    (9, 'Which sport uses a shuttlecock?', 7, 1),
    (10, 'Who composed the Symphony No. 9?', 6, 3);
CREATE TABLE Answers (
    answer_id INT PRIMARY KEY NOT NULL,
    answer_text VARCHAR(120) NOT NULL,
    is_correct BOOLEAN NOT NULL,
    question_id INT,
    FOREIGN KEY (question_id) REFERENCES Questions(question_id)
);
INSERT INTO Answers (answer_id, answer_text, is_correct, question_id) VALUES
    (1, 'Paris', TRUE, 1),
    (2, 'William Shakespeare', TRUE, 2),
    (3, '100 degrees Celsius', TRUE, 3),
    (4, '1945', TRUE, 4),
    (5, 'Leonardo da Vinci', TRUE, 5),
    (6, 'Jupiter', TRUE, 6),
    (7, 'Albert Einstein', TRUE, 7),
    (8, '1969', TRUE, 8),
    (9, 'Badminton', TRUE, 9),
    (10, 'Ludwig van Beethoven', TRUE, 10);

SELECT question_id, question_text, category_id, level
FROM Answers INNER JOIN Answers
ON Questions.question_id=questions.question_id;