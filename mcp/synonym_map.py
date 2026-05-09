# -*- coding: utf-8 -*-
"""
Semiconductor MCP Tools Synonym Map
반도체 공정 MCP 툴의 tags를 기반으로 구성한 동의어/유사어 매핑 사전.

- Key   : 대표 검색어 (영문 표준 용어 또는 약어)
- Value : 해당 개념과 동의어/유사어 리스트 (한국어, 영문 변형, 약어, 관련어)
"""

SYNONYM_MAP = {
    # ============================================================
    # 1. 웨이퍼 & 기본 자재
    # ============================================================
    "wafer": [
        "웨이퍼",
        "기판",
        "substrate"
    ],
    "ingot": [
        "잉곳",
        "결정",
        "성장",
        "단결정",
        "Czochralski"
    ],
    "slicing": [
        "슬라이싱",
        "절단",
        "치수",
        "두께",
        "직경"
    ],
    "lapping": [
        "래핑",
        "평탄도",
        "TTV",
        "표면연마"
    ],
    "polishing": [
        "폴리싱",
        "연마",
        "표면",
        "거칠기",
        "Ra"
    ],
    "cleaning": [
        "세정",
        "세척",
        "RCA",
        "화학약품"
    ],
    "bow": [
        "휨",
        "warp",
        "굽힘",
        "변형"
    ],
    "warp": [
        "굽힘",
        "휨",
        "bow",
        "변형"
    ],

    # ============================================================
    # 2. 산화 (Oxidation)
    # ============================================================
    "oxidation": [
        "산화",
        "산화공정",
        "oxide",
        "산화막"
    ],
    "oxide": [
        "산화막",
        "oxidation",
        "절연막"
    ],
    "dry oxidation": [
        "건식산화",
        "dry oxide",
        "건식"
    ],
    "wet oxidation": [
        "습식산화",
        "wet oxide",
        "습식"
    ],
    "furnace": [
        "퍼니스",
        "확산로",
        "산화로",
        "열처리로"
    ],
    "gate oxide": [
        "게이트산화막",
        "gate ox",
        "GOX"
    ],
    "breakdown": [
        "절연파괴",
        "BV",
        "항복전압",
        "내압"
    ],

    # ============================================================
    # 3. 포토 / 리소그래피 (Photo / Lithography)
    # ============================================================
    "photo": [
        "포토",
        "사진공정",
        "litho",
        "lithography",
        "리소"
    ],
    "litho": [
        "리소",
        "lithography",
        "포토",
        "photo"
    ],
    "mask": [
        "마스크",
        "reticle",
        "레티클"
    ],
    "reticle": [
        "레티클",
        "mask",
        "마스크"
    ],
    "alignment": [
        "정합도",
        "정렬",
        "얼라인",
        "align"
    ],
    "overlay": [
        "오버레이",
        "정렬오차",
        "오차",
        "정합오차"
    ],
    "photoresist": [
        "포토레지스트",
        "PR",
        "감광액",
        "레지스트"
    ],
    "PR": [
        "포토레지스트",
        "photoresist",
        "감광액",
        "레지스트"
    ],
    "coating": [
        "코팅",
        "도포",
        "스핀코팅"
    ],
    "exposure": [
        "노광",
        "조사",
        "expose"
    ],
    "dose": [
        "도즈",
        "노광량",
        "도즈량",
        "조사량"
    ],
    "develop": [
        "현상",
        "developing",
        "현상공정"
    ],
    "stepper": [
        "스테퍼",
        "노광기",
        "scanner",
        "스캐너"
    ],
    "critical dimension": [
        "임계치수",
        "CD",
        "선폭",
        "패턴폭"
    ],
    "CD": [
        "임계치수",
        "critical dimension",
        "선폭",
        "패턴폭"
    ],
    "rework": [
        "재작업",
        "리워크",
        "재가공"
    ],

    # ============================================================
    # 4. 식각 (Etching)
    # ============================================================
    "etch": [
        "식각",
        "etching",
        "에칭"
    ],
    "etching": [
        "식각",
        "etch",
        "에칭"
    ],
    "dry etch": [
        "건식식각",
        "drying etch",
        "플라즈마식각"
    ],
    "wet etch": [
        "습식식각",
        "wet etching",
        "약품식각"
    ],
    "plasma": [
        "플라즈마",
        "plasma etch",
        "RIE",
        "이온"
    ],
    "RF": [
        "RF파워",
        "고주파",
        "파워",
        "power"
    ],
    "endpoint": [
        "엔드포인트",
        "EPD",
        "종점검출"
    ],
    "selectivity": [
        "선택비",
        "etch ratio",
        "식각선택비"
    ],
    "profile": [
        "프로파일",
        "단면",
        "사이드월",
        "sidewall"
    ],
    "byproduct": [
        "부산물",
        "잔류물",
        "by-product"
    ],
    "bath": [
        "배스",
        "약품조",
        "도금조",
        "용액조"
    ],
    "chamber cleaning": [
        "챔버청소",
        "PM",
        "장비청소",
        "wet clean"
    ],

    # ============================================================
    # 5. 증착 (Deposition / CVD / PVD / ALD)
    # ============================================================
    "deposition": [
        "증착",
        "박막형성",
        "성막",
        "deposit"
    ],
    "CVD": [
        "화학기상증착",
        "chemical vapor deposition",
        "화학기상"
    ],
    "PVD": [
        "물리기상증착",
        "physical vapor deposition",
        "물리기상",
        "sputtering"
    ],
    "ALD": [
        "원자층증착",
        "atomic layer deposition",
        "원자층"
    ],
    "sputtering": [
        "스퍼터링",
        "스퍼터",
        "PVD",
        "물리기상"
    ],
    "epi": [
        "에피",
        "epitaxy",
        "epitaxial",
        "에피택셜"
    ],
    "epitaxy": [
        "에피택시",
        "epi",
        "에피"
    ],
    "deposition rate": [
        "증착속도",
        "rate",
        "성막속도"
    ],
    "film": [
        "박막",
        "film layer",
        "thin film",
        "층"
    ],
    "stress": [
        "응력",
        "필름응력",
        "tensile",
        "compressive"
    ],
    "refractive index": [
        "굴절률",
        "RI",
        "n-value"
    ],
    "particle": [
        "파티클",
        "이물",
        "오염",
        "분진"
    ],

    # ============================================================
    # 6. 이온주입 (Ion Implantation)
    # ============================================================
    "implant": [
        "이온주입",
        "implantation",
        "도핑",
        "doping"
    ],
    "implanter": [
        "이온주입기",
        "implant 장비",
        "임플란터"
    ],
    "dopant": [
        "도펀트",
        "species",
        "불순물",
        "도핑물질"
    ],
    "species": [
        "도펀트",
        "이온종",
        "dopant"
    ],
    "beam current": [
        "빔전류",
        "이온빔",
        "beam"
    ],
    "annealing": [
        "어닐링",
        "열처리",
        "anneal",
        "활성화"
    ],
    "junction": [
        "접합",
        "접합깊이",
        "Xj",
        "junction depth"
    ],
    "Xj": [
        "접합깊이",
        "junction depth",
        "junction"
    ],
    "sheet resistance": [
        "면저항",
        "Rs",
        "시트저항"
    ],
    "Rs": [
        "면저항",
        "sheet resistance",
        "시트저항"
    ],

    # ============================================================
    # 7. 금속배선 (Metallization / Interconnect)
    # ============================================================
    "metal": [
        "금속",
        "metallization",
        "배선"
    ],
    "metallization": [
        "금속배선",
        "metal",
        "배선공정"
    ],
    "metal line": [
        "금속선",
        "배선",
        "interconnect"
    ],
    "interconnect": [
        "배선",
        "metal line",
        "연결선"
    ],
    "copper": [
        "구리",
        "Cu",
        "구리배선"
    ],
    "electroplating": [
        "전기도금",
        "도금",
        "plating",
        "ECP"
    ],
    "CMP": [
        "화학기계연마",
        "chemical mechanical polishing",
        "연마",
        "polishing"
    ],
    "barrier": [
        "배리어",
        "barrier metal",
        "확산방지막",
        "TiN",
        "TaN"
    ],
    "via": [
        "비아",
        "via hole",
        "관통홀"
    ],
    "filling": [
        "충전",
        "fill",
        "갭필",
        "gap fill"
    ],
    "continuity": [
        "단선",
        "도통",
        "연속성",
        "open"
    ],
    "resistance": [
        "저항",
        "resistance",
        "저항값",
        "Ω"
    ],
    "grain size": [
        "결정립크기",
        "grain",
        "결정립"
    ],

    # ============================================================
    # 8. EDS / 테스트 (Test)
    # ============================================================
    "test": [
        "테스트",
        "검사",
        "시험",
        "측정"
    ],
    "EDS": [
        "전기검사",
        "electrical die sorting",
        "die sorting",
        "웨이퍼테스트"
    ],
    "die sorting": [
        "다이소팅",
        "EDS",
        "분류"
    ],
    "BIN": [
        "빈",
        "bin map",
        "분류등급"
    ],
    "bin map": [
        "빈맵",
        "BIN",
        "분류맵"
    ],
    "fail bit": [
        "페일비트",
        "FBM",
        "fail bit map",
        "불량비트"
    ],
    "FBM": [
        "fail bit map",
        "페일비트맵",
        "불량비트맵"
    ],
    "probe card": [
        "프로브카드",
        "probing",
        "테스트카드"
    ],
    "tester": [
        "테스터",
        "검사장비",
        "테스트장비"
    ],
    "parametric": [
        "파라메트릭",
        "PT",
        "전기특성"
    ],
    "PT": [
        "parametric test",
        "파라메트릭테스트",
        "전기특성검사"
    ],
    "test program": [
        "테스트프로그램",
        "TP",
        "검사프로그램"
    ],
    "test yield": [
        "테스트수율",
        "검사수율",
        "EDS yield"
    ],
    "repair": [
        "리페어",
        "수리",
        "redundancy",
        "리던던시"
    ],
    "redundancy": [
        "리던던시",
        "예비셀",
        "repair",
        "리페어"
    ],
    "burn-in": [
        "번인",
        "burnin",
        "에이징",
        "신뢰성테스트"
    ],
    "final test": [
        "최종검사",
        "FT",
        "최종테스트"
    ],
    "FT": [
        "final test",
        "최종검사",
        "최종테스트"
    ],

    # ============================================================
    # 9. 패키징 (Packaging / Assembly)
    # ============================================================
    "package": [
        "패키지",
        "packaging",
        "조립",
        "assembly"
    ],
    "assembly": [
        "어셈블리",
        "조립",
        "package"
    ],
    "die attach": [
        "다이어태치",
        "다이부착",
        "die bond",
        "본딩"
    ],
    "wire bonding": [
        "와이어본딩",
        "wire bond",
        "본딩"
    ],
    "molding": [
        "몰딩",
        "EMC",
        "컴파운드",
        "봉지"
    ],
    "marking": [
        "마킹",
        "각인",
        "인쇄",
        "laser marking"
    ],
    "solder ball": [
        "솔더볼",
        "BGA",
        "볼"
    ],
    "BGA": [
        "솔더볼",
        "ball grid array",
        "볼"
    ],
    "shipment": [
        "출하",
        "배송",
        "선적"
    ],

    # ============================================================
    # 10. 품질 / 수율 / 결함
    # ============================================================
    "yield": [
        "수율",
        "양품률",
        "FPY",
        "생산성"
    ],
    "yield loss": [
        "수율손실",
        "loss",
        "손실",
        "수율저하"
    ],
    "quality": [
        "품질",
        "퀄리티",
        "QA",
        "QC"
    ],
    "defect": [
        "결함",
        "디펙트",
        "불량",
        "이상"
    ],
    "inspection": [
        "검사",
        "점검",
        "inspect"
    ],
    "Cpk": [
        "공정능력지수",
        "공정능력",
        "process capability"
    ],
    "audit": [
        "감사",
        "품질감사",
        "심사"
    ],
    "complaint": [
        "불만",
        "클레임",
        "claim",
        "고객불만",
        "품질불만"
    ],
    "uniformity": [
        "균일도",
        "uniform",
        "산포",
        "편차"
    ],

    # ============================================================
    # 11. 설비 / 운영 / 모니터링
    # ============================================================
    "equipment": [
        "설비",
        "장비",
        "tool"
    ],
    "PM": [
        "정기점검",
        "preventive maintenance",
        "예방보전",
        "유지보수"
    ],
    "OEE": [
        "설비종합효율",
        "overall equipment effectiveness",
        "설비효율"
    ],
    "alarm": [
        "알람",
        "이상",
        "경고",
        "fault"
    ],
    "fault": [
        "이상",
        "고장",
        "fault detection",
        "FDC"
    ],
    "FDC": [
        "fault detection and classification",
        "이상감지",
        "이상분류"
    ],
    "SPC": [
        "통계공정관리",
        "statistical process control",
        "관리도"
    ],
    "throughput": [
        "처리량",
        "생산량",
        "출력"
    ],
    "cycle time": [
        "사이클타임",
        "TAT",
        "리드타임",
        "공정시간"
    ],
    "TAT": [
        "turn around time",
        "사이클타임",
        "리드타임"
    ],
    "WIP": [
        "재공품",
        "work in process",
        "재공"
    ],
    "line": [
        "라인",
        "생산라인",
        "FAB",
        "팹"
    ],
    "summary": [
        "요약",
        "현황",
        "대시보드",
        "리포트"
    ],
    "performance": [
        "성능",
        "지표",
        "KPI",
        "퍼포먼스"
    ],
    "history": [
        "이력",
        "log",
        "기록",
        "히스토리"
    ],
    "log": [
        "로그",
        "기록",
        "이력",
        "history"
    ],
    "tracking": [
        "추적",
        "트래킹",
        "모니터링"
    ],
    "traceability": [
        "추적성",
        "이력추적",
        "tracking"
    ],
    "lot": [
        "로트",
        "lot id",
        "배치",
        "batch"
    ],

    # ============================================================
    # 12. 시설 / 환경 / 자재 / 인력
    # ============================================================
    "cleanroom": [
        "클린룸",
        "청정실",
        "FFU",
        "class"
    ],
    "facility": [
        "시설",
        "유틸리티",
        "utility",
        "팹시설"
    ],
    "utility": [
        "유틸리티",
        "전기",
        "DI water",
        "가스"
    ],
    "material": [
        "자재",
        "원자재",
        "raw material",
        "부자재"
    ],
    "inventory": [
        "재고",
        "stock",
        "재고관리",
        "MRP"
    ],
    "chemical": [
        "화학물질",
        "약품",
        "케미컬",
        "화학약품"
    ],
    "operator": [
        "오퍼레이터",
        "작업자",
        "운전자"
    ],
    "customer": [
        "고객",
        "고객사",
        "client",
        "CS"
    ],

    # ============================================================
    # 13. 측정 / 분석 / 변경관리
    # ============================================================
    "recipe": [
        "레시피",
        "공정조건",
        "파라미터",
        "parameter"
    ],
    "compare": [
        "비교",
        "대조",
        "comparison"
    ],
    "correlation": [
        "상관관계",
        "상관성",
        "연관성"
    ],
    "wafer map": [
        "웨이퍼맵",
        "맵",
        "map"
    ],
    "change": [
        "변경",
        "수정",
        "변경관리"
    ],
    "ECN": [
        "engineering change notice",
        "공정변경",
        "변경요청"
    ],
    "PCN": [
        "process change notice",
        "공정변경통지",
        "변경통보"
    ],
    "process": [
        "공정",
        "프로세스",
        "공정단계"
    ],
    "production": [
        "생산",
        "제조",
        "manufacturing"
    ],
    "data": [
        "데이터",
        "자료",
        "정보"
    ],

    # ============================================================
    # 14. 측정 항목 / 단위 / 일반
    # ============================================================
    "pressure": [
        "압력",
        "기압",
        "진공도",
        "vacuum"
    ],
    "temperature": [
        "온도",
        "temp",
        "thermal"
    ],
    "rate": [
        "속도",
        "비율",
        "rate"
    ],
    "carbon": [
        "카본",
        "탄소",
        "C"
    ],
    "AI": [
        "인공지능",
        "artificial intelligence",
        "머신러닝",
        "ML"
    ],

    # ============================================================
    # 15. 분석 / 보고 / 시각화 / 운영 일반
    # ============================================================
    "analysis": [
        "분석",
        "원인분석",
        "분해",
        "해석"
    ],
    "trend": [
        "트렌드",
        "추이",
        "동향",
        "변화"
    ],
    "chart": [
        "차트",
        "그래프",
        "도표",
        "시각화"
    ],
    "pareto": [
        "파레토",
        "Pareto",
        "주요원인",
        "Top N"
    ],
    "visualization": [
        "시각화",
        "맵",
        "차트",
        "그래픽"
    ],
    "status": [
        "상태",
        "현황",
        "공정상태",
        "진행"
    ],
    "schedule": [
        "일정",
        "스케줄",
        "계획",
        "plan"
    ],
    "version": [
        "버전",
        "version",
        "리비전",
        "revision"
    ],
    "check": [
        "점검",
        "확인",
        "체크",
        "검증"
    ],
    "detection": [
        "검출",
        "감지",
        "탐지",
        "이상감지"
    ],
    "improvement": [
        "개선",
        "향상",
        "보완",
        "최적화"
    ],
    "management": [
        "관리",
        "통제",
        "운영",
        "control"
    ],
    "utilization": [
        "활용",
        "가동률",
        "가동",
        "사용률"
    ],
    "consumption": [
        "소비량",
        "사용량",
        "소모량"
    ],
    "supply": [
        "공급",
        "지급",
        "제공"
    ],
    "energy": [
        "에너지",
        "전력",
        "power",
        "에너지량"
    ],
    "pattern": [
        "패턴",
        "형상",
        "패턴결함",
        "이상패턴"
    ],
    "fail": [
        "페일",
        "불량",
        "실패",
        "fail"
    ],
    "memory": [
        "메모리",
        "DRAM",
        "NAND",
        "memory chip"
    ],
    "reliability": [
        "신뢰성",
        "수명",
        "TCT",
        "HAST"
    ],
    "skill": [
        "스킬",
        "역량",
        "기술",
        "능력"
    ],
    "certification": [
        "인증",
        "자격",
        "qualification",
        "qual"
    ],
    "index": [
        "지수",
        "지표",
        "score"
    ],
    "chamber": [
        "챔버",
        "공정챔버",
        "반응실",
        "cavity"
    ],
    "composition": [
        "성분",
        "조성",
        "구성",
        "성분비"
    ],
    "location": [
        "위치",
        "포지션",
        "좌표",
        "지점"
    ],
    "usage history": [
        "사용이력",
        "사용기록",
        "이력"
    ],
    "attach": [
        "부착",
        "접착",
        "부착공정"
    ],
    "crystal quality": [
        "결정품질",
        "결정성",
        "단결정품질"
    ],
}


def get_synonyms(keyword: str) -> list:
    """
    키워드에 대한 동의어 리스트를 반환한다.
    매칭이 없으면 빈 리스트를 반환한다.
    """
    return SYNONYM_MAP.get(keyword, [])


def find_canonical_key(term: str) -> str | None:
    """
    임의의 용어(한국어/영어/약어)에 대해 SYNONYM_MAP의 대표 키를 역으로 찾아 반환한다.
    매칭되는 대표 키가 없으면 None을 반환한다.
    """
    term_lower = term.lower().strip()
    # 1) 키 자체와 일치
    for key in SYNONYM_MAP:
        if key.lower() == term_lower:
            return key
    # 2) value 리스트 내에서 매칭
    for key, synonyms in SYNONYM_MAP.items():
        for syn in synonyms:
            if syn.lower() == term_lower:
                return key
    return None


if __name__ == "__main__":
    print(f"총 동의어 그룹 수: {len(SYNONYM_MAP)}")
    print(f"\n예시 - 'yield' 동의어: {get_synonyms('yield')}")
    print(f"예시 - '수율'의 대표 키: {find_canonical_key('수율')}")
    print(f"예시 - '레티클'의 대표 키: {find_canonical_key('레티클')}")
