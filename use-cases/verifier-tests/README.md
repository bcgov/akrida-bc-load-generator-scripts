# Verifier Load Testing

This folder contains the work-in-progress changes to the Akrida framework (https://github.com/openwallet-foundation/owl-akrida), and design/running notes needed for load testing excercises with various Verifier use cases.

## Load Scripts Contained

## locustMediatorVerifier.py
On startup 
- Connects user agent to issuer (Issuer ACA-Py agent created invitation and local Credo user accepts)
- Issues configured credential and accepts
- Connects to verifier

Repeating task 
- Calls Verifier agent to do Pres Req to connection
- Accepts/completes presntation request as Credo agent
- Verifier agent checks status is verified


## locustMediatorVerifierConnectionless.py
*In Progress*

On startup 
- Connects and issues cred as above
- Calls verifier to create a connectionless Pres Req

Need to add Akrida changes for Credo agent to handle connectionless. 
**TODO TBD** need to check up on things if we pick this back up with the new Credo setup in Akrida.


### LocustMediatorVerifier

## .env
Add various `CRED_DEF` identifiers for the "anchor cred" simple cred and the copy of the IAS Person Credential.
These both reference the Sandbox env DIDs on bcovrin-test.

So this is using a copy of the person credential that IAS issues (doesn't point to any actual IAS person cred def) so we can test verification cases with credentials of that size.

Include a `CRED_ATTR` of the IAS Person Cred attributes including a dummy base64 encoded profile pic (see Pull Request description/comments)

## Akrida Changes Required


### Dockerfile
https://pypi.org/project/beautifulsoup4/ import for parsing HTML (get deep link for VCauthn)