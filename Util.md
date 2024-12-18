Here’s the step-by-step guide formatted in Markdown:

```markdown
# How to Create a Virtual Environment in Django

## 1. Install Python
- Ensure Python is installed on your system. Check the version by running:
  ```bash
  python --version
  ```
  or
  ```bash
  python3 --version
  ```

- If Python is not installed, download it from [python.org](https://www.python.org/).

---

## 2. Install `virtualenv` (if not already installed)
- Install the `virtualenv` package globally by running:
  ```bash
  pip install virtualenv
  ```

---

## 3. Create a Virtual Environment
- Navigate to your Django project directory:
  ```bash
  cd path/to/your/project
  ```

- Create the virtual environment:
  ```bash
  python -m venv venv
  ```
  Replace `venv` with your desired folder name for the virtual environment.

---

## 4. Activate the Virtual Environment
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

- After activation, your terminal prompt will change to include the virtual environment name, e.g., `(venv)`.

---

## 5. Install Django and Other Dependencies
- Once the virtual environment is activated, install Django:
  ```bash
  pip install django
  ```

- Save the installed dependencies to a `requirements.txt` file (optional):
  ```bash
  pip freeze > requirements.txt
  ```

---

## 6. Deactivate the Virtual Environment
- To exit the virtual environment, run:
  ```bash
  deactivate
  ```

---

## Notes
- To recreate the virtual environment later, use the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

- Always activate the virtual environment before running Django commands to ensure proper environment isolation.
```