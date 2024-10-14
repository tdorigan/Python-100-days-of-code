# Quiz App - 100 Days of Python Code (Day 34)

A simple quiz app that fetches **True/False** questions from an API and presents them in a graphical interface. This project is part of the **100 Days of Python Code** course.

## Features

- Fetches 10 **True/False** questions from an API.
- Displays one question at a time.
- Tracks and displays the user's score.

## Requirements

- Python 3.9+
- `requests` library
- `tkinter` for GUI

## API

The quiz uses the [Open Trivia Database API](https://opentdb.com/api_config.php) to get **True/False** questions.

Example API URL:
```bash
https://opentdb.com/api.php?amount=10&type=boolean
