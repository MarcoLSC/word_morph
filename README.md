# Word Morph - Daily Word Puzzle

Transform words through a daily journey! Like Wordle, but with word transformations. Each day brings a new challenge where you transform words by changing one letter at a time.

## 🎮 How to Play

Every day you get three connected words:
```
HOUSE → MOUSE → MOOSE
```

Your goal: Complete both transformations in as few moves as possible!

1. **Click any letter** to select it
2. **Choose a new letter** from the keyboard
3. **Create valid words** with each change
4. **Complete the journey** with minimal moves

## 🌟 Features

- **Daily Challenges** - New puzzle every day at midnight
- **Progress Tracking** - See your moves and best scores
- **Beautiful UI** - Modern dark theme with smooth animations
- **Mobile Friendly** - Works perfectly on all devices
- **Offline Play** - No internet required after first load
- **Word Definitions** - Learn new words as you play

## 🏆 Game Modes

### Daily Challenge (Current)
Transform through a chain of 3 words with the fewest moves possible. Compare your score with friends!

### Classic Mode (Coming Soon)
Create endless word chains starting from any word. How long can you go?

## 🎯 Example

Starting word: **HOUSE**
1. HOUSE → MOUSE (change H to M)
2. MOUSE → MOOSE (change U to O)

Total moves: 2 (Perfect score!)

## 🚀 Play Online

Visit the game at: [Word Morph Game](https://marcolesci.github.io/word_morph/)

## 💻 Technical Details

- Pure HTML, CSS, and JavaScript - no frameworks
- Pre-computed word graph for instant validation
- Dictionary API for word definitions
- LocalStorage for progress saving
- Responsive design for all screen sizes

## 📁 Files

- `index.html` - The complete game
- `word_graph.json` - Pre-computed word connections
- `precomputed_words_aggregated.json` - Optimized word data
- `CROSSWD.TXT` - Source word list
- `generate_word_graph.py` - Tool to generate word connections

## 🛠️ Development

The word graph generation scripts create the data that powers the game's word validation system. They find all valid one-letter transformations between words in the dictionary.

## 🎨 Future Updates

- Social sharing
- Global leaderboards
- Achievement system
- Hint system
- Multiple difficulty levels
- Friend challenges

---

Inspired by Wordle and word ladder puzzles. Built with ❤️ for word game enthusiasts!
