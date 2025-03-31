import json
from word_morph.generate_word_graph import find_one_edit_words, generate_word_graph

def test_with_small_wordlist():
    """Test the word graph generation with a small word list."""
    # Small test word list
    test_words = [
        "cat", "bat", "hat", "rat", "mat", "sat",
        "car", "bar", "far", "tar", "mar", "par",
        "can", "ban", "fan", "man", "pan", "ran",
        "cap", "map", "lap", "tap", "gap", "nap",
        "at", "it", "to", "do", "go", "no",
        "cats", "bats", "hats", "rats", "mats"
    ]
    
    word_set = set(test_words)
    
    # Test find_one_edit_words function
    print("Testing find_one_edit_words function:")
    test_cases = ["cat", "at", "cats"]
    for word in test_cases:
        connections = find_one_edit_words(word, word_set)
        print(f"{word}: {connections}")
    
    # Test generate_word_graph function
    print("\nTesting generate_word_graph function:")
    word_graph = generate_word_graph(test_words)
    
    # Print the entire graph for inspection
    print("\nGenerated word graph:")
    for word, connections in sorted(word_graph.items()):
        print(f"{word}: {connections}")
    
    # Save the test graph to a file
    with open("test_word_graph.json", "w") as f:
        json.dump(word_graph, f, indent=2)
    
    print("\nTest word graph saved to test_word_graph.json")

if __name__ == "__main__":
    test_with_small_wordlist() 