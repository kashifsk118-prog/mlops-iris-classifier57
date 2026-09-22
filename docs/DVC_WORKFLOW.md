# DVC Workflow

## Remote Configuration

The DVC remote used in this experiment is a local folder:

`~/dvc-remote-storage`

It was configured as the default DVC remote using:

```bash
dvc remote add -d myremote ~/dvc-remote-storage
## Dataset Versioning Workflow

For every dataset change, the following workflow was followed:

Dataset → dvc add → git add → git commit → dvc push → DVC Remote Storage

The `.dvc` metafile is committed to Git, while the actual dataset is stored and versioned by DVC.

## Dataset Versions

### Version 1

- Dataset: `data/raw/iris_v1.csv`
- Rows: 150
- Git commit: `2a22d3b`

### Version 2

- Dataset: `data/raw/iris_v1.csv`
- Rows: 170
- Git commit: `63775a5`
- 20 synthetic rows were added.

## Comparing Versions

The dataset versions were compared using:

```bash
dvc diff 2a22d3b 63775a5
The result showed:

```text
Modified:
    data\raw\iris_v1.csv

files summary: 1 modified
```

## Restoring Dataset Versions

To restore the older dataset version:

```bash
git checkout 2a22d3b -- data/raw/iris_v1.csv.dvc
dvc checkout data/raw/iris_v1.csv.dvc
```

This restored the 150-row dataset.

To restore the latest version:

```bash
git checkout HEAD -- data/raw/iris_v1.csv.dvc
dvc checkout data/raw/iris_v1.csv.dvc
```

This restored the 170-row dataset.

## Verification

```bash
wc -l data/raw/iris_v1.csv
```

- 151 lines = 150 rows + header
- 171 lines = 170 rows + header

## Conclusion

DVC was successfully integrated with Git for dataset versioning. Different versions of the dataset were stored, compared, and restored using DVC and Git.