# Salary Survey 2021 — Data Cleaning and Wrangling Notes

## 1. Objective

The purpose of this data-cleaning process is to prepare the **Salary Survey 2021** dataset for analysis and visualization.

The raw dataset contains salary information together with demographic, employment, education, industry, job title, country, currency, and professional experience information.

The cleaning process focuses on:

- Inspecting the raw dataset
- Removing unnecessary columns
- Renaming columns for easier use
- Standardizing industry categories
- Standardizing job title categories
- Converting salary values into numeric format
- Removing records with unknown currency
- Standardizing country names
- Ordering professional experience categories
- Handling missing education values
- Handling missing gender values
- Ordering age-range categories
- Identifying salary outliers
- Validating the final dataset
- Exporting the cleaned dataset

---

# 2. Initial Data Inspection

The raw dataset contains:

- **28,225 rows**
- **18 columns**

The initial inspection was performed to understand the structure of the dataset and identify missing values before making any changes.

The inspection included:

- Dataset shape
- Column names
- Data types
- Unique values
- Missing values
- Basic salary statistics

The raw dataset contains a mixture of numerical and categorical/text-based variables. The annual salary field requires cleaning and conversion before it can be reliably used for statistical analysis.

## Missing Data

Several columns contain a significant number of missing values.

Examples include:

- Additional currency information
- Additional income context
- Additional job title context
- Additional monetary compensation
- U.S. state
- City

Some of these fields contain a large percentage of missing values.

## Decision

Columns that were highly incomplete or outside the scope of the main analysis were removed.

The analysis focuses on:

- Age range
- Industry
- Job title
- Annual salary
- Currency
- Country
- Professional experience
- Education
- Gender

---

# 3. Column Selection

Columns that were not required for the main analysis were removed.

These include:

- Timestamp
- Job title additional context
- Additional monetary compensation
- Other currency information
- Income additional context
- U.S. state
- City
- Race

The overall years of professional work experience column was retained because it is used as the current_years_experience variable in the analysis.

## Reason

The removed columns were excluded because they were either:

1. Highly incomplete
2. Outside the scope of the project
3. Free-text information that would create excessive categories
4. Not required for the planned salary analysis

Keeping only relevant variables makes the dataset easier to analyze and visualize.

---

# 4. Column Renaming

The original survey questions contain long column names.

These columns were renamed using shorter and more consistent names.

| Original Column | New Column |
|---|---|
| How old are you? | `age_range` |
| What industry do you work in? | `industry` |
| Job title | `job_title` |
| What is your annual salary? | `annual_salary` |
| Please indicate the currency | `currency` |
| What country do you work in? | `country` |
| How many years of professional work experience do you have overall? | `current_years_experience` |
| What is your highest level of education completed? | `education` |
| What is your gender? | `gender` |

## Reason

Shorter column names make the dataset easier to work with in Python, pandas, and visualization tools.

They also make the code easier to read and maintain.

---

# 5. Industry Cleaning

## Problem

The original industry column contains a very large number of unique responses.

Respondents may describe similar industries using different wording.

For example:

- Information Technology
- Computing or Tech
- Software
- Technology
- Computer
- Engineering
- Manufacturing

Treating every response as a separate category would make industry analysis difficult.

## Action

Regular-expression keyword matching was used to group similar industry responses into standardized categories.

The cleaning function checks each industry response against a predefined mapping of keywords and patterns.

Examples of standardized categories include:

- Information Technology
- Finance
- Education
- Health
- Engineering/Manufacturing
- Government
- Nonprofit
- Marketing
- Retail/Sales
- Hospitality
- Energy
- Insurance
- Real Estate
- Transportation
- Agriculture
- Arts/Design
- Legal
- Business/Consulting
- Media/Entertainment
- Biotech
- Veterinary
- Contact Center Services

Industry responses that do not match one of the predefined categories are classified as:

`Other`

Missing industry values are classified as:

`Not Specified`

## Reason

Grouping similar responses reduces the number of categories and makes industry-level analysis and visualization more meaningful.

---

# 6. Job Title Cleaning

## Problem

The original job title column contains thousands of unique responses.

Different respondents may use different titles for similar types of work.

For example:

- Software Engineer
- Software Developer
- Web Developer
- Backend Developer
- Full Stack Developer

Analyzing thousands of individual job titles would make the results difficult to interpret.

## Action

Job titles were grouped into standardized categories using regular-expression keyword matching.

Examples of standardized categories include:

- Software Engineer
- Data Scientist/Analyst
- IT/Systems
- DevOps/Cloud
- QA/Test Engineer
- Product Manager
- Project Manager
- UX/UI Designer
- VP/Senior Leadership
- Director
- Sales Manager
- Marketing Manager
- HR Generalist/Manager
- Executive Assistant
- Administrative Assistant
- Office Manager
- Receptionist
- Coordinator
- Accountant
- Financial Analyst
- Bookkeeper
- Auditor
- Controller
- Sales Representative
- Content/Copywriter
- Social Media
- Teacher
- Professor/Faculty
- Librarian
- Customer Service
- Graphic Designer
- Writer/Editor
- Consultant
- Social Worker
- Team Lead
- Supervisor
- Manager (General)
- Analyst (General)
- Engineer (Non-software)

Missing job titles are classified as:

`Not Specified`

## Classification Rule

The mapping was ordered so that specific job titles are checked before broader categories.

For example:

`Sales Manager`

is checked before:

`Manager (General)`

This prevents specific job titles from being incorrectly classified into a general category.

---

# 7. Annual Salary Cleaning

## Problem

Annual salary values may contain formatting characters such as commas and dollar signs.

For example:

`$55,000`

These values need to be converted into a numeric format before statistical analysis.

## Action

The salary values were cleaned by:

1. Converting the values to string format
2. Removing commas
3. Removing dollar signs
4. Removing unnecessary whitespace
5. Converting the resulting values to numeric format

For example:

`$55,000`

becomes:

`55000`

The cleaned column is stored as:

`annual_salary`

## Validation

The salary data type and missing values were checked after conversion.

Salary statistics were also reviewed using descriptive statistics.

---

# 8. Currency Cleaning

## Problem

The dataset contains multiple currencies.

Salary values from different currencies cannot be directly compared without currency conversion.

The dataset also contains records where the currency is specified as:

`Other`

These records do not provide a clearly identified standard currency.

## Action

Records where the currency is listed as `Other` were removed.

The remaining currency values were also stripped of unnecessary whitespace.

## Reason

Removing unknown currency records prevents unclear currency information from being used in salary comparisons.

No currency conversion was performed during this cleaning stage.

For future salary comparisons across countries, an appropriate exchange-rate dataset corresponding to the survey period should be used.

---

# 9. Country Cleaning

## Problem

The country column contains many different responses.

The same country may be entered using different spellings or abbreviations.

For example, the United States may appear as:

- United States
- USA
- US
- U.S.
- U.S.A.

Treating these as separate categories would make geographic analysis inaccurate.

## Action

Regular-expression matching was used to standardize commonly occurring countries.

The main standardized countries include:

- United States
- United Kingdom
- Canada
- Australia
- Germany
- India
- Ireland
- France
- Netherlands
- New Zealand

Responses that do not match the predefined country categories are classified as:

`Other`

Missing country values are classified as:

`Not Specified`

## Reason

Country standardization reduces duplicate representations of the same country and makes geographic analysis easier.

---

# 10. Current Years of Professional Experience

## Problem

Professional experience is represented using grouped categories.

If these categories are treated as normal text, pandas may display them alphabetically rather than in a logical experience progression.

## Action

The `current_years_experience` column was converted into an ordered categorical variable.

The program extracts the first numerical value from each experience category and uses that value to determine the order.

For example, a category beginning with a smaller number will appear before a category beginning with a larger number.

## Reason

Ordering the categories numerically allows future tables and visualizations to display professional experience from lower to higher experience levels.

---

# 11. Education

## Problem

Some respondents did not provide education information.

Leaving these values as missing would make some analyses more difficult.

## Action

Missing education values were replaced with:

`Not Specified`

The original education responses were otherwise preserved.

## Reason

Missing information should not be replaced with an assumed education level.

Using `Not Specified` preserves the distinction between respondents who provided education information and those who did not.

---

# 12. Gender

## Problem

The gender column contains multiple categories and some missing values.

One response was longer than necessary:

`Other or prefer not to answer`

## Action

The response was standardized to:

`Prefer not to answer`

Missing gender values were replaced with:

`Not Specified`

## Reason

Standardizing the category makes the values easier to analyze and visualize while preserving the meaning of the original response.

---

# 13. Age Range

## Problem

Age is represented as a categorical variable.

If the categories are treated as ordinary text, they may not appear in the correct age progression during analysis or visualization.

## Action

The age range values were cleaned and converted into an ordered categorical variable.

The intended order follows the natural progression from younger to older age groups:

1. Under 18
2. 18–24
3. 25–34
4. 35–44
5. 45–54
6. 55–64
7. 65 or over

The program also checks which categories are actually present in the dataset before applying the categorical ordering.

## Reason

Ordering the age groups makes future visualizations easier to interpret.

---

# 14. Salary Outlier Detection

## Problem

The annual salary variable contains extreme values.

Very low or extremely high salary values can have a significant effect on averages and other statistical measurements.

Salary data is also naturally right-skewed because a smaller number of respondents may have substantially higher salaries.

## Action

A practical salary range was established for this project.

### Lower Bound

`10,000`

### Upper Bound

`2,000,000`

Any salary below 10,000 or above 2,000,000 was flagged as a potential salary outlier.

The program creates a temporary column:

`salary_outlier_flag`

This identifies whether each salary falls outside the selected range.

The flagged records are exported separately to:

`salary_outliers.csv`

The flagged records are then excluded from the final analysis-ready dataset.

## Reason

A purely statistical method such as the IQR method could classify legitimate high-income respondents as outliers.

For this project, practical salary boundaries were used to identify extreme values that are outside the selected analysis range.

The separate outlier file allows these records to be reviewed without losing the original information.

---

# 15. Final Data Types

After the cleaning process, selected categorical columns were converted to the pandas `category` data type.

These include:

- `industry`
- `job_title`
- `currency`
- `country`
- `education`
- `gender`
- `current_years_experience`
- `age_range`

Categorical data types are appropriate because these variables represent groups or classifications rather than continuous numerical measurements.

The `annual_salary` column remains numeric so that it can be used for statistical calculations and visualization.

---

# 16. Final Validation

Before exporting the final dataset, several validation checks were performed.

## Dataset Shape

The program prints the final number of rows and columns.

The exact final shape depends on the number of records removed during cleaning and salary outlier detection.

## Missing Values

The final dataset is checked for missing values.

Categorical missing values that are relevant to the analysis are represented using:

`Not Specified`

## Duplicate Rows

The final dataset is checked for duplicate rows.

## Salary Statistics

Descriptive statistics are calculated again after salary outlier removal.

This allows the cleaned salary distribution to be reviewed before the dataset is used for analysis.

---

# 17. Output Files

The cleaning script produces two CSV files.

## Main Cleaned Dataset

`salary_survey_cleaned.csv`

This is the main analysis-ready dataset.

It should be used for:

- Exploratory Data Analysis
- Data Visualization
- Salary comparisons
- Industry analysis
- Job title analysis
- Country analysis
- Education analysis
- Gender analysis
- Age analysis
- Experience analysis

## Salary Outliers

`salary_outliers.csv`

This file contains the records identified as salary outliers based on the selected salary boundaries.

It is kept separately so that the excluded records can still be reviewed.

---

# 18. Cleaning Workflow Summary

The complete data-cleaning workflow is:

Raw Dataset
↓
Initial Data Inspection
↓
Remove Unnecessary Columns
↓
Rename Columns
↓
Clean Industry
↓
Clean Job Titles
↓
Convert Salary to Numeric
↓
Remove Unknown Currency
↓
Standardize Country
↓
Order Professional Experience
↓
Handle Education Missing Values
↓
Handle Gender Missing Values
↓
Order Age Categories
↓
Detect Salary Outliers
↓
Save Salary Outliers
↓
Remove Salary Outliers
↓
Set Final Data Types
↓
Final Validation
↓
Export Clean Dataset

---

# 19. Final Dataset

The final cleaned dataset is intended to be used for the next stage of the project.

The analysis-ready dataset can be used for:

- Exploratory Data Analysis
- Data Visualization
- Salary distribution analysis
- Salary comparisons by industry
- Salary comparisons by job title
- Salary comparisons by country
- Salary analysis by education
- Salary analysis by gender
- Salary analysis by age
- Salary analysis by professional experience

The primary dataset for the next stage is:

`salary_survey_cleaned.csv`

The separate:

`salary_outliers.csv`

file is retained for documentation and review of the records excluded from the final analysis.

## Final Output

The data-cleaning process transforms the original survey responses into a more structured, standardized, and analysis-ready dataset while preserving important categorical information and documenting the treatment of extreme salary values.
