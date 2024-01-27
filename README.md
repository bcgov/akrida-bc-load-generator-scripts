[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# OWL Akrida: BC Load Generator Scripts
This repository includes scripts and documentation specific to setting up our BC Gov use cases to use with the "owl-akrida" (formerly Aries Akrida), load testing tool.

Documentation and instructions for that tool can be found at the repository: https://github.com/openwallet-foundation/owl-akrida

## BC Gov load testing scripts
Akrida uses [Credo](https://github.com/openwallet-foundation/credo-ts) agents spun up locally (or can be distibuted with Locust accross multiple machines) as holder agents. This allows us to test various issuance or verification setups, and with a mediator.

There are plenty of built-in Akrida features that can be used to test ACA-Py deployments and Credo interactions (see Akrida repo for instructions and features), but this repo is specific to add-on scripts to run some specific BC Gov testing cases.

### How to use

Use cases here include the test scripts, environmental settings, and instructions that are used with the Akrida code base to run our load use cases. In some events there may be Akrida code base changes that would be included here too (ie files/changes that would overwrite the cloned Akrida code) but generally if that is needed we'd try to propose that change into Akrida itself in a way that can accomodate our needs. The goal isn't to ever have a separate Akrida fork.

Akrida runs Locust Python scripts so test cases (and additional agent controllers) can be dropped in as standalone Python files and configured in the `env` file to run.  
So this repository contains those `.py` scripts, `env` specifications, and `docker compose overrides` to get additional environment variables in as needed.

See the use-cases directory in this repo for each specific load test case.

Required tools
- Docker/Docker Compose