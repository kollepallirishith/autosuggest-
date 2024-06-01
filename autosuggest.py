import tkinter as tk
from tkinter import messagebox


class TrieNode:
    def __init__(self):
        self.trie = [None] * 256
        self.isEnd = False


class AutoCorrectGUI:
    def __init__(self):
        self.root_node = TrieNode()
        self.modified_sentence = ""

        self.root = tk.Tk()
        self.root.title("Auto Correct")

        self.create_widgets()

        self.load_dictionary()

    def create_widgets(self):
        input_label = tk.Label(self.root, text="Enter a sentence:")
        input_label.pack()
        self.input_entry = tk.Entry(
            self.root,
            width=40,
            font=("Arial", 12)
        )
        self.input_entry.pack(pady=10, padx=10)

        modify_button = tk.Button(self.root, text="Modify", command=self.modify_sentence)
        modify_button.pack()

        self.output_label = tk.Label(self.root, text="Modified sentence:")
        self.output_label.pack()

    def load_dictionary(self):
        try:
            with open('dict.txt', 'r') as file:
                dictionary = [line.strip() for line in file]
                for word in dictionary:
                    self.insert_word(word)
        except FileNotFoundError:
            messagebox.showerror("Error", "Dictionary file not found.")

    def insert_word(self, word):
        temp = self.root_node
        for char in word:
            if not temp.trie[ord(char)]:
                temp.trie[ord(char)] = TrieNode()
            temp = temp.trie[ord(char)]

        temp.isEnd = True

    def print_suggestions(self, root, res):
        suggestions = []
        if root.isEnd:
            suggestions.append(res)
        for i in range(256):
            if root.trie[i]:
                res_list = list(res)
                res_list.append(chr(i))
                suggestions += self.print_suggestions(root.trie[i], "".join(res_list))
        return suggestions

    def check_present(self, root, key):
        for i in range(len(key)):
            if not root.trie[ord(key[i])]:
                suggestions = self.print_suggestions(root, key[:i])
                return suggestions

            root = root.trie[ord(key[i])]
        if root.isEnd:
            return True
        suggestions = self.print_suggestions(root, key)
        return suggestions

    def modify_sentence(self):
        sentence = self.input_entry.get()
        words = sentence.split()
        modified_sentence = []

        for word in words:
            word = word.lower()
            suggestions = self.check_present(self.root_node, word)
            if suggestions is not True:
                suggestion_idx = self.show_suggestions(suggestions, word)
                if suggestion_idx == 0:
                    

modified_sentence.append(word)
                else:
                    suggestion_idx -= 1
                    if suggestion_idx < len(suggestions):
                        modified_sentence.append(suggestions[suggestion_idx])
                    else:
                        modified_sentence.append(word)
            else:
                modified_sentence.append(word)

        self.modified_sentence = " ".join(modified_sentence)
        self.output_label.config(text="Modified sentence: " + self.modified_sentence)
        self.input_entry.delete(0, tk.END)
        self.write_to_file()


    def show_suggestions(self, suggestions, word):
        suggestion_window = tk.Toplevel(self.root)
        suggestion_window.title("Suggestions")
        packer = tk.Label(suggestion_window, text="Choose the word to replace "+ word+ " with")
        packer.pack()

        suggestion_var = tk.IntVar()
        suggestion_var.set(0)

        for idx, suggestion in enumerate(suggestions):
            suggestion_button = tk.Radiobutton(
                suggestion_window,
                text=suggestion,
                variable=suggestion_var,

                value=idx + 1
            )
            suggestion_button.pack(anchor="w")

        submit_button = tk.Button(
            suggestion_window,
            text="Submit",
            command=lambda: self.submit_suggestion(suggestion_var, suggestion_window)
        )
        submit_button.pack()

        suggestion_window.wait_window()
        return suggestion_var.get()

    def submit_suggestion(self, suggestion_var, suggestion_window):
        suggestion_window.destroy()

    def write_to_file(self):
        try:
            with open('output.txt', 'a') as file:
                file.write(self.modified_sentence + "\n")
            messagebox.showinfo("Success", "Modified sentence appended to 'output.txt'.")
        except:
            messagebox.showerror("Error", "Failed to write to file.")


app = AutoCorrectGUI()
app.root.mainloop()
