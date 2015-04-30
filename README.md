# **Tournament-Planner**

##**Background**
Tournament Planner correspond to the second project within the Udacity FullStack Developer Nanodegree
Consist of a Python module (tournament.py) that uses the PostgreSQL database (created with the script tournament.sql) to keep track of players and matches in a game tournament.

##**Description**
Tournament Planner keep track of players and matches in a game tournament.
The game tournament uses the Swiss system (http://en.wikipedia.org/wiki/Swiss-system_tournament) for pairing up players in each round where players are not eliminated, and each player should is paired with another player with the same number of wins, or as close as possible. You start by registering an even number of players and you pair them up and record the match results. You keep doing this as many times as needed till you get a champion.

###**Modules**
1. tournament.sql :  This is the script that contains the database schema and once ran it creates all the tables and views need.
2. tournament.py : This is the python module that contains the implementation of the functionality. This is the module you want to use when you need to register a player, record a match result or check who is the champ!
3. tournament_test.py :  This is module which represent a test throughtly all the functionalities within tournament.py

##How to use it
The following is just a simple example of how to use the software:
Make sure you import the module into your project, then you can star for example by registering players:
```
registerPlayer("John")
registerPlayer("Andrew")
registerPlayer("Naomi")
registerPlayer("Heidi")
```
Once you have some players you can pair them up to get the games going:
```
standings = playerStandings()
```
After you got some games played, dont forget to register the match results:
```
reportMatch(id1, id2)
reportMatch(id3, id4)
```

##License and Copyright
Released under the MIT License.
##Documentation
The following is just a brief description of each method within the tournament.py  module:

1. registerPlayer(name) : Adds a player to the tournament by putting an entry in the database.
2. countPlayers() : Returns the number of currently registered players.
3. deletePlayers() : Clear out all the player records from the database.
4. reportMatch(winner, loser) : Stores the outcome of a single match between two players in the database.
5. deleteMatches() : Clear out all the match records from the database.
6. playerStandings() : Returns a list of id, name, wins, matches for each player, sorted by the number of wins each player has.
7. swissPairings() : Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system.

##Installation
If you would like to run this project using the Udacity VM you will need to do the following: 

1. Install Git. If you don't already have Git installed, download Git from http://git-scm.com/. Install the version for your operating system.
2. Install VirtualBox. VirtualBox is the software that actually runs the VM. You can download it from https://www.virtualbox.org/ , here. Install the platform package for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.Ubuntu 14.04 Note: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.
3. Install Vagrant. Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Install from https://www.vagrantup.com/
4. Use Git to fetch the VM configuration. Use the Git Bash program (installed with Git) or a terminal and run : ``` git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack ```
5. Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), then type vagrant up to launch your virtual machine. 
6. type vagrant ssh to log into it. 
7. type ```cd /vagrant/tournament``` . Make sure all files from this repo are in the directory tournament , you can either copy directly or clone them from github. Check everything is in place by typing ``` ls ``` and you should see the three files; tournament.sql, tournament_test.py and tournament.py
8. type ``` psql ```
9. run ``` \i tournament.sql ```. This should install the database
10. exit the psql by typing ``` \q ``` 
11. run ``` python tournament_test.py ```
12. if everything went ok, then you should see a final messege saying All the test were passed!

However, if you dont wanna use the Udacity VM:

1. you can download the postgres database from http://www.postgresql.org
2. After you have installed the ddbb, create a database called tournament
3. Edit the tournament.sql script by commenting the DROP DATABASE and the CREATE DATABASE lines
4. Run the script
5. Make sure you have python 2.7 intalled or intalled from https://www.python.org/
6. Make sure you have install the psycopg2 (https://pypi.python.org/pypi/psycopg2) and bleach (https://pypi.python.org/pypi/bleach) module
7. Using the IDLE or you favority IDE edit the tournament.py ddbb connection in order to connect to your new installed ddbb.
8. Run the tournament_test.py and make sure there are no errors.
9. If there are no errors you are ready to go, enjoy it!

Everything was program with a Postgres DDBBB 9.3.6 and Python 2.7

##Authors
Tartufo Taruffetti
