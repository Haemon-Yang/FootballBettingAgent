from fake_useragent import UserAgent

class Data:
    ScrappedUrl = "https://fbref.com/en/comps/9/Premier-League-Stats"
    targetTable = "table.stats_table"
    team_data_savePath = r"Teams/"

    @staticmethod
    def get_headers():
        ua = UserAgent()
        return {
            'User-Agent': ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }
    
    # Turn into markdown format & add description (Use LLM)
    team_data_2md_prompt = """
    Given that the following table is a dataframe in string format,
    provide a detailed description of the table. 
    Then, include the table in markdown format while preserving every single row, column and cell exactly as provided. 
    Do not summarize, omit or alter any part of the data.
    When processing markdown tables, please ignore any columns whose header contains 'Unnamed:' as these are likely to be index or placeholder columns. 
    However, if a subsequent row provides meaningful information for an 'Unnamed:' column (i.e. when the first row is only used for alignment or non-informative numbering), please include that data in the output. 
    If the table doesn’t include any 'Unnamed:' columns, process the table normally.

    Table content:
    {table_content}

    Please provide:
        1. A comprehensive description of the table.
        2. The table in markdown format.
    """

    # Dictionary mapping DataFrames to worksheet names
    sheet_names = {
        -1: "Matches",
        0: "Standard Stats",
        1: "Shooting Stats",
        2: "Passing Stats", 
        3: "Pass Types",
        4: "Goal & Shot Creation",
        5: "Defensive Actions",
        6: "Possession",
        7: "Playing Time",
        8: "Miscellaneous Stats"
    }