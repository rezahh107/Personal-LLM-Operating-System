# Claim Authority Model

Not every actor may write every claim or field.

| Claim or field | User | LLM | Tool | Validator/CI | Downstream model |
| --- | ---: | ---: | ---: | ---: | ---: |
| User goal | yes | no | no | no | no |
| User preference | yes | no | no | no | no |
| Candidate observation | yes | yes | yes | no | yes |
| Execution result | no | no | yes | yes | no |
| Tool output | no | no | yes | may store/check | no |
| Evidence hash | no | no | tool/orchestrator | yes | no |
| Severity suggestion | yes | only if marked suggestion | if tool-defined | may check | no |
| Risk acceptance | yes | no | no | no | no |
| Production readiness | out of scope | out of scope | out of scope | out of scope | out of scope |
| Compliance certification | out of scope | out of scope | out of scope | out of scope | out of scope |
| Memory promotion | yes | no direct write | no | may recommend/enforce | no |

LLMs may propose. They must not silently promote.
