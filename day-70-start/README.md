## Day 70 - Mastering Git & GitHub 🚀

### Overview  
Today, I dedicated my time to mastering **Git** and **GitHub**. I focused on understanding how to use Git both locally and remotely, exploring its capabilities, and practicing essential Git commands. This knowledge is crucial for efficient version control and collaboration in software development.

---

### 📌 What I Learned  

#### 1️⃣ **Understanding Git & GitHub**  
- **Git** is a distributed version control system that helps track changes in code efficiently.  
- **GitHub** is a cloud-based platform that hosts repositories, enabling collaboration and remote code management.  
- Git works locally, while GitHub extends its capabilities for team collaboration and remote storage.  

#### 2️⃣ **Setting Up & Configuring Git**  
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --list  # Verify configuration
```

#### 3️⃣ **Basic Git Commands**  
| Command | Description |
|---------|-------------|
| `git init` | Initialize a new Git repository |
| `git clone <repo-url>` | Clone an existing repository from GitHub |
| `git status` | Check the current status of the working directory |
| `git add <file>` | Stage a file for commit |
| `git commit -m "Commit message"` | Save changes with a descriptive message |
| `git log` | View commit history |
| `git diff` | Show changes between commits |
| `git reset <file>` | Unstage a file from staging area |
| `git rm <file>` | Remove a file from the repository |

#### 4️⃣ **Working with Branches**  
```bash
git branch <branch-name>  # Create a new branch
git checkout <branch-name>  # Switch to another branch
git merge <branch-name>  # Merge a branch into the current branch
git branch -d <branch-name>  # Delete a branch
```

#### 5️⃣ **Pushing & Pulling to GitHub**  
```bash
git remote add origin <repo-url>  # Connect local repo to GitHub
git push origin <branch-name>  # Push changes to GitHub
git pull origin <branch-name>  # Pull updates from GitHub
git fetch  # Get latest updates without merging
```

#### 6️⃣ **Handling Merge Conflicts**  
- Use `git status` to check conflicting files.  
- Open the files and manually resolve conflicts.  
- After fixing, stage the file using `git add <file>` and commit changes.  

#### 7️⃣ **Undoing Changes**  
| Action | Command |
|---------|-------------|
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Undo last commit (discard changes) | `git reset --hard HEAD~1` |
| Revert a specific commit | `git revert <commit-hash>` |

#### 8️⃣ **Git Ignore & Best Practices**  
- Use `.gitignore` to prevent unnecessary files from being tracked.  
- Keep commit messages clear and concise.  
- Use branches for new features or bug fixes before merging into `main`.  
- Regularly push changes to prevent data loss.  

---

### 🔥 Key Takeaways  
✅ Git is an essential tool for version control and collaboration.  
✅ Mastering Git commands improves productivity and workflow efficiency.  
✅ Understanding GitHub’s remote capabilities enhances teamwork.  
✅ Always commit frequently and use clear commit messages.  
✅ Handling merge conflicts is a crucial skill for smooth collaboration.  
