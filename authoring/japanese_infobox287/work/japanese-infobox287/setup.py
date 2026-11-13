from pathlib import Path

root=Path(__file__).parent
source=Path('work/japanese-preservation/board.py').read_text(encoding='utf8')
marker='elif a in ("status", "agent"):'
assert marker in source
source=source.replace(marker,'''elif a == "assign":
    issue=call("PATCH","repos/swccg-guild/work/issues/"+sys.argv[2],{"assignees":["MemoryCoreChatGPT2"]})
    print("assigned",issue["number"],[x["login"] for x in issue["assignees"]])
'''+marker)
(root/'board.py').write_text(source,encoding='utf8')
(root/'claim.md').write_text('''CLAIM: (MemoryCoreChatGPT) Bill explicitly directed: “Update your AI team skills and proceed with your plan.” The agreed order is #287 infobox migration first, then the remaining Japanese-set content audits. #287 is Ready; its recorded comments contain readiness and #361 recommendations, with no implementation claim or live migration recorded. Taking implementation ownership from the queued Alpha1 assignment under Bill's current direction.

Refresh the 794-page baseline after #361, extend Template:Card in the sandbox, prove the required sample/conservation and English regression checks, migrate guarded batches, complete the lint follow-up, then audit the remaining Japanese products on the shared structure. Translation/content changes remain separate from this verbatim migration.

MemoryCoreChatGPT
''',encoding='utf8')
