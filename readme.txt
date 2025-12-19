Assignment
Objective: Analyze the impact of remote work and job satisfaction on overall productivity.

Data Cleaning

Handle Missing Values: Identify and replace null or missing values in the Satisfaction or PerformanceScore columns.
Standardize Categorical Variables: Ensure consistency in categories (e.g., converting various formats into a standard "Yes/No").

Feature Engineering: Create a new column named ProductivityIndex using the following formula: ProductivityIndex = {PerformanceScore + (Satisfaction *10) \{HoursPerWeek}

Exploratory Data Analysis (EDA) with Python

Calculate the average productivity levels for each department.
Compare the performance levels between remote workers and on-site (in-person) workers
Analyze the correlation/relationship between absences and performance scores.


Data Visualization

Using the seaborn library (sns), generate the following charts:

sns.violinplot(): To compare productivity distribution across different work types (Remote vs. On-site).

sns.barplot(): To display the average productivity per department.

sns.scatterplot(): To visualize the relationship between satisfaction levels and performance.


Power BI Dashboard

Create a dashboard featuring the following Key Performance Indicators (KPIs):

Overall Productivity.

Percentage (%) of Remote Work.

Correlation between Satisfaction and Productivity.

Conclusions

Provide a final assessment based on your findings:

Does remote work improve or reduce employee performance?

Which departments present the most significant opportunities for improvement?