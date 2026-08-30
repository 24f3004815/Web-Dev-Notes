# 📊 IIT Madras Grade Calculation — Comprehensive Analysis

> **Date:** Aug 24, 2026 | **Scores read from dashboard screenshot**

---

## 📋 Scores Read From Dashboard

| Subject | Quiz 1 | Quiz 2 | Notes |
|---------|--------|--------|-------|
| **PDSA** | 24 | 36 | Mock Assignment: 94, OPPE Eligible: Yes |
| **DBMS** | 37 | 48 | OPPE Eligible: Yes, ET Eligible: Yes |
| **AppDev 1** | 54 | 52 | Mock Assignment: 100, ET Eligible: Yes |

> ⚠️ **Please verify these scores!** Read from screenshot — if any are wrong, recalculate using the formulas below.

---

## 🎓 IIT Madras Grading Scale

| Grade | Min Score (T) | Grade Points |
|-------|--------------|-------------|
| S | ≥ 90 | 10 |
| A | ≥ 80 | 9 |
| B | ≥ 70 | 8 |
| C | ≥ 60 | 7 |
| D | ≥ 50 | 6 |
| E | ≥ 40 | 5 |

**Your target: 7+ grade points = Grade C or above (T ≥ 60)**

---

# ═══════════════════════════════════════
# SUBJECT 1: PDSA
# ═══════════════════════════════════════

## Formula
```
T = 0.05×GAA + 0.2×OP + 0.45×F + max(0.2×max(Qz1,Qz2), 0.10×Qz1 + 0.20×Qz2)
```

## Step-by-Step Calculation (GAA = 75, Q1 = 24, Q2 = 36)

**Step 1: GAA component**
- 0.05 × 75 = **3.75**

**Step 2: Quiz component**
- Option A: 0.2 × max(24, 36) = 0.2 × 36 = **7.20**
- Option B: 0.10 × 24 + 0.20 × 36 = 2.40 + 7.20 = **9.60**
- Quiz component = max(7.20, 9.60) = **9.60** ← Option B wins

**Step 3: Fixed total (everything except OPPE & ET)**
- Fixed = 3.75 + 9.60 = **13.35**

**Step 4: Final formula**
```
T = 13.35 + 0.2×OP + 0.45×F
```

**Step 5: Maximum possible from OPPE + ET**
- 0.2×100 + 0.45×100 = 20 + 45 = **65**
- Max T = 13.35 + 65 = **78.35**

## PDSA: Required Scores Table

| Grade | T needed | 0.2×OP + 0.45×F needed | Achievable? |
|-------|----------|----------------------|-------------|
| **S (≥90)** | 90 | 76.65 | ❌ NOT POSSIBLE (max 65) |
| **A (≥80)** | 80 | 66.65 | ❌ NOT POSSIBLE (max 65) |
| **B (≥70)** | 70 | 56.65 | ✅ Yes |
| **C (≥60)** | 60 | 46.65 | ✅ Yes |
| **D (≥50)** | 50 | 36.65 | ✅ Yes |

## PDSA: OPPE vs End Term Combinations

### For Grade B (T ≥ 70): need 0.2×OP + 0.45×F ≥ 56.65

| OPPE Score | Min ET Required | Feasible? |
|-----------|----------------|-----------|
| 100 | **82** | ✅ |
| 90 | **86** | ✅ |
| 80 | **91** | ✅ |
| 70 | **95** | ✅ (tough) |
| 60 | **100** | ⚠️ Need perfect ET |
| 50 or less | — | ❌ Not possible |

### For Grade C (T ≥ 60) — YOUR 7+ TARGET: need 0.2×OP + 0.45×F ≥ 46.65

| OPPE Score | Min ET Required | Feasible? |
|-----------|----------------|-----------|
| 100 | **60** | ✅ Comfortable |
| 90 | **64** | ✅ |
| 80 | **69** | ✅ |
| 70 | **73** | ✅ |
| 60 | **77** | ✅ |
| 50 | **82** | ✅ |
| 40 | **86** | ✅ (tough) |

### For Grade D (T ≥ 50): need 0.2×OP + 0.45×F ≥ 36.65

| OPPE Score | Min ET Required | Feasible? |
|-----------|----------------|-----------|
| 100 | **37** | ✅ Easy |
| 80 | **46** | ✅ |
| 60 | **55** | ✅ |
| 40 | **64** | ✅ |

---

# ═══════════════════════════════════════
# SUBJECT 2: DBMS
# ═══════════════════════════════════════

## Formula
```
T = 0.03×GAA2 + 0.02×GAA3 + 0.2×OPPE + 0.45×F + max(0.2×max(Qz1,Qz2), 0.10×Qz1 + 0.20×Qz2)
```

## Step-by-Step Calculation (GAA2 = 75, GAA3 = 75, Q1 = 37, Q2 = 48)

**Step 1: GAA components**
- 0.03 × 75 = **2.25**
- 0.02 × 75 = **1.50**

**Step 2: Quiz component**
- Option A: 0.2 × max(37, 48) = 0.2 × 48 = **9.60**
- Option B: 0.10 × 37 + 0.20 × 48 = 3.70 + 9.60 = **13.30**
- Quiz component = max(9.60, 13.30) = **13.30** ← Option B wins

**Step 3: Fixed total**
- Fixed = 2.25 + 1.50 + 13.30 = **17.05**

**Step 4: Final formula**
```
T = 17.05 + 0.2×OPPE + 0.45×F
```

**Step 5: Max T = 17.05 + 65 = 82.05**

## DBMS: Required Scores Table

| Grade | T needed | 0.2×OPPE + 0.45×F needed | Achievable? |
|-------|----------|-------------------------|-------------|
| **S (≥90)** | 90 | 72.95 | ❌ NOT POSSIBLE (max 65) |
| **A (≥80)** | 80 | 62.95 | ⚠️ Barely (OPPE≥100, ET≥96) |
| **B (≥70)** | 70 | 52.95 | ✅ Yes |
| **C (≥60)** | 60 | 42.95 | ✅ Yes |
| **D (≥50)** | 50 | 32.95 | ✅ Yes |

## DBMS: OPPE vs End Term Combinations

### For Grade A (T ≥ 80): need 0.2×OPPE + 0.45×F ≥ 62.95

| OPPE Score | Min ET Required | Feasible? |
|-----------|----------------|-----------|
| 100 | **96** | ⚠️ Extremely tough |
| 90 | **100** | ⚠️ Need perfect ET |
| 80 or less | — | ❌ Not possible |

### For Grade B (T ≥ 70): need 0.2×OPPE + 0.45×F ≥ 52.95

| OPPE Score | Min ET Required | Feasible? |
|-----------|----------------|-----------|
| 100 | **74** | ✅ |
| 90 | **78** | ✅ |
| 80 | **83** | ✅ |
| 70 | **87** | ✅ |
| 60 | **91** | ✅ (tough) |
| 50 | **96** | ⚠️ Very tough |

### For Grade C (T ≥ 60) — YOUR 7+ TARGET: need 0.2×OPPE + 0.45×F ≥ 42.95

| OPPE Score | Min ET Required | Feasible? |
|-----------|----------------|-----------|
| 100 | **51** | ✅ Comfortable |
| 90 | **56** | ✅ |
| 80 | **60** | ✅ |
| 70 | **65** | ✅ |
| 60 | **69** | ✅ |
| 50 | **74** | ✅ |
| 40 | **78** | ✅ |
| 35 (min pass) | **80** | ✅ |

### For Grade D (T ≥ 50): need 0.2×OPPE + 0.45×F ≥ 32.95

| OPPE Score | Min ET Required | Feasible? |
|-----------|----------------|-----------|
| 100 | **29** | ✅ Easy |
| 80 | **38** | ✅ |
| 60 | **47** | ✅ |
| 40 | **56** | ✅ |
| 35 | **58** | ✅ |

> **DBMS Note:** You MUST score ≥ 35 in OPPE AND get Python-DB connectivity question correct, otherwise you get I_OP (incomplete) regardless of ET score!

---

# ═══════════════════════════════════════
# SUBJECT 3: AppDev 1
# ═══════════════════════════════════════

## Formula
```
T = 0.05×GLA + max(0.6×F + 0.25×max(Qz1,Qz2), 0.4×F + 0.25×Qz1 + 0.3×Qz2)
```

## ⚡ NO OPPE IN AppDev 1 — Only End Term pending!

## Step-by-Step Calculation (GLA = 75, Q1 = 54, Q2 = 52)

**Step 1: GLA component**
- 0.05 × 75 = **3.75**

**Step 2: Quiz options**
- Option A: 0.6×F + 0.25×max(54,52) = 0.6F + 0.25×54 = **0.6F + 13.50**
- Option B: 0.4×F + 0.25×54 + 0.3×52 = 0.4F + 13.50 + 15.60 = **0.4F + 29.10**

**Step 3: Which option wins?**
- Option A > Option B when: 0.6F + 13.50 > 0.4F + 29.10
- → 0.2F > 15.60 → **F > 78**
- If ET > 78: T = 3.75 + 0.6F + 13.50 = **17.25 + 0.6F**
- If ET ≤ 78: T = 3.75 + 0.4F + 29.10 = **32.85 + 0.4F**

**Step 4: Max T (F=100) = 17.25 + 60 = 77.25**

## AppDev 1: Required End Term Scores

| Grade | T needed | Min ET Required | Achievable? |
|-------|----------|----------------|-------------|
| **S (≥90)** | 90 | — | ❌ NOT POSSIBLE (max T = 77.25) |
| **A (≥80)** | 80 | — | ❌ NOT POSSIBLE (max T = 77.25) |
| **B (≥70)** | 70 | **88** | ✅ (using formula: 17.25 + 0.6×88 = 70.05) |
| **C (≥60)** | 60 | **68** | ✅ (using formula: 32.85 + 0.4×68 = 60.05) |
| **D (≥50)** | 50 | **43** | ✅ (using formula: 32.85 + 0.4×43 = 50.05) |

---

# ═══════════════════════════════════════
# 🎯 PART 1 SUMMARY: What you need for 7+ (Grade C, T ≥ 60)
# ═══════════════════════════════════════

## Quick Answer Table

| Subject | Has OPPE? | Minimum Combo for C Grade (T ≥ 60) |
|---------|-----------|-------------------------------------|
| **PDSA** | ✅ Yes | OPPE=70 & ET=73 **OR** OPPE=80 & ET=69 **OR** OPPE=60 & ET=77 |
| **DBMS** | ✅ Yes | OPPE=70 & ET=65 **OR** OPPE=80 & ET=60 **OR** OPPE=60 & ET=69 |
| **AppDev 1** | ❌ No | ET ≥ 68 (only exam remaining!) |

### 💡 Realistic Scenario: If you score ~70 in OPPE

| Subject | OPPE | Min ET for C (7+) |
|---------|------|-------------------|
| PDSA | 70 | **73** |
| DBMS | 70 | **65** |
| AppDev 1 | N/A | **68** |

### 💡 Realistic Scenario: If you score ~80 in OPPE

| Subject | OPPE | Min ET for C (7+) |
|---------|------|-------------------|
| PDSA | 80 | **69** |
| DBMS | 80 | **60** |
| AppDev 1 | N/A | **68** |

---

# ═══════════════════════════════════════
# 📊 PART 2 SUMMARY: Complete Grade Table (GAA = 75)
# ═══════════════════════════════════════

## PDSA — All Grades (Fixed = 13.35)

| Grade | OPPE=40 | OPPE=50 | OPPE=60 | OPPE=70 | OPPE=80 | OPPE=90 | OPPE=100 |
|-------|---------|---------|---------|---------|---------|---------|----------|
| **S (≥90)** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **A (≥80)** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **B (≥70)** | ❌ | ❌ | ET≥100 | ET≥95 | ET≥91 | ET≥86 | ET≥82 |
| **C (≥60)** | ET≥86 | ET≥82 | ET≥77 | ET≥73 | ET≥69 | ET≥64 | ET≥60 |
| **D (≥50)** | ET≥64 | ET≥60 | ET≥55 | ET≥51 | ET≥46 | ET≥42 | ET≥37 |

## DBMS — All Grades (Fixed = 17.05)

| Grade | OPPE=35 | OPPE=50 | OPPE=60 | OPPE=70 | OPPE=80 | OPPE=90 | OPPE=100 |
|-------|---------|---------|---------|---------|---------|---------|----------|
| **S (≥90)** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **A (≥80)** | ❌ | ❌ | ❌ | ❌ | ❌ | ET≥100 | ET≥96 |
| **B (≥70)** | ❌ | ET≥96 | ET≥91 | ET≥87 | ET≥83 | ET≥78 | ET≥74 |
| **C (≥60)** | ET≥80 | ET≥74 | ET≥69 | ET≥65 | ET≥60 | ET≥56 | ET≥51 |
| **D (≥50)** | ET≥58 | ET≥52 | ET≥47 | ET≥43 | ET≥38 | ET≥34 | ET≥29 |

> ⚠️ DBMS OPPE minimum is 35 + Python-DB correct to pass. Below 35 = fail OPPE = I_OP grade.

## AppDev 1 — All Grades (No OPPE)

| Grade | Min ET Required | Achievable? |
|-------|----------------|-------------|
| **S (≥90)** | — | ❌ NOT POSSIBLE (max T = 77.25) |
| **A (≥80)** | — | ❌ NOT POSSIBLE (max T = 77.25) |
| **B (≥70)** | **ET ≥ 88** | ✅ Tough but doable |
| **C (≥60)** | **ET ≥ 68** | ✅ Achievable |
| **D (≥50)** | **ET ≥ 43** | ✅ Easy |

---

# ⚠️ CRITICAL REMINDERS

1. **DBMS OPPE:** Must score ≥35 AND get Python-DB connectivity question correct. Otherwise = FAIL OPPE regardless of other scores.

2. **PDSA OPPE Eligibility:** All GrPA weeks 2-8 must be ≥40. You appear eligible (OPPE_ELIGIBLE = 1.00).

3. **AppDev 1:** Has NO OPPE. Only End Term is pending. S and A grades are mathematically impossible with Q1=54, Q2=52, GAA=75.

4. **PDSA:** S and A grades are mathematically impossible with Q1=24, Q2=36 (quiz scores too low, max T = 78.35).

5. **DBMS:** S grade impossible. A grade barely possible only with OPPE≥90 AND ET≥96+.

---

# 🔢 Formula Verification Examples

## PDSA: If OPPE=80, ET=69
T = 13.35 + 0.2(80) + 0.45(69) = 13.35 + 16 + 31.05 = **60.40** ✅ (C grade)

## DBMS: If OPPE=80, ET=60
T = 17.05 + 0.2(80) + 0.45(60) = 17.05 + 16 + 27 = **60.05** ✅ (C grade)

## AppDev: If ET=68
T = 32.85 + 0.4(68) = 32.85 + 27.2 = **60.05** ✅ (C grade)

## AppDev: If ET=88
T = 17.25 + 0.6(88) = 17.25 + 52.8 = **70.05** ✅ (B grade)

---

# 📝 SCORES I READ FROM YOUR SCREENSHOT (Please verify!)

**PDSA weekly scores visible:**
- W1: 94, W2: 100, W3: ~96, W4: 100, W5: 83, W6: ~83
- Multiple GrPA scores: mostly 100
- Week 8 GrPAs: Absent
- Mock: 94

**DBMS weekly scores visible:**
- W1: 85, W2: ~91, W3: 100, W4: 100, W5: ~85, W6: 100, W7: 100
- W8: Absent
- GrPA scores: mostly 100

**AppDev weekly scores visible:**
- W1: 75, W2: ~88, W3: 100, W4: 100, W5: 100, W6: 100, W7: 100
- W8: Absent, Mock: 100
