# 1. 개요 및 전체 흐름

## 목적

사용자의 자연어 질문을 분석하여
사내에 등록된 다수의 MCP 서버 중 적절한 Tool을 선택하고,
필요한 순서대로 실행한 후 최종 결과를 반환하는 AI Agent 시스템
여기서는 mock-data를 기반으로 동작한다.

---

## 예시 질문

```text
AA라인의 BB공정에서 만들어진 웨이퍼의 이번 달 수율을 알려줘
```

---

## 전체 흐름

```text
User Query
    ↓
Intent Parser
    ↓
Tool Retrieval (RAG)
    ↓
LLM Tool Planning
    ↓
Execution DAG 생성
    ↓
Executor Engine
    ↓
MCP 호출
    ↓
Result Aggregator
    ↓
Final LLM Response
```

---

# 2. User Query

## 사용자 입력

```text
AA라인의 BB공정에서 만들어진 웨이퍼의 이번 달 수율을 알려줘
```

---

## 특징

사용자는:

* DB 구조를 모름
* API 명을 모름
* 공정 흐름을 모름

오직 업무 용어만 사용

---

## Agent의 역할

AI Agent는:

* 질문 의미 파악
* 필요한 시스템 식별
* Tool 선택
* 실행 순서 결정
* 결과 조합

수행 필요

---

# 3. Intent Parser

## 역할

사용자 질문에서:

* Intent
* Entity
* 기간
* 대상

등을 구조화

---

## Intent Parser Prompt 예시

```text
당신은 반도체 제조 업무 분석 AI입니다.

사용자 질문에서 아래 정보를 추출하세요.

반드시 JSON으로만 응답하세요.

추출 항목:
- intent
- line
- process
- metric
- period
```

---

## User Query

```text
AA라인의 BB공정에서 만들어진 웨이퍼의 이번 달 수율을 알려줘
```

---

## LLM 반환 예시

```json
{
  "intent": "wafer_yield_query",
  "line": "AA",
  "process": "BB",
  "metric": "yield",
  "period": "2026-05"
}
```

---

# 4. Tool Retrieval (RAG 검색)

## 목적

100개 이상의 MCP Tool 중
관련성이 높은 Tool 후보만 추출

---

## MCP Tool Metadata 예시

```json
{
  "tool_name": "wafer_yield_query",
  "description": "라인 및 공정 기준 웨이퍼 수율 조회",
  "tags": [
    "wafer",
    "yield",
    "process",
    "manufacturing"
  ],
  "examples": [
    "라인별 수율 조회",
    "공정별 수율 조회"
  ]
}
```

---

## Vector Embedding 대상

```text
tool_name
description
tags
examples
```

---

## Retrieval Query

Intent Parser 결과 기반:

```text
wafer yield AA line BB process monthly yield
```

---

## Retrieval 결과 예시

```json
[
  {
    "tool_name": "wafer_yield_query",
    "score": 0.94
  },
  {
    "tool_name": "process_defect_query",
    "score": 0.81
  },
  {
    "tool_name": "equipment_alarm_history",
    "score": 0.63
  }
]
```

---

# 5. LLM Tool Planning

## 목적

검색된 Tool 후보 중:

* 어떤 Tool을 사용할지
* 어떤 순서로 사용할지
* 어떤 데이터가 필요한지

계획 생성

---

## Planner Prompt 예시

```text
당신은 반도체 공장 업무 Agent Planner입니다.

사용자의 요청을 해결하기 위한 실행 계획을 작성하세요.

규칙:
- 필요한 Tool만 선택
- 단계별 의존성을 정의
- JSON만 반환

사용자 요청:
AA라인의 BB공정 웨이퍼 이번 달 수율 조회

사용 가능한 Tool:
1. process_master_query
2. wafer_yield_query
3. process_defect_query
```

---

## Planner 결과 예시

```json
{
  "plan": [
    {
      "id": "step1",
      "tool": "process_master_query",
      "reason": "BB 공정 ID 조회"
    },
    {
      "id": "step2",
      "tool": "wafer_yield_query",
      "reason": "수율 조회",
      "depends_on": ["step1"]
    }
  ]
}
```

---

# 6. Execution DAG 생성

## 목적

Tool 간 의존 관계를 기반으로 실행 그래프 생성

---

## DAG 구조 예시

```text
step1: process_master_query
            ↓
step2: wafer_yield_query
```

---


## DAG의 장점

* 병렬 실행 가능
* 불필요한 대기 제거
* 실행 순서 명확화
* 장애 지점 추적 가능

---

# 7. Executor Engine

## 역할

실제 Tool 실행 담당

LLM은 실행하지 않고 계획만 생성

---

## Executor 주요 기능

* Dependency 관리
* 병렬 실행
* Retry
* Timeout
* Permission Check
* Audit Logging

---

## Executor 입력 예시

```json
{
  "plan": [
    {
      "id": "step1",
      "tool": "process_master_query",
      "arguments": {
        "line": "AA",
        "process": "BB"
      }
    },
    {
      "id": "step2",
      "tool": "wafer_yield_query",
      "arguments": {
        "process_id": "$step1.data.process_id",
        "period": "2026-05"
      },
      "depends_on": ["step1"]
    }
  ]
}
```

---

## Variable Reference 예시

```text
$step1.data.process_id
```

의미:

```text
step1 실행 결과의 process_id 사용
```

---

# 8. MCP 호출

## 실제 MCP Server 호출

Executor는 MCP Registry를 통해 Tool 호출

---

## MCP 호출 예시

```http
POST /mcp/wafer_yield_query
```

---

## Request 예시

```json
{
  "process_id": "PROC-BB-001",
  "period": "2026-05"
}
```

---

## MCP 응답 예시

```json
{
  "status": "success",
  "data": {
    "yield": 97.32,
    "unit": "%",
    "wafer_count": 12840
  }
}
```

---

## 실패 응답 예시

```json
{
  "status": "error",
  "error_code": "PROCESS_NOT_FOUND",
  "message": "Invalid process id"
}
```

---

# 9. Result Aggregator

## 목적

여러 MCP 결과를 통합 및 정규화

---

## Aggregator 입력 예시

```json
{
  "step1": {
    "status": "success",
    "data": {
      "process_id": "PROC-BB-001"
    }
  },
  "step2": {
    "status": "success",
    "data": {
      "yield": 97.32,
      "unit": "%"
    }
  }
}
```

---

## Aggregated Result 예시

```json
{
  "line": "AA",
  "process": "BB",
  "period": "2026-05",
  "yield": 97.32,
  "unit": "%"
}
```

---

## 추가 가능 기능

* 데이터 정합성 검증
* 이상치 탐지
* 중복 제거
* 단위 통합

---

# 10. Final LLM Response

## 목적

최종 데이터를 사용자 친화적 자연어로 변환

---

## Final Response Prompt 예시

```text
당신은 반도체 제조 분석 AI입니다.

아래 데이터를 기반으로 자연스럽고 간결하게 답변하세요.

데이터:
{
  "line": "AA",
  "process": "BB",
  "period": "2026-05",
  "yield": 97.32,
  "unit": "%"
}
```

---

## 최종 응답 예시

```text
AA라인의 BB공정 웨이퍼 이번 달 평균 수율은 97.32% 입니다.
총 분석 대상 웨이퍼 수는 12,840장입니다.
```
