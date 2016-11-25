#!/bin/bash
set -ex
cd `dirname $0`
gcloud app deploy --version staging --no-promote --no-stop-previous-version 
