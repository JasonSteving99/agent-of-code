# Agent of Code

My first attempt at building an AI "agent". The agent will try iteratively solving Advent of Code puzzles. It'll be run as a Temporal workflow, largely just to be able to go back and inspect the full process that the agent takes in working through the problem since Temporal conveniently logs history. I'll also be making use of Temporal's ability to configure timeouts and schedule the timing of activity execution so that I can have confidence that I can keep the agent from just pounding the AoC server with guesses.
