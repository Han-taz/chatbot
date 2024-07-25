import os
from dotenv import load_dotenv
from pathlib import Path

# 프로젝트 디렉토리 기준 .env 파일 로드
basedir = Path(__file__).resolve().parent.parent.parent
load_dotenv(basedir / '.env')


class Config:
    """기본 설정"""
    ENV = os.getenv('FASTAPI_ENV', 'production')
    DEBUG = os.getenv('FASTAPI_DEBUG', 'False').lower() in ['true', '1', 't']
    TESTING = os.getenv('FASTAPI_TESTING', 'False').lower() in ['true', '1', 't']
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')

    # 데이터베이스 설정
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///' + str(basedir / 'app.db'))

    # OpenAI API 설정
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # CORS 설정
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')

    # 외부 API 설정
    FETCH_COUNT_LIMIT = int(os.getenv("FETCH_COUNT_LIMIT", 10))
    MYPAGE_EDU_CONTENTS_POPUP_URL = os.getenv("MYPAGE_EDU_CONTENTS_POPUP_URL")

    # 기타 설정
    SOME_OTHER_CONFIG = os.getenv('SOME_OTHER_CONFIG', 'default_value')


class DevelopmentConfig(Config):
    """개발 환경 설정"""
    DEBUG = True
    DATABASE_URL = os.getenv('DEV_DATABASE_URL', 'sqlite:///' + str(basedir / 'dev.db'))


class TestingConfig(Config):
    """테스트 환경 설정"""
    TESTING = True
    DATABASE_URL = os.getenv('TEST_DATABASE_URL', 'sqlite:///' + str(basedir / 'test.db'))


class ProductionConfig(Config):
    """운영 환경 설정"""
    DEBUG = False


# 환경 변수에 따라 적절한 설정 클래스를 반환
def get_config(env: str):
    if env == 'development':
        return DevelopmentConfig()
    elif env == 'testing':
        return TestingConfig()
    elif env == 'production':
        return ProductionConfig()
    return Config()


current_config = get_config(os.getenv('FASTAPI_ENV', 'production'))
