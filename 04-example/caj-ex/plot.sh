#!/bin/bash

for x in f*/*dot; do x=$(echo $x | sed "s/.dot//"); neato $x.dot -Tpdf -o$x.pdf; done
