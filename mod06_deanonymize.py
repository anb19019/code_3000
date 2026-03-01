import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    # Merge on quasi-identifiers
    merged = pd.merge(
        anon_df,
        aux_df,
        on=["age", "zip3", "gender"],
        how="left"
    )

    # Count how many matches each anon_id has
    match_counts = merged.groupby("anon_id")["name"].count()

    # Keep only anon_ids with exactly 1 match
    unique_ids = match_counts[match_counts == 1].index

    unique_matches = merged[merged["anon_id"].isin(unique_ids)]

    # Return required columns only
    return unique_matches[["anon_id", "name"]].rename(
        columns={"name": "matched_name"}
    )



def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    total_records = len(anon_df)
    matched_records = len(matches_df)

    return matched_records / total_records
