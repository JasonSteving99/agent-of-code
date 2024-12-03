# Agent of Code

My first attempt at building an AI "agent". The agent will try iteratively solving Advent of Code puzzles. It'll be run as a Temporal workflow, largely just to be able to go back and inspect the full process that the agent takes in working through the problem since Temporal conveniently logs history. I'll also be making use of Temporal's ability to configure timeouts and schedule the timing of activity execution so that I can have confidence that I can keep the agent from just pounding the AoC server with guesses.

# Advent of Code Automation Guidelines Acknowledgement

This agent does follow the [automation guidelines on the /r/adventofcode community wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation). Specifically:

- Puzzle inputs/solutions are not tracked by git (see: `.gitignore`).
- Outbound call retries are throttled to every 1 minute in `agent/temporal/workflow.py`.
- Once inputs are downloaded, they are cached locally (see: `agent/adventofcode/scrape_problems.py`).
- If you suspect a day's input is corrupted, you can manually request a fresh copy by deleting the cached `problem.html` file for that day.
- The User-Agent header in `agent/adventofcode/_HEADERS.py` is set to me since I maintain this tool :)
