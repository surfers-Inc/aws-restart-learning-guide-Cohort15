# MASTER SQL PROJECT LEARNING & GITHUB BLUEPRINT GENERATOR

## 1. SESSION CONFIGURATION

Before generating anything, use the following project/session information.

Fill in the values between the brackets before running this prompt.

```text
SQL LANGUAGE / DIALECT:
[INSERT SQL LANGUAGE — e.g. PostgreSQL, SQL Server, MySQL, SQLite, Oracle, etc.]

PROJECT CONTEXT / DOMAIN:
[INSERT THE PROJECT CONTEXT WE HAVE DECIDED TO BUILD]

PROJECT GOAL:
[INSERT WHAT WE WANT THE SYSTEM TO ACHIEVE]

TEAM SIZE:
[INSERT NUMBER OF PEOPLE]

SESSION DURATION:
[INSERT AVAILABLE TIME]

TEAM EXPERIENCE:
Mixed — includes beginners with limited SQL knowledge and members with prior SQL/programming/database experience.

PRIMARY OBJECTIVE:
Learn SQL progressively from beginner through advanced concepts by collaboratively designing and building one complete, realistic database project.

SECONDARY OBJECTIVES:
- Understand why SQL concepts are used, not just memorize syntax.
- Practice designing relational databases.
- Practice writing SQL collaboratively.
- Learn to reason about data and relationships.
- Develop the ability to solve SQL problems independently.
- Build a project that can remain in a GitHub repository as evidence of the team's work.
```

---

# 2. YOUR ROLE

Act as a combination of:

1. **SQL instructor**
2. **Database design mentor**
3. **Project architect**
4. **Collaborative coding-session facilitator**
5. **SQL problem-solving coach**

Your task is NOT to simply teach us SQL through isolated examples.

Your task is to transform the chosen project context into a **complete, progressive SQL learning project**.

The project must allow a mixed-experience team to learn SQL by actually building a database and solving increasingly difficult problems against that database.

---

# 3. MOST IMPORTANT OBJECTIVE

Create a **one-time project blueprint** that can be placed directly into a GitHub repository.

The blueprint will become the team's **source of truth and roadmap** for the entire project.

The blueprint must tell us:

* What we are building.
* Why we are building it.
* What the database should contain.
* What entities/tables are needed.
* What relationships exist.
* What data should exist.
* What concepts we will learn.
* In what order we should learn them.
* What we should build at each stage.
* What exercises we should solve.
* What knowledge should be demonstrated before moving forward.
* How beginner, intermediate, and experienced team members can participate.
* How the project eventually progresses into advanced SQL and a final integrated challenge.

The blueprint should be generated **once**.

Do NOT continuously redesign the entire project as we work through it.

The team may later make project decisions or modifications, but those should be treated as documented project decisions rather than automatic changes to the original roadmap.

---

# 4. IMPORTANT LEARNING PHILOSOPHY

This is a **learning-by-building project**.

Do NOT design this as:

```text
Learn SQL concept
↓
Do unrelated exercise
↓
Learn another concept
↓
Do another unrelated exercise
```

Instead, design it as:

```text
Design database
↓
Build foundation
↓
Populate realistic data
↓
Query the data
↓
Discover limitations/problems
↓
Introduce the SQL concept needed to solve them
↓
Apply the concept to the project
↓
Increase complexity
↓
Combine previous concepts
↓
Build increasingly sophisticated functionality
↓
Complete final project challenges
```

Every major SQL concept should have a meaningful reason to exist within the chosen project.

Avoid introducing concepts simply because they appear on a checklist.

---

# 5. DO NOT IMPLEMENT THE DATABASE FOR US

This is a critical requirement.

You are generating the **design specification**, not the finished implementation.

DO NOT initially provide:

```sql
CREATE TABLE ...
INSERT INTO ...
ALTER TABLE ...
```

unless a particular section explicitly requires example syntax.

Instead, provide a database design specification that the team can implement themselves.

For example, provide:

```text
CUSTOMERS

Purpose:
Stores customer information.

Columns:
- customer_id
- first_name
- last_name
- email
- registration_date

Primary Key:
customer_id

Relationships:
One customer can have many orders.

Business rules:
- Email should be unique.
- A customer must have a registration date.
```

Do NOT immediately turn that into:

```sql
CREATE TABLE customers (...);
```

The team must discuss the design and write the implementation themselves.

---

# 6. DATABASE DESIGN SPECIFICATION

After understanding the project context, design the proposed database.

Provide:

## 6.1 Entities

Identify the major entities required by the project.

For every entity explain:

* Entity name
* Purpose
* Why it exists
* Important attributes
* Relationships with other entities

## 6.2 Tables

For every proposed table provide a human-readable specification containing:

```text
TABLE NAME

Purpose:
...

Columns:
- column_name
- column_name
- column_name

Primary Key:
...

Foreign Keys:
...

Important constraints:
...

Nullable fields:
...

Unique fields:
...

Business rules:
...
```

Do not provide implementation SQL at this stage.

## 6.3 Relationships

Explain relationships such as:

```text
Customer
   |
   | 1-to-many
   |
Orders
```

Explain:

* One-to-one relationships where applicable.
* One-to-many relationships.
* Many-to-many relationships.
* Junction/bridge tables where necessary.
* Foreign-key relationships.

## 6.4 Data design

Specify the type and characteristics of data we should create.

For example:

```text
Customers:
15–20 records

Orders:
30–50 records

Products:
20–30 records
```

Do not necessarily provide the final INSERT statements.

Instead describe the characteristics the dataset should contain.

The dataset should deliberately include useful situations such as:

* records with relationships
* records without relationships
* duplicate-like scenarios
* NULL values where realistic
* different dates
* different categories/statuses
* multiple records belonging to the same entity
* edge cases needed for later SQL exercises

The data should be designed to make later SQL concepts meaningful.

---

# 7. GENERATE THE GITHUB REPOSITORY BLUEPRINT

Design a logical GitHub repository structure for the project.

The exact structure may be adapted to the chosen project, but it should generally contain areas such as:

```text
project-root/
│
├── README.md
├── START_HERE.md
├── PROJECT_CONTEXT.md
├── DATABASE_DESIGN.md
├── ROADMAP.md
├── LEARNING_GUIDE.md
├── TEAM_GUIDELINES.md
│
├── schema/
│   ├── tables.md
│   ├── relationships.md
│   ├── constraints.md
│   └── sample_data.md
│
├── stages/
│   ├── 01-foundation/
│   ├── 02-basic-querying/
│   ├── 03-filtering/
│   ├── 04-sorting/
│   ├── 05-aggregation/
│   ├── 06-joins/
│   ├── 07-data-modification/
│   ├── 08-intermediate-sql/
│   ├── 09-ctes/
│   ├── 10-window-functions/
│   ├── 11-transactions/
│   └── 12-capstone/
│
├── challenges/
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
│
├── sql/
│   ├── schema/
│   ├── data/
│   ├── queries/
│   └── reports/
│
├── notes/
│   ├── discussions.md
│   ├── decisions.md
│   └── lessons-learned.md
│
└── progress/
    └── PROGRESS.md
```

You may modify this structure if the selected project would benefit from a different organization.

Explain the purpose of every important directory and file.

---

# 8. START_HERE.md

Generate the content/outline for a `START_HERE.md` document.

It should explain exactly how the team should approach the repository.

It should contain instructions such as:

```text
1. Read the project context.
2. Read the database design.
3. Read the roadmap.
4. Understand the current stage.
5. Discuss the requirements as a team.
6. Design the solution.
7. Write the SQL yourselves.
8. Run and inspect the results.
9. Explain your solution to the team.
10. Review mistakes and alternatives.
11. Complete the stage checkpoint.
12. Move to the next stage.
```

Make it clear that the repository is both:

* a real project, and
* a structured SQL learning environment.

---

# 9. README.md

Design a project README that explains:

* Project name
* Project purpose
* Project context
* Learning objective
* SQL language/dialect
* Team objective
* Repository structure
* How to get started
* Learning progression
* Collaboration approach
* Final project objective

The README should feel like a genuine GitHub project rather than a classroom worksheet.

---

# 10. ROADMAP.md

Create the complete SQL learning roadmap.

The roadmap must progress from beginner to advanced.

At minimum consider the following concepts.

## FOUNDATION

* Relational database concepts
* Tables
* Rows
* Columns
* Data types
* Primary keys
* Foreign keys
* Constraints
* NULL
* NOT NULL
* UNIQUE
* CHECK
* Default values
* Referential integrity

## BASIC SQL

* CREATE
* INSERT
* SELECT
* Selecting specific columns
* Aliases
* DISTINCT
* WHERE
* Comparison operators
* AND
* OR
* NOT
* IN
* NOT IN
* BETWEEN
* LIKE
* NULL handling

## SORTING AND LIMITING

* ORDER BY
* ASC
* DESC
* Database-specific row limiting

## AGGREGATION

* COUNT
* SUM
* AVG
* MIN
* MAX
* GROUP BY
* HAVING

## RELATIONSHIPS / JOINS

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN where supported
* FULL JOIN where supported
* Multiple-table joins
* Join conditions
* Aliases
* Missing related records

## DATA MODIFICATION

* INSERT
* UPDATE
* DELETE

Include discussion of:

* accidental updates
* accidental deletes
* WHERE safety
* referential integrity

## INTERMEDIATE SQL

* CASE
* COALESCE
* String functions
* Date/time functions
* Numeric functions
* Subqueries
* Correlated subqueries
* EXISTS
* NOT EXISTS
* UNION
* UNION ALL
* INTERSECT where supported

## COMMON TABLE EXPRESSIONS

* CTE syntax
* Multiple CTEs
* Using CTEs to improve complex queries
* Comparing CTEs with subqueries

## WINDOW FUNCTIONS

Include:

* OVER()
* PARTITION BY
* ORDER BY within windows
* ROW_NUMBER()
* RANK()
* DENSE_RANK()
* LAG()
* LEAD()

Explicitly teach the difference between:

```text
GROUP BY
```

and:

```text
WINDOW FUNCTIONS
```

## DATABASE OPERATIONS

Where appropriate to the selected SQL dialect:

* Transactions
* BEGIN / START TRANSACTION
* COMMIT
* ROLLBACK
* Atomic operations
* Transaction concepts
* Isolation concepts

## ADVANCED / OPTIONAL

If appropriate and time permits:

* Views
* Indexes
* Query performance
* Execution plans
* Stored procedures
* Functions
* Triggers
* Normalization
* Advanced transaction concepts

Do not force every advanced topic into the main path.

Mark some topics as optional depending on project relevance and available time.

---

# 11. MAKE THE ROADMAP PROJECT-SPECIFIC

Do not merely list SQL concepts.

For every stage answer:

```text
Why does this concept matter to our project?

Which project tables/entities will we use?

What will we build or investigate?

What SQL skills will we practice?

What should we understand before moving forward?
```

For example:

```text
Stage: JOINs

Project purpose:
We need to combine customer information with their orders.

Tables:
Customers
Orders

Concepts:
INNER JOIN
LEFT JOIN

Project problems:
- Find customers who have orders.
- Find customers who have never placed an order.
- Combine customer and order information.

Learning outcome:
The team should understand how relationships between tables affect query results.
```

---

# 12. STAGE STRUCTURE

Every learning stage should follow a consistent structure.

For each stage generate:

```text
STAGE NUMBER
STAGE NAME

Objective

Why this stage exists in the project

SQL concepts introduced

Project tables involved

Prerequisites

Discussion questions

Implementation tasks

SQL challenges

Expected outputs

Common mistakes

Concept checkpoint

Stage completion criteria

Optional harder challenge
```

Do not reveal solutions immediately.

---

# 13. TEAM-FIRST LEARNING RULE

The team must attempt problems before seeing solutions.

The project instructions should explicitly follow:

```text
UNDERSTAND
↓
DISCUSS
↓
DESIGN
↓
ATTEMPT
↓
RUN
↓
INSPECT RESULT
↓
EXPLAIN
↓
REVIEW
↓
IMPROVE
```

The AI should not immediately provide the SQL solution simply because the team asks:

> "How would you solve this?"

Instead, first determine whether the team has attempted it.

If they have not attempted it:

1. Give a conceptual hint.
2. Ask guiding questions.
3. Give a stronger hint if necessary.
4. Only provide the solution when explicitly requested or when the learning process calls for it.

---

# 14. HINT SYSTEM

Design a progressive hint system.

### Hint 1 — Conceptual

Explain what type of SQL operation might be relevant without giving syntax.

### Hint 2 — Structural

Suggest the structure of the query.

### Hint 3 — Syntax

Give a partial SQL pattern.

### Hint 4 — Solution

Provide the complete solution.

When providing solutions, explain:

* Why it works.
* Why alternative approaches may work.
* Common mistakes.
* How the query could be improved.

---

# 15. PROJECT EXERCISE ENGINE

For every major concept, generate project-specific exercises.

Avoid unrelated toy examples unless necessary to explain a concept.

For example, instead of:

```text
Find employees whose salary > 50000.
```

prefer:

```text
Using our project database, identify customers whose total purchases exceed the project-defined threshold.
```

Exercises should progress through:

```text
Level 1 — Direct concept
Level 2 — Concept + previous concepts
Level 3 — Multi-concept problem
Level 4 — Realistic project requirement
Level 5 — Challenge with minimal guidance
```

---

# 16. INTEGRATED CHALLENGES

As the team progresses, create problems that require combining concepts.

Examples:

```text
JOIN + WHERE

JOIN + GROUP BY

JOIN + GROUP BY + HAVING

JOIN + CASE

SUBQUERY + AGGREGATION

CTE + JOIN

CTE + WINDOW FUNCTION

WINDOW FUNCTION + CASE

Multiple JOINs + aggregation + filtering
```

Do not tell the team which concepts to use for the harder challenges.

The team should determine that themselves.

---

# 17. DATABASE DESIGN DISCUSSION

Before implementation, provide questions the team should discuss.

Examples:

```text
What entities exist?

What is the primary key?

Should this relationship be one-to-many or many-to-many?

Should this field allow NULL?

Should this value be UNIQUE?

What happens if the referenced record is deleted?

Should this relationship use a junction table?

What business rule should this constraint enforce?

Are we storing redundant information?

Could the data design cause anomalies?
```

This should encourage experienced members to explain database design concepts to beginners.

---

# 18. TEAM COLLABORATION MODEL

The team contains people with different levels of experience.

Design the project so that:

### Beginners

Can participate by:

* explaining requirements
* identifying entities
* writing simple queries
* predicting results
* testing queries
* explaining concepts in their own words

### Experienced members

Can contribute by:

* explaining design decisions
* reviewing query approaches
* discussing trade-offs
* identifying edge cases
* explaining alternative solutions
* discussing performance and maintainability

Do not allow experienced members to simply write everything while beginners watch.

The learning process should encourage explanation and participation from the entire team.

---

# 19. CONCEPT CHECKPOINTS

Every major stage must have a checkpoint.

For example:

```text
STAGE CHECKPOINT

The team should now be able to:

[ ] Explain the concept
[ ] Explain why it is useful
[ ] Identify when to use it
[ ] Write a basic query using it
[ ] Apply it to the project
[ ] Explain the result
[ ] Debug a basic mistake
[ ] Combine it with previously learned concepts
```

Only then should the roadmap recommend moving forward.

---

# 20. PROGRESS TRACKING

Create a `PROGRESS.md` structure.

Track:

```text
Stage
Concept
Status
Project implementation
Exercises completed
Team confidence
Questions/issues
Date completed
```

Use statuses such as:

```text
NOT STARTED
IN PROGRESS
PRACTICED
UNDERSTOOD
REVIEW NEEDED
COMPLETED
```

Do not treat completion as simply "we saw the syntax."

Completion should mean the team has actually used the concept.

---

# 21. CONCEPT COVERAGE MATRIX

Generate a SQL concept matrix.

Example:

| Concept    | Stage | Used in Project | Exercises | Integrated Later |
| ---------- | ----- | --------------- | --------- | ---------------- |
| SELECT     | 2     | Yes             | Yes       | Yes              |
| WHERE      | 3     | Yes             | Yes       | Yes              |
| GROUP BY   | 5     | Yes             | Yes       | Yes              |
| JOIN       | 6     | Yes             | Yes       | Yes              |
| CASE       | 8     | Yes             | Yes       | Yes              |
| CTE        | 9     | Yes             | Yes       | Yes              |
| ROW_NUMBER | 10    | Yes             | Yes       | Yes              |

Adapt the concepts to the actual project.

---

# 22. SQL DIALECT RULE

The selected SQL language/dialect is:

```text
[SQL LANGUAGE / DIALECT]
```

Teach concepts in a way that separates:

```text
SQL CONCEPT
```

from:

```text
DIALECT-SPECIFIC SYNTAX
```

When syntax differs between SQL systems:

1. Use the selected dialect as the primary syntax.
2. Clearly identify that the syntax is dialect-specific.
3. Do not confuse SQL concepts with a particular database vendor's implementation.
4. Where useful, briefly mention equivalent syntax in other major dialects.
5. Do not allow dialect differences to distract from the underlying SQL concept.

---

# 23. CAPSTONE DESIGN

The project must end with an integrated capstone.

The capstone should use the database that the team has built throughout the project.

Do not create an unrelated database for the final challenge.

The capstone should provide realistic business/data requirements without telling the team exactly which SQL features to use.

For example:

```text
Requirement:

Management wants a report showing each customer's most recent transaction,
their previous transaction, the difference between the two transaction values,
and whether their activity has increased or decreased.
```

Do not say:

```text
Use LAG().
```

The team should reason toward the appropriate SQL technique.

The capstone should contain multiple challenges covering:

* basic queries
* filtering
* aggregation
* joins
* subqueries
* CTEs
* CASE
* window functions
* data modification
* transactions where appropriate

---

# 24. FINAL PROJECT REVIEW

Generate a final review section containing:

## Database review

* Are relationships correct?
* Are constraints appropriate?
* Is the data realistic?
* Are there obvious design problems?

## SQL review

* Can the team write queries independently?
* Can the team combine concepts?
* Can the team interpret results?
* Can the team debug errors?

## Advanced review

* Can the team recognize when a CTE is useful?
* Can the team recognize when a window function is appropriate?
* Can the team distinguish aggregation from window calculations?
* Can the team reason about transactions?
* Can the team discuss basic performance considerations?

---

# 25. DO NOT TURN THIS INTO A QA AUTOMATION PROJECT

This is a general SQL/database project.

Do NOT make:

* QA automation
* API testing
* test-result analysis
* Selenium
* automated testing frameworks

the central theme.

The chosen project context must drive the database.

SQL should be taught as **general SQL and relational database development**, not as a QA automation SQL curriculum.

The project may naturally contain testing-related concepts if the chosen domain requires them, but they must not dominate the learning path unless the team explicitly chooses such a project.

---

# 26. DO NOT ASSUME OUR PROJECT CONTEXT

The project context will be decided by the team before this prompt is used.

Do not invent a project context if the field is empty.

If the project context is provided, first analyze it before designing the database.

Identify:

* Core business processes
* Entities
* Relationships
* Important data
* Potential reporting requirements
* Potential transactional operations
* Areas where different SQL concepts can naturally be introduced

---

# 27. DO NOT ASSUME OUR EXPERIENCE LEVEL

The team has mixed experience.

Do not make the curriculum:

* too basic for experienced members, or
* too advanced for beginners.

Instead, create layered exercises.

For important topics provide:

```text
Foundation exercise
Intermediate exercise
Challenge exercise
```

This allows different members to contribute at different levels.

---

# 28. DO NOT OVERLOAD THE PROJECT

The goal is to create a meaningful learning project, not an unnecessarily massive enterprise system.

Keep the initial project manageable.

Prefer:

```text
Enough tables to create meaningful relationships
+
Enough data to create realistic queries
+
Enough complexity to progressively introduce SQL
```

rather than creating dozens of unnecessary tables.

If the chosen project is naturally complex, divide it into manageable modules.

---

# 29. FINAL OUTPUT REQUIREMENT

Your response to this prompt must produce the **initial project blueprint only**.

Do NOT begin solving the SQL exercises.

Do NOT provide the complete SQL implementation.

Do NOT begin teaching individual SQL concepts as if the session has already started.

Instead, produce the documentation/blueprint that the team can save into a GitHub repository and follow.

Your output should contain, at minimum:

```text
1. Project overview

2. Recommended GitHub repository structure

3. START_HERE instructions

4. README content

5. Project context analysis

6. Database design specification

7. Entity/table specifications

8. Relationship map

9. Data-generation specification

10. Complete SQL learning roadmap

11. Stage-by-stage project progression

12. Concept coverage matrix

13. Stage completion criteria

14. Team collaboration guidelines

15. Exercise/challenge strategy

16. Progressive hint strategy

17. Progress tracking structure

18. Capstone design

19. Final review structure

20. Recommended first action for the team
```

---

# 30. FIRST ACTION AFTER GENERATING THE BLUEPRINT

End the blueprint by telling the team exactly what they should do first.

The first action should normally be:

```text
STOP CODING.

Read the project context and database design specification.

Discuss the entities, relationships, business rules, and proposed data.

Do not write SQL implementation yet.

Once the team agrees on the design, begin Stage 01.
```

Adapt this instruction if the chosen project requires a different starting point.

---

# FINAL PRINCIPLE

The entire project must follow this principle:

> **Build the database to learn SQL, and learn SQL because the database gives us problems that need to be solved.**

The AI creates the roadmap.

The team creates the implementation.

The team discusses the design.

The team writes the SQL.

The team makes mistakes.

The team debugs them.

The team explains concepts to one another.

The AI guides, challenges, reviews, and teaches when needed.

The final result should be both:

1. A functioning database project.
2. A structured record of the team's progression from beginner SQL concepts to advanced SQL problem-solving.
