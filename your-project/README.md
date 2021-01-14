<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Terminal Mastermind Game
*Pau Serra*

*Data Analyst Bootcamp, Barcelona, Jan 2021*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
Mastermind Game developped in order to put in practice the learnings from Week 1 in Data Analyst Bootcamp at Ironhack.
Mastermint consist on finding the color code pickup randomly by the computer.

## Rules:

- The computer picks a sequence of colors. The number of colors is the code length. The default code length is 4.
- The objective of the game is to guess the exact positions of the colors in the computer's sequence.
- By default, a color can be used only once in a code sequence. If you start a new game with the 'repeat' parameter active, then any color can be used any number of times in the code sequence.
- After entering your sequence of colors, the computer responses with the result of your guess.
- For each color in your guess that is in the correct color and correct position in the code sequence, the computer would display the amount in the column R.
- For each color in your guess that is in the correct color but is NOT in the correct position in the code sequence, the computer would display the amount in the column W.
- You win the game when you manage to guess all the colors in the code sequence and when they all in the right position.
- You lose the game if you use all attempts without guessing the computer code sequence.
- By default you have 10 chances to guess the code sequence, you can change it by calling the game with 'chances' parameter.

## How to play this game:

- Start a new game by calling the function startGame() from your terminal.
- If you want to have also repeated color codes you should call the function with the repeat parameter. Example: startGame(repeat=1)
- If you want to have more or less chances, you can change the 'chances' parameter. Example: startGame(chances=8)
- You would be asked to input your choice, you need to use the numeric keyboard to select the desired colors following this parameters:
	1 - RED
	2 - GREEN
	3 - YELLOW
	4 - BLUE
	5 - WHITE
	6 - CYAN
- Example: BLUE GREEN WHITE RED ---> 4 2 5 1
- Good Luck!!

## Workflow
1 - Search game information.
2 - Design code structure
3 - Coding
4 - Test code.
5 - Implement color to the terminal output.

## Organization
To organize my work I have used a kanban using Trello.

## Links
[Repository](https://github.com/p93serra/Project-Week-1-Build-Your-Own-Game)  
[Slides](https://drive.google.com/file/d/1QXMDSfNif1u3iYdPwyF1QwnMRWn5cWcB/view?usp=sharing)  
[Trello](https://trello.com/invite/b/IzFQBVnr/0b7fa21e9c513bf7dd86abf776d33a5b/project1-game)  
