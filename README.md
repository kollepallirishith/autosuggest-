

---

# AutoSuggest and Autocorrect

AutoCorrectGUI is a Python-based application that provides a user-friendly graphical interface for auto-correcting sentences using a trie data structure. The application suggests corrections for misspelled words based on a predefined dictionary, allowing users to select the best replacement or keep the original word. The corrected sentences can then be saved to a file.

## Features

- **Graphical User Interface (GUI):** Built with Tkinter, providing an easy-to-use interface for entering and modifying  sentences.
- **Trie Data Structure:** Efficiently stores and searches words from a dictionary.
- **Word Suggestions:** Provides suggestions for misspelled words and allows users to choose the correct word.
- **Persistent Storage:** Saves the modified sentences to a file for later reference.

## How It Works

1. **Loading Dictionary:** The application reads words from a file named `dict.txt` and stores them in a trie data structure.
2. **Entering a Sentence:** Users can input a sentence in the provided entry field.
3. **Modifying Sentence:** When the 'Modify' button is clicked, the application checks each word in the sentence against the dictionary.
4. **Word Suggestions:** If a word is not found, a suggestion window pops up, offering possible corrections. Users can select a suggestion or keep the original word.
5. **Saving Output:** The modified sentence is displayed and appended to a file named `output.txt`.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Usage

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/AutoCorrectGUI.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd AutoCorrectGUI
   ```
3. **Ensure you have a `dict.txt` file with a list of valid words, one per line.**
4. **Run the application:**
   ```sh
   python autocorrect_gui.py
   ```

## Project Structure
- `autosuggest.py`: Main application script.
- `dict.txt`: Dictionary file containing a list of valid words.
- `output.txt`: File where modified sentences are saved.

