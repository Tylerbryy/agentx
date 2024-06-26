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

# Test rag tools
print(agent.rag_search_tools.search_rag_txt('what is the medical codes for autism?', txt_file=r'C:\Users\tyler\OneDrive\Documents\Agentx\Combined_Codes_Datasetv7.txt'))
# Test scraping tools
print(agent.scraping_tools.scrape_website('https://www.nbcnews.com/politics/politics-news/live-blog/hunter-biden-trial-live-updates-rcna156114'))

# Test search tools
print(agent.search_tools.search_internet.invoke('what is hawking radiation?'))

# Test statistical tools
print(agent.statistical_tools.calculate_mean.invoke({"values": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_median.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_std.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_variance.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_min.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_max.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_sum.invoke({"numbers": [1, 2, 3, 4, 5]}))
print(agent.statistical_tools.calculate_percentile.invoke({"numbers": [1, 2, 3, 4, 5], "percentile": 50}))
