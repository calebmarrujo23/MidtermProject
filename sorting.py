def sort_by_strikeouts_pitchers(data):
    """
    Sort pitchers strikeout percentage in descending order.
    """
    return data.sort_values('k_percent', ascending=False)


def sort_by_walks_pitchers(data):
    """
    Sort pitchers  walk percentage in descending order.
    """
    return data.sort_values('bb_percent', ascending=False)

def sort_by_strikeouts_hitters(data):
    """
    Sort hitters strikeout percentage in descending order.
    """
    return data.sort_values('k_percent', ascending=False)


def sort_by_walks_hitters(data):
    """
    Sort hitters. walk percentage in descending order.
    """
    return data.sort_values('bb_percent', ascending=False)


def sort_by_woba(data):
    """
    Sort hitters by wOBA (Weighted On-base Average) in descending order.
    """
    return data.sort_values('woba', ascending=False)
