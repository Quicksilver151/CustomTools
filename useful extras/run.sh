#!/bin/bash
if [ -e ./run*sh ]; then
    echo "Running..."
    ./run*sh $@
else
    echo "No run.sh script found"
fi

