import json
from collections import defaultdict
import time
import os

def load_words(file_path):
    """Load words from the given file."""
    with open(file_path, 'r') as f:
        return [word.strip().lower() for word in f if word.strip()]

def find_one_edit_words(word, word_set):
    """Find all words that can be formed by adding, removing, or changing one letter."""
    results = set()
    
    # Words formed by removing one letter
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in word_set:
            results.add(new_word)
    
    # Words formed by adding one letter
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(word) + 1):
        for char in alphabet:
            new_word = word[:i] + char + word[i:]
            if new_word in word_set and new_word != word:
                results.add(new_word)
    
    # Words formed by changing one letter
    for i in range(len(word)):
        for char in alphabet:
            if char != word[i]:
                new_word = word[:i] + char + word[i+1:]
                if new_word in word_set:
                    results.add(new_word)
    
    return list(results)

def generate_word_graph(words, batch_size=5000, save_interval=10000):
    """
    Generate a graph where each word maps to words that can be formed by one edit.
    
    Args:
        words: List of words to process
        batch_size: Number of words to process before saving intermediate results
        save_interval: How often to save progress (in number of words processed)
    """
    word_set = set(words)
    word_graph = {}
    
    # Check if we have a partial result to resume from
    temp_file = "word_graph_partial.json"
    start_index = 0
    
    if os.path.exists(temp_file):
        try:
            with open(temp_file, 'r') as f:
                word_graph = json.load(f)
                start_index = len(word_graph)
                print(f"Resuming from word {start_index}")
        except:
            print("Could not load partial results, starting from scratch")
    
    total_words = len(words)
    print(f"Processing {total_words} words...")
    
    start_time = time.time()
    last_save_time = start_time
    
    for i in range(start_index, total_words):
        word = words[i]
        
        if i % 1000 == 0:
            current_time = time.time()
            elapsed = current_time - start_time
            elapsed_since_save = current_time - last_save_time
            progress = (i / total_words) * 100
            
            # Calculate estimated time remaining
            if i > start_index:
                words_per_second = (i - start_index) / elapsed
                remaining_words = total_words - i
                eta_seconds = remaining_words / words_per_second if words_per_second > 0 else 0
                eta_minutes = eta_seconds / 60
                eta_hours = eta_minutes / 60
                
                if eta_hours >= 1:
                    eta_str = f"{eta_hours:.1f} hours"
                elif eta_minutes >= 1:
                    eta_str = f"{eta_minutes:.1f} minutes"
                else:
                    eta_str = f"{eta_seconds:.1f} seconds"
                
                print(f"Progress: {progress:.2f}% ({i}/{total_words}) - Time elapsed: {elapsed:.2f}s - ETA: {eta_str}")
            else:
                print(f"Progress: {progress:.2f}% ({i}/{total_words}) - Time elapsed: {elapsed:.2f}s")
        
        word_graph[word] = find_one_edit_words(word, word_set)
        
        # Save intermediate results periodically
        if (i % save_interval == 0 and i > start_index) or i == total_words - 1:
            with open(temp_file, 'w') as f:
                json.dump(word_graph, f)
            last_save_time = time.time()
            print(f"Saved intermediate results at word {i}")
    
    return word_graph

def main():
    input_file = "CROSSWD.TXT"
    output_file = "word_graph.json"
    
    print(f"Loading words from {input_file}...")
    words = load_words(input_file)
    print(f"Loaded {len(words)} words.")
    
    print("Generating word graph...")
    word_graph = generate_word_graph(words)
    
    print(f"Saving word graph to {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(word_graph, f)
    
    # Remove temporary file if it exists
    temp_file = "word_graph_partial.json"
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    print("Done!")
    
    # Print some statistics
    total_connections = sum(len(connections) for connections in word_graph.values())
    avg_connections = total_connections / len(word_graph) if word_graph else 0
    print(f"Total connections: {total_connections}")
    print(f"Average connections per word: {avg_connections:.2f}")
    
    # Print a few examples
    print("\nExample entries:")
    examples = list(word_graph.items())[:5]
    for word, connections in examples:
        print(f"{word}: {connections}")

if __name__ == "__main__":
    main() 