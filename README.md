# Tic-Tac-Toe AI using Minimax Algorithm

## Description
This is a Tic-Tac-Toe game I made for my second semester flipped course project.  
Everything is kept in a single code file. 
This project is a command-line Tic-Tac-Toe game where a human player competes against an AI. The AI uses the Minimax algorithm to make optimal decisions, meaning it will never lose if played correctly.

## Problem Statement
Tic-Tac-Toe is a simple game, but designing an AI that always makes the best move requires strategic decision-making. This project demonstrates how adversarial search can be used to solve such problems.

## Approach
The game is modeled as an adversarial problem:
- The human player tries to win
- The AI tries to maximize its chances of winning

The Minimax algorithm is used:
- The AI simulates all possible future moves
- It assumes the opponent will also play optimally
- It chooses the move that leads to the best outcome

## Features
- Play against an AI opponent
- AI never loses (optimal play)
- Simple command-line interface
- Handles win, lose, and draw conditions

## How to Run
1. Make sure Python 3 is installed
2. Run: python main.py
3. Enter row and column values (0–2) when prompted

## Gameplay Instructions
- You play as `X`
- AI plays as `O`
- Enter positions using:
- Row: 0 to 2
- Column: 0 to 2

Example:
Enter row: 1
Enter col: 2

## AI Concepts Used
- Adversarial Search
- Minimax Algorithm
- Rational Agent Decision Making

## Challenges Faced
- Implementing Minimax correctly
- Handling all game states (win/draw)
- Ensuring the AI responds instantly

## What I Learned
- How AI can simulate future decisions
- How adversarial problems are solved
- Importance of evaluating game states properly
