CREATE TABLE IF NOT EXISTS `RB_ANSWER` ( 
    `ANSWER_ID`             INTEGER PRIMARY KEY, 
    `ANSWER_JSON_MESSAGES`  TEXT NOT NULL,
    `ANSWER_RESPONSE`       TEXT NOT NULL,
    `ANSWER_DATE`           DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `ANSWER_CALLER_ID`      TEXT NOT NULL,
    `ANSWER_THUMBS_UP`      INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS `RB_GUILD` (
    `GUILD_ID`              INTEGER PRIMARY KEY,
    `GUILD_LANG`            TEXT NOT NULL,
    `GUILD_ACTIVE`          BOOLEAN NOT NULL DEFAULT TRUE
);

