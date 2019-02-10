2048_scoutgame
==============

Play the online game [2048](http://gabrielecirulli.github.io/2048/) in real life. 

In the original 2048 game, numbers add up once they collide. 2 and 2 makes 4, 16 and 16 add up to 32 etc.

Prepration
----------
- Divide the sorted cards over ca. 4 leaders, that will walk around the playing field. Divide the cards such that leaders do not have consecutive numbers. Eg. give A only 4, 32, 256, B only 2, 16, 512 etc. 

Game
----

In this real-life game every player gets a card of value 2 or 4 when starting the game.
After the start, each player tries to find someone with the same value on their card.
Once they found such a player, they go find the leader that has cards with the sum of their numbers (e.g. if you are both 16, go find a leader who can give you 32)

When that leader is found, only *one* card of the next value is handed back to the players. Which of the two players gets the new card is decided by throwing dices, rock-paper-scissors or something similar.
The winner gets the 'added-up' card, the losing player gets an equal or lower card than (s)he came in with, e.g. a 2 or a 4. 

After they leave the post, both players try to find someone with the same card again. 

The game ends when you decide or cards run out. Of course, the winner is the player with the highest number. 

Extra
-----
When your scouts are too smart, the game ends too soon or you want to make the game a bit more exciting, you can add the Denominator. When this player taps a normal player, his/her value is halved.

Cards
-----
There are several variants for donload, but this is the [most](https://github.com/LoyVanBeek/2048_scoutgame/blob/master/2048%20Colored%20met%20Gemene%20Deler.pdf) complete.
The cards can be generated with the provided Python script that outputs HTML. 
