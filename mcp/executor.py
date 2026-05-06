import asyncio
import random
from typing import Dict, Any, List


# =========================================================
# MCP SERVER MOCK
# =========================================================

class MCPServerRegistry:
    """
    실제 환경에서는:
    - HTTP 호출
    - gRPC
    - websocket
    - MCP protocol
    등으로 바뀔 부분
    """

    async def call_tool(
        self,
        tool_name: str,
        arguments: Dict[str, Any]
    ) -> Dict[str, Any]:

        print(f"[CALL] {tool_name} -> {arguments}")

        # 네트워크 지연 시뮬레이션
        await asyncio.sleep(random.uniform(0.3, 1.0))

        # -------------------------------
        # TOOL MOCKS
        # -------------------------------

        if tool_name == "employee_lookup":

            employee_name = arguments["employee_name"]

            return {
                "status": "success",
                "tool": tool_name,
                "data": {
                    "employee_id": "EMP-1001",
                    "employee_name": employee_name,
                    "department": "플랫폼개발팀"
                }
            }

        elif tool_name == "expense_query":

            employee_id = arguments["employee_id"]

            return {
                "status": "success",
                "tool": tool_name,
                "data": {
                    "employee_id": employee_id,
                    "total_expense": 1230000,
                    "currency": "KRW",
                    "month": "2026-05"
                }
            }

        elif tool_name == "corp_card_history":

            employee_id = arguments["employee_id"]

            return {
                "status": "success",
                "tool": tool_name,
                "data": {
                    "employee_id": employee_id,
                    "cards": [
                        {
                            "date": "2026-05-01",
                            "amount": 120000,
                            "store": "KTX"
                        },
                        {
                            "date": "2026-05-03",
                            "amount": 80000,
                            "store": "스타벅스"
                        }
                    ]
                }
            }

        else:
            return {
                "status": "error",
                "tool": tool_name,
                "message": f"Unknown tool: {tool_name}"
            }


# =========================================================
# EXECUTOR
# =========================================================

class AgentExecutor:

    def __init__(self, registry: MCPServerRegistry):
        self.registry = registry

    async def execute_plan(
        self,
        plan: List[Dict[str, Any]],
        initial_context: Dict[str, Any]
    ) -> Dict[str, Any]:

        """
        plan 예시:

        [
            {
                "id": "step1",
                "tool": "employee_lookup",
                "arguments": {
                    "employee_name": "$user_name"
                }
            },
            {
                "id": "step2",
                "tool": "expense_query",
                "arguments": {
                    "employee_id": "$step1.data.employee_id"
                },
                "depends_on": ["step1"]
            },
            {
                "id": "step3",
                "tool": "corp_card_history",
                "arguments": {
                    "employee_id": "$step1.data.employee_id"
                },
                "depends_on": ["step1"]
            }
        ]
        """

        results = {}

        completed_steps = set()

        while len(completed_steps) < len(plan):

            runnable_steps = []

            for step in plan:

                step_id = step["id"]

                if step_id in completed_steps:
                    continue

                dependencies = step.get("depends_on", [])

                if all(dep in completed_steps for dep in dependencies):
                    runnable_steps.append(step)

            if not runnable_steps:
                raise Exception("Dependency deadlock detected")

            tasks = []

            for step in runnable_steps:
                tasks.append(
                    self._execute_step(
                        step=step,
                        results=results,
                        initial_context=initial_context
                    )
                )

            step_results = await asyncio.gather(*tasks)

            for step_id, result in step_results:
                results[step_id] = result
                completed_steps.add(step_id)

        return results

    async def _execute_step(
        self,
        step: Dict[str, Any],
        results: Dict[str, Any],
        initial_context: Dict[str, Any]
    ):

        step_id = step["id"]
        tool_name = step["tool"]

        resolved_args = self._resolve_arguments(
            step["arguments"],
            results,
            initial_context
        )

        try:

            tool_result = await self.registry.call_tool(
                tool_name=tool_name,
                arguments=resolved_args
            )

            normalized_result = {
                "status": tool_result.get("status"),
                "tool": tool_name,
                "data": tool_result.get("data"),
                "raw": tool_result
            }

            print(f"[SUCCESS] {step_id}")

            return step_id, normalized_result

        except Exception as e:

            error_result = {
                "status": "error",
                "tool": tool_name,
                "message": str(e)
            }

            print(f"[ERROR] {step_id} -> {e}")

            return step_id, error_result

    def _resolve_arguments(
        self,
        arguments: Dict[str, Any],
        results: Dict[str, Any],
        initial_context: Dict[str, Any]
    ) -> Dict[str, Any]:

        resolved = {}

        for key, value in arguments.items():

            if isinstance(value, str) and value.startswith("$"):

                resolved[key] = self._resolve_variable(
                    value,
                    results,
                    initial_context
                )

            else:
                resolved[key] = value

        return resolved

    def _resolve_variable(
        self,
        expression: str,
        results: Dict[str, Any],
        initial_context: Dict[str, Any]
    ):

        """
        지원 형태:

        $user_name
        $step1.data.employee_id
        """

        expr = expression[1:]

        # initial context
        if "." not in expr and expr in initial_context:
            return initial_context[expr]

        parts = expr.split(".")

        step_id = parts[0]

        if step_id not in results:
            raise Exception(f"Missing dependency result: {step_id}")

        current = results[step_id]

        for part in parts[1:]:

            if isinstance(current, dict):
                current = current.get(part)
            else:
                raise Exception(f"Invalid path: {expression}")

        return current


# =========================================================
# DEMO
# =========================================================

async def main():

    registry = MCPServerRegistry()

    executor = AgentExecutor(registry)

    # ---------------------------------
    # Planner가 생성한 실행 계획
    # ---------------------------------

    plan = [
        {
            "id": "step1",
            "tool": "employee_lookup",
            "arguments": {
                "employee_name": "$user_name"
            }
        },
        {
            "id": "step2",
            "tool": "expense_query",
            "arguments": {
                "employee_id": "$step1.data.employee_id"
            },
            "depends_on": ["step1"]
        },
        {
            "id": "step3",
            "tool": "corp_card_history",
            "arguments": {
                "employee_id": "$step1.data.employee_id"
            },
            "depends_on": ["step1"]
        }
    ]

    # ---------------------------------
    # 사용자 입력에서 추출된 값
    # ---------------------------------

    initial_context = {
        "user_name": "김대리"
    }

    results = await executor.execute_plan(
        plan=plan,
        initial_context=initial_context
    )

    print("\n================ FINAL RESULTS ================\n")

    for step_id, result in results.items():
        print(step_id)
        print(result)
        print()


# =========================================================

if __name__ == "__main__":
    asyncio.run(main())