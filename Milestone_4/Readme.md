# Milestone 4: Sentiment Analysis from Classic NLP to LLMs

> **Question:** When is a simple model good enough, and when does an LLM earn its cost?

**Author:** Carlo Sismundo

In this project I sort GitHub pull-request and commit comments into *positive*, *negative* or *neutral*.
I tried three kinds of approaches on the same comments and compared them using accuracy, macro-F1 and a small
set of hard sentences.

---

## 1. Approaches

| Tier | Approach | Training? | Tools |
|---|---|---|---|
| 1 | Rule-based: a word-score dictionary plus a few rules | None | VADER |
| 2 | Classic ML: Naive Bayes on words (NLTK), and Naive Bayes on TF-IDF words and word pairs (scikit-learn) | Yes, on the training split | NLTK, scikit-learn |
| 3 | LLM, zero-shot: only an instruction, no examples | None | Claude API (`claude-haiku-5-5`) |

Everything is in one notebook: `Sentiment_Analysis_GitHub_Comments.ipynb`.

## 2. Dataset

**A gold standard for polarity of emotions of software developers in GitHub** (`github_gold.csv`)
by Novielli, Calefato, Dongiovanni, Girardi and Lanubile (2020).
Source: <https://doi.org/10.6084/m9.figshare.11604597>

| Item | Value |
|---|---|
| Rows | 7,122 comments after cleaning |
| Labels | neutral 3,022 (42%), negative 2,087 (29%), positive 2,013 (28%) |
| License | See the figshare page linked above |

Cleaning removed rows with missing text or labels, labels other than the three above, empty comments and
duplicate comments. The file uses `;` between columns, and the notebook reads it that way.

**Why this dataset:** it is real developer talk. Words like "kill", "crash" or "dead code" are normal technical
words here and do not mean the person is angry. I expected general tools like VADER to have trouble with this,
so it is a good test.

**Citation:** N. Novielli, F. Calefato, D. Dongiovanni, D. Girardi, F. Lanubile (2020). *Can We Use
SE-specific Sentiment Analysis Tools in a Cross-Platform Setting?* 17th International Conference on Mining
Software Repositories (MSR 2020).

## 3. How I tested the models

* **One split for everyone.** I split the data 80/20 with the same random seed (`42`), keeping the label
  proportions the same in both parts. That gives 5,697 training comments and 1,425 test comments. Every model is
  scored on the same 1,425 test comments.
* **No peeking.** The test comments are never used for training. I did not tune anything on them either. The
  settings are fixed: VADER uses the usual cut-offs (+0.05 and -0.05), the NLTK model uses the 3,000 most
  common training words, and TF-IDF uses single words and word pairs that appear in at least 2 comments.
* **Hard cases.** `hard_cases.csv` has 30 short sentences that simple tools often get wrong, for example technical
  words that sound negative but are neutral ("Kill the process and restart the service."). Each one has a category.
* **Metrics.** Accuracy, **macro-F1 (my main metric)**, a confusion matrix for each model, and accuracy on the
  hard cases. I use macro-F1 because 42% of the comments are neutral, so a model could get a decent accuracy
  just by guessing neutral. Macro-F1 gives each of the three labels the same weight.

## 4. Results

| Model | Accuracy | Macro-F1 | Hard-cases accuracy |
|---|---|---|---|
| VADER | 0.585 | 0.584 | 0.367 (11 of 30) |
| NLTK + Naive Bayes | TBD | TBD | TBD |
| TF-IDF + Naive Bayes | 0.691 | 0.663 | 0.467 (14 of 30) |
| Claude API (`claude-haiku-5-5`) | TBD | TBD | TBD |

The charts and confusion matrices are in the notebook.

### Key findings
1. **TF-IDF + Naive Bayes had the best macro-F1 of the finished models** (0.663 compared with 0.584 for VADER).
   The gap is about 0.08. I did not calculate a confidence interval, so I can not say how sure this is, but it
   is a clear difference on 1,425 test comments.
2. **Every model did badly on the hard cases.** VADER got 11 out of 30 right and TF-IDF + Naive Bayes got 14 out
   of 30, so both were below half. The hard cases are made to be tricky, but it shows that jargon, sarcasm and
   mixed feelings are a real problem for the simple tools.
3. **Speed and cost.** I did not time the models or work out the cost. VADER and the two Naive Bayes models run
   on my own computer and are free. Claude needs one API call for every comment, and each call costs money.

## 5. Error analysis (summary)

VADER often calls neutral comments positive. Its recall for neutral is only 0.36, and only half of the comments
it calls positive really are positive (precision 0.50). It also reads technical words as negative: "Kill the
process and restart the service." gets a score of -0.69 even though the comment is neutral.

TF-IDF + Naive Bayes is the opposite. It is very good at neutral (recall 0.96) but finds only about half of the
negative and positive comments (recall 0.50 and 0.48). It is cautious and falls back on the most common label,
neutral.

The comments that the models got wrong are often very short or use emoticons like `:p`, `:/` and `:'(`, which
VADER and TF-IDF mostly ignore (for example "mergefail! :'("). Others are polite or mild complaints such as
"I'm concerned that this code is too functional..." or "Hate to add noise, but I would really prefer...", where
the negative feeling is not in a single word. Some labels are also debatable, so part of the error may come
from the annotation and not from the model.

## 6. Conclusion: which model, and when?

Of the models I finished, TF-IDF + Naive Bayes worked best. It learns from the labelled GitHub comments, so it
knows the words developers use, while VADER only has a general word list. But it is still far from perfect. It
plays safe and says "neutral" too often, and on the hard cases no model got even half right.

So my answer to the question: **a simple model is good enough** when I have labelled comments from the same place,
a large number of comments to process, a small budget, and I only need a rough picture, for example the overall
mood of a project. VADER is a fine quick start when there is no labelled data at all, but it gets confused by
technical words, so I would not trust it on its own for software text.

An **LLM like Claude is worth its cost** when the comments are tricky (sarcasm, jargon, mixed feelings), when
there are not too many of them, when the budget allows paying for each call, and when it is fine to send the text
to an outside service. Claude reads the whole sentence, so I expect it to do better on the hard cases. The Claude
row in the table above is where this gets checked. If the comments are private or there are millions of them, I
would stay with the simple model that runs on my own computer.

## 7. Files

```
README.md
Sentiment_Analysis_GitHub_Comments.ipynb   the whole project
github_gold.csv                            the dataset (downloaded from figshare)
hard_cases.csv                             the 30 hard sentences
.env                                       my API key (not uploaded to GitHub)
```

## 8. How to run

1. Install the packages (Python 3.10 or newer):
   ```bash
   pip install pandas numpy matplotlib nltk vaderSentiment scikit-learn python-dotenv anthropic
   ```
2. Put `github_gold.csv` and `hard_cases.csv` in the same folder as the notebook.
3. For the Claude part, create a file named `.env` in the same folder with this line:
   ```text
   ANTHROPIC_API_KEY=your_key_here
   ```
   Never write the key in the notebook or upload the `.env` file to GitHub.
4. Open the notebook and run the cells from top to bottom. The Claude cells send one request per comment, which
   costs money, so look at the five-comment check before running the full set.

## 9. Reproducibility notes

* The random seed is `42` in the train/test split, so the split is the same every time.
* The VADER and Naive Bayes results are the same on every run.
* Claude answers can change a little between runs, so its scores may move slightly.

## 10. Limitations

* There are 1,425 test comments, so small differences between models are not conclusive.
* The labels were made by people and contain some noise and opinion.
* I used one dataset, one LLM and one simple prompt. Results could be different on other platforms (such as
  Stack Overflow or Jira) or with a prompt that includes examples.
* The hard-cases set has only 30 sentences, so its scores show a pattern and not an exact accuracy.
* I did not measure speed or cost, and I did not tune the models.

## 11. References

* Novielli, N., Calefato, F., Dongiovanni, D., Girardi, D., Lanubile, F. (2020). Can We Use SE-specific Sentiment Analysis Tools in a Cross-Platform Setting? *MSR 2020*.
* Novielli et al. (2020). A gold standard for polarity of emotions of software developers in GitHub. figshare. <https://doi.org/10.6084/m9.figshare.11604597>
* Hutto, C. J., Gilbert, E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. *ICWSM*.
* Bird, S., Klein, E., Loper, E. (2009). *Natural Language Processing with Python* (NLTK). O'Reilly.
* Pedregosa et al. (2011). Scikit-learn: Machine Learning in Python. *JMLR* 12.
* Anthropic. Claude API documentation. <https://docs.claude.com>

*AI-assistance statement:* I used an AI assistant (Claude) to help write and fix parts of the code and to edit this
README. I ran the notebook myself and the results come from my own runs.
