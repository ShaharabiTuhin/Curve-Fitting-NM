import unittest

import numpy as np

from src.curve_fitting_project import (
    calculate_errors,
    fit_polynomial_curve,
    predict_gpa,
)


class CurveFittingProjectTests(unittest.TestCase):
    def test_fit_polynomial_returns_expected_length(self):
        x = np.array([1, 2, 3, 4, 5], dtype=float)
        y = np.array([2.0, 2.4, 2.8, 3.2, 3.6], dtype=float)

        coeffs = fit_polynomial_curve(x, y, degree=2)

        self.assertEqual(len(coeffs), 3)

    def test_predict_gpa_shape_matches_input(self):
        coeffs = np.array([0.01, 0.1, 2.0])
        x = np.array([3.0, 4.5, 6.2], dtype=float)

        preds = predict_gpa(coeffs, x)

        self.assertEqual(preds.shape, x.shape)

    def test_error_metrics_for_perfect_fit(self):
        actual = np.array([2.0, 2.5, 3.0], dtype=float)
        predicted = np.array([2.0, 2.5, 3.0], dtype=float)

        metrics = calculate_errors(actual, predicted)

        self.assertAlmostEqual(metrics["MSE"], 0.0)
        self.assertAlmostEqual(metrics["RMSE"], 0.0)
        self.assertAlmostEqual(metrics["MAE"], 0.0)
        self.assertAlmostEqual(metrics["R2"], 1.0)


if __name__ == "__main__":
    unittest.main()
