# Runge-Kutta Fehlberg (RKF) ODE Solver – Project 2 (CST-305)

## 📘 Overview

This project implements the Runge-Kutta 4th Order (RK4) method to solve a given Ordinary Differential Equation (ODE) of the form:

```
dy/dx = -y + ln(x)
```

The goal is to solve this equation both manually and programmatically, analyze the accuracy of RK4 compared to traditional methods (like Euler's), and evaluate the computing system's performance based on runtime and number of steps.

---

## 🧠 Problem Description

- **ODE Assigned**: dy/dx = -y + ln(x)
- **Initial Values**: x₀ = 2.0, y₀ = 1.0
- **Step Size**: h = 0.3
- **Steps**: 5
- **Method Used**: Runge-Kutta 4th Order (RK4)

---

## 🧮 Mathematical Approach

The RK4 method estimates y at the next step using a weighted average of slopes:

```
k1 = f(x, y)
k2 = f(x + h/2, y + h*k1/2)
k3 = f(x + h/2, y + h*k2/2)
k4 = f(x + h, y + h*k3)

y_next = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
```

This method provides good accuracy for many practical problems involving ODEs.

---

## 💻 Code Overview

### File: `RungeKutta_Timed.py`

- Solves the ODE using RK4.
- Displays each step’s x and y values along with k1, k2, k3, and k4.
- Calculates and prints the total runtime and number of steps.
- Uses `matplotlib` to plot the results.

---

## 🧪 System Requirements

- **Python**: 3.11 or newer recommended
- **Libraries**:
  - `math`
  - `matplotlib`

Install dependencies using pip:

```bash
pip install matplotlib
```

---

## 🏃 How to Run

```bash
python RungeKutta_Timed.py
```

The script will:
- Display numerical results for 5 RK4 steps.
- Plot the solution curve.
- Print total computation time and step count.

---

## 🧭 Additional Features

- ✅ Can be adapted to test additional ODEs like `dy/dx = x + y` or `dy/dx = x * sin(y)`
- ✅ Easily expandable to compare with Euler’s method
- ✅ Performance tested on a modern laptop for benchmarking

---

## 📊 Performance Evaluation

- **Processor**: Intel Core i7  
- **RAM**: 16 GB  
- **OS**: Windows 11  
- **Python Version**: 3.11  
- **Runtime**: ~0.0004 seconds for 5 steps

---

## 📂 Files Included

| File Name              | Description                              |
|------------------------|------------------------------------------|
| `RungeKutta_Timed.py`  | Main Python script with RK4 implementation |
| `README.md`            | This documentation file                  |
| `CST305_Project2_Report.docx` | Detailed project report               |

---

## 👤 Author

**Christian Nshuti Manzi**  
Grand Canyon University – CST-305  
Summer 2025

---

## 📚 References

- Burden, R. L., & Faires, J. D. (2011). *Numerical Analysis* (9th ed.). Cengage Learning.  
- Python Official Documentation: https://docs.python.org/3/  
- Matplotlib Library: https://matplotlib.org/

