# Word Morph Game

A modern word-morphing game where players transform words by changing one letter at a time. Start with "HOUSE" and create a chain of valid words!

## Game Modes

1. **Classic Mode**
   - Start with the word "HOUSE"
   - Create new words by changing one letter
   - Track your chain length
   - Progress is saved automatically

2. **Daily Challenge**
   - New challenge every day
   - Compete with others
   - Track your daily progress

## Features

- Real-time word validation
- Word definitions display
- Chain length tracking
- Duplicate word prevention
- Mobile-friendly design
- Dark theme with modern UI
- Smooth animations and transitions

## Technical Details

The game uses:
- Vanilla JavaScript for game logic
- Dictionary API for word validation
- LocalStorage for saving progress
- Modern CSS with variables and animations
- Responsive design for all devices

## Files

- `index.html`: Main game interface
- `word_graph.json`: Pre-computed word connections
- `CROSSWD.TXT`: Word list source
- `precomputed_words_aggregated.json`: Optimized word data

## Play Online

Visit the game at: [Word Morph Game](https://marcolesci.github.io/word_morph/)

## Development

The game is built with pure HTML, CSS, and JavaScript - no frameworks required. The word graph generation scripts (`generate_word_graph.py` and `test_word_graph.py`) are used to create the word connection data used by the game.
