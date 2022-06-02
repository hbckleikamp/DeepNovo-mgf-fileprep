#!/bin/bash

for file in $1
do
	echo "${file}"
	out=$( dirname "${file}")
    msconvert.exe --mgf "${file}" -o "${out}" --filter "peakPicking true [2]"  --filter "threshold count 100 most-intense" --filter "titleMaker <ScanNumber>.<Id>.<ChargeState>" --zlib
done
#hbckleikamp 2022