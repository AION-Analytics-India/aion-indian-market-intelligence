# AION Open Source — Migration Queue
# Last updated: 2026-06-05

## Blocked Migrations (prerequisites unresolved)
| Item | Blocker | Priority |
|---|---|---|
| wheel_build/ cleanup | Divergent source copies | Medium |
| aion_news_to_signal_self_hosted/ | Weights bundling doctrine | Medium |
| hf_space_aion_news_to_signal/ | Weights staging | Medium |
| src/api/ → private | Import roots + private remote | High |
| aion_taxonomy/ coupling | Ship-with vs pinned-dep decision | High |
| frontend-api-contract-v1 → main | Rebase with dirty worktree | High |

## Safe Pending Migrations
| Item | Action | Status |
|---|---|---|
| aion-newsimpact/ | Move to packages/ after dep validation | Queued |
| docs/ | Split public/private | Queued |
