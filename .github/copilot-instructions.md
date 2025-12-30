# Copilot Instructions for Python Learning Workspace

## Project Overview
This is a personal Python learning repository containing individual exercise scripts for practicing programming concepts. Each file is a standalone command-line application focusing on basic Python features like loops, conditionals, data structures, and input validation.

## Architecture & Patterns
- **Standalone Scripts**: No interconnected components; each `.py` file is independent
- **Entry Point**: Use `if __name__ == "__main__":` to call the main function (e.g., `calcul .py`, `worky.py`)
- **Menu-Driven Interfaces**: Common pattern with `while True` loops for user choices (see `calcul .py` lines 3-5, `joe liste` lines 10-12)
- **Input Validation**: Wrap `int(input())` in `try-except ValueError` for robust number parsing (see `worky.py` lines 8-12, `password_enter` lines 6-7)
- **Data Structures**: Practice with lists, dicts, and basic operations (see `les_boucles_for_while_et_autre _graven` for dict/list examples)

## Developer Workflows
- **Running Scripts**: Execute with `python "filename.py"` (use quotes for spaces in filenames)
- **No Build Process**: Direct Python execution; no compilation or packaging
- **Manual Testing**: Run scripts interactively to verify behavior; no automated tests
- **Debugging**: Use `print()` statements for variable inspection (common in exercises like `revision`)

## Conventions
- **Naming**: Mixed French/English; function names like `operations()`, `verification()`
- **Error Handling**: Basic `try-except` for input errors; `raise SystemExit` for invalid inputs (see `calculatrice openclassrooms` line 13)
- **Code Style**: Simple, imperative style with minimal functions; focus on learning syntax over structure

## Key Examples
- Calculator implementations: `calcul .py` (menu-based), `calculatrice openclassrooms` (operation selection)
- List/dict manipulation: `joe liste` (append/remove/insert), `les_boucles_for_while_et_autre _graven` (for loops with collections)
- Input validation: `password_enter` (retry logic), `worky.py` (age/name checks)

## Dependencies
- Standard Python library only; no external packages required
- Compatible with Python 3.x

Focus on writing clear, executable scripts that demonstrate specific concepts. Avoid over-engineering for learning exercises.</content>
<parameter name="filePath">c:\Users\TOSHIBA\Desktop\joe-python-work first-git -projet\.github\copilot-instructions.md