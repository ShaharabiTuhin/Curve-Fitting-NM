# Student Performance Prediction Using Curve Fitting Techniques

An undergraduate Numerical Methods project that uses curve fitting to predict student GPA from study-related factors such as study hours, attendance, and assignment marks. The project is designed to be simple enough for viva explanation while still looking polished, realistic, and presentation-ready.

## Project Overview

This project demonstrates how numerical curve fitting can be used to model the relationship between student performance and academic effort. The goal is to use a small, realistic dataset and fit a polynomial curve that can estimate GPA for new input values.

### Abstract

Student performance is influenced by several measurable academic activities, such as study time, attendance, and assignment completion. In this project, curve fitting is used to build a prediction model that estimates GPA from these factors. A polynomial least-squares approach is used because it is easy to explain, mathematically sound, and suitable for undergraduate numerical methods coursework. The project also includes graph visualization, prediction output, and error analysis to evaluate model quality.

### Problem Statement

Universities often need a simple way to estimate student performance early in a semester. This project addresses that need by building a numerical model that predicts GPA based on study-related inputs instead of relying on advanced machine learning techniques.

### Objectives

* Build a realistic student performance prediction model.
* Apply curve fitting and least squares methods.
* Visualize data and fitted curves using graphs.
* Calculate prediction error using simple metrics.
* Present the method in a viva-friendly academic format.

### Scope

This project focuses on undergraduate-level numerical analysis. It uses a small dataset, polynomial curve fitting, and clear visualization. It does not attempt to replace full-scale academic analytics systems.

### Real-Life Applications

* Early GPA estimation for students.
* Academic monitoring and counseling.
* Identifying students who may need support.
* Demonstrating numerical modeling in education.

### Expected Outcomes

* A working prediction system.
* A fitted polynomial curve for student performance.
* Graphs showing data trends and model behavior.
* Error values that show how well the model fits.

## Theory Summary

### Numerical Analysis

Numerical analysis studies methods for solving mathematical problems using approximations. It is useful when exact formulas are difficult or impossible to derive.

### Curve Fitting

Curve fitting is the process of finding a mathematical curve that best represents a set of data points.

### Polynomial Curve Fitting

Polynomial fitting uses an equation of the form:

$$
y = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n
$$

where the coefficients are chosen so that the curve is as close as possible to the observed data.

### Least Squares Method

The least squares method minimizes the sum of squared differences between the actual values and predicted values:

$$
S = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

### Error Measures

* Mean Error:

$$
ME = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)
$$

* Root Mean Squared Error (RMSE):

$$
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

## Dataset Design

The project uses a realistic dataset with the following columns:

* Study Hours
* Attendance Percentage
* Assignment Marks
* GPA

The data is designed to show a natural trend: higher study hours, attendance, and assignment marks generally lead to better GPA values, but with small variations to keep the dataset realistic.

### Sample Dataset Assumptions

* GPA is on a 0 to 4 scale.
* Attendance is expressed as a percentage.
* Assignment marks are out of 100.
* Performance is not perfectly linear, so polynomial fitting is appropriate.

## Methodology

1. Collect or create the student dataset.
2. Clean and prepare the data.
3. Fit a polynomial curve using least squares.
4. Predict GPA for new student input values.
5. Compute error measures.
6. Plot scatter and fitted curve graphs.
7. Display results clearly for academic presentation.

## Visualization Included

The project supports the following graphs:

* Scatter plot of actual student data.
* Fitted polynomial curve.
* Prediction graph for new input values.
* Error visualization for model performance.

## Project Structure

At the moment, the workspace contains a single front-end file:

* `index.html` - interactive dashboard interface for the project

You can later extend this workspace with Python files, a dataset CSV, and a report document.

## How To Use

1. Open `index.html` in a browser.
2. Enter student-related values in the input section.
3. Generate the prediction.
4. Review the fitted curve, graphs, and error analysis.

## Report Outline

### Chapter 1 - Introduction

Project background, problem statement, objectives, and scope.

### Chapter 2 - Literature Review

Basic discussion of numerical methods, curve fitting, and prediction systems.

### Chapter 3 - Methodology

Dataset description, polynomial model, least squares fitting, and error metrics.

### Chapter 4 - Implementation and Results

Code explanation, graph results, prediction output, and evaluation.

### Chapter 5 - Conclusion and Future Work

Summary of findings, limitations, and improvement ideas.

## Presentation Support

The project is suitable for a 10 to 12 slide presentation covering:

* Topic introduction
* Theory
* Dataset design
* Mathematical model
* Implementation
* Graphs and results
* Error analysis
* Conclusion
* Viva questions

## Viva Preparation Topics

* Why curve fitting was chosen
* Why polynomial fitting is suitable
* How least squares works
* What RMSE means
* Limitations of the model
* Practical uses in education

## Future Improvements

* Add a Python backend.
* Load data from CSV.
* Compare multiple curve types.
* Build a Tkinter or Streamlit UI.
* Add real-time prediction features.

## Tech Stack

* HTML
* Tailwind CSS
* Chart.js
* Font Awesome

## License

This project is prepared for academic use.