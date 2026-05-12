import re
def english_to_predicate(sentence):
    sentence = sentence.lower().strip()
    if sentence.startswith("all") or sentence.startswith("every"):
        parts = re.findall(r"(?:all|every)\s+(\w+)\s+are\s+(\w+)", sentence)
        if parts:
            subject, predicate = parts[0]
            return f"∀x ({subject}(x) → {predicate}(x))"
    elif sentence.startswith("some"):
        parts = re.findall(r"some\s+(\w+)\s+are\s+(\w+)", sentence)
        if parts:
            subject, predicate = parts[0]
            return f"∃x ({subject}(x) ∧ {predicate}(x))"
    elif sentence.startswith("no"):
        parts = re.findall(r"no\s+(\w+)\s+are\s+(\w+)", sentence)
        if parts:
            subject, predicate = parts[0]
            return f"¬∃x ({subject}(x) ∧ {predicate}(x))"
    return "Sorry, I couldn't translate that sentence. Try: 'All dogs are friendly'"
def predicate_to_english(expression):
    expression = expression.replace(" ", "")
    if "∀x" in expression:
        parts = re.findall(r"∀x\((\w+)\(x\)→(\w+)\(x\)\)", expression)
        if parts:
            subject, predicate = parts[0]
            return f"All {subject}s are {predicate}"
    elif "∃x" in expression and "¬" not in expression:
        parts = re.findall(r"∃x\((\w+)\(x\)∧(\w+)\(x\)\)", expression)
        if parts:
            subject, predicate = parts[0]
            return f"Some {subject}s are {predicate}"
    elif "¬∃x" in expression:
        parts = re.findall(r"¬∃x\((\w+)\(x\)∧(\w+)\(x\)\)", expression)
        if parts:
            subject, predicate = parts[0]
            return f"No {subject}s are {predicate}"
    return "Sorry, I couldn't translate that logic expression."
def main():
    print("English ↔ Predicate Logic Translator")
    print("Type 'e' to convert English to Logic")
    print("Type 'p' to convert Logic to English")
    choice = input("Your choice: ").lower().strip()
    if choice == 'e':
        sentence = input("Enter English sentence ('All dogs are friendly'): ")
        print("Result:", english_to_predicate(sentence))
    elif choice == 'p':
        print("Tip: Use symbols like ∀, ∃, →, ∧, ¬")
        expression = input("Enter Logic expression: ")
        print("Result:", predicate_to_english(expression))
    else:
        print("Invalid choice!")
if __name__ == "__main__":
    main()

    #∀x (human(x) → mortal(x))
    #∃x (student(x) ∧ smart(x))
