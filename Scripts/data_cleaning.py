import pandas as pd
import numpy as np

DATE_COL = "Date"
TIME_COL = "Time"

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def to_datetime(df: pd.DataFrame, date_col: str = DATE_COL, time_col: str = TIME_COL) -> pd.DataFrame:
    # Combine Date + Time into a single datetime if both exist
    if date_col in df.columns and time_col in df.columns:
        df["booking_datetime"] = pd.to_datetime(df[date_col].astype(str) + " " + df[time_col].astype(str), errors="coerce", dayfirst=True)
    elif date_col in df.columns:
        df["booking_datetime"] = pd.to_datetime(df[date_col], errors="coerce", dayfirst=True)
    # Derive handy time parts
    if "booking_datetime" in df.columns:
        df["year"] = df["booking_datetime"].dt.year
        df["month"] = df["booking_datetime"].dt.month
        df["day"] = df["booking_datetime"].dt.day
        df["hour"] = df["booking_datetime"].dt.hour
        df["day_of_week"] = df["booking_datetime"].dt.day_name()
    return df

def standardize_categories(df: pd.DataFrame) -> pd.DataFrame:
    # Lowercase and strip string categories for consistency
    cat_cols = [
        "Booking Status", "Vehicle Type", "Pickup Location", "Drop Location",
        "Reason for Cancelling by Customer", "Driver Cancellation Reason",
        "Incomplete Rides Reason", "Payment Method"
    ]
    for c in cat_cols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()
            # Example mappings (extend as needed)
            df[c] = df[c].replace({
                "cancelled": "Cancelled",
                "completed": "Completed",
                "incomplete": "Incomplete",
                "cash": "Cash",
                "card": "Card",
                "wallet": "Wallet"
            })
    return df

def coerce_numbers(df: pd.DataFrame) -> pd.DataFrame:
    num_cols = [
        "Avg VTAT", "Avg CTAT", "Booking Value", "Ride Distance",
        "Driver Ratings", "Customer Rating",
        "Cancelled Rides by Customer", "Cancelled Rides by Driver",
        "Incomplete Rides"
    ]
    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    # Simple strategy: leave critical cols, fill numeric NAs with median, categorical with 'Unknown'
    num = df.select_dtypes(include=[np.number]).columns
    for c in num:
        df[c] = df[c].fillna(df[c].median())
    obj = df.select_dtypes(include=["object"]).columns
    for c in obj:
        df[c] = df[c].fillna("Unknown")
    return df

def save_data(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)

def clean_pipeline(raw_path: str, out_path: str) -> pd.DataFrame:
    df = load_data(raw_path)
    df = to_datetime(df)
    df = standardize_categories(df)
    df = coerce_numbers(df)
    df = handle_missing(df)
    save_data(df, out_path)
    return df