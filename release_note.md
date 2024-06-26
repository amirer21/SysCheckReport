# Release Notes for SysCheck Report v0.0.1

## 개요
이 문서는 SysCheck Report 버전 0.0.1의 릴리스 노트입니다. 이 초기 릴리스는 시스템 정보를 수집하고 스트레스 테스트를 수행하여 결과를 HTML 보고서로 출력하는 기능을 제공합니다.

## 새로운 기능
- **시스템 정보 수집**: 사용자의 시스템에서 CPU, 메모리, 디스크 사용량 및 운영 체제 정보를 수집합니다.
- **스트레스 테스트 실행**: CPU와 메모리 사용률을 증가시키는 테스트를 실행하여 시스템의 성능을 측정합니다.
- **HTML 보고서 생성**: 수집된 데이터와 테스트 결과를 HTML 형식의 보고서로 생성하여 사용자가 쉽게 결과를 확인할 수 있습니다.

<div style="text-align: center">
  <img src="images/report_screenshot.png" alt="Project Screenshot">
</div>

## 파일별 기능
> time_test01.py 

기본 time.time() start ~ end

> time_test_datetime.py

datetime.now()

> time_test_time.py

time.time()

> time_test_timeit.py

 timeit.timeit()

> time_test_time_perf_counter.py

 timeit.perf_counter()

## 수정 사항
- 이 버전에는 수정 사항이 포함되어 있지 않습니다.

## 알려진 문제
- 대규모 데이터를 처리할 때 메모리 사용량이 예상보다 높을 수 있습니다. 다음 버전에서 성능 최적화를 계획하고 있습니다.

## 설치 및 업그레이드 방법
이 버전을 설치하거나 업그레이드하려면 다음 지침을 따르십시오:
1. GitHub에서 최신 릴리스를 다운로드하세요: `https://github.com/amirer21/syscheckreport`
2. 다운로드 받은 파일을 압축 해제합니다.
3. 터미널에서 다음 명령어를 실행하여 필요한 패키지를 설치합니다:
4. `system_checker_*.py` 파일들을 실행하여 프로그램을 시작합니다.

---------------

## 빌드 환경(파이썬 가상환경 설정 명령어)

## 가상환경 생성
### Windows
> python -m venv [가상환경 이름]

### macOS/Linux
> python3 -m venv [가상환경 이름]

## 가상환경 활성화
### Windows
> [가상환경 이름]\Scripts\activate

### macOS/Linux
> source [가상환경 이름]/bin/activate

## 가상환경 비활성화
> deactivate

## 패키지 설치
# 가상환경이 활성화된 상태에서 다음 명령어를 실행합니다.
> pip install [패키지 이름]

## 패키지 목록 출력
# 가상환경이 활성화된 상태에서 다음 명령어를 실행합니다.
> pip list

## 패키지 제거
# 가상환경이 활성화된 상태에서 다음 명령어를 실행합니다.
> pip uninstall [패키지 이름]

## 가상환경 삭제
# 가상환경을 비활성화한 상태에서 가상환경 디렉터리를 직접 삭제합니다.
> rm -r [가상환경 이름]

----------

## 지원
이 버전과 관련된 문제가 발생한 경우, GitHub 이슈 트래커를 통해 보고하거나 직접 문의할 수 있습니다.

## 감사의 글
이 프로젝트의 첫 릴리스를 가능하게 해 준 모든 개발자와 기여자에게 감사합니다.
