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
INSERT INTO `Mood` VALUES (null, "silly");INSERT INTO `Mood` VALUES (null, "sick");
INSERT INTO `Mood` VALUES (null, "surprised");
INSERT INTO `Mood` VALUES (null, "nervous");






INSERT INTO `Entry` VALUES (null, "Snickers", "Recreation", "Dalmation", 4, 1);
INSERT INTO `Entry` VALUES (null, "Jax", "Treatment", "Beagle", 1, 1);
INSERT INTO `Entry` VALUES (null, "Falafel", "Treatment", "Siamese", 4, 2);
INSERT INTO `Entry` VALUES (null, "Doodles", "Kennel", "Poodle", 3, 1);
INSERT INTO `Entry` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);
INSERT INTO `Entry` VALUES (null, "Cleo", "Kennel", "Poodle", 2, 2);
INSERT INTO `Entry` VALUES (null, "Popcorn", "Kennel", "Beagle", 3, 2);
INSERT INTO `Entry` VALUES (null, "Curly", "Treatment", "Poodle", 4, 2);
