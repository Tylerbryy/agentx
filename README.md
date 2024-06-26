![AgentX Logo](https://i.ibb.co/xMpPhRs/logo22.png)

# AgentX

AgentX is a comprehensive toolkit designed for use with Large Language Models (LLMs). It provides a variety of tools that can be utilized by LLM agents to perform a wide range of tasks, from date manipulation to statistical analysis, web scraping, and internet searching.

## Features

- **Date Tools**: Perform various date-related operations such as getting the current date, calculating the number of days between dates, and converting dates to different formats.
- **RAG Search Tools**: Search through text files for specific information.
- **Scraping Tools**: Scrape data from websites in a LLM friendly format.
- **Search Tools**: Search the internet for information on various topics.
- **Statistical Tools**: Perform statistical calculations such as mean, median, standard deviation, and more.

## Installation

To install AgentX, run the following command:
```
pip install agentx
```

## Usage

Here are some examples of how to use the various tools provided by AgentX:

### Date Tools

```python
from agentx import AgentX

agent = AgentX()

# Test date tools
print(agent.date_tools.get_current_date.invoke({}))
print(agent.date_tools.get_current_time.invoke({}))
print(agent.date_tools.get_date_after_days.invoke({"days": 5}))
print(agent.date_tools.get_date_before_days.invoke({"days": 5}))
print(agent.date_tools.get_day_of_week({"date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_days_between_dates.invoke({"start_date": {"year": 2023, "month": 6, "day": 1}, "end_date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_first_day_of_month.invoke({"year": 2023, "month": 6}))
print(agent.date_tools.get_last_day_of_month.invoke({"year": 2023, "month": 6}))
print(agent.date_tools.get_next_month.invoke({"year": 2023, "month": 6}))
print(agent.date_tools.get_previous_month.invoke({"year": 2023, "month": 6}))
print(agent.date_tools.get_previous_year.invoke({"year": 2023}))
print(agent.date_tools.get_days_in_month.invoke({"year": 2023, "month": 6}))
print(agent.date_tools.get_week_number.invoke({"date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_quarter.invoke({"month": 6}))
print(agent.date_tools.get_date_from_week_and_year.invoke({"week": 23, "year": 2023}))
print(agent.date_tools.get_date_from_day_of_year.invoke({"day_of_year": 162, "year": 2023}))
print(agent.date_tools.get_day_of_year.invoke({"date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_days_until_end_of_year.invoke({"date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_days_since_beginning_of_year.invoke({"date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_next_weekday.invoke({"date": {"year": 2023, "month": 6, "day": 10}, "weekday": 0}))
print(agent.date_tools.get_previous_weekday.invoke({"date": {"year": 2023, "month": 6, "day": 10}, "weekday": 0}))
print(agent.date_tools.get_nth_weekday_of_month.invoke({"year": 2023, "month": 6, "day": 10, "weekday": 0, "n": 2}))
print(agent.date_tools.get_last_weekday_of_month.invoke({"year": 2023, "month": 6, "weekday": 0}))
print(agent.date_tools.get_age.invoke({"birth_date": {"year": 1990, "month": 1, "day": 1}, "current_date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_date_from_timestamp.invoke({"timestamp": 1686412800}))
print(agent.date_tools.get_timestamp_from_date.invoke({"date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_date_from_iso_format.invoke("2023-06-10"))
print(agent.date_tools.get_iso_format_from_date.invoke({"date": {"year": 2023, "month": 6, "day": 10}}))
print(agent.date_tools.get_date_from_ordinal.invoke({"ordinal": 738532}))
```
### RAG Search Tools

```python
from agentx import AgentX

agent = AgentX()

print(agent.rag_search_tools.search_rag_txt('what is the medical codes for autism?', txt_file=r'path/to/file.txt'))
```

### Scraping Tools
```python
from agentx import AgentX

agent = AgentX()

print(agent.scraping_tools.scrape_website('https://www.nbcnews.com/politics/politics-news/live-blog/hunter-biden-trial-live-updates-rcna156114'))

```
### Search Tools
```python
from agentx import AgentX

agent = AgentX()

print(agent.search_tools.search_internet.invoke('what is hawking radiation?'))

```
### Statistical Tools
```python
from agentx import AgentX

agent = AgentX()

print(agent.statistical_tools.calculate_mean.invoke({"values": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_median.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_std.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_variance.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_min.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_max.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_sum.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_percentile.invoke({"numbers": [1, 2, 3, 4, 5], "percentile": 50}))

```