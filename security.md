# Security Controls

## Intended Users

The intended users of this repository are:

- The course instructor  
- The repository owner (student) 

## Risk Assessment

If the code or data in this repository were improperly accesed. 

### 1. Academic Integrity Risks
- Unauthorized copying of assignments
- Redistribution of solutions
- Plagiarism or misuse of submitted work

### 2. Code Misuse
Although the repository contains coursework and not production systems, risks may include:
- Accidental inclusion of sensitive configuration data
- Scripts being modified and reused in unintended ways

## Security Controls Implemented

### Branch Protection Rules

The default branch is protected with the following rules:

- Prevention of branch deletion  
- Prevention of non-fast-forward pushes  
- Pull requests required for changes  
- Code owner review required  

These controls reduce the likelihood of:
- Accidental destructive changes  
- Unauthorized direct commits  
- Unreviewed modifications  

### CODEOWNERS Enforcement

Code owner review is required before pull requests can be merged. This ensures:

- Oversight of all changes  
- Accountability for contributions  
- Reduced risk of malicious or accidental harmful updates  

### No-Secrets 

The repository does not intentionally store:

- API keys  
- Passwords  
- Private certificates  
- Authentication tokens  

### Scope Limitation

This repository:

- Does not store regulated or confidential data  
- Does not contain personal identifiable information (PII)  
- Is limited to educational content  

## Justification of Security Posture

Because this repository is used for coursework and does not contain production systems or sensitive operational data, extensive enterprise-level security controls are not necessary.

However, the implemented protections (branch rules, pull request requirements, and code owner review) provide reasonable safeguards appropriate to its academic purpose.
