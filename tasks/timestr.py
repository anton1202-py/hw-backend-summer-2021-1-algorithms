__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    M = 60
    H = 3600
    D = 86400
    if seconds >= D:
        d = seconds // D
        h = (seconds - (d * D)) // H
        m = (seconds - (d * D) - (H * h)) // M
        s = (seconds - (d * D) - (H * h) - (M * m))
        return f'{d:02d}d{h:02d}h{m:02d}m{s:02d}s'
    elif seconds >= H:
        h = (seconds) // H
        m = (seconds - (H * h)) // M
        s = (seconds - (H * h) - (M * m))
        return f'{h:02d}h{m:02d}m{s:02d}s'
    elif seconds >= M:
        m = seconds // M
        s = seconds - (M * m)
        return f'{m:02d}m{s:02d}s'
    else:
        return f'{seconds:02d}s'




