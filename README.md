# 🌳 tree-menu-project - Create Seamless Navigation Menus

## 🚀 Getting Started

Welcome to tree-menu-project! This application helps you create and manage tree menus. It's perfect for websites that need multi-level navigation and want to keep database use low. Follow these steps to download and run the application.

## 🔗 Download

[![Download](https://img.shields.io/badge/Download%20Latest%20Release-blue.svg)](https://github.com/renaldyazis/tree-menu-project/releases)

## 📦 Requirements

Before you download, make sure your computer meets these requirements:

- **Operating System:** Windows, macOS, or Linux
- **Python Version:** Python 3.6 or higher
- **Database:** SQLite (for local use) or PostgreSQL (for production)
- **Docker:** Must be installed for easy deployment

## 🔽 Download & Install

To download tree-menu-project, please visit this page to download: [Releases Page](https://github.com/renaldyazis/tree-menu-project/releases).

### Step-by-Step Installation

1. **Visit the Releases Page:** Click this link to go to our [Releases Page](https://github.com/renaldyazis/tree-menu-project/releases).
  
2. **Download the Latest Version:** On the Releases Page, look for the latest version. You will find several files. Click the one that says `tree-menu-project.zip` or similar.

3. **Extract the Files:** After downloading, find the zipped file in your Downloads folder. Right-click on it and choose "Extract All" to unpack the files.

4. **Open a Terminal or Command Prompt:**
   - **Windows:** Press `Win + R`, type `cmd`, and hit `Enter`.
   - **macOS:** Open `Terminal` from Launchpad.
   - **Linux:** Open your preferred terminal application.

5. **Navigate to the Project Folder:** Type `cd path_to_download_folder/tree-menu-project` (replace `path_to_download_folder` with your actual folder path) and press `Enter`.

6. **Install Dependencies:**
   Run the following command to install the necessary packages:
   ```
   pip install -r requirements.txt
   ```

### 🛠 Running the Application

1. **Set Up Database:**
   You can use SQLite for local testing. If you're using PostgreSQL for production:
   - Ensure PostgreSQL is set up.
   - Update `settings.py` in the project folder with your database information.

2. **Run the Server:**
   After installing dependencies and setting up the database, run the command:
   ```
   python manage.py runserver
   ```

3. **Access the Application:**
   Open a web browser and type `http://127.0.0.1:8000` to see your application in action.

## 📄 Features

- **User-Friendly Interface:** No programming skills needed to manage your menus.
- **Multi-Level Navigation:** Ideal for complex site structures.
- **Lightweight:** Minimal database use ensures fast performance.
- **Responsive Design:** Works well on mobile and desktop devices.

## 🛠 Technologies Used

- **Backend Framework:** Django
- **Frontend Framework:** Bootstrap 5
- **Testing:** Django Test Framework
- **Containerization:** Docker
- **Continuous Integration:** GitHub Actions
- **Web Server:** Gunicorn
- **Database Options:** PostgreSQL & SQLite
- **Static File Handling:** Whitenoise

## 🤝 Contributing

We welcome contributions to improve this project. If you want to help, please fork the repository and create a pull request. We appreciate every effort to enhance the software.

## 📞 Support

If you encounter issues or need help, you can reach out through GitHub issues on the repository page. 

Thank you for using tree-menu-project! We hope you enjoy managing your tree menus effortlessly.