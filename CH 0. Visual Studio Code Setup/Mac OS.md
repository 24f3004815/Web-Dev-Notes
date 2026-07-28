# 🚀 Complete Visual Studio Code Setup Guide for macOS (Apple Silicon & Intel)

Welcome to the definitive, senior-developer guide for installing, configuring, and optimizing **Visual Studio Code (VS Code)** on **macOS** (compatible with Apple Silicon M1/M2/M3/M4 & Intel Macs).

Whether you are building iOS/macOS apps, full-stack web platforms, or cloud-native microservices, this guide equips you with an elite engineering environment on macOS.

---

## 📊 macOS System Architecture & Workflow

Below is an overview of how VS Code integrates with macOS native subsystems, Homebrew, terminals, and toolchains:

```
+-----------------------------------------------------------------------------------+
|                                  macOS HOST OS                                    |
|  +-----------------------------------------------------------------------------+  |
|  |                            NATIVE GRAPHICS (METAL)                          |  |
|  |                                                                             |  |
|  |  +-----------------------------------------------------------------------+  |  |
|  |  |                         VISUAL STUDIO CODE                            |  |  |
|  |  |  +-----------------------+ +---------------------+ +-----------------+  |  |  |
|  |  |  |   UI / EDITOR CORE    | | EXTENSION MARKETPLACE| | INTEGRATED      |  |  |  |
|  |  |  (Themes, Keybindings) | | (Swift, Python, Go) | | TERMINAL      |  |  |  |
|  |  |  +-----------+-----------+ +----------+----------+ | (zsh / bash)    |  |  |  |
|  |  +--------------|------------------------|------------+--------+--------+  |  |
|  +-----------------|------------------------|---------------------|------------+  |
|                    |                        |                     |               |
|                    v                        v                     v               |
|  +-----------------------------------------------------------------------------+  |
|  |                       HOMEBREW & macOS TOOLCHAINS                           |  |
|  |  +------------------+     +--------------------+     +------------------+   |  |
|  |  | Git / Apple Clang|     | Xcode Command Line |     | Homebrew / Node  |   |  |
|  |  |   (Xcode SDK)    |     |   Tools (xcode-select)|   |    / Python      |   |  |
|  |  +------------------+     +--------------------+     +------------------+   |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  |                        CONTAINER & REMOTE WORKFLOWS                         |  |
|  |               [OrbStack / Docker Desktop / Remote SSH / Podman]             |  |
|  +-----------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------------+
```

---

## 📥 Step 1: Installing VS Code on macOS

You can install VS Code using either **Homebrew (Recommended)** or the direct **GUI Installer**.

### Option A: Homebrew Cask (Fastest & Standard Developer Workflow)
If you have [Homebrew](https://brew.sh) installed, run the following command in Terminal (`⌘ + Space` -> type `Terminal`):

```bash
# Install VS Code via Homebrew Cask
brew install --cask visual-studio-code
```

---

### Option B: Direct GUI Installation
1. Open Safari or Chrome and navigate to: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click **Download for Mac (Universal / Apple Silicon)**.
3. Open your **Downloads** folder and locate `VSCode-darwin-universal.zip`.
4. Double-click to unzip it and drag **Visual Studio Code.app** into your **`Applications`** folder.

```
+---------------------------------------------------------------------------+
| Finder: Applications                                                      |
|---------------------------------------------------------------------------|
|                                                                           |
|   [ 📂 Downloads ] ----------> [ 📂 Applications ]                        |
|   Visual Studio Code.app       Drag & Drop into Applications              |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

## ⚙️ Step 2: Enabling the `code` CLI Command in macOS Terminal

To open projects directly from macOS Terminal, iTerm2, or Warp using `code .`:

1. Launch **Visual Studio Code**.
2. Open the Command Palette: **`Cmd (⌘) + Shift + P`**
3. Type: `Shell Command: Install 'code' command in PATH`
4. Press **Enter** and enter your Mac system password when prompted.

```
+---------------------------------------------------------------------------+
| Command Palette                                                           |
| > Shell Command: Install 'code' command in PATH                           |
|---------------------------------------------------------------------------|
| Shell Command: Install 'code' command in PATH  (Successfully Installed)   |
+---------------------------------------------------------------------------+
```

Verify in Terminal:
```bash
# Open current folder in VS Code
code .
```

---

## 🎨 Step 3: UI Overview & Customization

```
+--+------------------------------------------------------------------------+
|🔴| Code  File  Edit  Selection  View  Go  Run  Terminal  Window  Help     |
+--+------------------------------------------------------------------------+
|  |                                                                        |
|  |  Visual Studio Code (macOS Edition)                                    |
|🔍|  Editing evolved                                                       |
|  |                                                                        |
|🌿|  Start                                  Recent                         |
|  |  📄 New File...                         📂 ~/Developer/mac-app         |
|▶️|  📂 Open File...                        📂 ~/.config                    |
|  |  📁 Open Folder...                                                     |
|🧩|                                                                        |
|  |  Walkthroughs                                                          |
|  |  ⚡ Get Started with VS Code                                           |
|⚙️|  🍎 Xcode Command Line Tools Setup                                     |
+--+------------------------------------------------------------------------+
```

---

## 🧩 Step 4: Essential Extensions for macOS Developers

Install extensions via terminal or GUI (`⌘ + Shift + X`):

```bash
code --install-extension esbenp.prettier-vscode
code --install-extension eamodio.gitlens
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode-remote.remote-ssh
code --install-extension pkief.material-icon-theme
```

### Recommended Extension Suite

| Extension | Publisher | Key Feature |
| :--- | :--- | :--- |
| **Prettier** | Esben Petersen | Code formatting on save |
| **GitLens** | GitKraken | Inline Git blame, branch graph, and history |
| **Xcode / Swift** | Swift Server Workgroup | IntelliSense and build tools for Swift development |
| **Docker / OrbStack** | Microsoft | Container management & status monitoring |
| **Error Lens** | Alexander | Highlighting errors inline in code lines |

---

## ⚙️ Step 5: Master macOS Developer Settings (`settings.json`)

1. Open Command Palette: **`Cmd (⌘) + Shift + P`**
2. Type **`Preferences: Open User Settings (JSON)`** and press **Enter**.
3. macOS Config File Path: `~/Library/Application Support/Code/User/settings.json`

Paste the following optimized configuration:

```json
{
  "editor.fontSize": 14,
  "editor.fontFamily": "'Fira Code', 'Menlo', 'Monaco', 'SF Mono', monospace",
  "editor.fontLigatures": true,
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.wordWrap": "on",
  "editor.minimap.enabled": false,
  "editor.formatOnSave": true,
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": true,
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "files.trimTrailingWhitespace": true,
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.fontFamily": "Menlo",
  "workbench.iconTheme": "material-icon-theme",
  "workbench.colorTheme": "Default Dark Modern",
  "window.nativeTabs": true,
  "window.titleBarStyle": "custom"
}
```

---

## ⌨️ Step 6: macOS Keybindings Cheat Sheet

| Action | macOS Shortcut | Description |
| :--- | :--- | :--- |
| **Command Palette** | `⌘ + Shift + P` | Access all VS Code commands |
| **Quick Open File** | `⌘ + P` | Fast file navigation |
| **Integrated Terminal** | `Ctrl + \`` or `⌘ + \`` | Toggle built-in terminal (`zsh`) |
| **Duplicate Line** | `Option + Shift + Down/Up` | Duplicate current line |
| **Move Line** | `Option + Down/Up` | Move line position up/down |
| **Toggle Comment** | `⌘ + /` | Comment out current line or selection |
| **Format Document** | `Option + Shift + F` | Trigger code formatting |
| **Multi-Cursor Selection**| `Option + Click` | Place multiple cursor points |

---

## 🛠️ Step 7: Toolchain & Xcode Developer Setup Verification

Before running code, ensure Apple Xcode Command Line Tools and Homebrew tools are properly linked:

```bash
# 1. Install Xcode Command Line Tools (Required for GCC, Clang, Git, Make)
xcode-select --install

# 2. Check installed runtime tools in VS Code Terminal
git --version
python3 --version
swift --version
brew --version
```

```
+---------------------------------------------------------------------------+
| TERMINAL                                                                  |
|---------------------------------------------------------------------------|
| macbook-pro:~$ xcode-select -p                                            |
| /Library/Developer/CommandLineTools                                       |
| macbook-pro:~$ git --version                                              |
| git version 2.39.5 (Apple Git-154)                                        |
| macbook-pro:~$ swift --version                                            |
| Apple Swift version 5.10 (swiftlang-5.10.0.13)                            |
| macbook-pro:~$ _                                                          |
+---------------------------------------------------------------------------+
```

🎉 **Congratulations!** Your macOS Visual Studio Code environment is fully installed and tuned for peak performance!