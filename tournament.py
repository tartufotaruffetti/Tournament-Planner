#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
'''
created by Tartufo Taruffetti
on April 29th, 2015
The python module was created to implement/develop the Second project of the
Udacity FullStack web Developer Nanodegree
it was tested agaisnt a Postgres 9.3.6 DDBB
In this project, you’ll be writing a Python module that uses the PostgreSQL database 
to keep track of players and matches in a game tournament.
The game tournament will use the Swiss system (See repo for details) for pairing up players in each round: 
players are not eliminated, and each player should be paired with another player with 
the same number of wins, or as close as possible.
This project has two parts: defining the database schema (SQL table definitions), and 
writing the code that will use it.

'''


import psycopg2
#import pprint
import bleach

#Define our connection string
#CONN_STRING = "host='localhost' dbname='tournament2' user='postgres' password=''"
CONN_STRING = "dbname=tournament"

#returns a lived connection to the DDBB
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    print "Connecting to database    ->%s" % (CONN_STRING)
    try:
        return psycopg2.connect(CONN_STRING)
    except Exception as e:
            print "Cannot connect to DB!!"
            print e.__doc__
            print e.message
			
			
#delete all matches from the DDBB
def deleteMatches():
    """Remove all the match records from the database."""
    try:
        
        # get a connection
        conn = connect()
        #conn.cursor we get the cursor to perform queryes, updates, deletes etc
        cursor = conn.cursor()
        
        try:
            #deleting entries from match table
            cursor.execute("""DELETE FROM matches;""")
            conn.commit()
            print "Success! entries in match where deleted..."
        except Exception as e:
            #if we cannto delete or we have some error, we rollback
            print "Error! cannot delete values from match..."
            conn.rollback()
            print e.__doc__
            print e.message
            
    except:
        print "Cannot connect to DB, therefore wont delete matches from DB!!"
    
    #closing the connection
    conn.close()

#delete all players from teh DDBB
def deletePlayers():
    """Remove all the player records from the database."""
    try:
        
        # get a connection
        conn = connect()
        #conn.cursor we get the cursor to perform queryes, updates, deletes etc
        cursor = conn.cursor()
        
        try:
            #deleting entries from player table
            cursor.execute("""DELETE FROM player;""")
            conn.commit()
            print "Success! entries in player where deleted..."
        except Exception as e:
            #if we cannto delete or we have some error, we rollback
            print "Error! cannot delete values from player..."
            conn.rollback()
            print e.__doc__
            print e.message
            
    except:
        print "Cannot connect to DB, therefore wont delete player from DB!!"
    
    #closing the connection
    conn.close()

#return the number of player available
def countPlayers():
    """Returns the number of players currently registered."""
    try:
        
        # get a connection
        conn = connect()
        #conn.cursor we get the cursor to perform queryes, updates, deletes etc
        cursor = conn.cursor()
        #querying player table
        cursor.execute("SELECT COUNT(*) FROM player;")
        # retrieve the records from the database
        records = cursor.fetchone()
        return records[0]
        
    except:
        print "Cannot connect to DB, therefore wont count player from DB!!"
    
    #closing the connection
    conn.close()

#add a player to the DDBB player table
#Args: name as String = the player Full name
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    try:
        #cleaning up the name value
		name = bleach.clean(name);
		name = bleach.linkify(name);
        # get a connection
        conn = connect()
        #conn.cursor we get the cursor to perform queryes, updates, deletes etc
        cursor = conn.cursor()
        
        try:
            #adding entries to player table
            cursor.execute("INSERT INTO player(name) VALUES (%s);", (name,))
            conn.commit()
            print "Success! player was added..."
        except Exception as e:
            #if we cannto add the player we print the error
            print "Error! cannot add the new player ..."
            conn.rollback()
            print e.__doc__
            print e.message
            
    except:
        print "Cannot connect to DB, therefore wont delete player from DB!!"
    
    #closing the connection
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    try:
        
        # get a connection
        conn = connect()
        #conn.cursor we get the cursor to perform queryes, updates, deletes etc
        cursor = conn.cursor()
        #adding entries to player table
        cursor.execute("select  \
            player.id, \
            player.name, \
            player_games_won.wins, \
            player_games_played.played \
            from player join player_games_played \
            on player.id = player_games_played.id join player_games_won on player_games_played.id = player_games_won.id order by wins DESC; ")
        records = cursor.fetchall()
#        pprint.pprint(records)
        return records
        
            
    except:
        print "Cannot connect to DB, therefore wont delete player from DB!!"
    
    #closing the connection
    conn.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    try:
        #cleaning up the variables
		winner = bleach.clean(winner);
		winner = bleach.linkify(winner);
		
		loser = bleach.clean(loser);
		loser = bleach.linkify(loser);
        
        # get a connection
        conn = connect()
        #conn.cursor we get the cursor to perform queryes, updates, deletes etc
        cursor = conn.cursor()
        
        try:
            #adding entries to player table
            cursor.execute("""INSERT INTO matches(player1, player2, winner) VALUES (%s, %s, %s);""", (winner,loser, winner))
            conn.commit()
            print "Success! match was added..."
        except Exception as e:
            #if we cannto add the player we print the error
            print "Error! cannot add the match ..."
            conn.rollback()
            print e.__doc__
            print e.message
            
            
    except:
        print "Cannot connect to DB, therefore wont delete player from DB!!"
    
    #closing the connection
    conn.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    try:
        
        # get a connection
        conn = connect()
        #conn.cursor we get the cursor to perform queryes, updates, deletes etc
        cursor = conn.cursor()
        #adding entries to player table
        cursor.execute('select player1, p1.name, player2, p2.name from '+
        '(select '+ 
        '    a.id as player1, '+
        '    a.wins as wins1, '+
        '    b.id as player2, '+
        '    b.wins as wins2 '+
        'from player_games_won as a join player_games_won as b '+ 
        'on a.wins = b.wins and a.id < b.id ) as c join player as p1 on c.player1 = p1.id join player as p2 on c.player2 = p2.id '+
        'order by wins1 desc'
        )
        records = cursor.fetchall()
#        pprint.pprint(records)
        return records
        
            
    except:
        print "Cannot connect to DB, therefore wont delete player from DB!!"
    
    #closing the connection
    conn.close()

