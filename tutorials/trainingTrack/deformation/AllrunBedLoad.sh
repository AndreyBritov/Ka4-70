#!/bin/bash
# Source tutorial run functions
iter=1
startTime=3.45

for ((i=1; i<=$iter; i++))
do
    echo "ITERATION = $i"
    python3 Consolidation.py
    mono BedLoadTaskNew.dll 0.5 5 ImportData.txt ExportData.txt BLParams.txt
    #rm ImportData
    mv ImportData.txt ImportDataDefault.txt
    python3 Diversity.py
#    let "rem = $i % 10"
#    if [ "$rem" = "0" ]
#    then
#       mv  ImportData.txt ImportData_i$i.txt
#       mv  ExportData.txt ExportData_i$i.txt
#    else
#       rm ImportData.txt
#    fi

#    mv MExportData.txt ImportData.txt
    cp -f pointDisplacementz  ../constant/boundaryData/down/$startTime
    

done

rm -rf faces points p wallShearStress faceCentres pointDisplacementz vectorField scalarField
#rmdir -rf vectorField scalarField
