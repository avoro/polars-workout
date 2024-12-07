import polars as pl
import numpy as np

scores = pl.Series(
    name="scores", values=np.round(np.random.uniform(70, 100, size=10), 2)
)
print(scores)

len_scores = len(scores)

avg_score = scores.mean()
print(f"Average score: {round(avg_score, 2)}")

first_half_avg_scores = scores.slice(0, len_scores // 2).mean()
print(f"First half average: {round(first_half_avg_scores, 2)}")

second_half_avg_scores = scores.slice(len_scores // 2, len_scores).mean()
print(f"Second half average: {round(second_half_avg_scores, 2)}")

print(
    f"Score performance change: {round(second_half_avg_scores - first_half_avg_scores, 2)}"
)

months = ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"]

max_index = scores.arg_max()
max_value = scores[max_index]
print(f"Highest score {max_value} was achieved in {months[max_index]}")

print(f"Top three highest scores are {(scores.top_k(3)).to_list()}")
