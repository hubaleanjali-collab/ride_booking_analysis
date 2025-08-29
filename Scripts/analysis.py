import pandas as pd

def popular_vehicle_types(df: pd.DataFrame, top_n: int = 10) -> pd.Series:
    if "Vehicle Type" in df.columns:
        return df["Vehicle Type"].value_counts().head(top_n)
    return pd.Series(dtype='int64')

def avg_distance_and_value(df: pd.DataFrame) -> pd.Series:
    out = {}
    if "Ride Distance" in df.columns:
        out["avg_distance"] = df["Ride Distance"].mean()
    if "Booking Value" in df.columns:
        out["avg_booking_value"] = df["Booking Value"].mean()
    return pd.Series(out)

def ratings_distribution(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in ["Driver Ratings", "Customer Rating"] if c in df.columns]
    return df[cols].describe()

def common_cancellation_reasons(df: pd.DataFrame, who: str = "customer") -> pd.Series:
    col = "Reason for Cancelling by Customer" if who == "customer" else "Driver Cancellation Reason"
    if col in df.columns:
        return df[col].value_counts()
    return pd.Series(dtype='int64')

def frequent_cancellers(df: pd.DataFrame, top_n: int = 10) -> pd.Series:
    if "Booking Status" in df.columns and "Customer ID" in df.columns:
        cancelled = df[df["Booking Status"].str.contains("Cancelled", case=False, na=False)]
        return cancelled["Customer ID"].value_counts().head(top_n)
    return pd.Series(dtype='int64')

def cancellations_by_time(df: pd.DataFrame, freq: str = "H") -> pd.Series:
    if "booking_datetime" in df.columns and "Booking Status" in df.columns:
        cancelled = df[df["Booking Status"].str.contains("Cancelled", case=False, na=False)]
        return cancelled.set_index("booking_datetime").resample(freq)["Booking Status"].count()
    return pd.Series(dtype='int64')

def correlation_metrics(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in ["Booking Value", "Ride Distance", "Driver Ratings", "Customer Rating"] if c in df.columns]
    return df[cols].corr()

def driver_ratings(df: pd.DataFrame) -> pd.Series:
    # If driver IDs existed we would group by; using 'Driver Ratings' globally here
    if "Driver Ratings" in df.columns:
        return df["Driver Ratings"].describe()
    return pd.Series(dtype='float64')

def driver_cancel_counts(df: pd.DataFrame) -> int:
    if "Cancelled Rides by Driver" in df.columns:
        return int(df["Cancelled Rides by Driver"].sum())
    return 0

def vtat_ctat_by_vehicle(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in ["Vehicle Type", "Avg VTAT", "Avg CTAT"] if c in df.columns]
    if set(["Vehicle Type", "Avg VTAT", "Avg CTAT"]).issubset(df.columns):
        return df.groupby("Vehicle Type")[["Avg VTAT", "Avg CTAT"]].mean().sort_values("Avg VTAT", ascending=False)
    return pd.DataFrame(columns=cols)

def peak_demand(df: pd.DataFrame) -> pd.Series:
    if "hour" in df.columns:
        return df["hour"].value_counts().sort_index()
    return pd.Series(dtype='int64')

def booking_status_over_time(df: pd.DataFrame, freq: str = "D") -> pd.DataFrame:
    if "booking_datetime" in df.columns and "Booking Status" in df.columns:
        return (df.set_index("booking_datetime")
                  .groupby("Booking Status")
                  .resample(freq)["Booking Status"]
                  .count()
                  .unstack(0)
                  .fillna(0))
    return pd.DataFrame()