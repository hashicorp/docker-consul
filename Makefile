
DIR := ${CURDIR}

#if make is typed with no further arguments, then show a list of available targets
default:
	@awk -F\: '/^[a-z_]+:/ && !/default/ {printf "- %-20s %s\n", $$1, $$2}' Makefile

help:
	@echo ""
	@echo "TODO"


build:
	cd 0.6; docker build -t 542640492856.dkr.ecr.ap-southeast-2.amazonaws.com/consul:base .

push:
	cd 0.6: docker push 542640492856.dkr.ecr.ap-southeast-2.amazonaws.com/consul:base

build_and_push: build push
	@echo ""
%:
	@: