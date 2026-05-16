# Student Performance Prediction Using Curve Fitting Techniques

This repository contains a complete undergraduate-ready Numerical Methods project on **Curve Fitting** using Python.

## Quick Project Highlights

- Numerical method: **Polynomial Curve Fitting (Least Squares)**
- Application: **Predicting student GPA from study-related data**
- Libraries: **numpy, pandas, matplotlib**
- Includes:
  - realistic dataset (30+ entries)
  - clean Python implementation
  - graph visualization
  - error analysis
  - viva-ready academic content

## Repository Structure

- `/data/student_performance.csv` -> Sample project dataset
- `/src/curve_fitting_project.py` -> Complete Python implementation
- `/tests/test_curve_fitting_project.py` -> Focused unit tests
- `/outputs/` -> Generated graphs after running the project
- `/docs/full_project_guide.md` -> Full academic write-up (Steps 1-12)

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python src/curve_fitting_project.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Notes

- The model uses a weighted **Study Index** derived from Study Hours, Attendance, and Assignment Marks.
- A degree-2 polynomial is used to keep mathematics simple and viva-friendly.
- Graphs are saved automatically in the `outputs` folder.
