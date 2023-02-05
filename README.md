# Pong-peli
Simple pong-game, Python

!!! INSTRUCTIONS AT THE END !!!

This is my first independent project, very exciting!

The program is a Pong-game, that is created with using Python turtle module
The idea of a Pong-game is very simple; there are two players who each can control their own paddle on the left and right of the screen
Between the paddles there is a ball, that bounces off when coming into contact with the upper or  bottom side of the screen, or either one of the players' paddles
Player can gain points by defending their own side of the screen with the paddle and making the ball reach the opposite side
The program ends, when either one of the players reaches ten points, and then shows the amount of times the winners paddle came in contact with the ball

First I created the screen in which I started adding the paddles and the ball as static objects, and then gave the ball its speed (the movement on x- and y axis) and defined functions for the paddle controls
Next I defined the functions that will be called when the players score count reaches ten, basically announcing which player won the game
Then I defined which controls will be used to move the paddles (w,s,UP,DOWN)

The main loop refreshes the balls position based on the speed I determined earlier
The ball is made to change direction when it comes to contact with either upper or bottom side of the screen, thus making it bounce
Next I defined what will happen, if the ball reaches either side of the screen; the ball will be set to the middle of the screen and a point will be added for the scoring player
Then I added collision for the paddles, making the ball bounce off of it and also adding a point to the "contact" counter (shows the winner how many times their ball touches the paddle).
When the score counter reaches ten for either one of the players, the game will end and print out the winner and the amount of touches they had with the paddle
The program will also use the file "Pelitilanne.txt" to first read it, and then create another file called "ViimePelinVoittaja", which will show who has won the most recent game



Now for the instructions:
To play the game correctly, the player needs to download the file called "Pelitilanne.txt" from the repository.

Player A has the controls "w" to move the paddle up, and "s" to move the paddle down.
Player B has the controls (arrow keys) "UP" to move the paddle up, and "DOWN" to move the paddle down.
