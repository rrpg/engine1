BEGIN;

INSERT INTO species (name, description) VALUES ('Human', 'Humans come from planet Earth');

INSERT INTO gender (name) VALUES ('male');
INSERT INTO gender (name) VALUES ('female');

INSERT INTO item (name, weight, flags, effects) VALUES ('Heavy breastplate', 5, 3, '{"defense": 10, "speed": -5}');
INSERT INTO item (name, weight, flags, effects) VALUES ('Mist potion', .1, 6, '{"stealth": 7}');

INSERT INTO region (region_name) VALUES ('The High lands');
INSERT INTO area_type (name) VALUES ('land');
INSERT INTO area_type (name) VALUES ('dungeon');
INSERT INTO area (id_region, id_area_type, container, x, y, directions, items)
	VALUES (1, (SELECT id_area_type FROM area_type WHERE name = 'land'), 'world', 0, 0, 1, '{"1": {"quantity": 1}, "2": {"quantity": 4}}');
INSERT INTO area (id_region, id_area_type, container, x, y, directions, items, has_save_point)
	VALUES (1, (SELECT id_area_type FROM area_type WHERE name = 'land'), 'world', 0, 1, 4, '{"1": {"quantity": 6}}', 'TRUE');

INSERT INTO item_container_type (label) VALUES ('chest');
INSERT INTO item_container_type (label) VALUES ('box');
INSERT INTO item_container_type (label) VALUES ('wardrobe');
INSERT INTO item_container (id_item_container_type, id_area, items) VALUES (1, 2, '{"1": {"quantity": 4}}');
INSERT INTO item_container (id_item_container_type, id_area, items) VALUES (3, 2, '{"1": {"quantity": 4}}');
INSERT INTO item_container (id_item_container_type, id_area, items) VALUES (3, 2, '{"2": {"quantity": 4}}');

INSERT INTO settings (key, value) VALUES ('START_CELL_ID', 1);

INSERT INTO place (id_area, id_area_type, name) VALUES (2, (SELECT id_area_type FROM area_type WHERE name = 'dungeon'), 'first dungeon');

INSERT INTO `character` (name, id_species, id_gender, id_area) VALUES ('Tom', 1, 1, 2);
INSERT INTO talk_answer (trigger_word, sentence, condition) VALUES ('hi', "Hi, my name is Tom, I'm a butcher", '{"met":0}');
INSERT INTO talk_answer (trigger_word, sentence, condition) VALUES ('hi', 'Hi, %(player_name)s', '{"met":1}');

INSERT INTO character_answer (id_character, id_talk_answer) VALUES (1, 1);
INSERT INTO character_answer (id_character, id_talk_answer) VALUES (1, 2);

INSERT INTO creature (name, stat_current_hp, stat_max_hp, stat_attack, stat_defence, stat_speed, stat_luck)
	VALUES ("rat", 15, 15, 2, 2, 2, 25),
		("gobelin", 25, 25, 5, 5, 4, 30),
		("giant spider", 10, 10, 3, 3, 3, 20),
		("C'thulhu", 1000, 1000, 100, 100, 100, 100);

INSERT INTO creature_area_type (id_creature, id_area_type, probability)
	VALUES (1, 2, 0.5), -- rat dungeon
		(1, 1, 0.2), -- rat land, less chances to meet rats outside
		(2, 2, 0.5), -- gobelin land
		(3, 1, 0.5), -- spider
		(4, 1, 0.01); -- c'thulhu

COMMIT;
