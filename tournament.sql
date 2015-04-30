-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--created by:Tartufo Taruffetti
--on April 29th, 2015
--SQL Script for Postgres 9.3.6
--the script creates the corresponding database for the used of
--tournament.py

--  dropping the tables just in case they exist already; just in case

--	DROP VIEW IF EXISTS player_standings CASCADE;
--	DROP VIEW IF EXISTS player_games_won CASCADE;
--	DROP VIEW IF EXISTS player_games_played CASCADE;
--	DROP TABLE IF EXISTS Matches CASCADE;
--	DROP TABLE IF EXISTS Player CASCADE;

--  we only need to drop the DDBB and everything else will be dropped
	DROP DATABASE IF EXISTS tournament;

--  creating the database with some options
	CREATE DATABASE tournament
		--WITH OWNER = vagrant
			--ENCODING = 'UTF8'
			--TABLESPACE = pg_default
			--LC_COLLATE = 'Spanish_Spain.1252'
			--LC_CTYPE = 'Spanish_Spain.1252'
			CONNECTION LIMIT = -1;
			
--  if you are using the vagrant VM you need to log into the new 
--  databse to create table and view within this DDBB
	\c tournament;
	
--  creating the player table
	CREATE TABLE Player(
		id SERIAL PRIMARY KEY,
		name text
	);

--  creating the matches table
	CREATE TABLE Matches(
		player1 integer references Player (id),
		player2 integer references Player (id),
		winner integer references Player (id)
	);
	
--  creating the view player standing; this view is not actually used in the current version	
	CREATE VIEW player_standings AS 
		SELECT Player.id,
			Player.name,
			matches.player1,
			matches.player2,
			matches.winner
		FROM Player,matches;

--  creating the view player games won		
	CREATE VIEW player_games_won AS 
		SELECT
			id, 
			sum(won) as wins
		FROM 
			(
			SELECT 
				* ,
				CASE WHEN winner>=1 THEN 1
				ELSE 0
				END as won
			FROM 
				player LEFT OUTER JOIN matches 
			ON 
				player.id = matches.winner
			) AS m
		GROUP BY id;

--  creating the view player games played		
		CREATE VIEW player_games_played AS
			SELECT 
				id, 
				sum(played) as played 
			FROM 
				(
				SELECT 
					player.id,
					player.name, 
					CASE WHEN player1>=1 THEN 1
					ELSE 0
					END as played,
					COALESCE(player1,0) 
				FROM 
					player LEFT OUTER JOIN matches 
				ON 
					player.id = matches.player1 OR player.id = matches.player2
				) AS m
			GROUP BY id;


