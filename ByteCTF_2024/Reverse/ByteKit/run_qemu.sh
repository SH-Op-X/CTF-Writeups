#!/bin/bash

qemu-system-x86_64 \
	-L . \
	-m 512M \
	-nographic \
	-monitor none \
	-serial stdio \
	-drive if=pflash,file=bios.bin,format=raw,readonly=off \
	-net none \
	-hda debian-12-nocloud-amd64-20240901-1857.qcow2
