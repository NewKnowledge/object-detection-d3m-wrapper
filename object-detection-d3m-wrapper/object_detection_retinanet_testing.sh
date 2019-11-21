#!/bin/bash -e

Datasets=('LL1_penn_fudan_pedestrian', 'LL1_tidy_terra_panicle_detection')

cd "/src/objectDetection/object-detection-d3m-wrapper/"

# create text file to record scores and timing information
touch pipeline_tests/scores.txt
echo "DATASET, SCORE, EXECUTION TIME" >> pipeline_tests/scores.txt

for i in "${Datasets[@]}"; do

    # generate and save pipeline
    python3 "/src/objectDetection/object-detection-d3m-wrapper/pipeline.py" $i

    # test and score pipeline    
    start=`date +%s`
    python3 -m d3m runtime -d /datasets/ fit-score -p *.json -i /datasets/seed_datasets_current/$i/TRAIN/dataset_TRAIN/datasetDoc.json -t /datasets/seed_datasets_current/$i/TEST/dataset_TEST/datasetDoc.json -a /datasets/seed_datasets_current/$i/SCORE/dataset_TEST/datasetDoc.json -r /datasets/seed_datasets_current/$i/${i}_problem/problemDoc.json -O ${i}_pipeline_run.yaml -c scores.csv
    end=`date +%s`
    runtime=$((end-start))
    
    IFS=, read col1 score col3 col4 < <(tail -n1 scores.csv)
        echo "$i, $score, $runtime" >> pipeline_tests/scores.txt

    # cleanup temporary file
    mv *.json pipeline_tests/${i}_pipeline.json
    mv ${i}_pipeline_run.yaml pipeline_tests/${i}_pipeline_run.yaml
    cp "/src/objectDetection/object-detection-d3m-wrapper/pipeline.py" "/src/objectDetection/object-detection-d3m-wrapper/pipeline_tests/${i}_pipeline.py"
    rm *.meta
    rm scores.csv  
done
