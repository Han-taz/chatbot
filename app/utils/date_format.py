from datetime import datetime

def date_format(date_str):
    """
    날짜 문자열을 지정된 형식으로 변환합니다.

    Args:
        date_str (str): 변환할 날짜 문자열

    Returns:
        str: 변환된 날짜 문자열
    """
    if date_str:
        try:
            # 시분초가 포함된 날짜 형식 처리
            return datetime.strptime(date_str, "%Y%m%d%H%M%S").strftime("%Y.%m.%d.%H:%M:%S")
        except ValueError:
            try:
                # 시분초가 없는 날짜 형식 처리
                return datetime.strptime(date_str, "%Y%m%d").strftime("%Y.%m.%d")
            except ValueError:
                # 알 수 없는 형식의 날짜는 그대로 반환
                return date_str
    return None