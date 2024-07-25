import requests
from app.core.config import current_config
from app.utils.date_format import date_format

base_header = {
    "Content-Type": "application/json"
}

# 콘텐츠 유형 매핑
content_type_mapping = {
    'VIDEO': '영상',
    'DOCUMENT': '문서',
    'MIX': '혼합'
}

def fetch_edu_contents(params: dict, authorization: str) -> list:
    """
    교육 콘텐츠 데이터를 가져옵니다.

    Args:
        params (dict): 요청 파라미터
        authorization (str): 인증 토큰

    Returns:
        list: 교육 콘텐츠 데이터 리스트
    """
    headers = {**base_header, "Authorization": authorization}
    response = requests.get(current_config.MYPAGE_EDU_CONTENTS_POPUP_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print("Error message:", response.text)
        return []

def get_wish_edu_contents(authorization: str) -> list:
    """
    찜한 교육 콘텐츠 데이터를 가져옵니다.

    Args:
        authorization (str): 인증 토큰

    Returns:
        list: 찜한 교육 콘텐츠 데이터 리스트
    """
    params = {
        "currentTab": 0,
        "startRow": 0,
        "endRow": current_config.FETCH_COUNT_LIMIT,
        "sortOrder": "LAST_MODIFY_DATE DESC"
    }
    data = fetch_edu_contents(params, authorization)
    wish_contents_list = []
    for item in data:
        start_date = date_format(item['SHOW_START_DATE']) if item['SHOW_START_DATE'] else '무기한'
        end_date = date_format(item['SHOW_END_DATE']) if item['SHOW_END_DATE'] else '무기한'
        course_info = {
            '교육 콘텐츠 이름': item['COURSE_NAME'],
            '콘텐츠 유형': content_type_mapping.get(item['EDU_CONTENTS_TYPE'], '알 수 없음'),
            '카테고리': item['CATEGORY_FULL_NAME'],
            '교육 콘텐츠 시작일': start_date,
            '교육 콘텐츠 종료일': end_date,
            '좋아요 수': item['TOTAL_COUNT'],
            '별점': item['SCORE']
        }
        wish_contents_list.append(course_info)
    return wish_contents_list

def get_current_edu_contents(authorization: str) -> list:
    """
    현재 수강 중인 교육 콘텐츠 데이터를 가져옵니다.

    Args:
        authorization (str): 인증 토큰

    Returns:
        list: 현재 수강 중인 교육 콘텐츠 데이터 리스트
    """
    params = {
        "currentTab": 1,
        "startRow": 0,
        "endRow": current_config.FETCH_COUNT_LIMIT,
        "listType": "ing",
        "sortOrder": "LAST_MODIFY_DATE DESC"
    }
    data = fetch_edu_contents(params, authorization)
    current_contents_list = []
    for item in data:
        course_info = {
            '교육 콘텐츠 이름': item['COURSE_NAME'],
            '콘텐츠 유형': content_type_mapping.get(item['EDU_CONTENTS_TYPE'], '알 수 없음'),
            '카테고리': item['CATEGORY_FULL_NAME'],
            '좋아요 수': item['TOTAL_COUNT'],
            '진도율': f"{round(item['PROGRESS_PERCENTAGE'])}%",
            '별점': item['SCORE']
        }
        current_contents_list.append(course_info)
    return current_contents_list

def get_completed_edu_contents(authorization: str) -> list:
    """
    수강 완료한 교육 콘텐츠 데이터를 가져옵니다.

    Args:
        authorization (str): 인증 토큰

    Returns:
        list: 수강 완료한 교육 콘텐츠 데이터 리스트
    """
    params = {
        "currentTab": 1,
        "startRow": 0,
        "endRow": current_config.FETCH_COUNT_LIMIT,
        "listType": "completed",
        "sortOrder": "LAST_MODIFY_DATE DESC"
    }
    data = fetch_edu_contents(params, authorization)
    completed_contents_list = []
    for item in data:
        course_info = {
            '교육 콘텐츠 이름': item['COURSE_NAME'],
            '콘텐츠 유형': content_type_mapping.get(item['EDU_CONTENTS_TYPE'], '알 수 없음'),
            '카테고리': item['CATEGORY_FULL_NAME'],
            '좋아요 수': item['TOTAL_COUNT'],
            '진도율': f"{round(item['PROGRESS_PERCENTAGE'])}%",
            '별점': item['SCORE']
        }
        completed_contents_list.append(course_info)
    return completed_contents_list

def total_contents_info(authorization_token: str) -> dict:
    """
    교육 콘텐츠 정보를 종합하여 반환합니다.

    Args:
        authorization_token (str): 인증 토큰

    Returns:
        dict: 교육 콘텐츠 정보
    """
    return {
        '찜한 교육 콘텐츠': get_wish_edu_contents(authorization_token),
        '수강 중인 교육 콘텐츠': get_current_edu_contents(authorization_token),
        '수강 완료한 교육 콘텐츠': get_completed_edu_contents(authorization_token)
    }