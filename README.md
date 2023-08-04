<h1> Tic-Tac-Toe-AI-Bot </h1>
Play against an unbeatable AI in a game of Tic-Tac-Toe!

<h2> Code Details </h2>
The main piece of this code lies in the functions getComputerInput() and computeMinimax() as these functions dictate the bot's next move. As the names suggests, the bot uses a <b> non-binary tree </b> data structure as it <b> recursively </b> calls itself to run the famous <b> minimax </b> algorithm with the inclusion of <b> alpha-beta pruning</b>; a process where branches of the search tree are not fully explored given the fact that the branch is an inferior path in its lowest-depth maximizing nodes compared to a branch already explored, and is therefore discarded.

<h2> Instructions </h2>
<div> Once the code has been run, the terminal will print out the tic-tac-toe board. The terminal will display the board at every turn as well as who's turn it is; the player or computer. </div>
<br>
<div> If it is your turn, the terminal will prompt you to select a tile to place your piece on via its assigned number. The numbers are assigned on the board from 1 to 9. For reference, the top left tile is 1, the middle tile is 5, and the bottom right tile is 9.</div> 
<br>
<div> Have fun! </div>


