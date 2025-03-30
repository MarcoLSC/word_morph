# Word Graph Generator

This project generates a JSON file that maps each word to a list of words that can be formed by adding, removing, or changing one letter.

## Files

- `CROSSWD.TXT`: A list of words to process
- `generate_word_graph.py`: The main script to generate the word graph
- `test_word_graph.py`: A test script with a smaller word list to verify functionality
- `word_graph.json`: The output file containing the word graph

## How to Use

1. Make sure you have Python 3 installed
2. Run the script:
   ```
   python3 generate_word_graph.py
   ```
3. The script will:
   - Load words from `CROSSWD.TXT`
   - Generate a graph where each word maps to words that can be formed by one edit
   - Save the result to `word_graph.json`

## Features

- **Resume capability**: If the script is interrupted, it can resume from where it left off
- **Progress tracking**: Shows progress percentage, elapsed time, and estimated time remaining
- **Intermediate saves**: Periodically saves intermediate results to avoid losing progress

## Word Transformations

The script finds words that can be formed by:
1. **Adding one letter**: e.g., "cat" → "chat", "coat", "cart"
2. **Removing one letter**: e.g., "cats" → "cat"
3. **Changing one letter**: e.g., "cat" → "bat", "rat", "cap"

## Example Output

The output JSON file has the following format:

```json
{
  "cat": ["at", "bat", "cap", "car", "hat", "mat", "rat", "sat"],
  "bat": ["at", "bar", "cat", "hat", "mat", "rat", "sat"],
  ...
}
```

## Performance

Processing the entire word list may take some time due to the large number of words and possible transformations. The script includes optimizations to make it as efficient as possible.

## Use Cases

This word graph can be used for:
- Word games like Word Morph
- Spell checkers
- Word suggestion systems
- Natural language processing applications 