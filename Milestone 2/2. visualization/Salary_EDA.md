# Salary Survey 2021 — Exploratory Data Analysis

## 1. Objective

The purpose of this Exploratory Data Analysis (EDA) is to examine salary patterns in the cleaned Salary Survey 2021 dataset.

The analysis focuses on five research questions:

1. Does more professional experience mean higher salary?
2. Is a Master's or PhD associated with higher salary?
3. Which industries have the highest and lowest median salaries?
4. Does location affect salary?
5. Which job titles have the highest salaries, and how consistent is pay within each title?

Median salary is primarily used instead of mean salary because salary data is typically right-skewed. A small number of very high earners can significantly increase the mean.

The analysis also considers sample size and limitations when interpreting the results.

---

# 2. Load Cleaned Data

The analysis uses the final cleaned dataset:

`salary_survey_cleaned.csv`

The dataset contains:

- **27,841 rows**
- **9 columns**

The nine variables are:

- `age_range`
- `industry`
- `job_title`
- `annual_salary`
- `currency`
- `country`
- `current_years_experience`
- `education`
- `gender`

The cleaned dataset was produced during the previous data-cleaning stage.

---

# 3. Missing Value Check

Before performing the analysis, the dataset was checked for missing values.

The final cleaned dataset contains zero missing values in the nine analysis columns.

This confirms that the cleaning process successfully handled missing categorical values and converted the salary field into a usable numeric format.

The annual salary statistics were also reviewed before starting the analysis.

The cleaned salary distribution has:

- Minimum salary: **$10,000**
- First quartile: **$54,080**
- Median salary: **$75,000**
- Third quartile: **$109,000**
- Maximum salary: **$2,000,000**

The median is substantially lower than the mean, showing that the salary distribution is right-skewed.

---

# 4. Research Question 1 — Does More Experience Mean More Money?

## Method

The `current_years_experience` variable represents grouped ranges of overall professional work experience.

To analyze the relationship between experience and salary, each experience range was assigned an approximate midpoint.

For example:

- `1 year or less` → 0.5 years
- `2 - 4 years` → 3 years
- `5-7 years` → 6 years
- `8 - 10 years` → 9 years
- `11 - 20 years` → 15 years
- `21 - 30 years` → 25 years
- `31 - 40 years` → 35 years
- `41 years or more` → 45 years

The midpoint is used as an approximate numerical representation of each experience group.

Median salary and the number of responses were then calculated for each experience category.

## Results

| Professional Experience | Median Salary | Responses |
|---|---:|---:|
| 1 year or less | $53,000 | 1,487 |
| 2 - 4 years | $62,000 | 6,182 |
| 5-7 years | $72,000 | 6,474 |
| 8 - 10 years | $82,500 | 4,936 |
| 11 - 20 years | $91,000 | 6,494 |
| 21 - 30 years | $102,000 | 1,850 |
| 31 - 40 years | $100,000 | 378 |
| 41 years or more | $99,039 | 40 |

## Takeaway

The results show a clear positive relationship between professional experience and median salary during the earlier and middle stages of a career.

Median salary increases from approximately **$53,000** for respondents with one year or less of experience to approximately **$102,000** for respondents with 21–30 years of experience.

After approximately 20 years of experience, the median salary levels off and slightly decreases in the older experience groups.

However, the `41 years or more` category contains only **40 responses**, so that estimate should be interpreted cautiously.

This analysis shows an association between experience and salary, but it does not prove that experience alone causes higher salary.

---

# 5. Research Question 2 — Is a Master's/PhD Worth It in Dollar Terms?

## Method

Education levels were ordered from lower to higher formal education.

The following categories were included:

- High School
- Some college
- College degree
- Master's degree
- Professional degree (MD, JD, etc.)
- PhD

Median salary and response count were calculated for each education level.

The median salary difference between respondents with a College degree and those with a Master's degree was also calculated.

## Results

| Education Level | Median Salary | Responses |
|---|---:|---:|
| High School | $56,000 | 636 |
| Some college | $61,000 | 2,044 |
| College degree | $72,800 | 13,419 |
| Master's degree | $79,000 | 8,800 |
| Professional degree | $114,000 | 1,311 |
| PhD | $92,000 | 1,417 |

The median salary difference between a Master's degree and a College degree is:

**$79,000 − $72,800 = $6,200**

## Takeaway

Respondents with a Master's degree have a median salary approximately **$6,200 higher** than respondents with a College degree.

The results also show generally higher median salaries at higher education levels, although the pattern is not perfectly linear.

Professional-degree holders have the highest median salary among the listed education groups.

Education is associated with salary in this dataset, but the analysis does not establish that obtaining a particular degree directly causes a specific salary increase.

Other factors such as occupation, industry, experience, location, and seniority may also contribute to the observed differences.

---

# 6. Research Question 3 — Which Industries Pay the Most and Least?

## Method

Industry categories were standardized during the data-cleaning stage.

To avoid drawing conclusions from very small groups, only industries with at least **100 responses** were included in the comparison.

Median salary was used to rank the industries.

## Results

| Industry | Median Salary | Responses |
|---|---:|---:|
| Retail/Sales | $49,000 | 511 |
| Education | $61,000 | 3,389 |
| Other | $63,000 | 2,183 |
| Nonprofit | $63,500 | 2,414 |
| Agriculture | $66,851 | 137 |
| Arts/Design | $67,000 | 363 |
| Transportation | $67,000 | 307 |
| Media/Entertainment | $70,000 | 1,104 |
| Marketing | $74,750 | 1,136 |
| Insurance | $75,000 | 528 |
| Health | $75,000 | 2,394 |
| Government | $77,463 | 1,926 |
| Finance | $78,000 | 1,808 |
| Engineering/Manufacturing | $83,500 | 2,184 |
| Energy | $85,000 | 420 |
| Business/Consulting | $88,000 | 887 |
| Legal | $90,000 | 1,142 |
| Information Technology | $112,500 | 4,693 |

## Takeaway

Among industries with at least 100 responses, **Information Technology** has the highest median salary at approximately **$112,500**.

**Retail/Sales** has the lowest median salary at approximately **$49,000**.

This represents a substantial difference between the highest- and lowest-paying industry groups.

However, industry is only one factor associated with salary. Job title, professional experience, location, education, and seniority may also influence compensation.

---

# 7. Research Question 4 — Does Location Change What You Get Paid?

## Method

The dataset contains salaries reported in different currencies.

To allow a rough comparison between countries, approximate exchange rates were applied to convert selected currencies into U.S. dollars.

The approximate rates used were:

- USD = 1.00
- CAD = 0.74
- GBP = 1.27
- EUR = 1.08
- AUD/NZD = 0.66
- CHF = 1.13
- SEK = 0.095
- ZAR = 0.055
- HKD = 0.13
- JPY = 0.0067

Only countries with at least **50 responses** were included.

The country labeled `Other` was excluded from the country comparison.

## Results

| Country | Approx. Median Salary (USD) | Responses |
|---|---:|---:|
| France | $50,760 | 67 |
| United Kingdom | $50,800 | 1,571 |
| Ireland | $54,000 | 126 |
| Canada | $56,240 | 1,677 |
| New Zealand | $61,050 | 124 |
| Australia | $64,680 | 385 |
| Netherlands | $64,800 | 85 |
| Germany | $73,980 | 187 |
| United States | $78,800 | 22,993 |

## Takeaway

The results show substantial differences in approximate median salary between countries.

The United States has the highest approximate median salary among the countries included, at approximately **$78,800**.

France has the lowest approximate median salary in this comparison, at approximately **$50,760**.

However, this comparison has important limitations.

Approximately **83% of the responses are from the United States**, making the dataset heavily concentrated in one country.

In addition, the exchange rates are approximate and do not account for:

- Cost of living
- Purchasing power
- Taxes
- Benefits
- Local salary structures

Therefore, these results should be treated as a rough comparison rather than an exact measure of which country provides the highest purchasing power.

---

# 8. Research Question 5 — Which Job Titles Pay the Most and How Consistent Is Pay?

## Method

Job titles were standardized during the data-cleaning stage.

Only job-title categories with at least **100 responses** were included.

The generic `Other` category was excluded.

For each job title, the analysis calculated:

- Median salary
- First quartile (Q1)
- Third quartile (Q3)
- Number of responses
- Interquartile range (IQR)

The IQR is calculated as:

`IQR = Q3 - Q1`

The IQR represents the range containing the middle 50% of salaries.

A smaller IQR indicates that salaries are more concentrated around the median.

A larger IQR indicates greater variation in salaries within that job-title category.

## Top Job Titles

The highest median salaries among job titles with at least 100 responses include:

| Job Title | Median Salary | IQR | Responses |
|---|---:|---:|---:|
| VP/Senior Leadership | $152,000 | $76,000 | 132 |
| Software Engineer | $135,600 | $67,000 | 985 |
| Executive (C-Suite) | $135,000 | $79,400 | 345 |
| Product Manager | $112,000 | $49,000 | 289 |
| UX/UI Designer | $110,000 | $58,068 | 139 |
| Director | $98,000 | $64,000 | 2,550 |
| Engineer (Non-software) | $95,000 | $47,850 | 1,108 |
| Consultant | $91,000 | $56,800 | 479 |
| Data Scientist/Analyst | $90,000 | $58,000 | 393 |
| Team Lead | $88,000 | $60,788 | 465 |

## Takeaway

`VP/Senior Leadership` has the highest median salary among the job-title groups analyzed, at approximately **$152,000**.

`Software Engineer` follows with a median salary of approximately **$135,600**.

The IQR values show that salaries can vary substantially even within the same standardized job-title category.

For example, VP/Senior Leadership has an IQR of approximately **$76,000**, meaning the middle 50% of salaries span a wide range.

Therefore, job title can provide a useful indication of salary level, but it does not determine an individual's exact salary.

---

# 9. Overall Findings

The EDA provides several important observations from the Salary Survey 2021 dataset.

## 1. Experience and Salary

Median salary generally increases with professional experience.

The largest increases occur during the early and middle stages of a career, while salary appears to level off at higher experience levels.

## 2. Education and Salary

Higher education levels are generally associated with higher median salaries.

A Master's degree has a median salary approximately **$6,200 higher** than a College degree in this dataset.

However, this does not mean that a Master's degree alone causes a $6,200 salary increase.

## 3. Industry and Salary

Salary differs substantially between industries.

Information Technology has the highest median salary among the industries analyzed, while Retail/Sales has the lowest.

## 4. Location and Salary

Salary differs between countries.

The United States has the highest approximate median salary among the countries included in the comparison.

However, the dataset is heavily concentrated in the United States and the currency conversion does not account for cost of living.

## 5. Job Title and Salary

Job title is strongly associated with salary differences.

Leadership and specialized technology roles appear among the highest-paying categories.

At the same time, the IQR analysis shows that salary can vary considerably among people with the same standardized job title.

---

# 10. Important Limitations

The results should be interpreted with several limitations in mind.

### Survey Data

The dataset is based on survey responses and may not represent the entire working population.

### Currency

Salary values are reported in different currencies.

The country comparison uses approximate exchange rates rather than a detailed historical currency-conversion analysis.

### Cost of Living

The analysis does not adjust salaries for differences in cost of living or purchasing power between countries.

### Correlation vs. Causation

The analysis identifies relationships between salary and factors such as experience, education, industry, location, and job title.

It does not prove that any individual factor directly causes a salary increase.

### Sample Size

Some categories contain substantially fewer observations than others.

Results from very small groups should therefore be interpreted cautiously.

### Job Title Grouping

Different original job titles were grouped into standardized categories.

This improves analysis but may hide differences between specific occupations within the same category.

---

# 11. Visualization Outputs

The Python program generates five charts.

### Chart 1

`chart1_experience.png`

Shows median salary by professional experience.

### Chart 2

`chart2_education.png`

Shows median salary by education level.

### Chart 3

`chart3_industry.png`

Shows median salary by industry.

### Chart 4

`chart4_country.png`

Shows approximate median salary by country.

### Chart 5

`chart5_jobtitle_top10.png`

Shows the top 10 standardized job titles by median salary.

---

# 12. Conclusion

The exploratory analysis shows that salary varies considerably according to professional experience, education, industry, country, and job title.

The strongest patterns observed are:

- More professional experience is generally associated with higher salary.
- Higher education levels are generally associated with higher median salary.
- Industry has a substantial relationship with salary.
- Country is associated with differences in reported salary, although the comparison is affected by the strong U.S. representation and lack of cost-of-living adjustment.
- Job titles show large differences in median salary, while the IQR demonstrates that individual salaries can still vary substantially within the same title.

These findings provide a foundation for the next stage of the project, which can include deeper statistical analysis and additional visualizations.
