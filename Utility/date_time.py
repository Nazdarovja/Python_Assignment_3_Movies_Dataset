from datetime import datetime

def str_2_datetime(string, format='%Y-%m-%d'):
    return datetime.strptime(string, '%Y-%m-%d')