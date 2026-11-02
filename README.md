# Library Management System

A Python-based Library Management System developed with Git version control, automated CI/CD pipeline via GitHub Actions, containerization using Docker, and automated unit testing.

---

## 1. Project Structure

```text
library-management-system/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD Workflow
├── .gitignore                 # Git ignore file
├── Dockerfile                 # Docker containerization file
├── library.py                 # Core Library Management System application
├── requirements.txt           # Python project dependencies
├── test_library.py            # Automated unit tests
└── README.md                  # Project documentation
```

---

## 2. Part A: Version Control using Git

### Step-by-Step Commands Executed:

1. **Initialize Git Repository and set main branch:**
   ```bash
   git init -b main
   ```

2. **Add initial files and make the root commit:**
   ```bash
   git add .
   git commit -m "Initial commit: Library Management System core module, Dockerfile, and CI workflow"
   ```

3. **Create and switch to `feature/book-search` branch:**
   ```bash
   git checkout -b feature/book-search
   ```

4. **Modify Python file (`library.py`) to add search features and update tests:**
   - Added `search_by_title(keyword)`
   - Added `search_by_author(author_name)`
   - Added search test cases in `test_library.py`

5. **Stage and commit the changes:**
   ```bash
   git add library.py test_library.py
   git commit -m "feat: Add book search functionality by title and author"
   ```

6. **Switch back to `main` branch and merge the feature branch:**
   ```bash
   git checkout main
   git merge --no-ff feature/book-search -m "Merge branch 'feature/book-search' into main"
   ```

7. **Display commit history:**
   ```bash
   git log --graph --oneline --all --decorate
   ```

---

## 3. Part B: CI/CD using GitHub Actions

The workflow file is located at `.github/workflows/ci.yml`.

### Key Features of the Workflow:
- **Trigger**: Automatically executes on every `push` to the `main` branch.
- **Environment**: Runs on `ubuntu-latest` with Python 3.10.
- **Dependency Installation**: Upgrades `pip` and installs dependencies specified in `requirements.txt`.
- **Application Execution**: Runs `python library.py`.
- **Automated Testing**: Executes unit tests via `python -m unittest test_library.py`.
- **Execution Status Display**: Always outputs a status summary report displaying `job.status`, commit SHA, branch, and trigger event.

---

## 4. Containerization (Docker)

### Build the Docker Image:
```bash
docker build -t library-management-system:latest .
```

### Run the Docker Container:
```bash
docker run --rm library-management-system:latest
```

---

## 5. Automated Testing

### Run Tests locally:
```bash
python -m unittest test_library.py
```
Or using pytest:
```bash
pytest test_library.py
```
