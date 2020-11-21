import numpy as np
import pandas as pd

def sample_test_results(size=(), df_covid_stats=pd.read_csv("data/covidstats_bw.csv"), seed=42):
    """
    Sample test results from a synthetic population based on COVID statistics.
    """
    
    # Random generator
    rng = np.random.default_rng(seed=seed)

    # Draw with replacement weighted by population
    sample_population = rng.choice(
        df_covid_stats.index,
        p=df_covid_stats["population"] / np.sum(df_covid_stats["population"]),
        size=size,
        replace=True,
    )

    # COVID infection probability based on RKI dataset
    covid_prob_by_traits = (
        df_covid_stats["positive_tests"] / df_covid_stats["population"]
    )
    df_covid_stats["prob_positive_test"] = covid_prob_by_traits

    # Determine positive test
    is_positive_test = rng.binomial(1, p=covid_prob_by_traits[sample_population])

    # Create dataframe of cases
    sample_case_df = df_covid_stats.iloc[sample_population, :]
    sample_case_df = sample_case_df.drop(["positive_tests"], axis=1)
    sample_case_df = sample_case_df.assign(positive_test=is_positive_test).reset_index(drop=True)

    return sample_case_df