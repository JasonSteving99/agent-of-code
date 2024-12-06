# Agent of Code

My first attempt at building an AI "agent". The agent will try iteratively solving Advent of Code puzzles. It'll be run as a Temporal workflow, largely just to be able to go back and inspect the full process that the agent takes in working through the problem since Temporal conveniently logs history. I'll also be making use of Temporal's ability to configure timeouts and schedule the timing of activity execution so that I can have confidence that I can keep the agent from just pounding the AoC server with guesses.

# Advent of Code Automation Guidelines Acknowledgement

This agent does follow the [automation guidelines on the /r/adventofcode community wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation). Specifically:

- Puzzle inputs/solutions are not tracked by git (see: `.gitignore`).
- Outbound call retries are throttled to every 1 minute in `agent/temporal/workflow.py`.
- Once inputs are downloaded, they are cached locally (see: `agent/adventofcode/scrape_problems.py`).
- If you suspect a day's input is corrupted, you can manually request a fresh copy by deleting the cached `problem.html` file for that day.
- The User-Agent header in `agent/adventofcode/_HEADERS.py` is set to me since I maintain this tool :)

# Status Updates
On day 4 I realized that it'd be fun to explicitly do a bit of a log on how things are going. 

#### :exclamation: \*Hypothetical [Global Leaderboard](https://adventofcode.com/2024/leaderboard) Rank\* :exclamation: 
_I'm not a rule-breaker so I'm intentionally not running the agent until AFTER the global leaderboard is full. But it's interesting to see what ranking I COULD'VE gotten_.

| Day | Part 1 | Part 2 | Global Rank\* | Total Agent Workflow Time |
|:---:|:---:|:---:|:---:|:---:|
| [1](https://github.com/JasonSteving99/agent-of-code/tree/main/advent_of_code/year2024/day1) | ✅ | ✅ | ? | - |
| [2](https://github.com/JasonSteving99/agent-of-code/tree/main/advent_of_code/year2024/day2) | ✅ | ✅ | ? | - |
| [3](https://github.com/JasonSteving99/agent-of-code/tree/main/advent_of_code/year2024/day3) | ✅ | ✅ | ? | - |
| [4](https://github.com/JasonSteving99/agent-of-code/tree/main/advent_of_code/year2024/day4) | ✅ | ✅ | #83 | <img src="https://github.com/JasonSteving99/agent-of-code/blob/main/images/day4_workflow_1_success.png?raw=true" width="500" height="100"> |
| [5](https://github.com/JasonSteving99/agent-of-code/tree/main/advent_of_code/year2024/day5) | ✅ | ✅ | #31 | <img src="https://github.com/JasonSteving99/agent-of-code/blob/main/images/day5_workflow_1_success.png?raw=true" width="500" height="100"> |
| [6](https://github.com/JasonSteving99/agent-of-code/tree/main/advent_of_code/year2024/day6) | ✅ | ❌ | N/A | <div><p>Multiple Attempts - None Passed Part 2</p><img src="https://github.com/JasonSteving99/agent-of-code/blob/main/images/day6_workflow_1_part2failure.png?raw=true" width="500" height="100"><img src="https://github.com/JasonSteving99/agent-of-code/blob/main/images/day6_workflow_2_part1failure.png?raw=true" width="500" height="100"><img src="https://github.com/JasonSteving99/agent-of-code/blob/main/images/day6_workflow_3_part2failure.png?raw=true" width="500" height="100"></div> |

<img src="https://raw.githubusercontent.com/JasonSteving99/agent-of-code/refs/heads/main/images/aoc_stars.png" alt="Advent of Code - Stars" height="600">
