---
name: 🐛 Bug Report
about: Report a bug in the calculator app
title: "[BUG] <short description>"
labels: bug
assignees: ''
---

## 🐞 Describe the bug

Division by zero doesn't crash but gives a string error message, which may cause type mismatch if further calculation is expected.

## 🔁 Steps to Reproduce

1. Run `python calculator.py`
2. Choose `divide`
3. Enter: `10` and `0`
4. Observe: Returns "Error: Cannot divide by zero"

## 🤔 Expected behavior

Should handle the error but also allow further processing if needed, or raise a typed exception.

## 📸 Screenshots / Output


