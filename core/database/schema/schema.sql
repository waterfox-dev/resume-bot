CREATE TABLE `RB_ANSWER` ( 
    `ANSWER_ID`            INTEGER PRIMARY KEY, 
    `ANSWER_JSON_MESSAGES` TEXT NOT NULL,
    `ANSWER_REPONSE`       TEXT NOT NULL,
    `ANSWER_DATE`          DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `ANSWER_CALLER_ID`     INTEGER NOT NULL,
    `ANSWER_THUMBS_UP`     INTEGER NOT NULL DEFAULT 0
);