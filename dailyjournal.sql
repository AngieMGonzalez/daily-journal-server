CREATE TABLE `Mood` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);

CREATE TABLE `Entry` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`  TEXT NOT NULL,
	`entry` TEXT NOT NULL,
	`date` TEXT NOT NULL,
	`mood_id` INTEGER NOT NULL,
	FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

INSERT INTO `Mood` VALUES (null, "happy");
INSERT INTO `Mood` VALUES (null, "sad");
INSERT INTO `Mood` VALUES (null, "tired");
INSERT INTO `Mood` VALUES (null, "calm");
INSERT INTO `Mood` VALUES (null, "scared");
INSERT INTO `Mood` VALUES (null, "worried");
INSERT INTO `Mood` VALUES (null, "excited");
INSERT INTO `Mood` VALUES (null, "confused");
INSERT INTO `Mood` VALUES (null, "angry");
INSERT INTO `Mood` VALUES (null, "love");
INSERT INTO `Mood` VALUES (null, "embarrassed");
INSERT INTO `Mood` VALUES (null, "silly");
INSERT INTO `Mood` VALUES (null, "sick");
INSERT INTO `Mood` VALUES (null, "surprised");
INSERT INTO `Mood` VALUES (null, "nervous");

INSERT INTO `Entry` VALUES (null, "Javascript", "I learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.", "Wed Sep 15 2021 10:10:47 ", 1);
INSERT INTO `Entry` VALUES (null, "Python", "Python is named after the Monty Python comedy group from the UK. I'm sad because I thought it was named after the snake", "Wed Sep 15 2021 10:11:33 ", 4);
INSERT INTO `Entry` VALUES (null, "Python", "Why did it take so long for python to have a switch statement? It's much cleaner than if/elif blocks", "Wed Sep 15 2021 10:13:11 ", 3);
INSERT INTO `Entry` VALUES (null, "Javascript", "Dealing with Date is terrible. Why do you have to add an entire package just to format a date. It makes no sense.", "Wed Sep 15 2021 10:14:05 ", 3);

SELECT * FROM Mood;
SELECT * FROM Entry;

-- Get only the entry row where the `id` field value is 3
SELECT
	e.id,
  e.concept,
  e.entry,
  e.date,
  e.mood_id
FROM entry e
WHERE e.id = 2;
