"""Finite falsifier/calibration for C045. Computation is not theorem authority."""
from itertools import product
import json

MAGIC="11100101"
NEW_EDGES=[(58696,37741),(58698,55881),(58697,9654),(58699,27794),(58728,37741),(58730,55881),(58729,9654),(58729,47103),(58731,27794),(58731,65243)]
CODES=[0,2,7,1,4,2,6,6,1,5]

def gamma(v):
    b=f"{v:b}"; return "0"*(len(b)-1)+b

def encode(v, clauses):
    width=v.bit_length(); bits=MAGIC+gamma(v)+gamma(len(clauses))
    for clause in clauses:
        for var,neg in clause: bits+=("1" if neg else "0")+f"{var:0{width}b}"
    return bits+("0" if len(bits)%2 else "")

def sat(v, clauses):
    for a in product((False,True), repeat=v):
        if all(any((not a[var-1]) if neg else a[var-1] for var,neg in cl) for cl in clauses): return True
    return False

def all_length32_unsat():
    out=[]
    for v in range(1,16):
      lits=[(i,n) for i in range(1,v+1) for n in (False,True)]
      for m in (1,2):
        # Only parameter pairs allowed by the hand length proof are enumerated exhaustively below.
        if (m==1 and not 8<=v<=15) or (m==2 and v not in (2,3)): continue
        if m==1: continue # one clause is always satisfiable
        clauses3=list(product(lits, repeat=3))
        for cls in product(clauses3, repeat=2):
            bits=encode(v, cls)
            if len(bits)==32 and not sat(v,cls): out.append(bits)
    return sorted(set(out))

def signatures():
    idx={e:i for i,e in enumerate(NEW_EDGES)}
    rows=sorted({r for r,c in NEW_EDGES}); cols=sorted({c for r,c in NEW_EDGES})
    rs={r:{idx[e] for e in NEW_EDGES if e[0]==r} for r in rows}
    cs={c:{idx[e] for e in NEW_EDGES if e[1]==c} for c in cols}
    def sig(star):
        z=[]
        for b in range(3):
            vals={(CODES[i]>>b)&1 for i in star}
            z.append('E' if vals=={0} else 'H' if vals=={1} else 'X')
        return ''.join(z)
    def opp(a,b): return any((x,y) in (('E','H'),('H','E')) for x,y in zip(a,b))
    bad=[]
    for r in rows:
        for c in cols:
            if (r,c) in idx: continue
            if not opp(sig(rs[r]),sig(cs[c])): bad.append((r,c))
    return {"rows":{r:sig(rs[r]) for r in rows},"cols":{c:sig(cs[c]) for c in cols},"bad":bad}

def verify():
    words=all_length32_unsat()
    derived=sorted(f"{r:016b}{c:016b}" for r,c in NEW_EDGES)
    assert words==derived, (len(words),len(derived))
    s=signatures(); assert not s["bad"],s["bad"]
    return {"unsat_word_count":len(words),"new_edge_count":len(NEW_EDGES),"local_uncovered_active_cells":0,"status":"CALIBRATION_MATCH"}

if __name__=="__main__": print(json.dumps(verify(), sort_keys=True, separators=(",", ":")))
