### Description of the Table

The table presents the match statistics for Arsenal Football Club during the 2024-2025 season. It includes various details about each match played, such as the date, time, competition, round, venue, result, goals for (GF), goals against (GA), opponent, expected goals (xG), expected goals against (xGA), possession percentage, attendance, captain, and formations used by both Arsenal and their opponents.

The data is organized in a tabular format with the following columns:

- **Date**: The date on which the match was played.
- **Time**: The time at which the match started.
- **Comp**: The competition in which the match took place (e.g., Premier League, Champions League, EFL Cup).
- **Round**: The specific round of the competition.
- **Day**: The day of the week the match was played.
- **Venue**: Indicates whether the match was played at home or away.
- **Result**: The outcome of the match (W for win, D for draw, L for loss).
- **GF**: Goals scored by Arsenal.
- **GA**: Goals conceded by Arsenal.
- **Opponent**: The team that Arsenal played against.
- **xG**: Expected goals for Arsenal.
- **xGA**: Expected goals against Arsenal.
- **Poss**: Possession percentage during the match.
- **Attendance**: The number of spectators present at the match.
- **Captain**: The player who served as captain for Arsenal during the match.
- **Formation**: The formation used by Arsenal.
- **Opp Formation**: The formation used by the opposing team.

The table contains a total of 56 rows, with the first few rows showing the results of matches played in the early part of the season, while the latter rows include matches that are either ongoing or have not yet been played, indicated by NaN values in the results and other statistics.

### Table in Markdown Format

```markdown
| Date       | Time   | Comp             | Round            | Day | Venue | Result | GF | GA | Opponent          | xG  | xGA | Poss | Attendance | Captain           | Formation | Opp Formation |
|------------|--------|------------------|------------------|-----|-------|--------|----|----|-------------------|-----|-----|------|------------|--------------------|-----------|---------------|
| 2024-08-17 | 15:00  | Premier League    | Matchweek 1      | Sat | Home  | W      | 2  | 0  | Wolves            | 1.2 | 0.5 | 53.0 | 60261.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2024-08-24 | 17:30  | Premier League    | Matchweek 2      | Sat | Away  | W      | 2  | 0  | Aston Villa       | 0.9 | 1.2 | 60.0 | 41587.0    | Martin Ødegaard    | 4-3-3    | 4-4-2       |
| 2024-08-31 | 12:30  | Premier League    | Matchweek 3      | Sat | Home  | D      | 1  | 1  | Brighton          | 2.1 | 1.7 | 36.0 | 60326.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2024-09-15 | 14:00  | Premier League    | Matchweek 4      | Sun | Away  | W      | 1  | 0  | Tottenham         | 0.7 | 0.7 | 37.0 | 61645.0    | Jorginho           | 4-4-2    | 4-3-3       |
| 2024-09-19 | 21:00  | Champions Lg      | League phase      | Thu | Away  | D      | 0  | 0  | it Atalanta       | 0.8 | 1.2 | 46.0 | 22858.0    | Gabriel Jesus      | 4-3-3    | 3-4-3       |
| 2024-09-22 | 16:30  | Premier League    | Matchweek 5      | Sun | Away  | D      | 2  | 2  | Manchester City   | 0.7 | 2.1 | 23.0 | 52846.0    | Bukayo Saka        | 4-4-2    | 4-3-3       |
| 2024-09-25 | 19:45  | EFL Cup          | Third round      | Wed | Home  | W      | 5  | 1  | Bolton            | NaN | NaN | 77.0 | 59056.0    | Jorginho           | 4-3-3    | 3-5-2       |
| 2024-09-28 | 15:00  | Premier League    | Matchweek 6      | Sat | Home  | W      | 4  | 2  | Leicester City    | 4.4 | 0.3 | 74.0 | 60323.0    | Bukayo Saka        | 4-4-2    | 4-2-3-1      |
| 2024-10-01 | 20:00  | Champions Lg      | League phase      | Tue | Home  | W      | 2  | 0  | fr Paris S-G     | 0.7 | 0.4 | 35.0 | 60103.0    | Bukayo Saka        | 4-4-2    | 4-3-3       |
| 2024-10-05 | 15:00  | Premier League    | Matchweek 7      | Sat | Home  | W      | 3  | 1  | Southampton       | 2.8 | 0.6 | 59.0 | 60307.0    | Jorginho           | 4-4-2    | 5-4-1       |
| 2024-10-19 | 17:30  | Premier League    | Matchweek 8      | Sat | Away  | L      | 0  | 2  | Bournemouth       | 0.7 | 1.8 | 51.0 | 11235.0    | Gabriel Magalhães  | 4-2-3-1  | 4-2-3-1      |
| 2024-10-22 | 20:00  | Champions Lg      | League phase      | Tue | Home  | W      | 1  | 0  | ua Shakhtar       | 1.8 | 0.7 | 56.0 | 59594.0    | Gabriel Jesus      | 4-4-2    | 4-2-3-1      |
| 2024-10-27 | 16:30  | Premier League    | Matchweek 9      | Sun | Home  | D      | 2  | 2  | Liverpool         | 0.9 | 0.8 | 45.0 | 60383.0    | Bukayo Saka        | 4-4-2    | 4-2-3-1      |
| 2024-10-30 | 19:45  | EFL Cup          | Fourth round     | Wed | Away  | W      | 3  | 0  | Preston           | NaN | NaN | 74.0 | 21811.0    | Jorginho           | 4-3-3    | 4-2-3-1      |
| 2024-11-02 | 12:30  | Premier League    | Matchweek 10     | Sat | Away  | L      | 0  | 1  | Newcastle Utd     | 1.1 | 0.5 | 63.0 | 52249.0    | Bukayo Saka        | 4-4-2    | 4-3-3       |
| 2024-11-06 | 21:00  | Champions Lg      | League phase      | Wed | Away  | L      | 0  | 1  | it Inter          | 1.8 | 1.1 | 62.0 | 75222.0    | Bukayo Saka        | 4-4-2    | 3-5-2       |
| 2024-11-10 | 16:30  | Premier League    | Matchweek 11     | Sun | Away  | D      | 1  | 1  | Chelsea           | 1.5 | 1.5 | 51.0 | 39780.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2024-11-23 | 15:00  | Premier League    | Matchweek 12     | Sat | Home  | W      | 3  | 0  | Nott'ham Forest   | 1.2 | 0.3 | 66.0 | 60298.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2024-11-26 | 20:00  | Champions Lg      | League phase      | Tue | Away  | W      | 5  | 1  | pt Sporting CP    | 4.0 | 1.0 | 48.0 | 47386.0    | Martin Ødegaard    | 4-3-3    | 3-4-3       |
| 2024-11-30 | 17:30  | Premier League    | Matchweek 13     | Sat | Away  | W      | 5  | 2  | West Ham          | 3.5 | 1.5 | 60.0 | 62475.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2024-12-04 | 20:15  | Premier League    | Matchweek 14     | Wed | Home  | W      | 2  | 0  | Manchester Utd    | 2.1 | 0.2 | 51.0 | 60256.0    | Martin Ødegaard    | 4-3-3    | 3-4-3       |
| 2024-12-08 | 14:00  | Premier League    | Matchweek 15     | Sun | Away  | D      | 1  | 1  | Fulham            | 1.8 | 0.2 | 66.0 | 26954.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2024-12-11 | 20:00  | Champions Lg      | League phase      | Wed | Home  | W      | 3  | 0  | fr Monaco         | 2.3 | 0.5 | 54.0 | 60157.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2024-12-14 | 15:00  | Premier League    | Matchweek 16     | Sat | Home  | D      | 0  | 0  | Everton           | 1.2 | 0.1 | 76.0 | 60176.0    | Martin Ødegaard    | 4-3-3    | 4-3-3       |
| 2024-12-18 | 19:30  | EFL Cup          | Quarter-finals    | Wed | Home  | W      | 3  | 2  | Crystal Palace    | NaN | NaN | 71.0 | NaN        | Jorginho           | 4-3-3    | 3-4-3       |
| 2024-12-21 | 17:30  | Premier League    | Matchweek 17     | Sat | Away  | W      | 5  | 1  | Crystal Palace    | 2.5 | 1.6 | 58.0 | 25167.0    | Martin Ødegaard    | 4-3-3    | 3-4-3       |
| 2024-12-27 | 20:15  | Premier League    | Matchweek 18     | Fri | Home  | W      | 1  | 0  | Ipswich Town      | 1.8 | 0.2 | 68.0 | 60271.0    | Martin Ødegaard    | 4-3-3    | 5-4-1       |
| 2025-01-01 | 17:30  | Premier League    | Matchweek 19     | Wed | Away  | W      | 3  | 1  | Brentford         | 1.9 | 0.3 | 50.0 | 47190.0    | Martin Ødegaard    | 4-3-3    | 4-3-1-2      |
| 2025-01-04 | 17:30  | Premier League    | Matchweek 20     | Sat | Away  | D      | 1  | 1  | Brighton          | 0.9 | 1.5 | 55.0 | 31714.0    | Jorginho           | 4-3-3    | 4-2-3-1      |
| 2025-01-07 | 20:00  | EFL Cup          | Semi-finals      | Tue | Home  | L      | 0  | 2  | Newcastle Utd     | NaN | NaN | 70.0 | 59125.0    | Martin Ødegaard    | 4-3-3    | 4-3-3       |
| 2025-01-12 | 15:00  | FA Cup           | Third round proper| Sun | Home  | D      | 1 (3) | 1 (5) | Manchester Utd | NaN | NaN | 70.0 | 60109.0    | Martin Ødegaard    | 4-3-3    | 3-4-3       |
| 2025-01-15 | 20:00  | Premier League    | Matchweek 21     | Wed | Home  | W      | 2  | 1  | Tottenham         | 1.4 | 0.8 | 53.0 | 60287.0    | Martin Ødegaard    | 4-3-3    | 4-3-3       |
| 2025-01-18 | 17:30  | Premier League    | Matchweek 22     | Sat | Home  | D      | 2  | 2  | Aston Villa       | 1.3 | 1.0 | 66.0 | 60067.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2025-01-22 | 20:00  | Champions Lg      | League phase      | Wed | Home  | W      | 3  | 0  | hr Dinamo Zagreb   | 2.4 | 0.1 | 63.0 | 60024.0    | Martin Ødegaard    | 4-3-3    | 5-4-1       |
| 2025-01-25 | 15:00  | Premier League    | Matchweek 23     | Sat | Away  | W      | 1  | 0  | Wolves            | 1.0 | 0.7 | 49.0 | 31503.0    | Gabriel Magalhães  | 4-3-3    | 3-4-3       |
| 2025-01-29 | 21:00  | Champions Lg      | League phase      | Wed | Away  | W      | 2  | 1  | es Girona         | 2.1 | 0.7 | 61.0 | 9048.0     | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2025-02-02 | 16:30  | Premier League    | Matchweek 24     | Sun | Home  | W      | 5  | 1  | Manchester City   | 1.0 | 0.8 | 46.0 | 60355.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2025-02-05 | 20:00  | EFL Cup          | Semi-finals      | Wed | Away  | L      | 0  | 2  | Newcastle Utd     | NaN | NaN | 68.0 | 52173.0    | Martin Ødegaard    | 4-3-3    | 5-4-1       |
| 2025-02-15 | 12:30  | Premier League    | Matchweek 25     | Sat | Away  | W      | 2  | 0  | Leicester City    | 1.4 | 0.2 | 60.0 | 31968.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2025-02-22 | 15:00  | Premier League    | Matchweek 26     | Sat | Home  | L      | 0  | 1  | West Ham          | 1.2 | 1.1 | 68.0 | 60262.0    | Martin Ødegaard    | 4-3-3    | 5-3-2       |
| 2025-02-26 | 19:30  | Premier League    | Matchweek 27     | Wed | Away  | D      | 0  | 0  | Nott'ham Forest   | 1.0 | 0.4 | 64.0 | 30200.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2025-03-04 | 21:00  | Champions Lg      | Round of 16      | Tue | Away  | W      | 7  | 1  | nl PSV Eindhoven   | 1.9 | 1.4 | 47.0 | 34400.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2025-03-09 | 16:30  | Premier League    | Matchweek 28     | Sun | Away  | D      | 1  | 1  | Manchester Utd    | 1.6 | 1.5 | 68.0 | 73812.0    | Martin Ødegaard    | 4-3-3    | 3-4-3       |
| 2025-03-12 | 20:00  | Champions Lg      | Round of 16      | Wed | Home  | D      | 2  | 2  | nl PSV Eindhoven   | 1.2 | 1.6 | 51.0 | 59410.0    | Jorginho           | 4-3-3    | 4-3-3       |
| 2025-03-16 | 13:30  | Premier League    | Matchweek 29     | Sun | Home  | W      | 1  | 0  | Chelsea           | 0.7 | 0.4 | 42.0 | 60311.0    | Martin Ødegaard    | 4-3-3    | 4-2-3-1      |
| 2025-04-01 | 19:45  | Premier League    | Matchweek 30     | Tue | Home  | NaN    | NaN | NaN | Fulham            | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-04-05 | 12:30  | Premier League    | Matchweek 31     | Sat | Away  | NaN    | NaN | NaN | Everton           | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-04-08 | 20:00  | Champions Lg      | Quarter-finals    | Tue | Home  | NaN    | NaN | NaN | es Real Madrid    | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-04-12 | 17:30  | Premier League    | Matchweek 32     | Sat | Home  | NaN    | NaN | NaN | Brentford         | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-04-16 | 21:00  | Champions Lg      | Quarter-finals    | Wed | Away  | NaN    | NaN | NaN | es Real Madrid    | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-04-20 | 14:00  | Premier League    | Matchweek 33     | Sun | Away  | NaN    | NaN | NaN | Ipswich Town      | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-04-26 | 17:30  | Premier League    | Matchweek 34     | Sat | Home  | NaN    | NaN | NaN | Crystal Palace    | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-05-03 | 17:30  | Premier League    | Matchweek 35     | Sat | Home  | NaN    | NaN | NaN | Bournemouth       | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-05-10 | 15:00  | Premier League    | Matchweek 36     | Sat | Away  | NaN    | NaN | NaN | Liverpool         | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-05-18 | 15:00  | Premier League    | Matchweek 37     | Sun | Home  | NaN    | NaN | NaN | Newcastle Utd     | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
| 2025-05-25 | 16:00  | Premier League    | Matchweek 38     | Sun | Away  | NaN    | NaN | NaN | Southampton       | NaN | NaN | NaN  | NaN        | NaN                | NaN       | NaN           |
```

### Description of the Table

The table presents shooting statistics for the Arsenal football team, detailing individual player performance metrics during a specific period. The data includes various attributes for each player, such as their position, age, minutes played, goals scored, assists, expected goals (xG), and other performance-related metrics. 

The columns in the table are as follows:

- **Player**: The name of the player.
- **Pos**: The position(s) the player occupies on the field.
- **Age**: The age of the player, formatted as years and days.
- **MP**: Matches played by the player.
- **Starts**: Number of matches the player started.
- **Min**: Total minutes played.
- **90s**: Equivalent number of full matches played (in 90-minute increments).
- **Gls**: Goals scored by the player.
- **Ast**: Assists made by the player.
- **G+A**: Total goals and assists combined.
- **G-PK**: Goals scored excluding penalties.
- **PK**: Penalties scored.
- **PKatt**: Penalties attempted.
- **CrdY**: Yellow cards received.
- **CrdR**: Red cards received.
- **xG**: Expected goals.
- **npxG**: Non-penalty expected goals.
- **xAG**: Expected assists.
- **npxG+xAG**: Combined non-penalty expected goals and expected assists.
- **PrgC**: Progressive carries.
- **PrgP**: Progressive passes.
- **PrgR**: Progressive runs.
- **Gls**: Goals scored.
- **Ast**: Assists made.
- **G+A**: Total goals and assists combined.
- **G-PK**: Goals scored excluding penalties.
- **G+A-PK**: Total goals and assists excluding penalties.
- **xG**: Expected goals.
- **xAG**: Expected assists.
- **xG+xAG**: Combined expected goals and expected assists.
- **npxG**: Non-penalty expected goals.
- **npxG+xAG**: Combined non-penalty expected goals and expected assists.

The table also includes summary rows for the total performance of the squad and the opponent's total performance, providing a comparative analysis of the team's statistics against their opponents.

### Table in Markdown Format

```markdown
| Player                  | Pos     | Age     | MP | Starts | Min  | 90s  | Gls | Ast | G+A | G-PK | PK | PKatt | CrdY | CrdR | xG  | npxG | xAG | npxG+xAG | PrgC | PrgP | PrgR | Gls | Ast | G+A | G-PK | G+A-PK | xG  | xAG | xG+xAG | npxG | npxG+xAG |
|------------------------|---------|---------|----|--------|------|------|-----|-----|-----|------|----|-------|------|------|-----|------|-----|----------|------|------|------|-----|-----|-----|------|---------|-----|-----|--------|------|-----------|
| David Raya             | GK      | 29-193  | 29 | 29     | 2610 | 29   | 0   | 0   | 0   | 0    | 0  | 0     | 2    | 0    | 0   | 0    | 0   | 0        | 0    | 0    | 0    | 11  | 0   | 0   | 0    | 0       | 0   | 0   | 0      | 0    | 0         |
| William Saliba         | DF      | 24-003  | 27 | 27     | 2364 | 26.3 | 2   | 0   | 2   | 2    | 0  | 0     | 2    | 1    | 2.1 | 2.1  | 0.5 | 2.6      | 13   | 113  | 6    | 0.08| 0   | 0.08| 0.08 | 0.08   | 0.02| 0.1 | 0.08   | 0.1  | 0.1       |
| Gabriel Magalhães      | DF      | 27-098  | 27 | 27     | 2348 | 26.1 | 3   | 1   | 4   | 3    | 0  | 0     | 4    | 0    | 2.6 | 2.6  | 0.9 | 3.5      | 10   | 124  | 11   | 0.11| 0.04| 0.15| 0.11 | 0.15   | 0.1 | 0.03| 0.13   | 0.1  | 0.13      |
| Jurriën Timber         | DF      | 23-283  | 26 | 25     | 2199 | 24.4 | 1   | 2   | 3   | 1    | 0  | 0     | 7    | 0    | 0.7 | 0.7  | 0.8 | 1.5      | 51   | 134  | 97   | 0.04| 0.08| 0.12| 0.04 | 0.12   | 0.03| 0.03| 0.06   | 0.03 | 0.06      |
| Declan Rice            | MF      | 26-072  | 27 | 25     | 2156 | 24   | 2   | 5   | 7   | 2    | 0  | 0     | 5    | 1    | 2   | 2    | 5.7 | 7.7      | 75   | 149  | 76   | 0.08| 0.21| 0.29| 0.08 | 0.29   | 0.08| 0.24| 0.32   | 0.08 | 0.32      |
| Thomas Partey          | MF,DF   | 31-287  | 28 | 24     | 2189 | 24.3 | 3   | 2   | 5   | 3    | 0  | 0     | 4    | 0    | 1.7 | 1.7  | 1.9 | 3.6      | 29   | 150  | 37   | 0.12| 0.08| 0.21| 0.12 | 0.21   | 0.07| 0.08| 0.15   | 0.07 | 0.15      |
| Leandro Trossard       | FW      | 30-113  | 29 | 21     | 1897 | 21.1 | 4   | 5   | 9   | 4    | 0  | 0     | 4    | 1    | 5.1 | 5.1  | 5   | 10.1     | 64   | 81   | 172  | 0.19| 0.24| 0.43| 0.19 | 0.43   | 0.24| 0.24| 0.48   | 0.24 | 0.48      |
| Kai Havertz            | FW,MF   | 25-289  | 21 | 21     | 1839 | 20.4 | 9   | 3   | 12  | 9    | 0  | 0     | 4    | 0    | 9.4 | 9.4  | 2.4 | 11.8     | 34   | 59   | 110  | 0.44| 0.15| 0.59| 0.44 | 0.59   | 0.46| 0.12| 0.58   | 0.46 | 0.58      |
| Martin Ødegaard        | MF      | 26-100  | 21 | 20     | 1726 | 19.2 | 2   | 4   | 6   | 1    | 1  | 1     | 3    | 0    | 3.7 | 2.9  | 3.7 | 6.7      | 62   | 185  | 118  | 0.1 | 0.21| 0.31| 0.05 | 0.26   | 0.19| 0.19| 0.39   | 0.15 | 0.35      |
| Gabriel Martinelli     | FW,MF   | 23-282  | 24 | 17     | 1569 | 17.4 | 6   | 3   | 9   | 6    | 0  | 0     | 1    | 0    | 4.5 | 4.5  | 3   | 7.5      | 87   | 32   | 199  | 0.34| 0.17| 0.52| 0.34 | 0.52   | 0.26| 0.17| 0.43   | 0.26 | 0.43      |
| Bukayo Saka            | FW,MF   | 23-203  | 16 | 16     | 1268 | 14.1 | 5   | 10  | 15  | 4    | 1  | 1     | 3    | 0    | 4.2 | 3.4  | 5.8 | 9.2      | 72   | 53   | 195  | 0.35| 0.71| 1.06| 0.28 | 0.99   | 0.3 | 0.41| 0.71   | 0.24 | 0.65      |
| Mikel Merino           | MF,FW   | 28-278  | 21 | 12     | 1149 | 12.8 | 5   | 1   | 6   | 5    | 0  | 0     | 2    | 0    | 3.7 | 3.7  | 1.4 | 5.1      | 7    | 53   | 70   | 0.39| 0.08| 0.47| 0.39 | 0.47   | 0.29| 0.11| 0.4    | 0.29 | 0.4       |
| Riccardo Calafiori     | DF      | 22-312  | 17 | 11     | 925  | 10.3 | 2   | 1   | 3   | 2    | 0  | 0     | 4    | 0    | 0.9 | 0.9  | 0.3 | 1.1      | 21   | 54   | 29   | 0.19| 0.1 | 0.29| 0.19 | 0.29   | 0.08| 0.03| 0.11   | 0.08 | 0.11      |
| Myles Lewis-Skelly     | DF      | 18-182  | 14 | 9      | 766  | 8.5  | 1   | 0   | 1   | 1    | 0  | 0     | 2    | 2    | 0   | 0    | 0.2 | 0.2      | 15   | 37   | 19   | 0.12| 0   | 0.12| 0.12 | 0.12   | 0   | 0.02| 0.03   | 0   | 0.03      |
| Ben White              | DF      | 27-170  | 11 | 7      | 706  | 7.8  | 0   | 1   | 1   | 0    | 0  | 0     | 2    | 0    | 0.2 | 0.2  | 0.4 | 0.6      | 5    | 32   | 18   | 0   | 0.13| 0.13| 0   | 0.13   | 0.02| 0.06| 0.08   | 0.02 | 0.08      |
| Ethan Nwaneri          | FW,MF   | 18-006  | 19 | 7      | 606  | 6.7  | 3   | 1   | 4   | 3    | 0  | 0     | 1    | 0    | 0.8 | 0.8  | 0.8 | 1.6      | 35   | 24   | 84   | 0.45| 0.15| 0.59| 0.45 | 0.59   | 0.12| 0.12| 0.24   | 0.12 | 0.24      |
| Jorginho               | MF      | 33-097  | 12 | 7      | 543  | 6    | 0   | 0   | 0   | 0    | 0  | 0     | 4    | 0    | 0   | 0    | 0.4 | 0.5      | 9    | 37   | 3    | 0   | 0   | 0   | 0   | 0       | 0   | 0.01| 0.07   | 0.08 | 0.01      |
| Gabriel Jesus          | FW      | 27-358  | 17 | 6      | 608  | 6.8  | 3   | 0   | 3   | 3    | 0  | 0     | 4    | 0    | 3   | 3    | 0.7 | 3.7      | 15   | 19   | 57   | 0.44| 0   | 0.44| 0.44 | 0.44   | 0.44| 0.1 | 0.54   | 0.44 | 0.54      |
| Raheem Sterling        | FW,MF   | 30-109  | 12 | 4      | 310  | 3.4  | 0   | 1   | 1   | 0    | 0  | 0     | 1    | 0    | 1   | 1    | 0.3 | 1.3      | 18   | 14   | 57   | 0   | 0.29| 0.29| 0   | 0.29   | 0.3 | 0.08| 0.38   | 0.3  | 0.38      |
| Jakub Kiwior           | DF      | 25-040  | 8  | 2      | 327  | 3.6  | 0   | 0   | 0   | 0    | 0  | 0     | 0    | 0    | 0   | 0    | 0.1 | 0.1      | 1    | 8    | 0    | 0   | 0   | 0   | 0   | 0       | 0   | 0.02| 0.02   | 0    | 0.02      |
| Oleksandr Zinchenko    | DF,MF   | 28-102  | 10 | 2      | 299  | 3.3  | 0   | 0   | 0   | 0    | 0  | 0     | 1    | 0    | 0.2 | 0.2  | 0   | 0.2      | 7    | 21   | 7    | 0   | 0   | 0   | 0   | 0       | 0   | 0.05| 0.01   | 0.05 | 0.05      |
| Kieran Tierney         | DF,FW   | 27-295  | 6  | 0      | 81   | 0.9  | 0   | 0   | 0   | 0    | 0  | 0     | 0    | 0    | 0.2 | 0.2  | 0.5 | 0.7      | 2    | 3    | 8    | 0   | 0   | 0   | 0   | 0       | 0   | 0.23| 0.54   | 0.77 | 0.23      |
| Takehiro Tomiyasu      | DF      | 26-142  | 1  | 0      | 7    | 0.1  | 0   | 0   | 0   | 0    | 0  | 0     | 0    | 0    | 0.2 | 0.2  | 0   | 0.2      | 0    | 1    | 0    | 0   | 0   | 0   | 0   | 0       | 0   | 2.37| 0      | 2.37 | 2.37      |
| Reiss Nelson           | FW      | 25-107  | 1  | 0      | 3    | 0    | 0   | 0   | 0   | 0    | 0  | 0     | 0    | 0    | 0   | 0    | 0   | 0        | 0    | 0    | 0    | 0   | 0   | 0   | 0   | 0       | 0   | 0   | 0      | 0    | 0         |
| Nathan Butler-Oyedeji  | FW      | 22-082  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Ayden Heaven           | DF      | 18-186  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Ismeal Kabia          | MF      | 19-107  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Maldini Kacurri       | DF      | 19-174  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Neto                   | GK      | 35-251  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Josh Nichols           | DF      | 18-244  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Eddie Nketiah         | FW      | 25-301  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Salah Oulad M'Hand    | MF      | 21-219  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Jack Porter            | GK      | 16-255  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Aaron Ramsdale         | GK      | 26-317  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Tommy Setford          | GK      | 19-014  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| Squad Total            | NaN     | 26.5    | 29 | 319    | 2610 | 29   | 51  | 40  | 91  | 49   | 2  | 2     | 60   | 5    | 44.5| 43   | 33.9| 76.9     | 632  | 1394 | 1373 | 1.76| 1.38| 3.14| 1.69 | 3.07   | 1.54| 1.17| 2.71   | 1.48 | 2.65      |
| Opponent Total         | NaN     | 26.8    | 29 | 319    | 2610 | 29   | 24  | 17  | 41  | 22   | 2  | 2     | 68   | 1    | 24.7| 23.2 | 17.1| 40.3     | 491  | 738  | 730  | 0.83| 0.59| 1.41| 0.76 | 1.34   | 0.85| 0.59| 1.44   | 0.8  | 1.39      |
```

### Description of the Table

The table presents passing statistics for the Arsenal football team, detailing individual player performance metrics. Each row corresponds to a player, while the columns provide various statistics related to their passing abilities and contributions during matches. The columns include:

- **Player**: The name of the player.
- **Pos**: The position the player occupies on the field.
- **Age**: The age of the player, formatted as years and days.
- **90s**: The number of matches played, expressed in terms of 90-minute equivalents.
- **Gls**: Goals scored by the player.
- **Sh**: Total shots taken by the player.
- **SoT**: Shots on target.
- **SoT%**: Percentage of shots that were on target.
- **Sh/90**: Shots per 90 minutes played.
- **SoT/90**: Shots on target per 90 minutes played.
- **G/Sh**: Goals per shot.
- **G/SoT**: Goals per shot on target.
- **Dist**: Average distance of shots taken.
- **FK**: Free kicks taken.
- **PK**: Penalties scored.
- **PKatt**: Penalties attempted.
- **xG**: Expected goals.
- **npxG**: Non-penalty expected goals.
- **npxG/Sh**: Non-penalty expected goals per shot.
- **G-xG**: Goals minus expected goals.
- **np:G-xG**: Non-penalty goals minus expected goals.

The table includes a header row that describes each column, followed by rows of data for each player. There are also summary rows at the end, indicating the total statistics for the squad and the opponent.

### Table in Markdown Format

```markdown
| Player                | Pos     | Age     | 90s   | Gls | Sh | SoT | SoT% | Sh/90 | SoT/90 | G/Sh | G/SoT | Dist | FK | PK | PKatt | xG  | npxG | npxG/Sh | G-xG | np:G-xG |
|----------------------|---------|---------|-------|-----|----|-----|------|-------|--------|------|-------|------|----|----|-------|-----|------|---------|------|---------|
| David Raya           | GK      | 29-193  | 29    | 0   | 0  | 0   | NaN  | 0     | 0      | NaN  | NaN   | NaN  | 0  | 0  | 0     | 0   | 0    | 0       | 0    | 0       |
| William Saliba       | DF      | 24-003  | 26.3  | 2   | 4  | 2   | 50   | 0.15  | 0.08   | 0.5  | 1     | 3.3  | 0  | 0  | 0     | 2.1 | 2.1  | 0.52    | -0.1 | -0.1    |
| Gabriel Magalhães    | DF      | 27-098  | 26.1  | 3   | 22 | 5   | 22.7 | 0.84  | 0.19   | 0.14 | 0.6   | 9.5  | 0  | 0  | 0     | 2.6 | 2.6  | 0.12    | 0.4  | 0.4     |
| Jurriën Timber       | DF      | 23-283  | 24.4  | 1   | 12 | 3   | 25   | 0.49  | 0.12   | 0.08 | 0.33  | 15.3 | 0  | 0  | 0     | 0.7 | 0.7  | 0.06    | 0.3  | 0.3     |
| Declan Rice          | MF      | 26-072  | 24    | 2   | 33 | 8   | 24.2 | 1.38  | 0.33   | 0.06 | 0.25  | 20.2 | 1  | 0  | 0     | 2   | 2    | 0.06    | 0    | 0       |
| Thomas Partey        | MF,DF   | 31-287  | 24.3  | 3   | 21 | 6   | 28.6 | 0.86  | 0.25   | 0.14 | 0.5   | 19.8 | 0  | 0  | 0     | 1.7 | 1.7  | 0.08    | 1.3  | 1.3     |
| Leandro Trossard     | FW      | 30-113  | 21.1  | 4   | 53 | 14  | 26.4 | 2.51  | 0.66   | 0.08 | 0.29  | 16.6 | 0  | 0  | 0     | 5.1 | 5.1  | 0.1     | -1.1 | -1.1    |
| Kai Havertz          | FW,MF   | 25-289  | 20.4  | 9   | 52 | 21  | 40.4 | 2.54  | 1.03   | 0.17 | 0.43  | 11.7 | 0  | 0  | 0     | 9.4 | 9.4  | 0.18    | -0.4 | -0.4    |
| Martin Ødegaard      | MF      | 26-100  | 19.2  | 2   | 33 | 11  | 33.3 | 1.72  | 0.57   | 0.03 | 0.09  | 19.2 | 2  | 1  | 1     | 3.7 | 2.9  | 0.09    | -1.7 | -1.9    |
| Gabriel Martinelli    | FW,MF   | 23-282  | 17.4  | 6   | 32 | 16  | 50   | 1.84  | 0.92   | 0.19 | 0.38  | 12.5 | 0  | 0  | 0     | 4.5 | 4.5  | 0.14    | 1.5  | 1.5     |
| Bukayo Saka          | FW,MF   | 23-203  | 14.1  | 5   | 45 | 17  | 37.8 | 3.19  | 1.21   | 0.09 | 0.24  | 15.9 | 0  | 1  | 1     | 4.2 | 3.4  | 0.08    | 0.8  | 0.6     |
| Mikel Merino         | MF,FW   | 28-278  | 12.8  | 5   | 25 | 11  | 44   | 1.96  | 0.86   | 0.2  | 0.45  | 11   | 0  | 0  | 0     | 3.7 | 3.7  | 0.15    | 1.3  | 1.3     |
| Riccardo Calafiori   | DF      | 22-312  | 10.3  | 2   | 10 | 6   | 60   | 0.97  | 0.58   | 0.2  | 0.33  | 14.1 | 0  | 0  | 0     | 0.9 | 0.9  | 0.09    | 1.1  | 1.1     |
| Myles Lewis-Skelly   | DF      | 18-182  | 8.5   | 1   | 1  | 1   | 100  | 0.12  | 0.12   | 1    | 1     | 13.9 | 0  | 0  | 0     | 0   | 0    | 0.04    | 1    | 1       |
| Ben White            | DF      | 27-170  | 7.8   | 0   | 5  | 1   | 20   | 0.64  | 0.13   | 0    | 0     | 21.8 | 0  | 0  | 0     | 0.2 | 0.2  | 0.04    | -0.2 | -0.2    |
| Ethan Nwaneri        | FW,MF   | 18-006  | 6.7   | 3   | 17 | 6   | 35.3 | 2.52  | 0.89   | 0.18 | 0.5   | 19.8 | 1  | 0  | 0     | 0.8 | 0.8  | 0.05    | 2.2  | 2.2     |
| Jorginho             | MF      | 33-097  | 6     | 0   | 1  | 0   | 0    | 0.17  | 0      | 0    | NaN   | 22.5 | 0  | 0  | 0     | 0   | 0    | 0.04    | 0    | 0       |
| Gabriel Jesus        | FW      | 27-358  | 6.8   | 3   | 20 | 7   | 35   | 2.96  | 1.04   | 0.15 | 0.43  | 11.1 | 0  | 0  | 0     | 3   | 3    | 0.15    | 0    | 0       |
| Raheem Sterling      | FW,MF   | 30-109  | 3.4   | 0   | 9  | 0   | 0    | 2.61  | 0      | 0    | NaN   | 15.3 | 2  | 0  | 0     | 1   | 1    | 0.11    | -1   | -1      |
| Jakub Kiwior         | DF      | 25-040  | 3.6   | 0   | 0  | 0   | NaN  | 0     | 0      | NaN  | NaN   | NaN  | 0  | 0  | 0     | 0   | 0    | NaN     | 0    | 0       |
| Oleksandr Zinchenko  | DF,MF   | 28-102  | 3.3   | 0   | 3  | 0   | 0    | 0.9   | 0      | 0    | NaN   | 14   | 0  | 0  | 0     | 0.2 | 0.2  | 0.05    | -0.2 | -0.2    |
| Kieran Tierney       | DF,FW   | 27-295  | 0.9   | 0   | 1  | 0   | 0    | 1.11  | 0      | 0    | NaN   | 2.6  | 0  | 0  | 0     | 0.2 | 0.2  | 0.21    | -0.2 | -0.2    |
| Takehiro Tomiyasu    | DF      | 26-142  | 0.1   | 0   | 1  | 0   | 0    | 12.86 | 0      | 0    | NaN   | 1.2  | 0  | 0  | 0     | 0.2 | 0.2  | 0.18    | -0.2 | -0.2    |
| Reiss Nelson         | FW      | 25-107  | 0     | 0   | 0  | 0   | NaN  | 0     | 0      | NaN  | NaN   | NaN  | 0  | 0  | 0     | 0   | 0    | NaN     | 0    | 0       |
| Squad Total          | NaN     | 26.5    | 29    | 51  | 400| 135 | 33.8 | 13.79 | 4.66  | 0.12 | 0.36  | 15.1 | 6  | 2  | 2     | 44.5| 43   | 0.11    | 6.5  | 6       |
| Opponent Total       | NaN     | 26.8    | 29    | 24  | 280| 93  | 33.2 | 9.66  | 3.21  | 0.08 | 0.24  | 18.4 | 10 | 2  | 2     | 24.7| 23.2 | 0.08    | -0.7 | -1.2    |
```

### Description of the Table

The table presents data related to the pass types of players from the Arsenal football team. It includes various statistics for each player, such as their position, age, number of 90-minute appearances (90s), completed passes (Cmp), attempted passes (Att), completion percentage (Cmp%), total distance covered (TotDist), progressive distance (PrgDist), and several other metrics related to passing performance.

The first row serves as the header, detailing the categories of data collected. The subsequent rows contain the statistics for individual players, including their names, positions, and various performance metrics. The last few rows summarize the total statistics for the squad and the opponent's total statistics, providing a comparative overview of performance.

The table includes several columns with headers that start with "Unnamed:", which are typically used for indexing or placeholders. However, the data in these columns is relevant and has been preserved in the markdown format.

### Table in Markdown Format

```markdown
| Player                | Pos     | Age     | 90s   | Cmp | Att  | Cmp% | TotDist | PrgDist | Cmp | Att | Cmp% | Cmp | Att | Cmp% | Cmp | Att | Cmp% | Ast | xAG | xA | A-xAG | KP | 1/3 | PPA | CrsPA | PrgP |
|----------------------|---------|---------|-------|-----|------|------|---------|---------|-----|-----|------|-----|-----|------|-----|-----|------|-----|-----|----|-------|----|-----|-----|-------|------|
| NaN                  | NaN     | NaN     | NaN   | NaN | NaN  | NaN  | NaN     | NaN     | NaN | NaN | NaN  | NaN | NaN | NaN  | NaN | NaN | NaN  | NaN | NaN | NaN| NaN   | NaN| NaN | NaN | NaN   | NaN  |
| David Raya           | GK      | 29-193  | 29    | 781 | 1060 | 73.7 | 18971   | 13142   | 213 | 215 | 99.1 | 400 | 406 | 98.5 | 167 | 435 | 38.4 | 0   | 0   | 0  | 0     | 0  | 34  | 1   | 0     | 11   |
| William Saliba       | DF      | 24-003  | 26.3  | 1798| 1923 | 93.5 | 30946   | 9558    | 771 | 809 | 95.3 | 919 | 964 | 95.3 | 101 | 126 | 80.2 | 0   | 0.5 | 0.9| -0.5  | 4  | 139 | 3   | 0     | 113  |
| Gabriel Magalhães    | DF      | 27-098  | 26.1  | 1468| 1628 | 90.2 | 25559   | 7812    | 596 | 615 | 96.9 | 772 | 819 | 94.3 | 83  | 154 | 53.9 | 1   | 0.9 | 1.2| 0.1   | 13 | 145 | 8   | 0     | 124  |
| Jurriën Timber       | DF      | 23-283  | 24.4  | 1053| 1238 | 85.1 | 15160   | 4263    | 609 | 671 | 90.8 | 403 | 473 | 85.2 | 23  | 44  | 52.3 | 2   | 0.8 | 1.2| 1.2   | 16 | 97  | 15  | 2     | 134  |
| Declan Rice          | MF      | 26-072  | 24    | 1097| 1312 | 83.6 | 18775   | 4999    | 543 | 587 | 92.5 | 433 | 479 | 90.4 | 100 | 202 | 49.5 | 5   | 5.7 | 5  | -0.7  | 46 | 110 | 27  | 5     | 149  |
| Thomas Partey        | MF,DF   | 31-287  | 24.3  | 1328| 1516 | 87.6 | 21248   | 5746    | 690 | 741 | 93.1 | 539 | 609 | 88.5 | 77  | 112 | 68.8 | 2   | 1.9 | 2.1| 0.1   | 17 | 128 | 30  | 2     | 150  |
| Leandro Trossard     | FW      | 30-113  | 21.1  | 507 | 695  | 72.9 | 8444    | 2493    | 264 | 313 | 84.3 | 191 | 256 | 74.6 | 41  | 77  | 53.2 | 5   | 5   | 3.1| 0     | 34 | 35  | 41  | 9     | 81   |
| Kai Havertz          | FW,MF   | 25-289  | 20.4  | 401 | 511  | 78.5 | 4833    | 1010    | 281 | 334 | 84.1 | 94  | 114 | 82.5 | 5   | 11  | 45.5 | 3   | 2.4 | 1.7| 0.6   | 16 | 26  | 8   | 1     | 59   |
| Martin Ødegaard      | MF      | 26-100  | 19.2  | 904 | 1094 | 82.6 | 13656   | 4121    | 518 | 568 | 91.2 | 316 | 363 | 87.1 | 48  | 100 | 48   | 4   | 3.7 | 5.2| 0.3   | 45 | 97  | 62  | 5     | 185  |
| Gabriel Martinelli    | FW,MF   | 23-282  | 17.4  | 333 | 477  | 69.8 | 4823    | 1034    | 213 | 263 | 81   | 92  | 137 | 67.2 | 19  | 35  | 54.3 | 3   | 3   | 3.3| 0     | 27 | 6   | 24  | 10    | 32   |
| Bukayo Saka          | FW,MF   | 23-203  | 14.1  | 406 | 546  | 74.4 | 6315    | 1918    | 238 | 265 | 89.8 | 119 | 163 | 73   | 36  | 77  | 46.8 | 10  | 5.8 | 5.6| 4.2   | 42 | 11  | 28  | 9     | 53   |
| Mikel Merino         | MF,FW   | 28-278  | 12.8  | 349 | 450  | 77.6 | 4719    | 1391    | 228 | 263 | 86.7 | 96  | 125 | 76.8 | 12  | 24  | 50   | 1   | 1.4 | 1  | -0.4  | 14 | 30  | 20  | 2     | 53   |
| Riccardo Calafiori   | DF      | 22-312  | 10.3  | 449 | 526  | 85.4 | 6549    | 1644    | 272 | 297 | 91.6 | 150 | 175 | 85.7 | 19  | 28  | 67.9 | 1   | 0.3 | 0.7| 0.7   | 6  | 40  | 9   | 1     | 54   |
| Myles Lewis-Skelly   | DF      | 18-182  | 8.5   | 377 | 414  | 91.1 | 5431    | 1252    | 229 | 240 | 95.4 | 131 | 146 | 89.7 | 9   | 12  | 75   | 0   | 0.2 | 0.3| -0.2  | 4  | 41  | 4   | 0     | 37   |
| Ben White            | DF      | 27-170  | 7.8   | 307 | 368  | 83.4 | 5011    | 1697    | 158 | 173 | 91.3 | 128 | 149 | 85.9 | 14  | 32  | 43.8 | 1   | 0.4 | 0.4| 0.6   | 3  | 29  | 6   | 1     | 32   |
| Ethan Nwaneri        | FW,MF   | 18-006  | 6.7   | 219 | 279  | 78.5 | 3147    | 904     | 140 | 153 | 91.5 | 57  | 78  | 73.1 | 13  | 26  | 50   | 1   | 0.8 | 1.2| 0.2   | 8  | 12  | 9   | 4     | 24   |
| Jorginho             | MF      | 33-097  | 6     | 308 | 359  | 85.8 | 4760    | 1164    | 166 | 185 | 89.7 | 121 | 137 | 88.3 | 15  | 26  | 57.7 | 0   | 0.4 | 0.5| -0.4  | 3  | 33  | 8   | 0     | 37   |
| Gabriel Jesus        | FW      | 27-358  | 6.8   | 156 | 203  | 76.8 | 2030    | 378     | 103 | 128 | 80.5 | 41  | 47  | 87.2 | 4   | 6   | 66.7 | 0   | 0.7 | 0.5| -0.7  | 8  | 10  | 9   | 1     | 19   |
| Raheem Sterling      | FW,MF   | 30-109  | 3.4   | 106 | 139  | 76.3 | 1320    | 264     | 74  | 87  | 85.1 | 25  | 36  | 69.4 | 2   | 3   | 66.7 | 1   | 0.3 | 0.4| 0.7   | 5  | 3   | 7   | 2     | 14   |
| Jakub Kiwior         | DF      | 25-040  | 3.6   | 147 | 175  | 84   | 2623    | 792     | 57  | 63  | 90.5 | 80  | 88  | 90.9 | 9   | 19  | 47.4 | 0   | 0.1 | 0  | -0.1  | 1  | 8   | 0   | 0     | 8    |
| Oleksandr Zinchenko  | DF,MF   | 28-102  | 3.3   | 193 | 243  | 79.4 | 3067    | 724     | 102 | 114 | 89.5 | 79  | 97  | 81.4 | 8   | 20  | 40   | 0   | 0   | 0.1| 0     | 1  | 14  | 2   | 1     | 21   |
| Kieran Tierney       | DF,FW   | 27-295  | 0.9   | 24  | 34   | 70.6 | 362     | 101     | 14  | 15  | 93.3 | 7   | 11  | 63.6 | 2   | 5   | 40   | 0   | 0.5 | 0.3| -0.5  | 3  | 2   | 3   | 1     | 3    |
| Takehiro Tomiyasu    | DF      | 26-142  | 0.1   | 3   | 4    | 75   | 42      | 10      | 1   | 1   | 100  | 2   | 2   | 100  | 0   | 1   | 0    | 0   | 0   | 0  | 0     | 0  | 0   | 0   | 0     | 0    |
| Reiss Nelson         | FW      | 25-107  | 0    | 0   | 0    | NaN | 0       | 0       | 0   | 0   | NaN  | 0   | 0   | NaN  | 0   | 0   | NaN  | 0   | 0   | 0  | 0     | 0  | 0   | 0   | 0     | 0    |
| Squad Total          | NaN     | 26.5    | 29    | 12714| 15194| 83.7 | 207791  | 66417   | 6480| 7100| 91.3 | 5195| 5874| 88.4 | 807 | 1575| 51.2 | 40  | 33.9| 34.7| 6.1   | 316| 1050| 324 | 56    | 1394 |
| Opponent Total       | NaN     | 26.8    | 29    | 9582 | 11968| 80.1 | 166666  | 55400   | 4465| 5000| 89.3 | 4099| 4703| 87.2 | 824 | 1748| 47.1 | 17  | 17.1| 17.2| -0.1  | 202| 714 | 144 | 50    | 738  |
```

### Description of the Table

The table presents data related to goal and shot creation for the Arsenal football team. It includes various statistics for individual players, categorized by their positions, ages, and performance metrics. The data is structured in a tabular format with the following key components:

- **Columns**: The table consists of multiple columns, some of which are labeled with specific performance metrics, while others are unnamed. The named columns include:
  - **Player**: The name of the player.
  - **Pos**: The position of the player on the field.
  - **Age**: The age of the player.
  - **90s**: The number of 90-minute matches played.
  - **Att**: Total attempts.
  - **Live**: Live ball attempts.
  - **Dead**: Dead ball attempts.
  - **FK**: Free kicks.
  - **TB**: Throw-ins.
  - **Sw**: Switches.
  - **Crs**: Crosses.
  - **TI**: Throw-ins.
  - **CK**: Corner kicks.
  - **In**: Successful passes.
  - **Out**: Unsuccessful passes.
  - **Str**: Shots.
  - **Cmp**: Completed passes.
  - **Off**: Offsides.
  - **Blocks**: Blocked shots.

- **Rows**: Each row represents a player or a summary statistic (like squad total or opponent total). The first row serves as a header, while subsequent rows contain player-specific data or summary statistics.

- **Data Types**: The data includes numerical values (e.g., age, attempts, passes) and categorical values (e.g., player names, positions).

- **Special Rows**: The last two rows summarize the total statistics for the squad and the opponent, providing a comparative overview of performance.

### Table in Markdown Format

```markdown
| Player                 | Pos     | Age     | 90s  | Att   | Live | Dead | FK | TB | Sw | Crs | TI | CK | In  | Out | Str | Cmp | Off | Blocks |
|-----------------------|---------|---------|------|-------|------|------|----|----|----|-----|----|----|-----|-----|-----|-----|-----|--------|
| David Raya            | GK      | 29-193  | 29   | 1060  | 878  | 179  | 68 | 0  | 1  | 0   | 0  | 0  | 0   | 0   | 781 | 3   | 0   |
| William Saliba        | DF      | 24-003  | 26.3 | 1923  | 1884 | 35   | 26 | 0  | 9  | 3   | 3  | 0  | 0   | 0   | 1798| 4   | 4   |
| Gabriel Magalhães     | DF      | 27-098  | 26.1 | 1628  | 1547 | 80   | 51 | 1  | 8  | 9   | 3  | 0  | 0   | 0   | 1468| 1   | 8   |
| Jurriën Timber        | DF      | 23-283  | 24.4 | 1238  | 1041 | 194  | 21 | 2  | 1  | 27  | 173| 0  | 0   | 0   | 1053| 3   | 24  |
| Declan Rice           | MF      | 26-072  | 24   | 1312  | 1134 | 174  | 65 | 3  | 16 | 137 | 3  | 81 | 75  | 3   | 0   | 1097| 4   | 8   |
| Thomas Partey         | MF,DF   | 31-287  | 24.3 | 1516  | 1431 | 80   | 19 | 5  | 2  | 9   | 55 | 0  | 0   | 0   | 1328| 5   | 12  |
| Leandro Trossard      | FW      | 30-113  | 21.1 | 695   | 667  | 21   | 4  | 5  | 3  | 74  | 5  | 9  | 8   | 0   | 0   | 507 | 7   | 27  |
| Kai Havertz           | FW,MF   | 25-289  | 20.4 | 511   | 503  | 6    | 1  | 1  | 0  | 11  | 5  | 0  | 0   | 0   | 0   | 401 | 2   | 11  |
| Martin Ødegaard       | MF      | 26-100  | 19.2 | 1094  | 997  | 87   | 26 | 17 | 1  | 69  | 11 | 33 | 27  | 0   | 0   | 904 | 10  | 18  |
| Gabriel Martinelli     | FW,MF   | 23-282  | 17.4 | 477   | 465  | 10   | 0  | 3  | 2  | 63  | 7  | 3  | 3   | 0   | 0   | 333 | 2   | 26  |
| Bukayo Saka           | FW,MF   | 23-203  | 14.1 | 546   | 476  | 67   | 7  | 4  | 2  | 99  | 10 | 50 | 47  | 0   | 2   | 406 | 3   | 18  |
| Mikel Merino          | MF,FW   | 28-278  | 12.8 | 450   | 443  | 3    | 3  | 4  | 1  | 10  | 0  | 0  | 0   | 0   | 0   | 349 | 4   | 11  |
| Riccardo Calafiori    | DF      | 22-312  | 10.3 | 526   | 460  | 65   | 7  | 0  | 2  | 11  | 58 | 0  | 0   | 0   | 0   | 449 | 1   | 11  |
| Myles Lewis-Skelly    | DF      | 18-182  | 8.5  | 414   | 337  | 73   | 7  | 3  | 1  | 4   | 66 | 0  | 0   | 0   | 0   | 377 | 4   | 1   |
| Ben White             | DF      | 27-170  | 7.8  | 368   | 307  | 59   | 12 | 1  | 5  | 8   | 43 | 0  | 0   | 0   | 0   | 307 | 2   | 2   |
| Ethan Nwaneri         | FW,MF   | 18-006  | 6.7  | 279   | 261  | 16   | 1  | 2  | 1  | 40  | 2  | 13 | 12  | 0   | 0   | 219 | 2   | 8   |
| Jorginho              | MF      | 33-097  | 6    | 359   | 354  | 5    | 4  | 2  | 1  | 1   | 0  | 0  | 0   | 0   | 0   | 308 | 0   | 4   |
| Gabriel Jesus         | FW      | 27-358  | 6.8  | 203   | 197  | 3    | 0  | 1  | 0  | 7   | 3  | 0  | 0   | 0   | 0   | 156 | 3   | 12  |
| Raheem Sterling       | FW,MF   | 30-109  | 3.4  | 139   | 137  | 0    | 0  | 0  | 1  | 11  | 0  | 0  | 0   | 0   | 0   | 106 | 2   | 3   |
| Jakub Kiwior          | DF      | 25-040  | 3.6  | 175   | 167  | 7    | 2  | 0  | 1  | 0   | 2  | 0  | 0   | 0   | 0   | 147 | 1   | 0   |
| Oleksandr Zinchenko   | DF,MF   | 28-102  | 3.3  | 243   | 209  | 33   | 9  | 1  | 3  | 8   | 23 | 0  | 0   | 0   | 0   | 193 | 1   | 2   |
| Kieran Tierney        | DF,FW   | 27-295  | 0.9  | 34    | 33   | 1    | 0  | 0  | 0  | 5   | 1  | 0  | 0   | 0   | 0   | 24  | 0   | 1   |
| Takehiro Tomiyasu     | DF      | 26-142  | 0.1  | 4     | 4    | 0    | 0  | 0  | 0  | 0   | 0  | 0  | 0   | 0   | 0   | 3   | 0   | 0   |
| Reiss Nelson          | FW      | 25-107  | 0    | 0     | 0    | 0    | 0  | 0  | 0  | 0   | 0  | 0  | 0   | 0   | 0   | 0   | 0   | 0   |
| Squad Total           | NaN     | 26.5    | 29   | 15194 | 13932| 1198 | 333| 55 | 61 | 606 | 473| 189| 172 | 3   | 2   | 12714| 64  | 211 |
| Opponent Total        | NaN     | 26.8    | 29   | 11968 | 10761| 1176 | 382| 33 | 64 | 407 | 401| 82 | 49  | 17  | 1   | 9582 | 31  | 193 |
```

### Description of the Table

The table presents data on defensive actions for the Arsenal football team. It includes various statistics related to player performance, categorized into two main sections: SCA (Shot-Creating Actions) and GCA (Goal-Creating Actions). Each row corresponds to a player, detailing their position, age, and performance metrics over a specified number of 90-minute matches (90s). 

The columns include:
- **Player**: The name of the player.
- **Pos**: The position(s) the player occupies on the field.
- **Age**: The age of the player.
- **90s**: The number of 90-minute matches played.
- **SCA**: Total shot-creating actions made by the player.
- **SCA90**: Shot-creating actions per 90 minutes.
- **PassLive**: Number of live passes made.
- **PassDead**: Number of dead ball passes made.
- **TO**: Turnovers committed.
- **Sh**: Shots taken.
- **Fld**: Fouls committed.
- **Def**: Defensive actions.
- **GCA**: Total goal-creating actions made by the player.
- **GCA90**: Goal-creating actions per 90 minutes.
- **PassLive**: Number of live passes made (again).
- **PassDead**: Number of dead ball passes made (again).
- **TO**: Turnovers committed (again).
- **Sh**: Shots taken (again).
- **Fld**: Fouls committed (again).
- **Def**: Defensive actions (again).

The table also includes summary rows for "Squad Total" and "Opponent Total," which aggregate the statistics for all players and their opponents, respectively.

### Table in Markdown Format

```markdown
| Player                  | Pos     | Age     | 90s   | SCA | SCA90 | PassLive | PassDead | TO | Sh | Fld | Def | GCA | GCA90 | PassLive | PassDead | TO | Sh | Fld | Def |
|------------------------|---------|---------|-------|-----|-------|----------|----------|----|----|-----|-----|-----|-------|----------|----------|----|----|-----|-----|
| David Raya             | GK      | 29-193  | 29    | 3   | 0.1   | 2        | 1        | 0  | 0  | 0   | 0   | 0   | 0     | 0        | 0        | 0  | 0  | 0   | 0   |
| William Saliba         | DF      | 24-003  | 26.3  | 21  | 0.8   | 20       | 0        | 0  | 0  | 0   | 0   | 1   | 1     | 0.04     | 1        | 0  | 0  | 0   | 0   |
| Gabriel Magalhães      | DF      | 27-098  | 26.1  | 35  | 1.34  | 31       | 0        | 0  | 3  | 1   | 0   | 6   | 0.23  | 4        | 0        | 0  | 1  | 1   | 0   |
| Jurriën Timber         | DF      | 23-283  | 24.4  | 48  | 1.96  | 42       | 1        | 3  | 0  | 1   | 1   | 7   | 0.29  | 6        | 0        | 1  | 0  | 0   | 0   |
| Declan Rice            | MF      | 26-072  | 24    | 88  | 3.67  | 46       | 28       | 3  | 4  | 5   | 2   | 7   | 0.29  | 4        | 2        | 0  | 1  | 0   | 0   |
| Thomas Partey          | MF,DF   | 31-287  | 24.3  | 51  | 2.1   | 41       | 2        | 1  | 2  | 1   | 4   | 12  | 0.49  | 7        | 2        | 0  | 1  | 1   | 1   |
| Leandro Trossard       | FW      | 30-113  | 21.1  | 71  | 3.37  | 56       | 2        | 4  | 4  | 1   | 6   | 6   | 0.28  | 6        | 0        | 0  | 0  | 0   | 0   |
| Kai Havertz            | FW,MF   | 25-289  | 20.4  | 41  | 2.01  | 34       | 0        | 1  | 6  | 0   | 0   | 3   | 0.15  | 2        | 0        | 0  | 1  | 0   | 0   |
| Martin Ødegaard        | MF      | 26-100  | 19.2  | 89  | 4.65  | 73       | 9        | 2  | 4  | 1   | 0   | 10  | 0.52  | 9        | 1        | 0  | 0  | 0   | 0   |
| Gabriel Martinelli     | FW,MF   | 23-282  | 17.4  | 45  | 2.58  | 37       | 1        | 5  | 1  | 1   | 0   | 4   | 0.23  | 3        | 0        | 1  | 0  | 0   | 0   |
| Bukayo Saka            | FW,MF   | 23-203  | 14.1  | 89  | 6.32  | 52       | 17       | 9  | 8  | 3   | 0   | 21  | 1.49  | 12       | 5        | 2  | 1  | 1   | 0   |
| Mikel Merino           | MF,FW   | 28-278  | 12.8  | 35  | 2.74  | 31       | 0        | 0  | 3  | 1   | 0   | 3   | 0.23  | 3        | 0        | 0  | 0  | 0   | 0   |
| Riccardo Calafiori     | DF      | 22-312  | 10.3  | 13  | 1.26  | 11       | 0        | 1  | 1  | 0   | 0   | 2   | 0.19  | 2        | 0        | 0  | 0  | 0   | 0   |
| Myles Lewis-Skelly     | DF      | 18-182  | 8.5   | 9   | 1.06  | 7        | 0        | 0  | 0  | 2   | 0   | 0   | 0     | 0        | 0        | 0  | 0  | 0   | 0   |
| Ben White              | DF      | 27-170  | 7.8   | 9   | 1.15  | 9        | 0        | 0  | 0  | 0   | 0   | 1   | 0.13  | 1        | 0        | 0  | 0  | 0   | 0   |
| Ethan Nwaneri          | FW,MF   | 18-006  | 6.7   | 16  | 2.37  | 8        | 2        | 3  | 2  | 1   | 0   | 2   | 0.3   | 2        | 0        | 0  | 0  | 0   | 0   |
| Jorginho               | MF      | 33-097  | 6     | 9   | 1.49  | 8        | 0        | 0  | 0  | 0   | 1   | 0   | 0     | 0        | 0        | 0  | 0  | 0   | 0   |
| Gabriel Jesus          | FW      | 27-358  | 6.8   | 18  | 2.66  | 10       | 0        | 1  | 5  | 1   | 1   | 4   | 0.59  | 1        | 0        | 0  | 3  | 0   | 0   |
| Raheem Sterling        | FW,MF   | 30-109  | 3.4   | 12  | 3.48  | 8        | 0        | 2  | 2  | 0   | 0   | 1   | 0.29  | 1        | 0        | 0  | 0  | 0   | 0   |
| Jakub Kiwior           | DF      | 25-040  | 3.6   | 1   | 0.28  | 1        | 0        | 0  | 0  | 0   | 0   | 0   | 0     | 0        | 0        | 0  | 0  | 0   | 0   |
| Oleksandr Zinchenko    | DF,MF   | 28-102  | 3.3   | 9   | 2.71  | 7        | 0        | 0  | 2  | 0   | 0   | 1   | 0.3   | 1        | 0        | 0  | 0  | 0   | 0   |
| Kieran Tierney         | DF,FW   | 27-295  | 0.9   | 3   | 3.33  | 3        | 0        | 0  | 0  | 0   | 0   | 0   | 0     | 0        | 0        | 0  | 0  | 0   | 0   |
| Takehiro Tomiyasu      | DF      | 26-142  | 0.1   | 1   | 12.86 | 1        | 0        | 0  | 0  | 0   | 0   | 0   | 0     | 0        | 0        | 0  | 0  | 0   | 0   |
| Reiss Nelson           | FW      | 25-107  | 0     | 0   | 0     | 0        | 0        | 0  | 0  | 0   | 0   | 0   | 0     | 0        | 0        | 0  | 0  | 0   | 0   |
| Squad Total            | NaN     |         | 26.5  | 29  | 716   | 24.69    | 538      | 63 | 35 | 47  | 23  | 10  | 91    | 3.14     | 65       | 10 | 4  | 8   | 3   | 1   |
| Opponent Total         | NaN     |         | 26.8  | 29  | 507   | 17.48    | 386      | 30 | 24 | 28  | 27  | 12  | 44    | 1.52     | 28       | 4  | 1  | 3   | 6   | 2   |
```

### Description of the Table

The table presents data related to the performance of the Arsenal football team, specifically focusing on player statistics in terms of possession and defensive actions during matches. Each row corresponds to a player, while the columns provide various metrics that quantify their contributions on the field. 

The columns include:

- **Player**: The name of the player.
- **Pos**: The position the player occupies on the field.
- **Age**: The age of the player.
- **90s**: The number of matches played expressed in 90-minute intervals.
- **Tkl**: Total tackles made by the player.
- **TklW**: Successful tackles (tackles won).
- **Def 3rd**: Defensive actions in the defensive third of the field.
- **Mid 3rd**: Defensive actions in the midfield third.
- **Att 3rd**: Defensive actions in the attacking third.
- **Challenges**: Total challenges made.
- **Tkl%**: Tackle success percentage.
- **Lost**: Number of tackles lost.
- **Blocks**: Total blocks made.
- **Sh**: Shots taken.
- **Pass**: Passes completed.
- **Int**: Interceptions made.
- **Tkl+Int**: Combined total of tackles and interceptions.
- **Clr**: Clearances made.
- **Err**: Errors leading to goals.

The table also includes summary rows for the total statistics of the squad and the opponent, providing a comparative overview of performance.

### Markdown Table

```markdown
| Player                | Pos     | Age     | 90s   | Tkl | TklW | Def 3rd | Mid 3rd | Att 3rd | Challenges | Tkl | Att | Tkl%  | Lost | Blocks | Sh | Pass | Int | Tkl+Int | Clr | Err |
|----------------------|---------|---------|-------|-----|------|---------|---------|---------|------------|-----|-----|-------|------|--------|----|------|-----|---------|-----|-----|
| David Raya           | GK      | 29-193  | 29    | 0   | 0    | 0       | 0       | 0       | 0          | 1   | 0   | 100   | 0    | 0      | 2  | 2    | 16  | 4       |
| William Saliba       | DF      | 24-003  | 26.3  | 50  | 31   | 30      | 18      | 2       | 17         | 23  | 73.9| 6     | 18   | 11     | 7  | 19   | 69  | 85      | 4   |
| Gabriel Magalhães    | DF      | 27-098  | 26.1  | 25  | 15   | 12      | 8       | 5       | 12         | 16  | 75  | 4     | 42   | 29     | 13 | 15   | 40  | 93      | 2   |
| Jurriën Timber       | DF      | 23-283  | 24.4  | 52  | 34   | 14      | 27      | 11      | 16         | 24  | 66.7| 8     | 18   | 4      | 14 | 21   | 73  | 44      | 1   |
| Declan Rice          | MF      | 26-072  | 24    | 41  | 18   | 17      | 18      | 6       | 13         | 31  | 41.9| 18    | 19   | 10     | 9  | 20   | 61  | 36      | 0   |
| Thomas Partey        | MF,DF   | 31-287  | 24.3  | 76  | 46   | 23      | 33      | 20      | 40         | 62  | 64.5| 22    | 19   | 6      | 13 | 28   | 104 | 38      | 4   |
| Leandro Trossard     | FW      | 30-113  | 21.1  | 24  | 16   | 5       | 14      | 5       | 8          | 27  | 29.6| 19    | 23   | 0      | 23 | 9    | 33  | 16      | 0   |
| Kai Havertz          | FW,MF   | 25-289  | 20.4  | 16  | 9    | 3       | 6       | 7       | 4          | 15  | 26.7| 11    | 22   | 4      | 18 | 6    | 22  | 31      | 1   |
| Martin Ødegaard      | MF      | 26-100  | 19.2  | 16  | 9    | 7       | 6       | 3       | 3          | 21  | 14.3| 18    | 4    | 0      | 4  | 3    | 19  | 4       | 0   |
| Gabriel Martinelli    | FW,MF   | 23-282  | 17.4  | 18  | 13   | 6       | 5       | 7       | 6          | 20  | 30  | 14    | 10   | 0      | 10 | 3    | 21  | 13      | 0   |
| Bukayo Saka          | FW,MF   | 23-203  | 14.1  | 22  | 13   | 5       | 10      | 7       | 9          | 19  | 47.4| 10    | 16   | 0      | 16 | 2    | 24  | 7       | 0   |
| Mikel Merino         | MF,FW   | 28-278  | 12.8  | 27  | 16   | 5       | 15      | 7       | 10         | 22  | 45.5| 12    | 17   | 5      | 12 | 39   | 18  | 1       |
| Riccardo Calafiori   | DF      | 22-312  | 10.3  | 26  | 18   | 15      | 9       | 2       | 18         | 29  | 62.1| 11    | 12   | 6      | 6  | 6    | 9   | 35      | 25  | 0   |
| Myles Lewis-Skelly   | DF      | 18-182  | 8.5   | 20  | 13   | 10      | 9       | 1       | 9          | 9   | 100 | 0     | 0    | 0      | 0  | 0    | 0   | 5       | 25  | 13  | 0   |
| Ben White            | DF      | 27-170  | 7.8   | 10  | 6    | 8       | 1       | 1       | 9          | 21  | 42.9| 12    | 7    | 6      | 1  | 11   | 21  | 23      | 0   |
| Ethan Nwaneri        | FW,MF   | 18-006  | 6.7   | 9   | 6    | 4       | 2       | 3       | 5          | 14  | 35.7| 9     | 7    | 1      | 6  | 1    | 10  | 2       | 1   |
| Jorginho             | MF      | 33-097  | 6     | 10  | 3    | 1       | 7       | 2       | 6          | 16  | 37.5| 10    | 2    | 0      | 2  | 5    | 15  | 2       | 2   |
| Gabriel Jesus        | FW      | 27-358  | 6.8   | 10  | 6    | 4       | 3       | 3       | 4          | 9   | 44.4| 5     | 10   | 1      | 9  | 4    | 14  | 8       | 0   |
| Raheem Sterling      | FW,MF   | 30-109  | 3.4   | 6   | 4    | 0       | 2       | 4       | 3          | 5   | 60  | 2     | 2    | 0      | 2  | 1    | 7   | 2       | 0   |
| Jakub Kiwior         | DF      | 25-040  | 3.6   | 4   | 2    | 3       | 1       | 0       | 3          | 5   | 60  | 2     | 5    | 2      | 3  | 1    | 5   | 16      | 1   |
| Oleksandr Zinchenko  | DF,MF   | 28-102  | 3.3   | 2   | 0    | 1       | 1       | 0       | 1          | 4   | 25  | 3     | 5    | 0      | 5  | 3    | 5   | 5       | 0   |
| Kieran Tierney       | DF,FW   | 27-295  | 0.9   | 2   | 1    | 1       | 0       | 1       | 0          | 2   | 0   | 0     | 0    | 0      | 0  | 1    | 3   | 2       | 0   |
| Takehiro Tomiyasu    | DF      | 26-142  | 0.1   | 0   | 0    | 0       | 0       | 0       | 0          | 0   | NaN | 0     | 0    | 0      | 0  | 0    | 0   | 0       | 0   |
| Reiss Nelson         | FW      | 25-107  | 0     | 1   | 0    | 0       | 1       | 0       | 0          | 1   | 0   | 1     | 0    | 0      | 0  | 0    | 0   | 1       | 1   | 0   |
| Squad Total          | NaN     |         | 26.5  | 29  | 467  | 279     | 174     | 196     | 97         | 196 | 396 | 49.5  | 200  | 258    | 85 | 173  | 181 | 648     | 501 | 21  |
| Opponent Total       | NaN     |         | 26.8  | 29  | 551  | 332     | 327     | 166     | 58         | 250 | 497 | 50.3  | 247  | 296    | 125| 171  | 198 | 749     | 782 | 27  |
```

### Description of the Table

The table presents detailed statistics for players from the Arsenal football team, focusing on their playing time and performance metrics during matches. Each row corresponds to a player, while the columns provide various statistics related to their playing time, touches, defensive actions, carries, and receiving metrics. 

The columns include:

- **Player**: The name of the player.
- **Pos**: The position(s) the player occupies on the field.
- **Age**: The age of the player.
- **90s**: The number of full matches played (in 90-minute equivalents).
- **Touches**: The total number of touches the player had during the matches.
- **Def Pen**: Defensive actions in the penalty area.
- **Def 3rd**: Defensive actions in the defensive third of the field.
- **Mid 3rd**: Defensive actions in the midfield third.
- **Att 3rd**: Defensive actions in the attacking third.
- **Att Pen**: Attacking actions in the penalty area.
- **Live**: Live actions taken by the player.
- **Att Succ**: Successful attacking actions.
- **Succ%**: Success percentage of attacking actions.
- **Tkld**: Number of tackles made.
- **Tkld%**: Tackle success percentage.
- **Carries**: Number of carries made by the player.
- **TotDist**: Total distance covered by the player.
- **PrgDist**: Progressive distance covered.
- **PrgC**: Progressive carries.
- **1/3**: Actions in the final third.
- **CPA**: Chances created.
- **Mis**: Missed opportunities.
- **Dis**: Dispossessions.
- **Rec**: Recoveries.
- **PrgR**: Progressive runs.

The last two rows summarize the total statistics for the squad and the opponent, providing an overview of the team's performance as a whole.

### Table in Markdown Format

```markdown
| Player                  | Pos     | Age     | 90s  | Touches | Def Pen | Def 3rd | Mid 3rd | Att 3rd | Att Pen | Live | Att Succ | Succ% | Tkld | Tkld% | Carries | TotDist | PrgDist | PrgC | 1/3 | CPA | Mis | Dis | Rec | PrgR |
|-------------------------|---------|---------|------|---------|---------|---------|----------|----------|---------|------|----------|-------|------|-------|---------|---------|---------|------|-----|-----|-----|-----|-----|------|
| David Raya              | GK      | 29-193  | 29   | 1106    | 661     | 1035    | 71       | 0        | 0       | 1106 | 1        | 100   | 0    | 0     | 690     | 3456    | 2046    | 0    | 0   | 0   | 1   | 0   | 628 | 0    |
| William Saliba          | DF      | 24-003  | 26.3 | 2129    | 148     | 847     | 1185     | 108      | 14      | 2129 | 15       | 60    | 5    | 33.3  | 1303    | 5639    | 2873    | 13   | 10  | 0   | 15  | 5   | 1574 | 6    |
| Gabriel Magalhães      | DF      | 27-098  | 26.1 | 1859    | 189     | 669     | 974      | 225      | 40      | 1859 | 5        | 80    | 1    | 20    | 1108    | 4449    | 2656    | 10   | 22  | 0   | 9   | 2   | 1357 | 11   |
| Jurriën Timber          | DF      | 23-283  | 24.4 | 1487    | 50      | 272     | 761      | 461      | 63      | 1487 | 51       | 45.1  | 23   | 45.1  | 796     | 3451    | 1843    | 51   | 25  | 11  | 31  | 22  | 922  | 97   |
| Declan Rice             | MF      | 26-072  | 24   | 1526    | 56      | 248     | 727      | 565      | 55      | 1526 | 23       | 43.5  | 12   | 52.2  | 821     | 5181    | 2771    | 75   | 50  | 11  | 29  | 20  | 1008 | 76   |
| Thomas Partey           | MF,DF   | 31-287  | 24.3 | 1727    | 57      | 355     | 938      | 443      | 22      | 1727 | 25       | 60    | 8    | 32    | 961     | 5102    | 2718    | 29   | 32  | 1   | 19  | 11  | 1215 | 37   |
| Leandro Trossard        | FW      | 30-113  | 21.1 | 932     | 13      | 105     | 281      | 561      | 108     | 932  | 65       | 27    | 41.5 | 29    | 44.6    | 592     | 3684    | 1652 | 64  | 41  | 22  | 42  | 36   | 689  | 172  |
| Kai Havertz             | FW,MF   | 25-289  | 20.4 | 768     | 31      | 88      | 282      | 403      | 103     | 768  | 38       | 9     | 23.7 | 24    | 63.2    | 411     | 1957    | 922  | 34  | 23  | 18  | 42  | 22   | 575  | 110  |
| Martin Ødegaard         | MF      | 26-100  | 19.2 | 1234    | 6       | 85      | 511      | 650      | 78      | 1233 | 45       | 20    | 44.4 | 24    | 53.3    | 847     | 5139    | 2581 | 62  | 54  | 18  | 25  | 36   | 984  | 118  |
| Gabriel Martinelli      | FW,MF   | 23-282  | 17.4 | 694     | 12      | 73      | 190      | 442      | 124     | 694  | 93       | 27    | 29   | 50    | 53.8    | 451     | 3377    | 1785 | 87  | 26  | 39  | 38  | 29   | 510  | 199  |
| Bukayo Saka             | FW,MF   | 23-203  | 14.1 | 733     | 6       | 40      | 163      | 536      | 115     | 732  | 73       | 33    | 45.2 | 29    | 39.7    | 463     | 3196    | 1846 | 72  | 19  | 37  | 24  | 35   | 526  | 195  |
| Mikel Merino            | MF,FW   | 28-278  | 12.8 | 593     | 28      | 109     | 251      | 242      | 60      | 593  | 13       | 6     | 46.2 | 5     | 38.5    | 297     | 1059    | 480  | 7   | 10  | 4   | 19  | 20   | 390  | 70   |
| Riccardo Calafiori      | DF      | 22-312  | 10.3 | 628     | 30      | 161     | 249      | 222      | 29      | 628  | 13       | 9     | 69.2 | 3     | 23.1    | 291     | 1572    | 839  | 21  | 12  | 3   | 11  | 5    | 377  | 29   |
| Myles Lewis-Skelly      | DF      | 18-182  | 8.5  | 486     | 11      | 83      | 264      | 147      | 11      | 486  | 15       | 8     | 53.3 | 5     | 33.3    | 263     | 1250    | 721  | 15  | 8   | 4   | 5   | 5    | 316  | 19   |
| Ben White               | DF      | 27-170  | 7.8  | 437     | 38      | 139     | 197      | 103      | 9       | 437  | 2        | 0     | 0    | 0     | 1       | 50      | 202     | 731  | 363 | 5   | 8   | 1   | 7    | 3    | 260  | 18   |
| Ethan Nwaneri           | FW,MF   | 18-006  | 6.7  | 361     | 2       | 37      | 123      | 204      | 26      | 361  | 44       | 26    | 59.1 | 13    | 29.5    | 250     | 1992    | 978  | 35  | 16  | 13  | 14  | 15   | 267  | 84   |
| Jorginho                | MF      | 33-097  | 6    | 396     | 7       | 78      | 228      | 95       | 2       | 396  | 3        | 1     | 33.3 | 1     | 33.3    | 231     | 1152    | 660  | 9   | 8   | 0   | 8   | 8    | 290  | 3    |
| Gabriel Jesus           | FW      | 27-358  | 6.8  | 299     | 9       | 28      | 108      | 165      | 48      | 299  | 22       | 9     | 40.9 | 10    | 45.5    | 179     | 953     | 432  | 15  | 6   | 11  | 13  | 13   | 217  | 57   |
| Raheem Sterling         | FW,MF   | 30-109  | 3.4  | 186     | 1       | 3       | 38       | 147      | 30      | 186  | 18       | 8     | 44.4 | 5     | 27.8    | 138     | 940     | 519  | 18  | 8   | 14  | 8   | 12   | 145  | 57   |
| Jakub Kiwior            | DF      | 25-040  | 3.6  | 202     | 31      | 91      | 103      | 8        | 0       | 202  | 2        | 1     | 50   | 1     | 50      | 94      | 333     | 153  | 1   | 0   | 0   | 0   | 0    | 138  | 0    |
| Oleksandr Zinchenko     | DF,MF   | 28-102  | 3.3  | 263     | 10      | 57      | 144      | 63       | 14      | 263  | 2        | 1     | 50   | 0     | 0       | 144     | 771     | 331  | 7   | 3   | 2   | 2   | 2    | 169  | 7    |
| Kieran Tierney          | DF,FW   | 27-295  | 0.9  | 42      | 1       | 6       | 15       | 21       | 3       | 42   | 1        | 0     | 0    | 1     | 100     | 16      | 80      | 49   | 2   | 1   | 1   | 1   | 0    | 30   | 8    |
| Takehiro Tomiyasu      | DF      | 26-142  | 0.1  | 7       | 1       | 4       | 1        | 2        | 1       | 7    | 0        | 0     | NaN  | 0     | NaN     | 1       | 7       | 5    | 0   | 0   | 0   | 0   | 0    | 2    | 0    |
| Reiss Nelson            | FW      | 25-107  | 0    | 2       | 0       | 1       | 1        | 0        | 0       | 2    | 0        | 0     | NaN  | 0     | NaN     | 1       | 4       | 4    | 0   | 0   | 0   | 0   | 0    | 1    | 0    |
| Squad Total             | NaN     | 26.5    | 29   | 18097   | 1398    | 4614    | 7805     | 5813     | 955     | 18095| 569      | 247   | 43.4 | 250   | 43.9    | 10550   | 55475   | 29227| 632 | 382 | 210 | 363 | 301  | 12590| 1373 |
| Opponent Total          | NaN     | 26.8    | 29   | 15061   | 2244    | 5849    | 5880     | 3510     | 472     | 15059| 466      | 200   | 42.9 | 196   | 42.1    | 8124    | 45128   | 23744| 491 | 332 | 125 | 343 | 271  | 9492 | 730  |
```

### Description of the Table

The table presents miscellaneous statistics for the Arsenal football team, detailing player performance metrics for a specific season. Each row corresponds to a player, while the columns contain various statistics related to their playing time, performance, and contributions on the field. 

The columns include:
- **Player Information**: Player name, position (Pos), age, and match appearances (MP).
- **Playing Time**: Number of starts, total minutes played, and the number of 90-minute matches (90s).
- **Performance Metrics**: Goals scored (Gls), assists (Ast), total goal contributions (G+A), goals minus penalties (G-PK), penalties awarded (PK), and penalties taken (PKatt).
- **Disciplinary Records**: Yellow cards (CrdY) and red cards (CrdR).
- **Expected Goals (xG)**: Expected goals (xG), non-penalty expected goals (npxG), expected assists (xAG), and the sum of non-penalty expected goals and expected assists (npxG+xAG).
- **Progression Metrics**: Progressive carries (PrgC), progressive passes (PrgP), and progressive runs (PrgR).
- **Per 90 Minutes Statistics**: Goals, assists, and goal contributions per 90 minutes, along with their respective metrics adjusted for penalties.

The last two rows summarize the total statistics for the squad and the opponent totals, providing an overview of the team's performance in comparison to their opponents.

### Table in Markdown Format

```markdown
|    | Player                  | Pos     | Age     | MP | Starts | Min  | 90s  | Gls | Ast | G+A | G-PK | PK | PKatt | CrdY | CrdR | xG  | npxG | xAG | npxG+xAG | PrgC | PrgP | PrgR | Gls | Ast | G+A | G-PK | G+A-PK | xG  | xAG | xG+xAG | npxG | npxG+xAG |
|----|------------------------|---------|---------|----|--------|------|------|-----|-----|-----|------|----|-------|------|------|-----|------|-----|----------|------|------|------|-----|-----|-----|------|---------|-----|-----|--------|------|-----------|
| 0  | NaN                    | Player  | Pos     | Age| MP     | Starts| Min  | 90s | Gls | Ast | G+A | G-PK | PK | PKatt | CrdY | CrdR | xG  | npxG | xAG | npxG+xAG | PrgC | PrgP | PrgR | Gls | Ast | G+A | G-PK | G+A-PK | xG  | xAG | xG+xAG | npxG | npxG+xAG |
| 1  | NaN                    | NaN     | NaN     | NaN| NaN    | NaN   | NaN  | NaN | NaN | NaN | NaN | NaN | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 2  | David Raya             | GK      | 29-193  | 29 | 29     | 2610 | 29   | 0   | 0   | 0   | 0    | 0  | 0     | 2    | 0    | 0   | 0    | 0   | 0        | 0    | 0    | 0    | 11  | 0   | 0   | 0    | 0       | 0   | 0   | 0      | 0    | 0         |
| 3  | William Saliba        | DF      | 24-003  | 27 | 27     | 2364 | 26.3 | 2   | 0   | 2   | 2    | 0  | 0     | 2    | 1    | 2.1 | 2.1  | 0.5 | 2.6      | 13   | 113  | 6    | 0.08| 0   | 0.08| 0.08 | 0.08   | 0.02| 0.1 | 0.08   | 0.1  | 0.1       |
| 4  | Gabriel Magalhães     | DF      | 27-098  | 27 | 27     | 2348 | 26.1 | 3   | 1   | 4   | 3    | 0  | 0     | 4    | 0    | 2.6 | 2.6  | 0.9 | 3.5      | 10   | 124  | 11   | 0.11| 0.04| 0.15| 0.11 | 0.15   | 0.1 | 0.03| 0.13   | 0.1  | 0.13      |
| 5  | Jurriën Timber        | DF      | 23-283  | 26 | 25     | 2199 | 24.4 | 1   | 2   | 3   | 1    | 0  | 0     | 7    | 0    | 0.7 | 0.7  | 0.8 | 1.5      | 51   | 134  | 97   | 0.04| 0.08| 0.12| 0.04 | 0.12   | 0.03| 0.03| 0.06   | 0.03 | 0.06      |
| 6  | Declan Rice           | MF      | 26-072  | 27 | 25     | 2156 | 24   | 2   | 5   | 7   | 2    | 0  | 0     | 5    | 1    | 2   | 2    | 5.7 | 7.7      | 75   | 149  | 76   | 0.08| 0.21| 0.29| 0.08 | 0.29   | 0.08| 0.24| 0.32   | 0.08 | 0.32      |
| 7  | Thomas Partey         | MF,DF   | 31-287  | 28 | 24     | 2189 | 24.3 | 3   | 2   | 5   | 3    | 0  | 0     | 4    | 0    | 1.7 | 1.7  | 1.9 | 3.6      | 29   | 150  | 37   | 0.12| 0.08| 0.21| 0.12 | 0.21   | 0.07| 0.08| 0.15   | 0.07 | 0.15      |
| 8  | Leandro Trossard      | FW      | 30-113  | 29 | 21     | 1897 | 21.1 | 4   | 5   | 9   | 4    | 0  | 0     | 4    | 1    | 5.1 | 5.1  | 5   | 10.1     | 64   | 81   | 172  | 0.19| 0.24| 0.43| 0.19 | 0.43   | 0.24| 0.24| 0.48   | 0.24 | 0.48      |
| 9  | Kai Havertz           | FW,MF   | 25-289  | 21 | 21     | 1839 | 20.4 | 9   | 3   | 12  | 9    | 0  | 0     | 4    | 0    | 9.4 | 9.4  | 2.4 | 11.8     | 34   | 59   | 110  | 0.44| 0.15| 0.59| 0.44 | 0.59   | 0.46| 0.12| 0.58   | 0.46 | 0.58      |
| 10 | Martin Ødegaard       | MF      | 26-100  | 21 | 20     | 1726 | 19.2 | 2   | 4   | 6   | 1    | 1  | 1     | 3    | 0    | 3.7 | 2.9  | 3.7 | 6.7      | 62   | 185  | 118  | 0.1 | 0.21| 0.31| 0.05 | 0.26   | 0.19| 0.19| 0.39   | 0.15 | 0.35      |
| 11 | Gabriel Martinelli     | FW,MF   | 23-282  | 24 | 17     | 1569 | 17.4 | 6   | 3   | 9   | 6    | 0  | 0     | 1    | 0    | 4.5 | 4.5  | 3   | 7.5      | 87   | 32   | 199  | 0.34| 0.17| 0.52| 0.34 | 0.52   | 0.26| 0.17| 0.43   | 0.26 | 0.43      |
| 12 | Bukayo Saka           | FW,MF   | 23-203  | 16 | 16     | 1268 | 14.1 | 5   | 10  | 15  | 4    | 1  | 1     | 3    | 0    | 4.2 | 3.4  | 5.8 | 9.2      | 72   | 53   | 195  | 0.35| 0.71| 1.06| 0.28 | 0.99   | 0.3 | 0.41| 0.71   | 0.24 | 0.65      |
| 13 | Mikel Merino          | MF,FW   | 28-278  | 21 | 12     | 1149 | 12.8 | 5   | 1   | 6   | 5    | 0  | 0     | 2    | 0    | 3.7 | 3.7  | 1.4 | 5.1      | 7    | 53   | 70   | 0.39| 0.08| 0.47| 0.39 | 0.47   | 0.29| 0.11| 0.4    | 0.29 | 0.4       |
| 14 | Riccardo Calafiori    | DF      | 22-312  | 17 | 11     | 925  | 10.3 | 2   | 1   | 3   | 2    | 0  | 0     | 4    | 0    | 0.9 | 0.9  | 0.3 | 1.1      | 21   | 54   | 29   | 0.19| 0.1 | 0.29| 0.19 | 0.29   | 0.08| 0.03| 0.11   | 0.08 | 0.11      |
| 15 | Myles Lewis-Skelly    | DF      | 18-182  | 14 | 9      | 766  | 8.5  | 1   | 0   | 1   | 1    | 0  | 0     | 2    | 2    | 0   | 0    | 0.2 | 0.2      | 15   | 37   | 19   | 0.12| 0   | 0.12| 0.12 | 0.12   | 0   | 0.02| 0.03   | 0   | 0.03      |
| 16 | Ben White             | DF      | 27-170  | 11 | 7      | 706  | 7.8  | 0   | 1   | 1   | 0    | 0  | 0     | 2    | 0    | 0.2 | 0.2  | 0.4 | 0.6      | 5    | 32   | 18   | 0   | 0.13| 0.13| 0   | 0.13   | 0.02| 0.06| 0.08   | 0.02 | 0.08      |
| 17 | Ethan Nwaneri         | FW,MF   | 18-006  | 19 | 7      | 606  | 6.7  | 3   | 1   | 4   | 3    | 0  | 0     | 1    | 0    | 0.8 | 0.8  | 0.8 | 1.6      | 35   | 24   | 84   | 0.45| 0.15| 0.59| 0.45 | 0.59   | 0.12| 0.12| 0.24   | 0.12 | 0.24      |
| 18 | Jorginho              | MF      | 33-097  | 12 | 7      | 543  | 6    | 0   | 0   | 0   | 0    | 0  | 0     | 4    | 0    | 0   | 0    | 0.4 | 0.5      | 9    | 37   | 3    | 0   | 0   | 0   | 0    | 0       | 0   | 0.01| 0.07   | 0.08 | 0.01      |
| 19 | Gabriel Jesus         | FW      | 27-358  | 17 | 6      | 608  | 6.8  | 3   | 0   | 3   | 3    | 0  | 0     | 4    | 0    | 3   | 3    | 0.7 | 3.7      | 15   | 19   | 57   | 0.44| 0   | 0.44| 0.44 | 0.44   | 0.44| 0.1 | 0.54   | 0.44 | 0.54      |
| 20 | Raheem Sterling       | FW,MF   | 30-109  | 12 | 4      | 310  | 3.4  | 0   | 1   | 1   | 0    | 0  | 0     | 1    | 0    | 1   | 1    | 0.3 | 1.3      | 18   | 14   | 57   | 0   | 0.29| 0.29| 0   | 0.29   | 0.3 | 0.08| 0.38   | 0.3  | 0.38      |
| 21 | Jakub Kiwior          | DF      | 25-040  | 8  | 2      | 327  | 3.6  | 0   | 0   | 0   | 0    | 0  | 0     | 0    | 0    | 0   | 0    | 0.1 | 0.1      | 1    | 8    | 0    | 0   | 0   | 0   | 0    | 0       | 0   | 0.02| 0.02   | 0    | 0.02      |
| 22 | Oleksandr Zinchenko   | DF,MF   | 28-102  | 10 | 2      | 299  | 3.3  | 0   | 0   | 0   | 0    | 0  | 0     | 1    | 0    | 0.2 | 0.2  | 0   | 0.2      | 7    | 21   | 7    | 0   | 0   | 0   | 0    | 0       | 0   | 0.05| 0.01   | 0.05 | 0.05      |
| 23 | Kieran Tierney        | DF,FW   | 27-295  | 6  | 0      | 81   | 0.9  | 0   | 0   | 0   | 0    | 0  | 0     | 0    | 0    | 0.2 | 0.2  | 0.5 | 0.7      | 2    | 3    | 8    | 0   | 0   | 0   | 0    | 0       | 0   | 0.23| 0.54   | 0.77 | 0.23      |
| 24 | Takehiro Tomiyasu     | DF      | 26-142  | 1  | 0      | 7    | 0.1  | 0   | 0   | 0   | 0    | 0  | 0     | 0    | 0    | 0.2 | 0.2  | 0   | 0.2      | 0    | 1    | 0    | 0   | 0   | 0   | 0    | 0       | 0   | 2.37| 0      | 2.37 | 2.37      |
| 25 | Reiss Nelson          | FW      | 25-107  | 1  | 0      | 3    | 0    | 0   | 0   | 0   | 0    | 0  | 0     | 0    | 0    | 0   | 0    | 0   | 0        | 0    | 0    | 0    | 0   | 0   | 0   | 0    | 0       | 0   | 0   | 0      | 0    | 0         |
| 26 | Nathan Butler-Oyedeji | FW      | 22-082  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 27 | Ayden Heaven          | DF      | 18-186  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 28 | Ismeal Kabia         | MF      | 19-107  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 29 | Maldini Kacurri      | DF      | 19-174  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 30 | Neto                  | GK      | 35-251  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 31 | Josh Nichols          | DF      | 18-244  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 32 | Eddie Nketiah        | FW      | 25-301  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 33 | Salah Oulad M'Hand    | MF      | 21-219  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 34 | Jack Porter           | GK      | 16-255  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 35 | Aaron Ramsdale        | GK      | 26-317  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 36 | Tommy Setford         | GK      | 19-014  | 0  | 0      | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN| NaN   | NaN  | NaN  | NaN | NaN  | NaN | NaN      | NaN  | NaN  | NaN  | NaN | NaN | NaN | NaN  | NaN     | NaN | NaN | NaN    | NaN  | NaN       |
| 37 | Squad Total           | NaN     | 26.5    | 29 | 319    | 2610 | 29   | 51  | 40  | 91  | 49   | 2  | 2     | 60   | 5    | 44.5| 43   | 33.9| 76.9     | 632  | 1394 | 1373 | 1.76| 1.38| 3.14| 1.69 | 3.07   | 1.54| 1.17| 2.71   | 1.48 | 2.65      |
| 38 | Opponent Total        | NaN     | 26.8    | 29 | 319    | 2610 | 29   | 24  | 17  | 41  | 22   | 2  | 2     | 68   | 1    | 24.7| 23.2 | 17.1| 40.3     | 491  | 738  | 730  | 0.83| 0.59| 1.41| 0.76 | 1.34   | 0.85| 0.59| 1.44   | 0.8  | 1.39      |
```

### Description of the Table

The table presents performance statistics for the Arsenal football team, specifically focusing on individual player metrics. Each row corresponds to a player, while the columns provide various performance indicators. The columns include:

- **Player**: The name of the player.
- **Pos**: The position(s) the player occupies on the field.
- **Age**: The age of the player, formatted as years and days.
- **90s**: The number of full 90-minute matches played.
- **CrdY**: The number of yellow cards received.
- **CrdR**: The number of red cards received.
- **2CrdY**: The number of times a player received two yellow cards in a match (resulting in a red card).
- **Fls**: The number of fouls committed.
- **Fld**: The number of fouls suffered.
- **Off**: The number of offsides.
- **Crs**: The number of crosses made.
- **Int**: The number of interceptions.
- **TklW**: The number of tackles won.
- **PKwon**: The number of penalties won.
- **PKcon**: The number of penalties conceded.
- **OG**: The number of own goals scored.
- **Recov**: The number of recoveries made.
- **Won**: The number of duels won.
- **Lost**: The number of duels lost.
- **Won%**: The percentage of duels won.

The table also includes summary rows for the total performance of the squad and the opponent's total performance, providing a comparative overview of the team's statistics.

### Table in Markdown Format

```markdown
| Player                | Pos     | Age     | 90s   | CrdY | CrdR | 2CrdY | Fls | Fld | Off | Crs | Int | TklW | PKwon | PKcon | OG | Recov | Won | Lost | Won%  |
|----------------------|---------|---------|-------|------|------|-------|-----|-----|-----|-----|-----|------|-------|-------|----|-------|-----|------|-------|
| David Raya           | GK      | 29-193  | 0.0   | 29   | 2    | 0     | 0   | 1   | 7   | 0   | 0   | 2    | 0     | 0     | 1  | 0     | 27  | 8    | 0     | 100   |
| William Saliba       | DF      | 24-003  | 1.0   | 26.3 | 2    | 1     | 0   | 26  | 13  | 1   | 3   | 19   | 31    | 0     | 1  | 0     | 118 | 48   | 28    | 63.2  |
| Gabriel Magalhães    | DF      | 27-098  | 2.0   | 26.1 | 4    | 0     | 0   | 19  | 19  | 0   | 9   | 15   | 15    | 1     | 0  | 0     | 62  | 52   | 36    | 59.1  |
| Jurriën Timber       | DF      | 23-283  | 3.0   | 24.4 | 7    | 0     | 0   | 29  | 27  | 6   | 27  | 21   | 34    | 0     | 0  | 0     | 87  | 20   | 19    | 51.3  |
| Declan Rice          | MF      | 26-072  | 4.0   | 24   | 5    | 1     | 1   | 16  | 15  | 1   | 137 | 20   | 18    | 0     | 0  | 0     | 111 | 27   | 20    | 57.4  |
| Thomas Partey        | MF,DF   | 31-287  | 5.0   | 24.3 | 4    | 0     | 0   | 36  | 25  | 1   | 9   | 28   | 46    | 0     | 0  | 0     | 111 | 22   | 16    | 57.9  |
| Leandro Trossard     | FW      | 30-113  | 6.0   | 21.1 | 4    | 1     | 1   | 19  | 36  | 5   | 74  | 9    | 16    | 0     | 0  | 0     | 78  | 5    | 18    | 21.7  |
| Kai Havertz          | FW,MF   | 25-289  | 7.0   | 20.4 | 4    | 0     | 0   | 36  | 21  | 14  | 11  | 6    | 9     | 0     | 0  | 0     | 39  | 62   | 73    | 45.9  |
| Martin Ødegaard      | MF      | 26-100  | 8.0   | 19.2 | 3    | 0     | 0   | 9   | 18  | 1   | 69  | 3    | 9     | 0     | 0  | 0     | 74  | 7    | 5     | 58.3  |
| Gabriel Martinelli    | FW,MF   | 23-282  | 9.0   | 17.4 | 1    | 0     | 0   | 13  | 14  | 7   | 63  | 3    | 13    | 0     | 0  | 0     | 62  | 13   | 22    | 37.1  |
| Bukayo Saka          | FW,MF   | 23-203  | 10.0  | 14.1 | 3    | 0     | 0   | 13  | 32  | 3   | 99  | 2    | 13    | 1     | 0  | 0     | 56  | 8    | 16    | 33.3  |
| Mikel Merino         | MF,FW   | 28-278  | 11.0  | 12.8 | 2    | 0     | 0   | 32  | 15  | 5   | 10  | 12   | 16    | 0     | 0  | 0     | 64  | 42   | 43    | 49.4  |
| Riccardo Calafiori   | DF      | 22-312  | 12.0  | 10.3 | 4    | 0     | 0   | 16  | 6   | 3   | 11  | 9    | 18    | 0     | 0  | 0     | 30  | 22   | 13    | 62.9  |
| Myles Lewis-Skelly   | DF      | 18-182  | 13.0  | 8.5  | 2    | 0     | 0   | 7   | 23  | 0   | 4   | 5    | 13    | 0     | 0  | 0     | 31  | 4    | 6     | 40    |
| Ben White            | DF      | 27-170  | 14.0  | 7.8  | 2    | 0     | 0   | 7   | 3   | 1   | 8   | 11   | 6     | 0     | 0  | 0     | 20  | 10   | 3     | 76.9  |
| Ethan Nwaneri        | FW,MF   | 18-006  | 15.0  | 6.7  | 1    | 0     | 0   | 6   | 4   | 3   | 40  | 1    | 6     | 0     | 0  | 0     | 29  | 3    | 6     | 33.3  |
| Jorginho             | MF      | 33-097  | 16.0  | 6    | 4    | 0     | 0   | 12  | 13  | 0   | 1   | 5    | 3     | 0     | 0  | 0     | 44  | 1    | 4     | 20    |
| Gabriel Jesus        | FW      | 27-358  | 17.0  | 6.8  | 4    | 0     | 0   | 14  | 10  | 9   | 7   | 4    | 6     | 0     | 0  | 0     | 28  | 9    | 18    | 33.3  |
| Raheem Sterling      | FW,MF   | 30-109  | 18.0  | 3.4  | 1    | 0     | 0   | 9   | 3   | 3   | 11  | 1    | 4     | 0     | 0  | 0     | 8   | 1    | 3     | 25    |
| Jakub Kiwior         | DF      | 25-040  | 19.0  | 3.6  | 0    | 0     | 0   | 5   | 1   | 0   | 0   | 1    | 2     | 0     | 0  | 0     | 9   | 5    | 3     | 62.5  |
| Oleksandr Zinchenko  | DF,MF   | 28-102  | 20.0  | 3.3  | 1    | 0     | 0   | 8   | 2   | 1   | 8   | 3    | 0     | 0     | 0  | 0     | 13  | 9    | 8     | 52.9  |
| Kieran Tierney       | DF,FW   | 27-295  | 21.0  | 0.9  | 0    | 0     | 0   | 0   | 0   | 0   | 5   | 1    | 1     | 0     | 0  | 0     | 3   | 3    | 1     | 75    |
| Takehiro Tomiyasu    | DF      | 26-142  | 22.0  | 0.1  | 0    | 0     | 0   | 0   | 0   | 0   | 0   | 0    | 0     | 0     | 0  | 0     | 0   | 0    | 0     | NaN   |
| Reiss Nelson         | FW      | 25-107  | 23.0  | 0    | 0    | 0     | 0   | 1   | 1   | 0   | 0   | 0    | 0     | 0     | 0  | 0     | 0   | 0    | 0     | NaN   |
| Squad Total          | NaN     | 26.5    | 29   | 60   | 5    | 2     | 334 | 308 | 64  | 606 | 181  | 279   | 2     | 2     | 0  | 1104  | 381 | 361  | 51.3  |
| Opponent Total       | NaN     | 26.8    | 29   | 68   | 1    | 1     | 319 | 324 | 31  | 407 | 198  | 332   | 2     | 2     | 2  | 1036  | 361 | 381  | 48.7  |
```

