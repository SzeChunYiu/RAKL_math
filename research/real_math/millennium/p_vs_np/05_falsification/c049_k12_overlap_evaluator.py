"""Inert record checker for frozen C049 k=12 overlap candidate.

No decoder, satisfiability solver, enumeration, or target capability.
"""
from __future__ import annotations
CANDIDATE_ID='C049-K12-FIRST-ADMISSIBLE-OVERLAP-SEPARATION-v1'
REQUIRED=('MINIMAL_K_JUSTIFICATION','K12_CANONICAL_UNSAT_PARAMETER_FORCING','K12_SUFFIX_ROW_FIXED_BIT','K13_CANONICAL_PREFIX_FIXED_BIT','BIT4_SEPARATION','SWAPPED_REDUCTION_PRESERVED')
def evaluate_certificate(certificate:dict,authorization:dict)->dict:
 if authorization.get('candidate_id')!=CANDIDATE_ID or authorization.get('proof_check_authorized') is not True:return {'verdict':'FAIL','reason':'authorization'}
 if certificate.get('candidate_id')!=CANDIDATE_ID:return {'verdict':'FAIL','reason':'candidate'}
 rows=certificate.get('obligations',[])
 if tuple(x.get('obligation_id') for x in rows)!=REQUIRED:return {'verdict':'FAIL','reason':'obligations'}
 if not all(x.get('status')=='PROVED' and x.get('evidence_pointer') for x in rows):return {'verdict':'FAIL','reason':'missing proof record'}
 return {'verdict':'PASS','candidate_id':CANDIDATE_ID}
