# gym-camelup

The camel up env aims to enumerate the broad game [camel up!](https://boardgamegeek.com/boardgame/153938/camel), which is a balanced, turn based, multiagent domain, with only limited unknown infomation.

To get started, check [openAI gym](https://github.com/openai/gy)

## camelup env

This env supposed to work exactly as the original boardgame, for two-player game, rewards +1 for a winning and -1 for a losing and for players more than two, rewards follows ```player_num // 2 - rank``` where ```rank``` indicates the rank of the coins at the end of each game.

## Installation

```
cd gym-soccer
pip install -e . // just follow the official, not tested.
```