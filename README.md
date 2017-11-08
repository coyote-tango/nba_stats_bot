# nba_statsbot

When called, nba_statsbot will reply with the player's overall statistcs for the current NBA season.
nba_statsbot will provide the following stats:

* MIN - Minutes Played
* PTS - Points per Game
* REB - Rebounds per Game
* AST - Assists per Game
* FG% - Field Goal Percentage
* 3P% - Three Point Percentage
* FT% - Fiel Throw Percentage
* STL - Steals per Game
* BLK - Blocks per Game
* +/- - Box Plus/Minus

In order to make call to nba_statsbot, you will need to comment the player's name followed by the word **statsbot**, example:

"lebron James _**statsbot**_"   <-- This will work 

"~~statsbot lebron james~~"   <-- This won't work (X)

_* note that you can write this sentence at any part of you comment, as long as it includes the word **statsbot**, the  will analyze your comment._

*nba_statsbot does not necesaryly necessarily need you to to specify the first name, you can use only the last name:

"Cousins **statsbot**"   <-- This will work

In case there are more players with the same name, you will need to specify the first name, otherwise, nba_statsbot will reply with all of the players with the same last name and will remind you to specify the first name, you can reply to that comment, this time, specifying the first and last name.

If nba_statsbot cannot find your player, it will let you know so and remind you to check for typos just in case.
