def hourly_return(prev_close, close):
    """Percentage return between two closes."""
    return (close - prev_close) / prev_close
