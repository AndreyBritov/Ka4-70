#!bin/bash


eT=3.45

#blockMesh
#snappyHexMesh -overwrite
#topoSet
#pimpleFoam


cp -f ./postProcessing/sample/$eT/triSurfaceSampling_foam/scalarField/p ./postProcessing/sample/$eT/triSurfaceSampling_foam
cp -f ./postProcessing/sample/$eT/triSurfaceSampling_foam/vectorField/wallShearStress ./postProcessing/sample/$eT/triSurfaceSampling_foam
cp -r ./postProcessing/sample/$eT/triSurfaceSampling_foam/. ./deformation
cd deformation/
cp -f dynamicMeshDict ../constant
cp -f ./util/pointDisplacementz ../$eT
bash AllrunBedLoad.sh
cd ..

cd system/
mv controlDict controlDictEndTime
mv controlDictWriteNow controlDict
cd ..
pimpleFoam
cd system/
mv controlDict controlDictWriteNow
mv controlDictEndTime controlDict
cd ..