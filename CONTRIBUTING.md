# Contributing to StrumSense 🎸

Thank you for your interest in contributing to **StrumSense**! This guide outlines our workflow, branch conventions, and quality standards for our submission to **Build with भारत 2.0**.

---

## 🧭 Code of Conduct

We are committed to providing a welcoming, inclusive, and collaborative environment. Please be respectful and constructive in all discussions, pull requests, and code reviews.

---

## 🛠️ Development Workflow

1. **Fork or Branch**:
   Create a descriptive branch for your work:
   ```bash
   git checkout -b feature/audio-chroma-template
   # or
   git checkout -b fix/stream-synchronization
   ```

2. **Set Up Local Environment**:
   ```bash
   python -m venv venv
   # Activate virtualenv (Windows)
   venv\Scripts\activate
   # Activate virtualenv (macOS/Linux)
   source venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Adhere to Code Standards**:
   - Write clear docstrings for public classes and methods.
   - Use Python type hints (`typing`).
   - Keep functions focused and modular.
   - Ensure imports are cleanly grouped.

4. **Verify Syntax**:
   Before committing, verify that your changes compile cleanly:
   ```bash
   python -m py_compile app.py audio/*.py vision/*.py fusion/*.py utils/*.py config/*.py
   ```

5. **Submit a Pull Request**:
   - Provide a concise summary of what your PR introduces or fixes.
   - Reference any related hackathon task checklist item.

---

## 🧪 Testing Guidelines

- Place unit tests for audio DSP algorithms or pose tracking utilities under the `tests/` directory.
- Avoid committing large raw `.wav` or video test recordings to version control (use lightweight reference samples under `models/` or keep heavy test assets in `.gitignore`).

---

## 📜 License

By contributing to StrumSense, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
