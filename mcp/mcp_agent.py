import asyncio
import random
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

from executor import AgentExecutor, MCPServerRegistry


# =========================================================
# TOOL CATALOG — 반도체 도메인 MCP Tool 메타데이터
# =========================================================

TOOL_CATALOG: List[Dict] = [
    {
        "tool_name": "process_master_query",
        "description": "라인 및 공정 마스터 정보 조회 공정 ID 공정명 노드 정보 반환",
        "tags": ["process", "master", "line", "공정", "라인", "id", "node", "마스터", "정보"],
        "examples": ["공정 정보 조회", "라인별 공정 마스터", "공정 ID 조회"],
    },
    {
        "tool_name": "wafer_yield_query",
        "description": "라인 및 공정 기준 웨이퍼 수율 조회 합격률 양품률",
        "tags": ["wafer", "yield", "수율", "process", "manufacturing", "공정", "라인", "웨이퍼", "합격", "양품"],
        "examples": ["라인별 수율 조회", "공정별 수율 조회", "이번 달 수율", "웨이퍼 수율"],
    },
    {
        "tool_name": "process_defect_query",
        "description": "공정별 웨이퍼 불량 현황 및 불량 유형 분석 결함 파티클",
        "tags": ["defect", "불량", "결함", "process", "공정", "파티클", "particle", "불량률", "분석"],
        "examples": ["불량률 조회", "공정 불량 분석", "파티클 불량", "결함 현황"],
    },
    {
        "tool_name": "equipment_alarm_history",
        "description": "설비 알람 이력 조회 공정별 장비 알람 경보 내역",
        "tags": ["alarm", "알람", "equipment", "설비", "장비", "이상", "경보", "process", "이력"],
        "examples": ["장비 알람 조회", "설비 이상 내역", "알람 이력", "장비 경보"],
    },
    {
        "tool_name": "line_summary_query",
        "description": "라인 전체 생산 현황 요약 수율 공정 수 납기율 대시보드 개요",
        "tags": ["line", "summary", "요약", "현황", "라인", "전체", "overview", "생산", "대시보드", "납기"],
        "examples": ["라인 현황", "전체 요약", "라인 대시보드", "생산 현황"],
    },
]


# =========================================================
# SEMICONDUCTOR MCP REGISTRY — 반도체 도메인 Tool mock 구현
# =========================================================

class SemiconductorMCPRegistry(MCPServerRegistry):

    async def call_tool(
        self,
        tool_name: str,
        arguments: Dict[str, Any]
    ) -> Dict[str, Any]:

        print(f"[CALL] {tool_name} -> {arguments}")

        await asyncio.sleep(random.uniform(0.2, 0.8))

        if tool_name == "process_master_query":
            return self._process_master_query(arguments)

        elif tool_name == "wafer_yield_query":
            return self._wafer_yield_query(arguments)

        elif tool_name == "process_defect_query":
            return self._process_defect_query(arguments)

        elif tool_name == "equipment_alarm_history":
            return self._equipment_alarm_history(arguments)

        elif tool_name == "line_summary_query":
            return self._line_summary_query(arguments)

        else:
            return await super().call_tool(tool_name, arguments)

    def _process_master_query(self, args: Dict) -> Dict:
        line = args.get("line", "AA")
        process = args.get("process", "BB")
        process_types = ["Diffusion", "Etch", "CVD", "CMP", "Lithography", "Ion Implant"]
        nodes = ["28nm", "14nm", "7nm", "5nm", "3nm"]
        random.seed(hash(f"{line}{process}") % 1000)
        return {
            "status": "success",
            "tool": "process_master_query",
            "data": {
                "process_id": f"PROC-{process}-{random.randint(100, 999):03d}",
                "line": line,
                "process_name": process,
                "process_type": random.choice(process_types),
                "node": random.choice(nodes),
            }
        }

    def _wafer_yield_query(self, args: Dict) -> Dict:
        process_id = args.get("process_id", "PROC-BB-001")
        period = args.get("period", "2026-05")
        random.seed(hash(f"{process_id}{period}") % 1000)
        wafer_count = random.randint(8000, 20000)
        yield_pct = round(random.uniform(90.0, 99.5), 2)
        pass_count = int(wafer_count * yield_pct / 100)
        fail_count = wafer_count - pass_count
        return {
            "status": "success",
            "tool": "wafer_yield_query",
            "data": {
                "process_id": process_id,
                "period": period,
                "yield_pct": yield_pct,
                "wafer_count": wafer_count,
                "pass_count": pass_count,
                "fail_count": fail_count,
                "unit": "%",
            }
        }

    def _process_defect_query(self, args: Dict) -> Dict:
        process_id = args.get("process_id", "PROC-BB-001")
        period = args.get("period", "2026-05")
        random.seed(hash(f"{process_id}{period}defect") % 1000)
        defect_types = ["Particle", "Scratch", "Bridge", "Open", "Void", "Pinhole"]
        defect_rate = round(random.uniform(0.5, 5.0), 2)
        defect_count = random.randint(100, 800)
        return {
            "status": "success",
            "tool": "process_defect_query",
            "data": {
                "process_id": process_id,
                "period": period,
                "defect_rate": defect_rate,
                "defect_count": defect_count,
                "top_defect_type": random.choice(defect_types),
            }
        }

    def _equipment_alarm_history(self, args: Dict) -> Dict:
        process_id = args.get("process_id", "PROC-BB-001")
        period = args.get("period", "2026-05")
        random.seed(hash(f"{process_id}{period}alarm") % 1000)
        alarm_codes = ["TEMP_HIGH", "PRESS_LOW", "FLOW_ERR", "VALVE_FAIL", "SENSOR_ERR"]
        severities = ["CRITICAL", "WARNING", "INFO"]
        alarm_count = random.randint(5, 30)
        critical_alarms = random.randint(0, 5)
        alarms = [
            {
                "eq_id": f"EQ-{random.randint(100,999)}",
                "eq_name": f"설비-{chr(65 + i)}",
                "alarm_code": random.choice(alarm_codes),
                "timestamp": f"{period}-{random.randint(1,28):02d} {random.randint(0,23):02d}:{random.randint(0,59):02d}",
                "severity": random.choice(severities),
            }
            for i in range(min(3, alarm_count))
        ]
        return {
            "status": "success",
            "tool": "equipment_alarm_history",
            "data": {
                "process_id": process_id,
                "period": period,
                "alarm_count": alarm_count,
                "critical_alarms": critical_alarms,
                "alarms": alarms,
            }
        }

    def _line_summary_query(self, args: Dict) -> Dict:
        line = args.get("line", "AA")
        period = args.get("period", "2026-05")
        random.seed(hash(f"{line}{period}summary") % 1000)
        processes = ["AA", "BB", "CC", "DD", "EE"]
        return {
            "status": "success",
            "tool": "line_summary_query",
            "data": {
                "line": line,
                "period": period,
                "total_wafers": random.randint(40000, 80000),
                "avg_yield_pct": round(random.uniform(92.0, 98.5), 1),
                "process_count": random.randint(8, 20),
                "top_issue_process": random.choice(processes),
                "on_time_rate": round(random.uniform(85.0, 99.0), 1),
            }
        }


# =========================================================
# INTENT PARSER — 사용자 질문 구조화
# =========================================================

@dataclass
class ParsedIntent:
    intent: str
    line: Optional[str]
    process: Optional[str]
    metric: Optional[str]
    period: str
    raw_query: str


class IntentParser:

    YIELD_KEYWORDS = {"수율", "yield", "양품", "합격률", "pass", "rate", "양품률"}
    DEFECT_KEYWORDS = {"불량", "defect", "결함", "파티클", "particle", "불량률", "스크래치"}
    ALARM_KEYWORDS = {"알람", "alarm", "경보", "장비", "equipment", "설비", "이상", "알람이력"}
    SUMMARY_KEYWORDS = {"요약", "현황", "summary", "전체", "overview", "대시보드", "dashboard"}

    LINE_PATTERN = re.compile(r'([A-Za-z]{1,3})\s*라인')
    PROC_PATTERN = re.compile(r'([A-Za-z]{1,3})\s*공정')
    PERIOD_PATTERN = re.compile(r'(\d{4}[-/]\d{2})')

    def parse(self, query: str) -> ParsedIntent:
        intent, metric = self._classify_intent(query)
        line = self._extract_line(query)
        process = self._extract_process(query)
        period = self._extract_period(query)

        result = ParsedIntent(
            intent=intent,
            line=line.upper() if line else None,
            process=process.upper() if process else None,
            metric=metric,
            period=period,
            raw_query=query,
        )
        print(f"[IntentParser] intent={result.intent} line={result.line} process={result.process} period={result.period}")
        return result

    def _classify_intent(self, query: str) -> Tuple[str, Optional[str]]:
        lower = query.lower()
        # 서브스트링 매칭: 조사 붙은 한국어 단어도 처리 (수율을, 라인의 등)
        has = lambda kws: any(kw in lower for kw in kws)

        if has(self.DEFECT_KEYWORDS):
            return "process_defect_query", "defect"
        if has(self.ALARM_KEYWORDS):
            return "equipment_alarm", "alarm"
        if has(self.SUMMARY_KEYWORDS) and not self._extract_process(query):
            return "line_summary", "summary"
        if has(self.YIELD_KEYWORDS):
            return "wafer_yield_query", "yield"
        if has(self.SUMMARY_KEYWORDS):
            return "wafer_yield_query", "yield"
        return "unknown", None

    def _extract_line(self, query: str) -> Optional[str]:
        m = self.LINE_PATTERN.search(query)
        return m.group(1) if m else None

    def _extract_process(self, query: str) -> Optional[str]:
        m = self.PROC_PATTERN.search(query)
        return m.group(1) if m else None

    def _extract_period(self, query: str) -> str:
        m = self.PERIOD_PATTERN.search(query)
        if m:
            return m.group(1).replace("/", "-")
        # 이번 달 기본값
        return datetime.now().strftime("%Y-%m")


# =========================================================
# TOOL RETRIEVER — 관련 Tool 후보 검색 (RAG 시뮬레이션)
# =========================================================

class ToolRetriever:

    def __init__(self, catalog: List[Dict], top_k: int = 3):
        self.catalog = catalog
        self.top_k = top_k

    def retrieve(self, intent: ParsedIntent) -> List[Dict]:
        scored = []
        for tool in self.catalog:
            score = self._score(tool, intent)
            scored.append({**tool, "score": round(score, 3)})
        scored.sort(key=lambda x: x["score"], reverse=True)
        results = scored[: self.top_k]
        print(f"[ToolRetriever] top-{self.top_k} candidates: {[(t['tool_name'], t['score']) for t in results]}")
        return results

    def _score(self, tool: Dict, intent: ParsedIntent) -> float:
        # 검색 대상: tool의 태그 + description 단어
        tool_tokens = set(t.lower() for t in tool["tags"])
        for word in tool["description"].lower().split():
            tool_tokens.add(word)

        # query 텍스트 (조사 붙은 한국어 처리 위해 서브스트링 매칭 사용)
        query_lower = intent.raw_query.lower()
        intent_parts = [p for p in intent.intent.split("_")]

        overlap = sum(
            1 for t in tool_tokens
            if t in query_lower or any(t in p for p in intent_parts)
        )
        raw_score = overlap / max(len(tool_tokens), 1)
        bonus = 0.3 if tool["tool_name"] == intent.intent else 0.0
        return min(1.0, raw_score + bonus)


# =========================================================
# TOOL PLANNER — 실행 계획 생성
# =========================================================

class ToolPlanner:

    def plan(
        self,
        intent: ParsedIntent,
        candidates: List[Dict],
    ) -> Tuple[List[Dict], Dict[str, Any]]:

        line = intent.line or "ALL"
        process = intent.process
        period = intent.period

        if intent.intent == "line_summary" or (intent.intent in ("wafer_yield_query", "unknown") and not process):
            plan, ctx = self._line_summary_plan(line, period)

        elif intent.intent == "wafer_yield_query" and process:
            plan, ctx = self._yield_plan(line, process, period)

        elif intent.intent == "process_defect_query" and process:
            plan, ctx = self._defect_plan(line, process, period)

        elif intent.intent == "equipment_alarm" and process:
            plan, ctx = self._alarm_plan(line, process, period)

        else:
            # fallback: 후보 1위 Tool로 단일 step
            top_tool = candidates[0]["tool_name"] if candidates else "line_summary_query"
            plan = [{"id": "step1", "tool": top_tool, "arguments": {"line": "$line", "period": "$period"}}]
            ctx = {"line": line, "period": period}

        step_summary = [f"{s['id']}:{s['tool']}" for s in plan]
        print(f"[ToolPlanner] plan steps: {step_summary}")
        return plan, ctx

    def _yield_plan(self, line: str, process: str, period: str):
        ctx = {"line": line, "process": process, "period": period}
        plan = [
            {
                "id": "step1",
                "tool": "process_master_query",
                "arguments": {"line": "$line", "process": "$process"},
            },
            {
                "id": "step2",
                "tool": "wafer_yield_query",
                "arguments": {"process_id": "$step1.data.process_id", "period": "$period"},
                "depends_on": ["step1"],
            },
        ]
        return plan, ctx

    def _defect_plan(self, line: str, process: str, period: str):
        ctx = {"line": line, "process": process, "period": period}
        plan = [
            {
                "id": "step1",
                "tool": "process_master_query",
                "arguments": {"line": "$line", "process": "$process"},
            },
            {
                "id": "step2",
                "tool": "wafer_yield_query",
                "arguments": {"process_id": "$step1.data.process_id", "period": "$period"},
                "depends_on": ["step1"],
            },
            {
                "id": "step3",
                "tool": "process_defect_query",
                "arguments": {"process_id": "$step1.data.process_id", "period": "$period"},
                "depends_on": ["step1"],  # step2, step3 병렬 실행
            },
        ]
        return plan, ctx

    def _alarm_plan(self, line: str, process: str, period: str):
        ctx = {"line": line, "process": process, "period": period}
        plan = [
            {
                "id": "step1",
                "tool": "process_master_query",
                "arguments": {"line": "$line", "process": "$process"},
            },
            {
                "id": "step2",
                "tool": "equipment_alarm_history",
                "arguments": {"process_id": "$step1.data.process_id", "period": "$period"},
                "depends_on": ["step1"],
            },
        ]
        return plan, ctx

    def _line_summary_plan(self, line: str, period: str):
        ctx = {"line": line, "period": period}
        plan = [
            {
                "id": "step1",
                "tool": "line_summary_query",
                "arguments": {"line": "$line", "period": "$period"},
            }
        ]
        return plan, ctx


# =========================================================
# RESULT AGGREGATOR — 단계별 결과 통합
# =========================================================

INTERNAL_KEYS = {"process_id", "defect_map_url"}


class ResultAggregator:

    def aggregate(
        self,
        results: Dict[str, Any],
        intent: ParsedIntent,
    ) -> Dict[str, Any]:

        aggregated: Dict[str, Any] = {
            "line": intent.line,
            "process": intent.process,
            "period": intent.period,
            "metric": intent.metric,
        }
        errors = []
        has_success = False

        for step_id in sorted(results.keys()):
            result = results[step_id]
            if result.get("status") == "error":
                errors.append({"step": step_id, "message": result.get("message")})
            elif result.get("status") == "success" and result.get("data"):
                has_success = True
                data = {k: v for k, v in result["data"].items() if k not in INTERNAL_KEYS}
                aggregated.update(data)

        aggregated["success"] = has_success and not errors
        if errors:
            aggregated["errors"] = errors

        print(f"[ResultAggregator] aggregated keys: {list(aggregated.keys())}")
        return aggregated


# =========================================================
# RESPONSE GENERATOR — 한국어 자연어 응답 생성
# =========================================================

class ResponseGenerator:

    def generate(self, aggregated: Dict[str, Any]) -> str:
        metric = aggregated.get("metric")
        prefix = ""
        if not aggregated.get("success"):
            prefix = "일부 데이터 조회에 실패했습니다. 확인 가능한 정보만 표시합니다.\n\n"

        print(f"[ResponseGenerator] template used: {metric}")

        if metric == "yield":
            body = self._yield_response(aggregated)
        elif metric == "defect":
            body = self._defect_response(aggregated)
        elif metric == "alarm":
            body = self._alarm_response(aggregated)
        elif metric == "summary":
            body = self._summary_response(aggregated)
        else:
            body = self._fallback_response(aggregated)

        return prefix + body

    def _yield_response(self, d: Dict) -> str:
        line = d.get("line", "-")
        process = d.get("process", "-")
        period = d.get("period", "-")
        yield_pct = d.get("yield_pct", 0)
        wafer_count = d.get("wafer_count", 0)
        pass_count = d.get("pass_count", 0)
        fail_count = d.get("fail_count", 0)
        process_type = d.get("process_type", "-")
        node = d.get("node", "-")
        return (
            f"{line}라인의 {process}공정 {period} 웨이퍼 수율 현황입니다.\n\n"
            f"- 평균 수율: {yield_pct:.2f}%\n"
            f"- 분석 웨이퍼 수: {wafer_count:,}장\n"
            f"- 합격: {pass_count:,}장 / 불합격: {fail_count:,}장\n"
            f"- 공정 유형: {process_type} ({node} 노드)"
        )

    def _defect_response(self, d: Dict) -> str:
        line = d.get("line", "-")
        process = d.get("process", "-")
        period = d.get("period", "-")
        defect_rate = d.get("defect_rate", 0)
        defect_count = d.get("defect_count", 0)
        top_defect = d.get("top_defect_type", "-")
        yield_pct = d.get("yield_pct")
        yield_line = f"- 수율 (참고): {yield_pct:.2f}%\n" if yield_pct is not None else ""
        return (
            f"{line}라인의 {process}공정 {period} 불량 현황입니다.\n\n"
            f"- 불량률: {defect_rate:.2f}%\n"
            f"- 불량 수: {defect_count:,}장\n"
            f"- 주요 불량 유형: {top_defect}\n"
            f"{yield_line}"
        ).rstrip()

    def _alarm_response(self, d: Dict) -> str:
        line = d.get("line", "-")
        process = d.get("process", "-")
        period = d.get("period", "-")
        alarm_count = d.get("alarm_count", 0)
        critical_alarms = d.get("critical_alarms", 0)
        alarms = d.get("alarms", [])
        alarm_lines = "\n".join(
            f"  · [{a.get('severity')}] {a.get('eq_name')} — {a.get('alarm_code')} ({a.get('timestamp')})"
            for a in alarms[:3]
        )
        return (
            f"{line}라인의 {process}공정 {period} 설비 알람 이력입니다.\n\n"
            f"- 총 알람 수: {alarm_count}건\n"
            f"- 긴급 알람: {critical_alarms}건\n"
            f"- 주요 알람 내역:\n{alarm_lines}"
        )

    def _summary_response(self, d: Dict) -> str:
        line = d.get("line", "-")
        period = d.get("period", "-")
        total_wafers = d.get("total_wafers", 0)
        avg_yield = d.get("avg_yield_pct", 0)
        process_count = d.get("process_count", 0)
        on_time = d.get("on_time_rate", 0)
        top_issue = d.get("top_issue_process", "-")
        return (
            f"{line}라인 {period} 전체 생산 현황 요약입니다.\n\n"
            f"- 총 웨이퍼 투입: {total_wafers:,}장\n"
            f"- 평균 수율: {avg_yield:.1f}%\n"
            f"- 관리 공정 수: {process_count}개\n"
            f"- 납기 준수율: {on_time:.1f}%\n"
            f"- 수율 이슈 공정: {top_issue}공정"
        )

    def _fallback_response(self, d: Dict) -> str:
        skip = {"success", "metric", "errors", "line", "process", "period"}
        lines = [f"- {k}: {v}" for k, v in d.items() if k not in skip]
        header = "조회된 데이터를 분석했습니다.\n\n"
        return header + "\n".join(lines)


# =========================================================
# MCP AGENT — 전체 파이프라인 오케스트레이터
# =========================================================

class MCPAgent:

    def __init__(self):
        self.registry = SemiconductorMCPRegistry()
        self.executor = AgentExecutor(self.registry)
        self.parser = IntentParser()
        self.retriever = ToolRetriever(TOOL_CATALOG, top_k=3)
        self.planner = ToolPlanner()
        self.aggregator = ResultAggregator()
        self.generator = ResponseGenerator()

    async def run(self, query: str) -> str:
        print(f"\n{'=' * 60}")
        print(f"[MCPAgent] Query: {query}")
        print(f"{'=' * 60}")

        # 1. Intent Parsing
        intent = self.parser.parse(query)

        # 2. Tool Retrieval (RAG 시뮬레이션)
        candidates = self.retriever.retrieve(intent)

        # 3. Tool Planning (실행 계획 생성)
        plan, initial_context = self.planner.plan(intent, candidates)

        # 4+5. Execution DAG + MCP 호출
        raw_results = await self.executor.execute_plan(plan, initial_context)

        # 6. Result Aggregation
        aggregated = self.aggregator.aggregate(raw_results, intent)

        # 7. Final Response Generation
        response = self.generator.generate(aggregated)

        print(f"\n{'─' * 60}")
        print(f"[최종 응답]\n{response}")
        print(f"{'─' * 60}\n")

        return response


# =========================================================
# DEMO
# =========================================================

async def main():
    agent = MCPAgent()

    queries = [
        # 1. 수율 조회 — process_master → wafer_yield (순차)
        "AA라인의 BB공정에서 만들어진 웨이퍼의 이번 달 수율을 알려줘",
        # 2. 불량 조회 — process_master → [wafer_yield + process_defect] (병렬)
        "CC라인 DD공정의 이번 달 불량 현황이 어떻게 돼?",
        # 3. 라인 요약 — line_summary 단일 step
        "AA라인 전체 현황 요약해줘",
    ]

    for query in queries:
        await agent.run(query)
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
