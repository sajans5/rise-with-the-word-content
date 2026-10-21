#!/usr/bin/env python3
"""Merge reviewed additions into a downloaded/checked-out live feed folder."""
from pathlib import Path
import sys, json, hashlib
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def write(p,obj):
    raw=(json.dumps(obj,ensure_ascii=False,indent=2)+"\n").encode("utf-8")
    p.write_bytes(raw)
    return hashlib.sha256(raw).hexdigest()
def main():
    if len(sys.argv)!=2: raise SystemExit("Usage: python3 merge_content_update.py /path/to/feed-folder")
    feed=Path(sys.argv[1]); bundle=Path(__file__).resolve().parent/"content"
    specs={"stories":("stories.json","stories-additions.json","id"),
           "quiz":("quiz.json","quiz-additions.json","q"),
           "trivia":("trivia.json","trivia-additions.json",None)}
    report={"date":"2026-10-21","before":{},"added":{},"after":{},"sha256":{}}
    manifest=load(feed/"manifest.json")
    objects={}
    for pack,(filename,addition_file,key) in specs.items():
        original=load(feed/filename); extra=load(bundle/addition_file)["items"]
        current=original["items"]; report["before"][pack]=len(current)
        if key:
            seen={str(x.get(key,"")).strip() for x in current}
            for item in extra:
                ident=str(item.get(key,"")).strip()
                if not ident or ident in seen: raise ValueError(f"{pack}: empty/duplicate {key}: {ident}")
                seen.add(ident); current.append(item)
        else:
            seen=set(current)
            for item in extra:
                if not isinstance(item,str) or not item.strip() or item in seen: raise ValueError(f"{pack}: blank/duplicate trivia")
                seen.add(item); current.append(item)
        objects[pack]=original
        report["added"][pack]=len(extra); report["after"][pack]=len(current)
    # Shape validation
    stories=objects["stories"]["items"]; quiz=objects["quiz"]["items"]; trivia=objects["trivia"]["items"]
    for i,s in enumerate(stories,1):
        if any(not str(s.get(k,"")).strip() for k in ("id","title","ref","summary","lesson","prayer")):
            raise ValueError(f"Story {i}: missing required field")
    for i,q in enumerate(quiz,1):
        opts=q.get("options",[]); ans=q.get("answer")
        if not q.get("q","").strip() or len(opts)<2 or not isinstance(ans,int) or ans<0 or ans>=len(opts) or not q.get("explain","").strip():
            raise ValueError(f"Quiz {i}: invalid structure or answer index")
    if any(not isinstance(t,str) or not t.strip() for t in trivia): raise ValueError("Trivia contains blank item")
    for pack,(filename,_,_) in specs.items():
        digest=write(feed/filename,objects[pack]); report["sha256"][pack]=digest
        if pack not in manifest.get("packs",{}): raise ValueError(f"Pack missing in manifest: {pack}")
        manifest["packs"][pack]["version"]=int(manifest["packs"][pack].get("version",1))+1
        manifest["packs"][pack]["sha256"]=digest
    write(feed/"manifest.json",manifest)
    (feed/"CONTENT_UPDATE_REPORT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
