# Senate Bills API

## Overview

The Senate Bills API provides access to information about proposed bills in the Brazilian Senate. Users can search for bills by number or keywords and retrieve summaries and details about each bill.

## Expected Features

- Users will input a bill number or keywords related to a bill proposal into a search bar.
- The system will display a list of bill proposals that match the user's search query.

## Local Installation

1.  Install the required packages using pip.
```
pip install -r requirements.txt
pip install -e src
```

2. Start the server.
```
python src/gov_proposals_explainer/main.py
```

## Usage

1. Type your search query into the search bar on the home page and click the "Search" button.

2. A list of bill proposals that match your query will be displayed on the results page. Click on a bill proposal to view more information about it.

3. On the bill proposal details page, you can view the bill's title, summary, and status.