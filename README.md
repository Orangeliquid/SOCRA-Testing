# SOCRA Testing 

SOCRA Testing is a Streamlit front-end application that allows users to practice multiple choice questions similar to those found on the Society of Clinical Research Associates (SOCRA) certification. The app offers tests of varying lengths: 5, 10, 15, 20, 30, or 50 questions.

After each question, the application immediately evaluates the answer and tracks statistics such as the total questions answered and total correct answers. Once the test is completed, users can review each question, see whether they answered it correctly or incorrectly, and view the correct answer. These statistics, along with detailed information about the SOCRA certification, are displayed on the landing page.

In addition to the front-end UI, the project includes backend logic for scraping, parsing, cleaning, and storing question, option, and answer data in a database.


## Table of Contents

- [Installation](#installation)
- [Getting-Started](#getting-started)
- [Screenshots](#screenshots)
  - [Landing-Page](#landing-page)
  - [Choose-Your-Path](#choose-your-path)
  - [Tests](#tests)
  - [Review](#review)
  - [Overall-Stats](#overall-stats)
- [License](#license)

## Installation

To run Socra Testing, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Orangeliquid/SOCRA-Testing
   cd SOCRA-Testing
   ```

2. Ensure UV is downloaded:
   - If UV is not downloaded on your system, download it via pip:
   ```bash
   pip install uv
   ```
   
3. Sync dependencies with UV:
   ```bash
   uv sync
   ```


## Getting Started

1. Navigate to SOCRA-Testing and open main.py
   - At the bottom under __main__ remove pass line.
   - uncomment steps 1 and 2
   - in terminal run:
      ```bash
      uv run main.py
      ```

3. Verify that Socra_Testing.db exists at Socra-Testing/Socra_Testing.db
   - Now the database is created and populated with 166 question/option/answers

5. Start the application via terminal:
   ```bash
   uv run streamlit run streamlit_app.py
   ```
   
6. Look around the landing page, data includes:
   - SOCRA Overview
   - Overall Stats
   - "Choose Your Path" button

7. Select "Choose Your Path"
   - Six buttons with be displayed, each name indicating the number of multiple choice questions within each test.
   - Fast Five
   - Power Ten
   - Funky Fifteen
   - Plenty Twenty
   - Sturdy Thirty
   - Nifty Fifty

8. Chose a test and try your best!

9. Review the end results of your test

10. Press 'Exit' button to return to the main menu

11. Take a look at Overall Stats
   - These stats will persist after each question answered and will load when the application is ran again.
   - Reset Stats button will set Total Correct Answers, Total Questions Answered, and Correct Percentage back to 0.

## Screenshots

### Landing Page
<img width="1168" height="811" alt="Socra_Landing" src="https://github.com/user-attachments/assets/50159d3a-5a6a-4e47-97dc-11807542aa87" />

### Choose Your Path
<img width="1067" height="627" alt="SOCRA_Choose" src="https://github.com/user-attachments/assets/686cfc38-7b79-4ec5-a423-7e85f1fc5356" />

### Tests
<img width="1086" height="767" alt="Socra_Test_FF" src="https://github.com/user-attachments/assets/4ca8943d-867d-47db-b554-0c994f7ef928" />
<img width="1091" height="750" alt="Socra_Test_PT" src="https://github.com/user-attachments/assets/268fa495-040a-4c61-9e71-04c45447934a" />
<img width="1053" height="769" alt="Socra_Test_FunkyF" src="https://github.com/user-attachments/assets/3f1238f8-e749-487f-9072-691be458fb51" />
<img width="1065" height="790" alt="Socra_Test_PlentyT" src="https://github.com/user-attachments/assets/24f8afeb-291a-4c33-95d2-b466551d2988" />
<img width="1015" height="783" alt="Socra_Test_ST" src="https://github.com/user-attachments/assets/b9e6b708-8443-434e-ab22-a0bfd7a836d4" />
<img width="1083" height="776" alt="Socra_Test_NF" src="https://github.com/user-attachments/assets/d3b3fdeb-2d7a-4a6c-ad7a-fbaac26a676a" />

### Review
<img width="917" height="824" alt="Socra_Results" src="https://github.com/user-attachments/assets/48220167-fc48-4603-8e8d-167037624429" />

### Overall Stats
<img width="1067" height="818" alt="Socra_Overall_Stats" src="https://github.com/user-attachments/assets/0d944aec-19e8-4f2c-ac10-1656e25a6e3a" />

## License

This project is licensed under the [MIT License](LICENSE.txt).

