STX STIXX Softball Player Performance Analysis

Created by: Andrea Cadena

Project Purpose

The purpose of my project is to use Python to analyze softball player statistics. I chose this topic because I am involved with the STX STIXX softball organization and wanted to work with a dataset that relates to my personal interests.

For this project, I used my cleaned dataset from the previous assignment. The dataset contains 50 fictional player records from five different STX STIXX teams.

Software and Libraries

- Python 3.13
- Python IDLE
- Pandas
- Matplotlib
- Windows Command Prompt
Programming Techniques

I used Pandas to read my cleaned CSV file, group the data by team, calculate total hits and batting averages, and sort individual batting records.

I used Matplotlib to create three bar graphs that make the results easier to understand and compare.

How to Run the Program

1. Install Python 3.13.
2. Download the project files.
3. Open Command Prompt.
4. Install the required libraries using:

   `python -m pip install pandas matplotlib`

5. Navigate to the project folder.
6. Run the program using:

   `python softball_analysis.py`

The program will display the calculated statistics and automatically save three graphs as PNG files.



 Graph 1: Total Hits by Team

This graph compares the total number of hits for each team. STX STIXX 12U Ruby had the most hits with 226, followed by STX STIXX 2033 with 209.



Graph 2: Batting Average by Team

This graph compares the overall batting averages of the five teams. STX STIXX 12U Ruby had the highest batting average of .587. I calculated each team's batting average by dividing its total hits by its total at-bats.


Graph 3: Top 10 Individual Batting Records

This graph displays the ten highest individual batting records in my dataset. Lila Collins from STX STIXX Vera had the highest recorded batting average of .947. Player IDs are included to distinguish records with the same player name.


Conclusion

This project helped me understand how Python can be used to analyze data and create visualizations. Instead of manually calculating statistics, I was able to write a program that completed the calculations and created graphs automatically.

I also learned how Pandas and Matplotlib can work together to turn a cleaned dataset into useful information. Although the player statistics are fictional, this program could be used with actual softball statistics in the future to help coaches compare batting performance.
